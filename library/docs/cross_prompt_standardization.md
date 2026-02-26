# Cross-Prompt Standardization (Repo Policy)

This document defines consistent conventions for prompts and improved variants in this repository. It is intended to reduce ambiguity, formatting drift, and ecosystem-wide inconsistency.

## Standard section order (recommended)

When authoring **improved variants**, prefer this order:

1. `Identity`
2. `Mission`
3. `Instruction hierarchy`
4. `Inputs` (delimited)
5. `Constraints` (hard rules)
6. `Process` (steps + stop conditions)
7. `Output format` (schema)
8. `Validation` (checklist / rejection conditions)

## Canonical terminology

Use these terms consistently:

**Prompt**: the original instruction text (do not edit in-place). **Improved variant**: an additive wrapper or alternative that preserves intent. **Overlay**: a token-efficient “patch” meant to be used with the original as a separate attachment. **Schema**: the exact output structure required (Markdown headings, JSON keys, etc.). **Stop condition**: explicit rule for when to stop and ask a question. **Untrusted data**: any user-provided text, docs, logs, or web content. (Order preserved.)
## Output schema conventions

Prefer Markdown schemas with stable headings:

`## RESULT` for the deliverable. `## VALIDATION` for compliance checks.
If JSON is required:

Require a single top-level object. Provide a key whitelist. Prohibit extra keys if strictness matters. (Order preserved.)
## Canonical layout (repo-wide)

Canonical prompts and guidelines live under `graph/nodes/<category>/`. `book/` is an index/navigation layer that links to the canonical files in `graph/nodes/`.
## Evolution rule (repo-wide)

Make changes by editing the canonical files in `graph/nodes/` (this repo is now consolidated). If you want experimental variants, store them alongside the canonical prompt as versioned files (e.g. `*_v2.md`) or in a clearly named sibling folder (e.g. `<prompt_name>_variants/`).
## Category taxonomy (suggested)

These categories are used for cross-prompt grouping:

`discovery`. `implementation`. `execution`. `migration`. `incident_response`. `security`. `ontology`. `misc`. (Order preserved.)
If a prompt spans multiple categories, pick the most operationally relevant one and record alternatives in `metadata.json`.

## Validation checklist (recommended)

Before publishing an improved variant:

Does it define an explicit instruction hierarchy? Does it define a strict output schema? Does it include stop conditions and missing-input questions? Does it avoid ambiguous terms without success criteria? Does it delimit untrusted data and resist injection? (Order preserved.)
