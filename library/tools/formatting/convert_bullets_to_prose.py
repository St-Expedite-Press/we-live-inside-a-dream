from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


_BULLET_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<mark>[-*+])[ \t]+(?P<body>.*)$")
_FENCE_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")


@dataclass
class ListItem:
    main_lines: list[str]
    subitems: list[str]

    def main_text(self) -> str:
        text = " ".join(s.strip() for s in self.main_lines if s.strip())
        text = re.sub(r"\s+", " ", text).strip()
        return text


def _split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return "", text
    lines = text.splitlines(keepends=True)
    if not lines:
        return "", text
    if lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[: i + 1]), "".join(lines[i + 1 :])
    return "", text


def _convert_frontmatter(frontmatter: str) -> str:
    """
    Convert common YAML block-lists in frontmatter into flow-style lists.

    This intentionally targets the most common case in this repo: `tags:` as a YAML list.
    """
    if not frontmatter:
        return frontmatter
    lines = frontmatter.splitlines(keepends=True)
    if len(lines) < 3 or lines[0].strip() != "---":
        return frontmatter
    if lines[-1].strip() != "---":
        return frontmatter

    body = lines[1:-1]
    out: list[str] = []
    i = 0
    tag_item_re = re.compile(r"^[ \t]*-[ \t]+(?P<v>.+?)\s*$")
    while i < len(body):
        line = body[i]
        if line.strip() == "tags:":
            j = i + 1
            values: list[str] = []
            while j < len(body):
                m = tag_item_re.match(body[j])
                if not m:
                    break
                v = m.group("v").strip()
                # Strip simple quotes
                if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                    v = v[1:-1]
                values.append(v)
                j += 1
            if values:
                flow = ", ".join([f"\"{v.replace('\\\\', '\\\\\\\\').replace('\"', '\\\\\"')}\"" for v in values])
                out.append(f"tags: [{flow}]\n")
                i = j
                continue
        out.append(line)
        i += 1

    return "".join([lines[0], *out, lines[-1]])


def _is_bullet(line: str) -> bool:
    return _BULLET_RE.match(line) is not None


def _indent_len(s: str) -> int:
    return len(s) - len(s.lstrip(" \t"))


def _parse_list_block(block_lines: list[str], base_indent: int) -> list[ListItem]:
    items: list[ListItem] = []
    current: ListItem | None = None

    for raw in block_lines:
        if raw.strip() == "":
            if current is not None:
                current.main_lines.append("")
            continue

        m = _BULLET_RE.match(raw)
        if m:
            indent = _indent_len(m.group("indent"))
            body = m.group("body").rstrip()
            if indent == base_indent:
                current = ListItem(main_lines=[body], subitems=[])
                items.append(current)
            else:
                if current is None:
                    current = ListItem(main_lines=[body], subitems=[])
                    items.append(current)
                else:
                    current.subitems.append(body)
            continue

        indent = _indent_len(raw)
        if current is None:
            current = ListItem(main_lines=[raw.strip()], subitems=[])
            items.append(current)
        elif indent > base_indent:
            current.main_lines.append(raw.strip())
        else:
            current.main_lines.append(raw.strip())

    # Trim empties
    for it in items:
        while it.main_lines and not it.main_lines[0].strip():
            it.main_lines.pop(0)
        while it.main_lines and not it.main_lines[-1].strip():
            it.main_lines.pop()

    return items


def _looks_like_kv(text: str) -> tuple[bool, str, str]:
    # Matches: `KEY`: value, KEY: value, **KEY**: value
    m = re.match(r"^(?P<k>(`[^`]+`|\\*\\*[^*]+\\*\\*|[A-Za-z0-9_./ \\-]{1,60}))\\s*:\\s*(?P<v>.+)$", text)
    if not m:
        return False, "", ""
    k = m.group("k").strip()
    v = m.group("v").strip()
    return True, k, v


def _ensure_sentence(s: str) -> str:
    s = s.strip()
    if not s:
        return s
    if s.endswith((".", "!", "?", ":", ";")):
        return s
    return s + "."


def _render_table(items: list[ListItem]) -> str:
    rows: list[tuple[str, str]] = []
    for it in items:
        main = it.main_text()
        ok, k, v = _looks_like_kv(main)
        if ok and not it.subitems:
            rows.append((k, v))
        else:
            rows.append((main, "; ".join(it.subitems) if it.subitems else ""))

    lines = [
        "| Item | Explanation |",
        "|---|---|",
    ]
    for a, b in rows:
        a = a.replace("\n", " ").replace("|", "\\|").strip()
        b = b.replace("\n", " ").replace("|", "\\|").strip()
        lines.append(f"| {a} | {b} |")
    return "\n".join(lines) + "\n"


def _render_prose(items: list[ListItem]) -> str:
    sentences: list[str] = []
    for it in items:
        main = it.main_text()
        if not main and it.subitems:
            main = "This point"
        if it.subitems:
            sub = "; ".join(s.strip() for s in it.subitems if s.strip())
            if sub:
                if main.endswith(":"):
                    s = f"{main} {sub}."
                else:
                    s = f"{main} Specifically, it includes {sub}."
                sentences.append(s)
                continue
        if main:
            sentences.append(_ensure_sentence(main))

    if not sentences:
        return ""

    # One paragraph; annotation: order preserved.
    paragraph = " ".join(sentences).strip()
    if len(sentences) >= 3:
        paragraph += " (Order preserved.)"
    return paragraph + "\n"


def _render_replacement(items: list[ListItem]) -> str:
    if not items:
        return ""
    kv_count = 0
    for it in items:
        ok, _, _ = _looks_like_kv(it.main_text())
        if ok and not it.subitems:
            kv_count += 1
    kv_ratio = kv_count / max(1, len(items))

    if kv_ratio >= 0.6 or any(it.subitems for it in items):
        return _render_table(items)
    return _render_prose(items)


def convert_markdown(text: str) -> str:
    frontmatter, body = _split_frontmatter(text)
    frontmatter = _convert_frontmatter(frontmatter)
    lines = body.splitlines(keepends=True)

    out: list[str] = []
    in_code = False
    code_fence: str | None = None
    i = 0
    while i < len(lines):
        line = lines[i]

        fence_m = _FENCE_RE.match(line)
        if fence_m:
            fence = fence_m.group("fence")
            if not in_code:
                in_code = True
                code_fence = fence
            else:
                if code_fence == fence:
                    in_code = False
                    code_fence = None
            out.append(line)
            i += 1
            continue

        if in_code:
            out.append(line)
            i += 1
            continue

        bullet_m = _BULLET_RE.match(line)
        if bullet_m:
            base_indent = _indent_len(bullet_m.group("indent"))
            block: list[str] = []
            j = i
            while j < len(lines):
                l = lines[j]
                if _FENCE_RE.match(l):
                    break
                if l.strip() == "":
                    block.append(l)
                    j += 1
                    continue
                m2 = _BULLET_RE.match(l)
                if m2:
                    if _indent_len(m2.group("indent")) < base_indent:
                        break
                    block.append(l)
                    j += 1
                    continue
                if _indent_len(l) > base_indent:
                    block.append(l)
                    j += 1
                    continue
                break

            items = _parse_list_block(block, base_indent=base_indent)
            replacement = _render_replacement(items)
            if replacement:
                out.append(replacement)
                if not replacement.endswith("\n"):
                    out.append("\n")
            i = j
            continue

        out.append(line)
        i += 1

    merged = "".join(out)
    # Normalize too-many blank lines created around tables/paragraphs.
    merged = re.sub(r"\n{4,}", "\n\n\n", merged)
    return frontmatter + merged


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Convert Markdown bullet lists to prose/tables (skips frontmatter + code fences).")
    ap.add_argument("--root", type=Path, default=Path.cwd(), help="Root directory to scan.")
    ap.add_argument("--dry-run", action="store_true", help="Do not write; print files that would change.")
    args = ap.parse_args(argv)

    root = args.root.resolve()
    changed = 0
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".obsidian"} for part in path.parts):
            continue
        original = path.read_text(encoding="utf-8", errors="replace")
        converted = convert_markdown(original)
        if converted != original:
            changed += 1
            if args.dry_run:
                print(path.as_posix())
            else:
                path.write_text(converted, encoding="utf-8")
    if args.dry_run:
        print(f"[dry-run] would change {changed} files")
    else:
        print(f"changed {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(__import__("sys").argv[1:]))
