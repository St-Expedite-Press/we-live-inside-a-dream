# Rust Path: Image Restoration Pipeline (Decision-Gated)

Use this path when you want a **Rust-first** pipeline (CLI + artifact discipline) with explicit decision points:

1) **Black-and-white only** vs **Colorization**
2) **Diffusion model use** vs **Deterministic-only**

Important reality constraint:

- If `MODEL_MODE=diffusion_allowed`, a practical architecture is often **Rust orchestration + Python diffusion worker** (or an external model service). Pure-Rust diffusion is possible but usually slower to ship.

## Step 0 — Inputs you must decide (stop if unknown)

- `RESTORE_MODE`: `bw_only` | `colorize`
- `MODEL_MODE`: `deterministic_only` | `diffusion_allowed`
- `TARGET`: `cli_only` | `cli_plus_notebook` (notebook typically Python even if Rust orchestrates)
- `HARD_CONSTRAINTS`: e.g. “no GPU”, “no network”, “no external APIs”

## Step 1 — Spec + constraint matrix

Run: `library/prompts/implementation/restore_simple_openai.md`

Artifacts:

- `inputs/restore_spec.md`
- `inputs/sample_images/`

## Step 2 — Choose a governed chain

Run: `library/prompts/execution/image_restoration_pipeline_router.md`

Artifacts:

- `runbook.md`
- `decision_record.md`

## Step 3 — Build the pipeline (Rust)

Run: `library/prompts/implementation/image_restoration_pipeline_builder_rust.md`

Artifacts (minimum):

- `crates/` (workspace)
- `bin/restore-cli` (CLI entrypoint via `clap`)
- `configs/` (mode presets)
- `outputs/` (artifact directory, never overwrite by default)
- `eval/` (before/after sheets + metrics)

## Step 4 — Optional hybrid diffusion worker

If `MODEL_MODE=diffusion_allowed`:

- implement a worker boundary (CLI subcommand, IPC, or HTTP) and make it swappable
- enforce: seed control + conservative presets + explicit human review gate

## Step 5 — Governance for iteration

- `library/prompts/execution/chain_execution_protocol.md`

