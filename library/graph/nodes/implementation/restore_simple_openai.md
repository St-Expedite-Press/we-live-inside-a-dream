---
title: "Restore Simple — OpenAI"
source: "Restore Simple-- OpenAI.pdf"
type: "prompt"
tags: ["image-restoration", "upscaling", "prompting"]
created: "2026-02-05"
---

# Restore Simple — OpenAI

Generalized meta‑prompt for **temporal + stylistic inference → hyperspecific reconstruction**.

## Table of contents

[Stage 1: Metadata Detection (Analytical, Non‑Generative)](#stage-1-metadata-detection-analytical-non-generative). [Stage 2: Metadata Matrix Intersection](#stage-2-metadata-matrix-intersection). [Stage 3: Hyperspecific Reconstruction Prompt (Generative)](#stage-3-hyperspecific-reconstruction-prompt-generative). [Final prompt template (copy/paste)](#final-prompt-template-copypaste). (Order preserved.)
---

## Stage 1: Metadata Detection (Analytical, Non‑Generative)

You are presented with an image. **Before any reconstruction or upscaling**, perform a *silent analytical pass* to infer its latent metadata. **Do not modify the image at this stage.**

Infer the following categories using only **visual evidence**, **material logic**, and **art‑historical plausibility**.

### A. Temporal indicators

Probable century range (with confidence band). Pre‑/post‑industrial markers. Lighting technology implied (natural light, candle, oil, gas, electric). Architectural period signals (window type, ceiling, joinery). (Order preserved.)
### B. Geographic / school indicators

Likely regional school(s) (e.g., Netherlandish, Italian, Germanic, Iberian). Climatic implications on light and materials. Cultural norms embedded in dress, posture, or interior layout. (Order preserved.)
### C. Medium & substrate

Medium (oil, tempera, mixed). Support (panel, canvas, vellum, metal). Scale inference (miniature, cabinet painting, altarpiece fragment). (Order preserved.)
### D. Optical & compositional devices

Perspective system (intuitive, linear, mixed). Mirror / convex / reflective logic if present. Framing conventions (roundel, tondo, inset panel). Viewer position implied. (Order preserved.)
### E. Condition & degradation

Evidence of glazing, varnish, or later restoration. Craquelure type (age‑consistent vs mechanical). Pigment fade patterns. Abrasion, loss, or overcleaning evidence. Compression artifacts vs original painterly softness. (Order preserved.)
### F. Stylistic lineage

Closest stylistic neighbors (not named artists, but schools or tendencies). Degree of naturalism vs symbolic abstraction. Surface priority: line, color mass, light, or texture. (Order preserved.)
> **Internal storage rule:** Store these internally as a *metadata vector*, not prose.

---

## Stage 2: Metadata Matrix Intersection

Construct a **constraint matrix** by intersecting:

Historically documented qualities of the inferred time/place/medium. The specific quirks and limitations visible in the image.
This matrix must answer:

What could exist here historically? What must exist because it already partially does? What is forbidden (anachronism, stylistic drift, modern optics)? (Order preserved.)
Use this matrix to set **upper and lower bounds** on:

Color saturation. Edge clarity. Detail density. Lighting contrast. Surface smoothness. (Order preserved.)
---

## Stage 3: Hyperspecific Reconstruction Prompt (Generative)

Only after Stages 1–2, generate a reconstruction and upscaling prompt that obeys all inferred constraints.

The prompt must:

Explicitly state the temporal window (e.g., “late 15th–early 16th century, Northern Europe”). Name the material logic (oil on panel, aged varnish, hand‑ground pigments). Describe lighting physics consistent with period interiors. Specify what may be clarified versus what must remain ambiguous. Enforce non‑invention rules for figures, objects, and symbolism. Treat damage and age as **data**, not noise. (Order preserved.)
---

## Final prompt template (copy/paste)

```text
Delicately reconstruct and upscale an image originating from a [temporal range] [regional school] context, executed in [medium] on [support], likely intended as a [scale/function].

Preserve the original [perspective system] and [optical device, if any], maintaining period-consistent lighting derived from [light source].

Color reconstruction must adhere to historically plausible pigments for this context, with restrained saturation and visible aging effects including [craquelure type, varnish behavior].

Figures, garments, and architectural elements should be clarified only where existing pixel evidence supports inference; areas of ambiguity must remain understated rather than resolved.

No modern sharpening, no stylistic fusion, no symbolic invention, and no correction of painterly irregularities that are consistent with period practice.

The final image should read as a conservation-grade digital restoration—revealing latent detail without exceeding the epistemic limits of the original artifact.
```

## Enrichment: practical usage notes

If you’re using this with an image model, run it in **two turns**: 1) Ask for the internal metadata vector + constraint matrix (no prompt output yet). 2) Ask it to emit *only* the final reconstruction prompt (using the template above). Keep “forbidden” constraints explicit; that’s what prevents the model from “helpfully” inventing. When uncertain, bias toward **understatement** rather than “completing” missing details. (Order preserved.)

---

## Concreteness + Knowledge Retention Protocol

Apply the shared protocol in `library/graph/protocols/concreteness_and_retention_protocol.md`. This protocol is mandatory for this node.
