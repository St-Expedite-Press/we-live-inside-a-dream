# Prompt Ecosystem Library

`library/` is the ship-ready prompt ecosystem: canonical prompts, an indexed book, ontology exports, and tooling to keep the whole system coherent as it evolves.

## Contents

Canonical prompts and guidelines: `library/graph/nodes/`. Graph workflows and rules: `library/graph/workflows/` and `library/graph/rules/`. Book index and ontology exports: `library/book/`. Tools (build and analysis helpers): `library/tools/`. Docs and indexes: `library/docs/`, including the mental model at `library/docs/repo_mental_model.md` and the forensic audit agent spec at `library/docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md`. Research notes: `library/research/`. (Order preserved.)
## Entry points

Read: `library/book/BOOK.md`. Run: `python library/library.py build-book`.
## Common tasks

| Item | Explanation |
|---|---|
| Rebuild book + ontology exports: | `python library/book/_build_book.py`; or `python library/library.py build-book` |
| Generate improvement artifacts (writes to `library/improvements/`): | `python library/library.py improve -- --dry-run` |
## Conventions

`library/graph/nodes/` is the canonical node source of truth. `library/graph/workflows/` defines orchestration (including Python and Rust branches). `library/book/` is navigation and export output. Generated artifacts should go under `library/improvements/` (ignored by git). (Order preserved.)
