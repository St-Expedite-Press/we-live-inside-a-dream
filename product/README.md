# Prompt Ecosystem (Product)

This `product/` directory is the consolidated, shippable prompt ecosystem:

- Canonical prompts/guidelines: `product/prompts/`
- Book index + ontology exports: `product/book/`
- Tools (build + analysis helpers): `product/tools/`
- Docs: `product/docs/`
- Research notes: `product/research/`

## Common tasks

- Open the book: `product/book/BOOK.md`
- Rebuild the book + ontology exports:
  - `python product/book/_build_book.py`
  - or `python product/product.py build-book`
- Generate prompt improvement artifacts (non-destructive, outputs to `product/improvements/`):
  - `python product/tools/context_engineering/generate_prompt_improvements.py --root product`
  - or `python product/product.py improve -- --dry-run`
