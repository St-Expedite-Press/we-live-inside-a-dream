# Prompt Ecosystem Library

`library/` is the ship-ready prompt ecosystem: canonical prompts, an indexed book, ontology exports, and tooling to keep the whole system coherent as it evolves.

## Contents

- Canonical prompts/guidelines: `library/prompts/`
- Book index + ontology exports: `library/book/`
- Tools (build + analysis helpers): `library/tools/`
- Docs + indexes: `library/docs/`
- Research notes: `library/research/`

## Entry points

- Read: `library/book/BOOK.md`
- Run: `python library/library.py build-book`

## Common tasks

- Rebuild book + ontology exports:
  - `python library/book/_build_book.py`
  - or `python library/library.py build-book`
- Generate improvement artifacts (writes to `library/improvements/`):
  - `python library/library.py improve -- --dry-run`

## Conventions

- `library/prompts/` is the source of truth.
- `library/book/` is navigation: it links to canonical prompts and exports a machine-readable ontology.
- Generated artifacts should go under `library/improvements/` (ignored by git).
