# Rust Path: Image Restoration Pipeline (Decision-Gated)

Use this path to build a **Rust-first** pipeline (CLI + artifact discipline) with explicit decision gates:

- Black-and-white only vs Colorization
- Diffusion use vs Deterministic-only

Reality constraint:

- If `MODEL_MODE=diffusion_allowed`, the fastest-to-ship architecture is often **Rust orchestration + a Python diffusion worker** (or a model service). Keep diffusion behind a clean boundary.

## Step 0 ? Decide the gates (STOP if unknown)

- `RESTORE_MODE`: `bw_only` | `colorize`
- `MODEL_MODE`: `deterministic_only` | `diffusion_allowed`
- `TARGET`: `cli_only` | `cli_plus_notebook` (notebook is typically Python even if Rust orchestrates)
- `HARD_CONSTRAINTS`: offline, CPU-only, no external APIs, etc.

## Step 1 ? Spec + constraint matrix

Run: `library/prompts/implementation/restore_simple_openai.md`

Artifacts:

- `inputs/restore_spec.md`
- `inputs/sample_images/`

## Step 2 ? Generate a governed runbook

Run: `library/prompts/execution/image_restoration_pipeline_router.md`

Artifacts:

- `runbook.md`
- `decision_record.md`

Tip: use templates from `library/paths/_templates/`.

## Step 3 ? Build the pipeline (Rust)

Run: `library/prompts/implementation/image_restoration_pipeline_builder_rust.md`

Minimum deliverables:

- workspace crates
- `restore-cli` (CLI via `clap`)
- `configs/`
- `outputs/` (run artifacts; never overwrite by default)
- `eval/`

## Step 4 ? Optional hybrid diffusion worker

If `MODEL_MODE=diffusion_allowed`:

- implement the worker boundary (subprocess, IPC, or HTTP)
- enforce seed control + conservative presets + human review gate

## Step 5 ? Chain governance (recommended)

- `library/prompts/execution/chain_execution_protocol.md`
