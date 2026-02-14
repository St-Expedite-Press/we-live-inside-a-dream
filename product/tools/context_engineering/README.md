# Context Engineering: Non-Destructive Prompt Improvement

This folder contains an additive workflow for analyzing and improving prompts in this repo **without editing originals**.

## Generate improvements

From the repo root:

```powershell
python product/tools/context_engineering/generate_prompt_improvements.py --root product
```

Outputs are written to:

- `product/improvements/` (per-prompt folders with `original.md`, analysis, improved variants, notes, evaluation, metadata)
- `product/improvements/_inventory.json` (index of discovered prompt files)

## Options

- Dry run: `python product/tools/context_engineering/generate_prompt_improvements.py --root product --dry-run`
- Include README.md files: `--include-readmes`
- Overwrite mode:
  - Default `timestamp`: if an output file exists, write a new `__generated_...` file instead.
  - `skip`: never write if a target exists.

```powershell
python product/tools/context_engineering/generate_prompt_improvements.py --root product --on-exists skip
```
