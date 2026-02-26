# Python Path: Image Restoration Pipeline (Decision-Gated)

Use this path to build a **Python image restoration pipeline** with explicit decision gates:

Black-and-white only vs Colorization. Diffusion use vs Deterministic-only.
## Step 0 ? Decide the gates (STOP if unknown)

`RESTORE_MODE`: `bw_only` | `colorize`. `MODEL_MODE`: `deterministic_only` | `diffusion_allowed`. `TARGET`: `cli_only` | `cli_plus_notebook`. `BATCH_SIZE`: approximate images per run. `HARD_CONSTRAINTS`: CPU-only, offline, no external APIs, strict reproducibility, etc. (Order preserved.)
If any are missing: ask for them and STOP.

## Step 1 ? Spec + constraint matrix

Run: `library/graph/nodes/implementation/restore_simple_openai.md`

Artifacts:

`inputs/restore_spec.md`. `inputs/sample_images/` (small representative set).
## Step 2 ? Generate a governed runbook

Run: `library/graph/nodes/execution/image_restoration_pipeline_router.md`

Artifacts:

`runbook.md` (steps + outputs + stop conditions). `decision_record.md` (final gate choices).
Tip: use templates from `library/graph/workflows/templates/`.

## Step 3 ? Build the pipeline (Python)

Run: `library/graph/nodes/implementation/image_restoration_pipeline_builder_python.md`

Minimum deliverables:

`pipeline/` (library code). `cli/` (entrypoint). `configs/` (presets per gate combination). `outputs/` (run artifacts; never overwrite by default). `eval/` (review sheet + light metrics). (Order preserved.)
## Step 4 ? Notebook packaging (optional)

If `TARGET=cli_plus_notebook`, run:

`library/graph/nodes/implementation/multimodal_restoration_pipeline.md`.
## Step 5 ? Chain governance (recommended)

If you are chaining multiple prompts/agents, wrap with:

`library/graph/nodes/execution/chain_execution_protocol.md`.
## Canonical decision rules

### RESTORE_MODE=bw_only

Output is grayscale restoration only. Focus on: denoise, deblur, scratch/dust removal, levels/contrast, geometric correction.
### RESTORE_MODE=colorize

Must produce a `restored_bw/` intermediate and a final `colorized/` output.
### MODEL_MODE=deterministic_only

No diffusion. If colorization is required: reference-based transfer OR human-in-the-loop.
### MODEL_MODE=diffusion_allowed

Diffusion allowed, but must log seeds + model versions and include a review gate.
