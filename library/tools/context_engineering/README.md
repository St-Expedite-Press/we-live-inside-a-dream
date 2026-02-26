# Context Engineering: Non-Destructive Prompt Improvement

This folder contains an additive workflow for analyzing and improving prompts in this repo **without editing originals**.

## Generate improvements

From the repo root:

```powershell
python library/tools/context_engineering/generate_prompt_improvements.py --root library
```

Outputs are written to:

`library/improvements/` (per-prompt folders with `original.md`, analysis, improved variants, notes, evaluation, metadata). `library/improvements/_inventory.json` (index of discovered prompt files).
## Options

| Item | Explanation |
|---|---|
| Dry run: `python library/tools/context_engineering/generate_prompt_improvements.py --root library --dry-run` |  |
| Include README.md files: `--include-readmes` |  |
| Overwrite mode: | Default `timestamp`: if an output file exists, write a new `__generated_...` file instead.; `skip`: never write if a target exists. |
```powershell
python library/tools/context_engineering/generate_prompt_improvements.py --root library --on-exists skip
```
