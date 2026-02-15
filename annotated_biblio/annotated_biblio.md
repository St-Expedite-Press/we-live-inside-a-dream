# Annotated Bibliography (Context Engineering + Prompt Governance)

This repository (see [`README.md`](../README.md) and [`library/docs/repo_mental_model.md`](../library/docs/repo_mental_model.md)) is a **deterministic prompt compilation and governance system**. It treats prompts as source code, compiles them into a book/catalog/ontology, and supports non-destructive prompt improvement workflows.

This annotated bibliography focuses on research and practitioner guidance that is directly relevant to building and operating a governed prompt ecosystem:

**Long-context reliability** (where information is placed in a large prompt, and how retrieval/context stacks should be ordered). **Instruction hierarchy and injection boundaries** (how to separate privileged instructions from untrusted data). **Evaluation and regression** (how to make prompt changes safe and reviewable). (Order preserved.)
Each entry includes: (a) what the work says, (b) what it implies for prompt ecosystems, and (c) concrete follow-ups that map to this repo’s build-oriented workflow.

---

## 1) Liu et al. (2023) — “Lost in the Middle: How Language Models Use Long Contexts”

**Link:** https://arxiv.org/abs/2307.03172

**What it is (summary):**
Liu et al. study how well language models use *long* contexts when the relevant information appears at different positions. They evaluate models on tasks requiring the model to identify and use relevant information embedded in the context.

**Methods / evidence (high level):**
Tasks: multi-document question answering and key–value retrieval. Intervention: move the relevant evidence (or key) to different positions in the input context. Finding: performance is often **U-shaped** with respect to position—highest when relevant text is at the **beginning or end**, and substantially worse when the evidence is **in the middle**. (Order preserved.)
**Key takeaways:**
“Long context” support does not imply uniform ability to use *any* part of that context. Placement effects can dominate: the same evidence can become effectively “invisible” depending on where it sits.
**Limitations / cautions:**
Results depend on model families, training, and tasks; the paper demonstrates a robust *phenomenon*, not a single universal curve. Long-context performance is not only about attention; retrieval, formatting, and instruction clarity also affect outcomes.
### Relevance to this repo (deterministic prompt compilation + governance)

This repository’s outputs (compiled book + ontology exports) are used downstream to build **stable, reusable prompt “programs.”** “Lost in the Middle” motivates treating *prompt layout* as a governed interface:

The canonical prompt skeleton in [`library/research/principles.md`](../library/research/principles.md) explicitly recommends **attention placement** and **end-of-prompt validation**. The strategies in [`library/research/context_window_strategies.md`](../library/research/context_window_strategies.md) directly operationalize this finding: front-load objectives/constraints, tail-load checklists, chunk + label, and re-rank context.
### Concrete follow-ups for this repository

1. **Encode “placement” as first-class prompt metadata.**
Add/standardize tags in prompt frontmatter (e.g., `context_window_strategy`, `frontload_constraints`, `tail_checklist`). Use the ontology export to make these strategies queryable.
2. **Add a long-context “layout lint” to the build.**
A deterministic check (no inference calls) that fails or warns when: constraints appear only in the middle; untrusted inputs are not delimited; extremely long “Inputs” are not chunked.
3. **Create “context stack ordering” guidance for RAG pipelines that consume these prompts.**
Because this repo is upstream of runtime inference, the deliverable should be an interface contract: “retrieval chunks MUST be ordered by relevance; key facts MUST be duplicated in a short ‘Salient facts’ section at the top.”.
---

## 2) Hsieh et al. (2024) — “Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization”

**Link:** https://arxiv.org/abs/2406.16008

**What it is (summary):**
Hsieh et al. investigate *why* the “lost-in-the-middle” effect occurs and propose a mitigation: a calibration mechanism (“found-in-the-middle”) intended to reduce positional attention bias so models attend according to relevance rather than position.

**Methods / evidence (high level):**
Diagnose a **U-shaped attention bias**: models overweight tokens at the beginning and end independent of relevance. Propose a calibration approach to make attention more faithful to relevance even for middle-position content. Evaluate improvements over baselines on long-context tasks. (Order preserved.)
**Key takeaways:**
“Lost in the middle” has a mechanistic correlate (positional attention bias), not just a benchmark artifact. Model-side mitigations may improve long-context use, but do not remove the need for good prompt layout and context ordering.
**Limitations / cautions:**
A model-side fix is not always available to downstream users (you may not control weights or the inference stack). Even if positional bias improves, prompt injection and instruction/data confusion remain separate concerns.
### Relevance to this repo

This repo is deliberately **model-agnostic** and **runtime-agnostic**: it compiles and governs prompts without assuming any one provider. “Found in the Middle” is still highly relevant because it tells us:

Prompt governance should treat **layout** as an *interface contract* that must be robust even on models with known biases. When downstream consumers upgrade models, long-context behavior may change. That motivates **regression-style evaluation** practices in prompt ecosystems.
### Concrete follow-ups for this repository

1. **Add a “model capability assumptions” section to canonical prompts that rely on long context.**
Example: “This prompt assumes the model may under-attend to middle context; therefore it requires a ‘Salient facts’ extraction step.”.
2. **Define evaluation fixtures for long-context prompts.**
Store “golden” input packs (long docs + questions) and expected structured outputs. Even without running models in this repo, you can define the fixtures + rubrics here and let downstream CI run them.
---

## 3) OpenAI (2024) — “The Instruction Hierarchy”

**Link:** https://openai.com/index/the-instruction-hierarchy/

**What it is (summary):**
This publication describes a practical ordering of instructions in multi-source contexts, emphasizing that some instructions are privileged (system/developer) and should override lower-priority content (user text, tool output, retrieved documents).

**Key takeaways:**
Always make *priority* explicit; do not let untrusted text compete with governing rules. In long or multi-document contexts, instruction conflicts and prompt injection are more likely unless you enforce separation.
**Limitations / cautions:**
The publication is provider guidance, not a formal proof; different platforms implement slightly different roles. Hierarchy helps with conflicts, but you still need explicit delimitation and “treat as data” rules.
### Relevance to this repo

This repo’s stance (“prompts as source code”) implies prompts should have stable structure that survives composition into chains. The hierarchy idea is already reflected in:

[`library/research/instruction_hierarchy_patterns.md`](../library/research/instruction_hierarchy_patterns.md). The “instruction hierarchy first” principle in [`library/research/principles.md`](../library/research/principles.md).
Hierarchy is a governance primitive: it supports deterministic prompt composition because each section has a clear privilege level and conflict resolution behavior.

### Concrete follow-ups for this repository

1. **Standardize a canonical header in all prompts** (or at least in governance + execution prompts):
`Identity` → `Mission` → `Hard constraints` → `Process` → `Output format` → `Validation` → `Inputs (delimited)`.
2. **Add a “delimited untrusted data” requirement to prompts intended to consume third-party content.**
This should be mechanically checkable (build-time lint), not just a suggestion.
3. **Add prompt-injection test cases to evaluation methods.**
See also: [`library/research/failure_modes.md`](../library/research/failure_modes.md) and [`library/research/evaluation_methods.md`](../library/research/evaluation_methods.md).
---

## Synthesis: how these works shape a governed prompt ecosystem

These sources converge on an engineering interpretation that matches this repo’s purpose:

1. **Prompt layout is part of the API.**
If placement can change correctness (Lost/Found in the Middle), then structure and ordering must be governed like an interface.
2. **Separation of privilege is non-negotiable.**
Hierarchy + delimitation turn “a big blob of text” into a composed program with explicit authority.
3. **Governance requires testability.**
A deterministic build system should emit artifacts that can be evaluated downstream (fixtures, rubrics, regression packs), even if this repo itself does not run inference.
---

## Suggested repo-local action items (non-destructive)

These are “improve the ecosystem” steps that align with the existing tooling model (canonical prompts remain the source of truth; improvements can be emitted separately):

1. Extend the ontology schema to include:
context-window strategy tags. whether the prompt consumes untrusted data. expected output strictness level (schema rigidity). (Order preserved.)
2. Add a build-time linter for:
missing instruction hierarchy sections. missing `Inputs` delimitation. “constraints only in the middle” anti-pattern. excessively long unchunked input blocks. (Order preserved.)
3. Add a `library/paths/` runbook for “long context ingestion” that:
requires a `Salient facts` extraction step. reorders retrieved chunks by relevance. duplicates top constraints at the end as a short checklist. (Order preserved.)
