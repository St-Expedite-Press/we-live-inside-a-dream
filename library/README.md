# Prompt Ecosystem Library

`library/` is the ship-ready prompt ecosystem: canonical prompts, an indexed book, ontology exports, and tooling to keep the whole system coherent as it evolves.

## Contents

Canonical prompts and guidelines: `library/prompts/`. Book index and ontology exports: `library/book/`. Tools (build and analysis helpers): `library/tools/`. Docs and indexes: `library/docs/`, including the mental model at `library/docs/repo_mental_model.md` and the forensic audit agent spec at `library/docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md`. Research notes: `library/research/`. (Order preserved.)
## Entry points

Read: `library/book/BOOK.md`. Run: `python library/library.py build-book`.
## Common tasks

| Item | Explanation |
|---|---|
| Rebuild book + ontology exports: | `python library/book/_build_book.py`; or `python library/library.py build-book` |
| Generate improvement artifacts (writes to `library/improvements/`): | `python library/library.py improve -- --dry-run` |
## Conventions

`library/prompts/` is the source of truth. `library/book/` is navigation: it links to canonical prompts and exports a machine-readable ontology. Generated artifacts should go under `library/improvements/` (ignored by git). (Order preserved.)
