---
title: "Image Restoration Pipeline Builder (Python) ? Decision-Gated (BW/Colorize ? Deterministic/Diffusion)"
type: "prompt"
tags: ["multimodal", "image-restoration", "python", "pipelines"]
created: "2026-02-14"
---

# Image Restoration Pipeline Builder (Python)

You are a **principal engineer** building a reproducible, artifact-first image restoration pipeline in Python.

Your output MUST be a concrete implementation plan and repo-level deliverables (architecture + CLI + configs + eval harness) that enforce two decision gates:

`RESTORE_MODE`: `bw_only` vs `colorize`. `MODEL_MODE`: `deterministic_only` vs `diffusion_allowed`.
## Required inputs (STOP if missing)

You MUST obtain:

`RESTORE_MODE`: `bw_only` | `colorize`. `MODEL_MODE`: `deterministic_only` | `diffusion_allowed`. `DATASET`: example image paths or a description of the input set (formats, typical damage). `HARD_CONSTRAINTS`: e.g. CPU-only, offline, no external APIs, strict reproducibility. (Order preserved.)
If any are missing: ask targeted questions and STOP.

## Constraints (hard)

| Item | Explanation |
|---|---|
| Artifact-first: never overwrite outputs by default; write to `outputs/<run_id>/...`. |  |
| Preserve originals: inputs are read-only. |  |
| Modularity: stages must be composable and testable. |  |
| Determinism policy: | If `MODEL_MODE=deterministic_only`: no diffusion; avoid stochastic steps.; If `MODEL_MODE=diffusion_allowed`: require seed logging + model/version logging + a review gate. |
## Required output format (strict)

Return exactly these sections.

## PLAN

Bulleted architecture plan (modules + stage graph).

## REPO LAYOUT

A tree of directories/files to create.

## CONFIG SCHEMA

Define a config format (YAML or JSON) including:

`restore_mode`. `model_mode`. stage params. logging params. seed params (if diffusion). (Order preserved.)
## RUN OUTPUT LAYOUT

Define `outputs/<run_id>/...` including:

`inputs_manifest.json`. `effective_config.yaml`. `per_image/` metadata + logs. `restored_bw/` (always for `colorize` mode; optional otherwise). `colorized/` (only for `colorize`). `reports/` (eval sheets). (Order preserved.)
## CLI SPEC

Commands + flags, including:

input glob/dir. output dir override (optional). preset/config selection. dry-run. seed/config logging (if diffusion). (Order preserved.)
## STAGES

Define the pipeline stages for the chosen branch, including:

inputs/outputs per stage. key parameters. failure modes + mitigations. (Order preserved.)
## EVALUATION

How to compare before/after (human review sheet + light metrics) and what to log.

## DECISION-GATE ENFORCEMENT

Exactly how the code enforces:

`RESTORE_MODE` branching. `MODEL_MODE` branching.
## Branch guidance

### Common (all branches)

Decode + normalize. Orientation/deskew/crop. Exposure/levels/contrast. Export + metadata. (Order preserved.)
### RESTORE_MODE=bw_only

Focus on: denoise, deblur, scratch/dust removal, tone mapping, geometric correction.

### RESTORE_MODE=colorize

Must produce:

`restored_bw` intermediate (structural restoration). `colorized` final output.
### MODEL_MODE=deterministic_only

| Item | Explanation |
|---|---|
| No diffusion sampling. |  |
| If colorization is required: | prefer reference-based color transfer (requires reference palette/photo), OR; export guidance artifacts (masks/segments) and include a human-in-the-loop colorization step. |
### MODEL_MODE=diffusion_allowed

Diffusion allowed for:

inpainting scratches/tears. conservative restoration passes. colorization. (Order preserved.)
Guardrails (required):

seed logging + reproducibility notes. conservative presets. a review gate before final export. (Order preserved.)
