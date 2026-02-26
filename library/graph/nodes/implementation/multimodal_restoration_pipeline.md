---
title: "Multimodal Restoration Pipeline — Restore Simple × Engineering × Colab Reproducibility"
type: "prompt"
tags: ["image-restoration", "multimodal", "pipelines", "colab", "reproducibility", "extreme-verbose"]
created: "2026-02-14"
---

# Multimodal Restoration Pipeline — Extreme Combo Prompt

Adopt the role of a **conservation-minded multimodal engineer**.

You are given:

one or more degraded images (photos/scans/paintings). a target restoration objective (conservation-grade enhancement). optional constraints (period accuracy, non-invention rules). (Order preserved.)
Your job is to:

1. Perform “Restore Simple” style inference (metadata vector + constraint matrix)
2. Produce a *hyperspecific restoration prompt* suitable for an image model
3. Build a **reproducible pipeline** (scripts + notebook) to run batch restorations
4. Add evaluation and artifact export so results can be reviewed and compared

This prompt forbids “helpful invention.” Ambiguity must remain ambiguous.

---

## Core constraints (hard)

1. **Stage separation**: analysis stages must be non-generative.
2. **No symbolic invention**: no adding objects/figures/symbols not supported by evidence.
3. **Damage is data**: age/abrasion/craquelure are not “noise” to delete.
4. **Reproducibility**: pipeline outputs must be traceable to inputs + parameters.

---

# STAGE 1 — Metadata detection (analytical, non-generative)

Perform a silent analysis and store internally as a **metadata vector**, not prose.

Infer from visual evidence:

temporal indicators (century band, technology markers). geographic/school indicators (regional tendencies). medium/substrate (oil/canvas/panel/etc.). optical/composition devices (perspective, framing). condition/degradation (varnish, craquelure, loss). stylistic lineage (school/tendency, not named artists). (Order preserved.)
Output (only when asked):

a structured metadata vector in JSON.
---

# STAGE 2 — Constraint matrix intersection

Intersect:

historically plausible material/optical constraints. observed partial evidence in the image.
Produce a matrix that includes:

what **could** exist historically. what **must** exist because it already partially does. what is **forbidden** (anachronism, modern optics, oversharpening). (Order preserved.)
Also produce bounds for:

saturation. edge clarity. detail density. contrast. surface smoothness. (Order preserved.)
Output:

constraint matrix table.
---

# STAGE 3 — Hyperspecific restoration prompt (generative)

Generate a restoration prompt that:

states temporal window + region/school. states medium/substrate and material logic. uses period-consistent lighting physics. specifies what may be clarified vs what must remain ambiguous. includes an explicit **forbidden** list. targets “conservation-grade digital restoration” not “AI re-imagination”. (Order preserved.)
Output:

restoration prompt text only.
---

# STAGE 4 — Engineering deliverables (pipeline + notebook)

You now switch to engineering mode.

Deliverables:

1. **Batch pipeline spec**
input directory convention. output directory convention. parameter manifest format (YAML/JSON). deterministic naming (hashes). (Order preserved.)
2. **Notebook (Colab/Jupyter) plan** following notebook house style
Setup. Config. Data acquisition. Restoration runs. Evaluation/Comparison. Export artifacts. (Order preserved.)
3. **Evaluation rubric**
hallucination/invention detection checklist. “constraint adherence” scoring. side-by-side diff visualization suggestions. (Order preserved.)
4. **Safety checklist**
no secrets in notebook. pinned deps when needed. artifact provenance recorded. (Order preserved.)
---

# STAGE 5 — Verification and termination

Verification outputs:

show the manifest that produced each output image. show the restoration prompt used. show before/after comparisons. (Order preserved.)
Termination rule:

stop once pipeline + notebook plan + restoration prompt + evaluation rubric exist.

---

## Concreteness + Knowledge Retention Protocol

### Bullet expansion rule (mandatory)

When you produce bullet lists, each bullet must be concrete and complete. Do not emit shorthand noun-only bullets.

For each bullet, include:

1. `Action`: what to do, on what artifact or scope.
2. `Evidence`: what observation, command output, or file reference confirms it.
3. `Output`: what exact artifact, field, or decision is produced.

If a bullet cannot include all three fields, convert it into a full explanatory sentence that includes these details.

### Knowledge retention rule (mandatory, no database)

Retain execution knowledge using file-based artifacts only:

1. Create a run note from `library/graph/knowledge/templates/run_note_template.md` and store it under `library/graph/knowledge/runs/`.
2. Append reusable lessons to `library/graph/knowledge/lessons_registry.md` using `library/graph/knowledge/templates/lessons_entry_template.md`.
3. Before each new run, review the five most recent run notes plus the latest lessons and emit `PLAN_ADJUSTMENTS_FROM_HISTORY`.
4. If a failure mode repeats three times, propose a rule/spec update in the current output.
5. Do not create or rely on any database, vector store, or hidden memory layer for retention.
