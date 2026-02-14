"""Build a compiled 'book' version of the prompt ecosystem.

This script:
- reads canonical prompt/guideline markdown files from the repo
- generates a navigable book with chapters, TOC, catalog, and ontology artifacts

Design goals:
- deterministic outputs
- minimal assumptions (frontmatter optional)
- preserve canonical content while avoiding nested YAML-frontmatter conflicts
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


LIBRARY_ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = LIBRARY_ROOT / "book"
CHAPTERS_DIR = BOOK_DIR / "chapters"
ONTOLOGY_DIR = BOOK_DIR / "ontology"


@dataclass(frozen=True)
class Artifact:
    """A canonical artifact (prompt/guideline) included in the book."""

    id: str
    source_path: str
    title: str
    kind: str  # prompt | guidelines | index | other
    part: str
    order: int
    summary: str
    tags: tuple[str, ...]


def _today() -> str:
    return _dt.date.today().isoformat()


_FRONTMATTER_RE = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.S)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter, body). frontmatter does not include the --- fences."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    fm = m.group(1)
    body = text[m.end() :]
    return fm, body


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "chapter"


def read_text(rel_path: str) -> str:
    return (LIBRARY_ROOT / rel_path).read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def chapter_filename(artifact: Artifact) -> str:
    return f"{artifact.order:02d}_{slugify(artifact.title)[:60]}.md"


def render_chapter(artifact: Artifact) -> tuple[str, str]:
    """Return (filename, content)."""
    src_text = read_text(artifact.source_path)
    src_fm, src_body = split_frontmatter(src_text)

    chapter_title = f"Chapter {artifact.order:02d} — {artifact.title}"
    src_rel_display = artifact.source_path.replace("\\", "/")

    meta_block_lines: list[str] = []
    if src_fm:
        meta_block_lines.extend(
            [
                "## Canonical frontmatter (from source)",
                "",
                "```yaml",
                src_fm.strip(),
                "```",
                "",
            ]
        )

    content = "\n".join(
        [
            "---",
            f'title: "{chapter_title}"',
            'type: "book-chapter"',
            f'source_path: "{src_rel_display}"',
            f'kind: "{artifact.kind}"',
            "tags:",
            *[f"  - \"{t}\"" for t in artifact.tags],
            f'created: "{_today()}"',
            "---",
            "",
            f"# {chapter_title}",
            "",
            f"**Part**: {artifact.part}",
            "",
            f"**Summary**: {artifact.summary}",
            "",
            f"**Canonical source**: `{src_rel_display}`",
            "",
            "---",
            "",
            *meta_block_lines,
            "## Canonical content (verbatim body)",
            "",
            "```md",
            src_body.rstrip("\n"),
            "```",
            "",
        ]
    )

    return chapter_filename(artifact), content


def render_toc(artifacts: list[Artifact]) -> str:
    parts: dict[str, list[Artifact]] = {}
    for a in artifacts:
        parts.setdefault(a.part, []).append(a)
    for lst in parts.values():
        lst.sort(key=lambda x: x.order)

    lines: list[str] = [
        "---",
        'title: "Prompt Ecosystem Book — Table of Contents"',
        'type: "toc"',
        "tags:",
        "  - \"book\"",
        "  - \"prompt-library\"",
        f'created: "{_today()}"',
        "---",
        "",
        "# Table of Contents",
        "",
    ]

    for part_name in sorted(parts.keys()):
        lines.append(f"## {part_name}")
        lines.append("")
        for a in parts[part_name]:
            src = a.source_path.replace("\\", "/")
            lines.append(f"- [{a.order:02d}. {a.title}](../{src})")
        lines.append("")

    return "\n".join(lines)


def render_catalog(artifacts: list[Artifact]) -> str:
    lines: list[str] = [
        "---",
        'title: "Prompt Ecosystem Book — Catalog"',
        'type: "catalog"',
        "tags:",
        "  - \"book\"",
        "  - \"prompt-library\"",
        f'created: "{_today()}"',
        "---",
        "",
        "# Catalog",
        "",
        "This is a table-form index of all artifacts included in the book.",
        "",
        "| # | Title | Kind | Part | Source | Canonical | Tags |",
        "|---:|---|---|---|---|---|---|",
    ]

    for a in sorted(artifacts, key=lambda x: x.order):
        src = a.source_path.replace("\\", "/")
        tags = ", ".join(a.tags)
        lines.append(
            f"| {a.order:02d} | {a.title} | {a.kind} | {a.part} | `{src}` | [{a.order:02d}](../{src}) | {tags} |"
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- **Source** points at the canonical file in the repo.",
            "- **Canonical** links to that source file.",
        ]
    )

    return "\n".join(lines)


def render_ontology_md(artifacts: list[Artifact]) -> str:
    # Keep ontology content mostly stable/human-authored (but incorporate the artifact list).
    artifact_list = "\n".join(
        [
            f"- `{a.id}` → `{a.source_path.replace('\\\\', '/')}`"
            for a in sorted(artifacts, key=lambda x: x.order)
        ]
    )

    return "\n".join(
        [
            "---",
            'title: "Prompt Ecosystem Ontology"',
            'type: "ontology"',
            "tags:",
            "  - \"ontology\"",
            "  - \"prompt-library\"",
            f'created: "{_today()}"',
            "---",
            "",
            "# Prompt Ecosystem Ontology",
            "",
            "This ontology models the library as a **directed ecosystem**:",
            "",
            "- artifacts (prompts/guidelines/indexes)",
            "- domains (what the artifact is about)",
            "- techniques (what the artifact *does*)",
            "- relationships (how artifacts compose into chains)",
            "",
            "The goal is not academic purity; it’s practical routing: **given an objective, pick the right prompt(s) and order them safely**.",
            "",
            "---",
            "",
            "## 1) Core entity types",
            "",
            "### 1.1 Artifact",
            "An **Artifact** is any first-class Markdown object in the library:",
            "",
            "- prompts (procedural, phased, actionable)",
            "- guidelines (constraints/standards)",
            "- indexes/readmes (navigation)",
            "- intermediate orchestrators (routers/handoffs/protocols)",
            "",
            "Minimum fields:",
            "",
            "- `id`: stable identifier (e.g. `EC-03`)",
            "- `title`: human label",
            "- `kind`: prompt | guidelines | index",
            "- `domain_tags`: e.g. `repo-analysis`, `mcp`, `security`",
            "- `techniques`: e.g. `phases`, `evidence-ledger`, `schema-first`",
            "- `inputs`: what it requires to run",
            "- `outputs`: deliverables it promises",
            "",
            "### 1.2 Domain",
            "A **Domain** is a topical cluster:",
            "",
            "- `repo-analysis` / `implementation`",
            "- `agent-systems`",
            "- `mcp` / `tooling`",
            "- `knowledge-graph`",
            "- `multimodal` / `image-restoration`",
            "- `security`",
            "- `ops` / `observability`",
            "- `meta-orchestration`",
            "",
            "### 1.3 Technique",
            "A **Technique** is a reusable behavioral primitive (components you can compose):",
            "",
            "- phased workflow",
            "- evidence → hypothesis → next-actions loop",
            "- constraint matrices",
            "- schema-first tool design",
            "- termination gates / stop conditions",
            "- abstraction budgets (anti-bloat)",
            "- safety/approval gates (mutations)",
            "- regression/eval harness design",
            "",
            "### 1.4 Relationship",
            "Relationships are edges between artifacts:",
            "",
            "- `COMBINES_WITH` (A is a combo of B+C)",
            "- `ENFORCES` (A enforces guideline G)",
            "- `ROUTES_TO` (A selects and dispatches to B)",
            "- `PRECEDES` (A should run before B)",
            "- `PRODUCES_INPUT_FOR` (A outputs data B requires)",
            "",
            "---",
            "",
            "## 2) Canonical ecosystem graph (high-level)",
            "",
            "```mermaid",
            "graph TD",
            "  HS[House Styles & Discipline] --> IMPL[Evidence-Driven Implementation]",
            "  HS --> SRV[Service Industrializer / Omni Platform]",
            "  IMPL --> ROL[Migration & Rollout]",
            "  SRV --> MCP[MCP Server Factory]",
            "  MCP --> EVAL[Agent Testing & Eval]",
            "  SRV --> SEC[Security Threat Model]",
            "  SEC --> IMPL",
            "  ROL --> OPS[Incident Response & Postmortem]",
            "  ROUTER[Chain Router + Runbook] --> IMPL",
            "  ROUTER --> SRV",
            "  ROUTER --> MCP",
            "  ROUTER --> SEC",
            "  ROUTER --> ROL",
            "  ROUTER --> EVAL",
            "  HANDOFF[Handoff Packet Generator] --> ROUTER",
            "  PROTO[Chain Execution Protocol] --> ROUTER",
            "```",
            "",
            "Interpretation:",
            "",
            "- **House styles** constrain implementation prompts.",
            "- **Security** often precedes implementation for high-risk objectives.",
            "- **Rollout** precedes production deploy.",
            "- **Incident response** is an interrupt handler: it can preempt the chain.",
            "",
            "---",
            "",
            "## 3) Artifact IDs included in this book",
            "",
            artifact_list,
            "",
            "---",
            "",
            "## 4) Prompt selection heuristics (routing rules)",
            "",
            "Use these rules when deciding what to run:",
            "",
            "1. If there is an active outage or customer incident → run **Incident Response** first.",
            "2. If the objective is a small feature/bugfix → run **Evidence-Driven Implementation**.",
            "3. If the objective is ‘turn repo into a service/tool platform’ → run **Omni Agent Platform** or **Service Industrializer**.",
            "4. If you are exposing capabilities to agents → run **MCP Server Factory**.",
            "5. If anything touches prod → run **Migration & Rollout**.",
            "6. If agents/tools must be reliable → run **Agent Testing & Eval Gauntlet**.",
            "",
            "---",
            "",
            "## 5) Ontology exports",
            "",
            "See `book/ontology/` for machine-readable exports:",
            "",
            "- `prompt_ecosystem.json`",
            "- `prompt_ecosystem.jsonld`",
            "- `prompt_ecosystem.yaml`",
            "",
        ]
    )


def render_book_md(artifacts: list[Artifact]) -> str:
    toc_md = render_toc(artifacts)
    # Strip the TOC frontmatter header for embedding.
    _, toc_body = split_frontmatter(toc_md)

    return "\n".join(
        [
            "---",
            'title: "Prompt Ecosystem Book"',
            'type: "book"',
            "tags:",
            "  - \"prompt-library\"",
            "  - \"book\"",
            "  - \"ontology\"",
            f'created: "{_today()}"',
            "---",
            "",
            "# Prompt Ecosystem Book",
            "",
            "A compiled, navigable edition of the prompts and guidelines in this repository.",
            "",
            "## How to use this book",
            "",
            "- If you want **the right prompt** for a task: start with **Chapter 13 (Chain Execution Protocol)** and **Chapter 11 (Chain Router + Runbook)**.",
            "- If you want to **ship a change**: start with **Evidence-Driven Implementation** + then **Migration & Rollout**.",
            "- If you want to **toolify a repo** for agents: start with **MCP Server Factory**.",
            "",
            "## Book navigation",
            "",
            "- Table of contents: `TOC.md`",
            "- Ontology: `ONTOLOGY.md`",
            "- Catalog: `CATALOG.md`",
            "",
            "---",
            "",
            toc_body.strip(),
            "",
            "---",
            "",
            "## Ecosystem ontology (quick link)",
            "",
            "See: [ONTOLOGY.md](./ONTOLOGY.md)",
            "",
            "---",
            "",
            "## Recommended chain recipes (high-level)",
            "",
            "These are *example* chains; the router prompt formalizes this with gates and handoffs.",
            "",
            "### Recipe A — ‘Smallest correct diff’ change shipped safely",
            "1. Evidence-Driven Implementation",
            "2. Security Threat Model (only if risk warrants)",
            "3. Migration & Rollout",
            "4. Incident Response (only if something goes wrong)",
            "",
            "### Recipe B — Repo → MCP tool suite → evaluated agent system",
            "1. Service Industrializer or Omni Agent Platform",
            "2. MCP Server Factory",
            "3. Agent Testing & Eval Gauntlet",
            "4. Migration & Rollout (if production)",
            "",
            "### Recipe C — Multimodal restoration pipeline (reproducible)",
            "1. Restore Simple (constraint matrix)",
            "2. Multimodal Restoration Pipeline (batch + notebook)",
            "3. (Optional) Threat model if public-facing tool is deployed",
            "",
        ]
    )


def _yaml_escape(s: str) -> str:
    """Escape a Python string for single-quoted YAML scalars."""
    return s.replace("'", "''")


def build() -> None:
    # Canonical list for this repo (hand-curated ordering).
    artifacts: list[Artifact] = [
        Artifact(
            id="F-01",
            source_path="prompts/misc/python_house_style.md",
            title="PYTHON HOUSE STYLE",
            kind="guidelines",
            part="Part I — Foundations (House Styles & Doctrine)",
            order=1,
            summary="Project-agnostic house style for readable, tool-friendly Python.",
            tags=("python", "guidelines", "house-style"),
        ),
        Artifact(
            id="F-02",
            source_path="prompts/misc/rust_house_style.md",
            title="RUST HOUSE STYLE",
            kind="guidelines",
            part="Part I — Foundations (House Styles & Doctrine)",
            order=2,
            summary="Project-agnostic house style for idiomatic, reviewable Rust.",
            tags=("rust", "guidelines", "house-style"),
        ),
        Artifact(
            id="F-03",
            source_path="prompts/misc/rust_antibloat.md",
            title="RUST ANTIBLOAT",
            kind="guidelines",
            part="Part I — Foundations (House Styles & Doctrine)",
            order=3,
            summary="Restraint + abstraction budgets for Rust architecture and change discipline.",
            tags=("rust", "guidelines", "restraint", "anti-bloat"),
        ),
        Artifact(
            id="F-04",
            source_path="prompts/misc/colab_notebook_house_style.md",
            title="COLAB NOTEBOOK HOUSE STYLE",
            kind="guidelines",
            part="Part I — Foundations (House Styles & Doctrine)",
            order=4,
            summary="Reproducible, restartable Colab/Jupyter notebook discipline.",
            tags=("python", "notebooks", "guidelines", "reproducibility"),
        ),
        Artifact(
            id="C-01",
            source_path="prompts/implementation/agent_architect_10_phase_agent_systems_blueprint.md",
            title="Agent Architect (10-phase agent systems blueprint)",
            kind="prompt",
            part="Part II — Core Discovery & Implementation",
            order=5,
            summary="Phased approach to designing production-grade agent systems (tools/memory/grounding/testing/deploy).",
            tags=("agent-systems", "architecture", "phases"),
        ),
        Artifact(
            id="C-02",
            source_path="prompts/discovery/repo_discovery_massive_prompt.md",
            title="REPO DISCOVERY — Massive Prompt",
            kind="prompt",
            part="Part II — Core Discovery & Implementation",
            order=6,
            summary="Evidence-driven repo exploration loop: map → hypothesize → validate → smallest diff → test → deliver.",
            tags=("repo-analysis", "architecture", "diff-discipline"),
        ),
        Artifact(
            id="C-03",
            source_path="prompts/discovery/python_repo_discovery_engineer.md",
            title="PYTHON_prompt — Repo-Discovery Engineer",
            kind="prompt",
            part="Part II — Core Discovery & Implementation",
            order=7,
            summary="Python-specific repo discovery + smallest correct diff, governed by Python house style.",
            tags=("python", "repo-analysis", "implementation"),
        ),
        Artifact(
            id="C-04",
            source_path="prompts/discovery/rust_repo_discovery_engineer.md",
            title="RUST_prompt — Repo-Discovery Engineer",
            kind="prompt",
            part="Part II — Core Discovery & Implementation",
            order=8,
            summary="Rust-specific repo discovery + smallest correct diff, governed by Rust house style + anti-bloat.",
            tags=("rust", "repo-analysis", "implementation"),
        ),
        Artifact(
            id="C-05",
            source_path="prompts/discovery/explore_repo.md",
            title="Terrifyingly Exhaustive Repo Analysis → Service Platform",
            kind="prompt",
            part="Part II — Core Discovery & Implementation",
            order=9,
            summary="Forensic, architectural, operational, semantic analysis producing a devtools corpus for industrializing a repo.",
            tags=("repo-analysis", "service-transformation", "mcp", "knowledge-graph"),
        ),
        Artifact(
            id="M-01",
            source_path="prompts/implementation/restore_simple_openai.md",
            title="Restore Simple — OpenAI",
            kind="prompt",
            part="Part III — Multimodal & Constraint-Matrix Prompts",
            order=10,
            summary="Metadata vector + constraint matrix → hyperspecific reconstruction prompt for conservation-grade restoration.",
            tags=("image-restoration", "multimodal", "constraints"),
        ),
        # Extreme combos
        Artifact(
            id="EC-01",
            source_path="prompts/implementation/omni_agent_platform.md",
            title="OMNI AGENT PLATFORM — Repo → Service → MCP → Agent Ecosystem",
            kind="prompt",
            part="Part IV — Extreme Combos (Production Platformization)",
            order=11,
            summary="Mega-combo prompt: repo forensics → service design → MCP tooling → agent orchestration → KG → hardening.",
            tags=("combo", "repo-analysis", "mcp", "agent-systems", "knowledge-graph"),
        ),
        Artifact(
            id="EC-02",
            source_path="prompts/implementation/evidence_driven_implementation.md",
            title="Evidence-Driven Implementation — Smallest Correct Diff (Python/Rust gated)",
            kind="prompt",
            part="Part IV — Extreme Combos (Production Platformization)",
            order=12,
            summary="Execution prompt for minimal diffs with explicit evidence/hypothesis loops and language gates.",
            tags=("combo", "implementation", "diff-discipline"),
        ),
        Artifact(
            id="EC-03",
            source_path="prompts/implementation/mcp_server_factory.md",
            title="MCP Server Factory — Tool Suite Design + Implementation",
            kind="prompt",
            part="Part IV — Extreme Combos (Production Platformization)",
            order=13,
            summary="Schema-first MCP tool suite design with safety, error models, tests, and ops handoff.",
            tags=("combo", "mcp", "tooling", "security", "testing"),
        ),
        Artifact(
            id="EC-04",
            source_path="prompts/implementation/prompt_library_composer.md",
            title="Prompt Library Composer — Component Extraction + Synthesis",
            kind="prompt",
            part="Part IV — Extreme Combos (Production Platformization)",
            order=14,
            summary="Meta prompt to extract a component catalog, find gaps, and synthesize coherent new prompts.",
            tags=("combo", "meta", "prompt-engineering"),
        ),
        Artifact(
            id="EC-05",
            source_path="prompts/implementation/multimodal_restoration_pipeline.md",
            title="Multimodal Restoration Pipeline — Restore Simple × Engineering × Colab",
            kind="prompt",
            part="Part III — Multimodal & Constraint-Matrix Prompts",
            order=15,
            summary="End-to-end restoration + reproducible batch pipeline + notebook plan + evaluation rubric.",
            tags=("combo", "multimodal", "pipelines", "colab"),
        ),
        Artifact(
            id="EC-06",
            source_path="prompts/implementation/service_industrializer.md",
            title="Service Industrializer — Exhaustive but Disciplined",
            kind="prompt",
            part="Part IV — Extreme Combos (Production Platformization)",
            order=16,
            summary="Exhaustive repo→service prompt with evidence ledger, speculation firewall, abstraction budgets, termination gates.",
            tags=("combo", "service-transformation", "restraint"),
        ),
        Artifact(
            id="EC-07",
            source_path="prompts/execution/agent_testing_eval_gauntlet.md",
            title="Agent Testing & Eval Gauntlet",
            kind="prompt",
            part="Part V — Reliability, Ops, Security",
            order=17,
            summary="Failure modes, coverage matrix, scenarios, metrics, observability, regression/change management for agents.",
            tags=("combo", "agent-systems", "testing", "observability"),
        ),
        Artifact(
            id="EC-08",
            source_path="prompts/security/security_threat_model.md",
            title="Security Threat Model — STRIDE/LINDDUN + Mitigations + Verification",
            kind="prompt",
            part="Part V — Reliability, Ops, Security",
            order=18,
            summary="Threat enumeration with concrete mitigations, verification plan, and a sprint-bounded security backlog.",
            tags=("combo", "security", "threat-model"),
        ),
        Artifact(
            id="EC-09",
            source_path="prompts/migration/migration_and_rollout.md",
            title="Migration & Rollout — Compatibility, Canary, Rollback",
            kind="prompt",
            part="Part V — Reliability, Ops, Security",
            order=19,
            summary="Backward compatibility contract + migration strategy + staged rollout + concrete rollback + validation checklist.",
            tags=("combo", "deployment", "migration", "rollout"),
        ),
        Artifact(
            id="EC-10",
            source_path="prompts/incident_response/incident_response_and_postmortem.md",
            title="Incident Response + Postmortem",
            kind="prompt",
            part="Part V — Reliability, Ops, Security",
            order=20,
            summary="Incident triage → stabilization → diagnosis → resolution → blameless postmortem → prevention backlog.",
            tags=("combo", "ops", "incident-response", "postmortem"),
        ),
        Artifact(
            id="EC-11",
            source_path="prompts/execution/chain_router_and_runbook.md",
            title="Chain Router + Runbook",
            kind="prompt",
            part="Part VI — Orchestration Layer (Chaining Prompts)",
            order=21,
            summary="Routes objectives to the correct extreme prompt sequence and produces a chain graph + step runbook + handoffs.",
            tags=("combo", "orchestration", "router"),
        ),
        Artifact(
            id="EC-12",
            source_path="prompts/execution/handoff_packet_generator.md",
            title="Handoff Packet Generator",
            kind="prompt",
            part="Part VI — Orchestration Layer (Chaining Prompts)",
            order=22,
            summary="Formats minimal, high-fidelity context handoff packets between prompts (no novel decisions).",
            tags=("combo", "orchestration", "handoff"),
        ),
        Artifact(
            id="EC-13",
            source_path="prompts/execution/chain_execution_protocol.md",
            title="Chain Execution Protocol",
            kind="prompt",
            part="Part VI — Orchestration Layer (Chaining Prompts)",
            order=23,
            summary="Defines chain state model, artifact naming, approval gates, quality gates, stop conditions, recovery/retry.",
            tags=("combo", "orchestration", "protocol", "governance"),
        ),
    ]

    # 1) TOC / Catalog / Ontology / Book
    write_text(BOOK_DIR / "TOC.md", render_toc(artifacts))
    write_text(BOOK_DIR / "CATALOG.md", render_catalog(artifacts))
    write_text(BOOK_DIR / "ONTOLOGY.md", render_ontology_md(artifacts))
    write_text(BOOK_DIR / "BOOK.md", render_book_md(artifacts))

    # 3) Machine-readable ontology exports
    ontology: dict[str, Any] = {
        "version": "1.0",
        "generated": _today(),
        "artifact_count": len(artifacts),
        "artifacts": [
            {
                "id": a.id,
                "title": a.title,
                "kind": a.kind,
                "part": a.part,
                "order": a.order,
                "source_path": a.source_path.replace("\\", "/"),
                "tags": list(a.tags),
                "summary": a.summary,
            }
            for a in sorted(artifacts, key=lambda x: x.order)
        ],
        "relationship_types": [
            "COMBINES_WITH",
            "ENFORCES",
            "ROUTES_TO",
            "PRECEDES",
            "PRODUCES_INPUT_FOR",
        ],
        "domain_hints": sorted({t for a in artifacts for t in a.tags}),
    }

    write_text(ONTOLOGY_DIR / "prompt_ecosystem.json", json.dumps(ontology, indent=2))

    # Minimal JSON-LD framing (lightweight; primarily for graph tooling compatibility)
    jsonld = {
        "@context": {
            "id": "@id",
            "type": "@type",
            "Artifact": "https://example.org/prompt-ontology#Artifact",
            "title": "https://purl.org/dc/terms/title",
            "kind": "https://example.org/prompt-ontology#kind",
            "part": "https://example.org/prompt-ontology#part",
            "order": "https://example.org/prompt-ontology#order",
            "sourcePath": "https://example.org/prompt-ontology#sourcePath",
            "tags": "https://example.org/prompt-ontology#tags",
            "summary": "https://purl.org/dc/terms/description",
        },
        "@graph": [
            {
                "id": f"artifact:{a.id}",
                "type": "Artifact",
                "title": a.title,
                "kind": a.kind,
                "part": a.part,
                "order": a.order,
                "sourcePath": a.source_path.replace("\\", "/"),
                "tags": list(a.tags),
                "summary": a.summary,
            }
            for a in sorted(artifacts, key=lambda x: x.order)
        ],
    }
    write_text(ONTOLOGY_DIR / "prompt_ecosystem.jsonld", json.dumps(jsonld, indent=2))

    # Simple YAML export (no external dependency)
    yaml_lines: list[str] = [
        f"version: '1.0'",
        f"generated: '{_today()}'",
        f"artifact_count: {len(artifacts)}",
        "artifacts:",
    ]
    for a in sorted(artifacts, key=lambda x: x.order):
        title = _yaml_escape(a.title)
        part = _yaml_escape(a.part)
        summary = _yaml_escape(a.summary)
        source_path = a.source_path.replace("\\", "/")
        yaml_lines.extend(
            [
                f"  - id: '{a.id}'",
                f"    title: '{title}'",
                f"    kind: '{a.kind}'",
                f"    part: '{part}'",
                f"    order: {a.order}",
                f"    source_path: '{source_path}'",
                "    tags:",
                *[f"      - '{_yaml_escape(t)}'" for t in a.tags],
                f"    summary: '{summary}'",
            ]
        )
    write_text(ONTOLOGY_DIR / "prompt_ecosystem.yaml", "\n".join(yaml_lines) + "\n")

    print(f"Built book in: {BOOK_DIR}")


if __name__ == "__main__":
    build()
