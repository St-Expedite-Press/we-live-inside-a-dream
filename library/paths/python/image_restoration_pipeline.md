# Python Path: Image Restoration Pipeline (Decision-Gated)

Use this path when you want to **build a Python-based image restoration pipeline** with explicit decision points:

1) **Black-and-white only** vs **Colorization**
2) **Diffusion model use** vs **Deterministic-only**

## Step 0 — Inputs you must decide (stop if unknown)

Answer these before implementation:

- `RESTORE_MODE`: `bw_only` | `colorize`
- `MODEL_MODE`: `deterministic_only` | `diffusion_allowed`
- `TARGET`: `cli_only` | `cli_plus_notebook`
- `BATCH_SIZE`: approximate images per run
- `HARD_CONSTRAINTS`: e.g. “no GPU”, “airgapped”, “no external APIs”, “reproducible outputs”

If any of these are missing, stop and ask for them.

## Step 1 — Spec + constraint matrix

Run: `library/prompts/implementation/restore_simple_openai.md`

Artifacts:

- `inputs/restore_spec.md` (goal, constraints, acceptance criteria)
- `inputs/sample_images/` (a small representative set)

## Step 2 — Choose a governed chain

Run: `library/prompts/execution/image_restoration_pipeline_router.md`

Artifacts:

- `runbook.md` (exact steps, outputs, stop conditions)
- `decision_record.md` (RESTORE_MODE + MODEL_MODE choices)

## Step 3 — Build the pipeline (Python)

Run: `library/prompts/implementation/image_restoration_pipeline_builder_python.md`

Artifacts (minimum):

- `pipeline/` (library code)
- `cli/` entrypoint (Typer/argparse)
- `configs/` (presets per mode)
- `outputs/` (artifact directory, never overwrite by default)
- `eval/` (small eval harness + comparison sheets)

## Step 4 — Multimodal + notebook packaging (optional)

If `TARGET=cli_plus_notebook`, run:

- `library/prompts/implementation/multimodal_restoration_pipeline.md`

## Step 5 — Governance for iteration

If you will iterate with multiple prompts/agents, wrap with:

- `library/prompts/execution/chain_execution_protocol.md`

## Decision rules (canonical)

### RESTORE_MODE=bw_only

- Output is grayscale restoration only.
- Focus on: denoise, deblur, scratch/dust removal, contrast/levels, geometric correction.
- No colorization deliverables.

### RESTORE_MODE=colorize

- Must still produce a “restored luminance” intermediate (pre-colorization).
- Output both:
  - `restored_bw/` (best reconstruction of structure/contrast)
  - `colorized/` (final color output)

### MODEL_MODE=deterministic_only

- No stochastic sampling; no diffusion.
- If any ML is used, it must be deterministic inference (fixed weights, fixed preprocessing) and documented.

### MODEL_MODE=diffusion_allowed

- Diffusion can be used for inpainting/scratch removal/colorization, but:
  - require seed control
  - require “conservative mode” presets
  - require a “no hallucinated detail” warning + review step

