#!/usr/bin/env python3
from pathlib import Path
import sys

repo = Path(__file__).resolve().parents[3]
graph = repo / "library" / "graph"
roots = [graph / "workflows", graph / "protocols", graph / "knowledge"]
search_files = [p for p in graph.rglob("*.md")]
orphans = []
for r in roots:
    for d in sorted(r.rglob("*.md")):
        rel = d.relative_to(repo).as_posix()
        if d.name.lower() == "readme.md":
            continue
        found = False
        for s in search_files:
            if s == d:
                continue
            txt = s.read_text(encoding="utf-8", errors="ignore")
            if rel in txt or d.name in txt:
                found = True
                break
        if not found:
            orphans.append(rel)

if orphans:
    print("\n".join(orphans))
    sys.exit(1)
print("orphan graph doc check: ok")
