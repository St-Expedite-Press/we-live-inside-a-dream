---
title: "COLAB NOTEBOOK HOUSE STYLE"
type: "guidelines"
tags:
  - "python"
  - "colab"
  - "jupyter"
  - "notebooks"
  - "reproducibility"
created: "2026-02-05"
---

# COLAB NOTEBOOK HOUSE STYLE

A project-agnostic house style for **Google Colab / Jupyter notebooks**.

Primary goals:

- Reproducible execution from a cold start
- Minimal hidden state and “works on my runtime” drift
- Notebook-as-document: readable narrative + verifiable results

This profile assumes Python, but most rules apply to any notebook language.

## Table of contents

- [Core doctrine](#core-doctrine)
- [Notebook structure](#notebook-structure)
- [Cell hygiene](#cell-hygiene)
- [Dependencies & environment](#dependencies--environment)
- [Data, paths, and secrets](#data-paths-and-secrets)
- [Outputs & artifacts](#outputs--artifacts)
- [Performance & cost control](#performance--cost-control)
- [Collaboration & review](#collaboration--review)
- [House self-audit (before sharing)](#house-self-audit-before-sharing)

---

## Core doctrine

- **C-00 — Restartability**: the notebook must run top-to-bottom on a fresh runtime without manual fixes.
- **C-01 — Explicit state**: no reliance on hidden variables; make inputs/outputs clear.
- **C-02 — Narrative + evidence**: every section should state intent and show results.
- **C-03 — Boundaries**: keep exploration in the notebook; keep reusable logic in `.py` modules.

---

## Notebook structure

- **S-01 — Use a visible outline** with headings:
  1) Setup
  2) Config
  3) Data acquisition
  4) Processing / training
  5) Evaluation
  6) Export / conclusion
- **S-02 — Put all configuration in one place** near the top (constants, paths, toggles).
- **S-03 — Separate “demo” from “library”**:
  - demonstration steps in the notebook
  - reusable functions/classes in importable modules
- **S-04 — Keep the first 1–3 cells fast** so a reviewer can validate setup quickly.

---

## Cell hygiene

- **H-01 — One intent per cell**: cells should be small enough to re-run safely.
- **H-02 — Idempotent cells**: re-running a cell should not corrupt state (avoid appending to lists, re-registering handlers, duplicating downloads).
- **H-03 — No implicit ordering tricks**: do not rely on “I ran cell 17 earlier”. If ordering matters, refactor.
- **H-04 — Avoid large hidden globals**: prefer returning values from functions or using a small config object.
- **H-05 — Use markdown cells for explanation** rather than long comment blocks.

---

## Dependencies & environment

- **E-01 — Pin when it matters**: if results depend on versions, pin them.
- **E-02 — Consolidate installs**: one “Install dependencies” cell, not scattered `pip install`.
- **E-03 — Silence is suspicious**: after installs, show versions (`pip show`, `python -V`, key libs `__version__`).
- **E-04 — Avoid notebook magics as core logic**: `%cd`, `%env`, shell pipelines are okay for setup, but keep core computation in Python.
- **E-05 — Determinism**: set random seeds; document remaining nondeterminism (GPU ops, data order).

---

## Data, paths, and secrets

- **D-01 — Never hard-code user-specific paths**.
  - Prefer `pathlib.Path` and a single `DATA_DIR` variable.
  - If using Drive: mount once, validate directory exists, and document expected structure.
- **D-02 — Treat downloads as cached steps**:
  - checksum when feasible
  - skip download if file already exists
- **D-03 — Secrets**:
  - do not paste API keys in cells
  - use Colab secrets/env vars
  - ensure outputs do not print secrets
- **D-04 — Explicit dataset provenance**: URLs, versions, or commit hashes.

---

## Outputs & artifacts

- **O-01 — Keep outputs intentional**: clear noisy outputs before sharing.
- **O-02 — Don’t store huge outputs** (massive logs, images) inside the notebook file.
- **O-03 — Save artifacts explicitly**:
  - write models/results/plots to a clearly named output directory
  - include a “Export artifacts” section
- **O-04 — Prefer deterministic filenames** (include timestamps only when necessary).

---

## Performance & cost control

- **P-01 — Know your runtime**: print GPU/TPU details when relevant.
- **P-02 — Avoid repeated expensive work**: cache intermediate results on disk.
- **P-03 — Bound your experiments**: small sample runs first; escalate only when validated.

---

## Collaboration & review

- **R-01 — Make review easy**: add a short “How to run” section near the top.
- **R-02 — Avoid local-only assumptions**: no references to unshared files.
- **R-03 — Keep diffs clean**:
  - consistent cell ordering
  - remove dead cells
  - clear outputs before committing (unless outputs are part of the deliverable)

---

## House self-audit (before sharing)

1. Can I **Runtime → Restart and run all** successfully?
2. Are installs/configuration in **one place**?
3. Are there any cells that are **not idempotent**?
4. Are **paths portable** and secrets excluded?
5. Are outputs **minimal and intentional**?
