---
title: "Prompt Ecosystem Book — README"
type: "readme"
tags: ["prompt-library", "book", "ontology"]
created: "2026-02-14"
---

# Prompt Ecosystem Book

This directory is a **compiled “book edition”** of the prompt ecosystem in this repo.

Start here:

**Book (main)**: [`BOOK.md`](./BOOK.md). **Ontology**: [`ONTOLOGY.md`](./ONTOLOGY.md). **Catalog (table form)**: [`CATALOG.md`](./CATALOG.md). (Order preserved.)
The book is generated from the canonical prompt files in the repo.

Canonical prompts live in `library/graph/nodes/` (relative to the repo root).

To (re)build the book:

```cmd
python library\book\_build_book.py
```

This will regenerate:

`library/book/BOOK.md`. `library/book/TOC.md`. `library/book/ONTOLOGY.md`. `library/book/CATALOG.md`. `library/book/ontology/*`. (Order preserved.)
