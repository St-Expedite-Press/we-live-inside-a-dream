---
title: "Chain Execution Protocol — Logging, State, Stop Conditions, and Human Approvals (Intermediate)"
type: "prompt"
tags: ["orchestration", "protocol", "governance", "meta", "extreme-verbose"]
created: "2026-02-14"
---

# Chain Execution Protocol — Intermediate Prompt

Adopt the role of a **governance layer** for a multi-prompt chain.

Your job is to define:

how each step records outputs. how decisions are versioned. when human approvals are required. when the chain must stop. (Order preserved.)
This prevents a verbose chain from turning into uncontrolled scope creep.

---

## Prime directives

1. **Every step produces artifacts** (not just chat text).
2. **Artifacts are referenced by stable IDs** (step numbers and filenames).
3. **Mutations require approval**.
4. **Stop conditions are explicit**.
5. **State is explicit**: what is carried forward is enumerated.

---

## Required outputs

Produce a “protocol” document with:

1. `CHAIN_STATE_MODEL`
2. `ARTIFACT_NAMING_CONVENTION`
3. `STEP_LOG_TEMPLATE`
4. `APPROVAL_GATES`
5. `QUALITY_GATES`
6. `STOP_CONDITIONS`
7. `RECOVERY_AND_RETRY`

---

# SECTION 1 — Chain state model

Define the state object that persists across steps:

```yaml
chain_state:
  objective: ...
  acceptance_criteria: ...
  constraints: ...
  evidence_ledger:
    - id: E-001
      kind: file | command | config | test | metric
      value: ...
  decisions:
    - id: D-001
      decision: ...
      rationale: ...
      evidence_refs: [E-001]
  risks:
    - id: R-001
      risk: ...
      severity: low|med|high
      mitigation: ...
  artifacts:
    - step: 2
      name: ...
      location: ...
```

---

# SECTION 2 — Artifact naming convention

Enforce:

`stepNN_<artifact_name>.md`. stable ordering. separate `analysis/` vs `implementation/` if needed. (Order preserved.)
---

# SECTION 3 — Step log template

Every step log must include:

start timestamp. inputs used. outputs produced. decisions made. open questions. next step chosen. (Order preserved.)
---

# SECTION 4 — Approval gates

Define when explicit human approval is required:

writing/deleting files. changing dependencies. deploying. running commands that mutate state. accessing secrets. (Order preserved.)
---

# SECTION 5 — Quality gates

Define quality bars:

schema validation passes. tests pass. threat model reviewed (if required). rollout plan includes rollback. observability in place before ramp-up. (Order preserved.)
---

# SECTION 6 — Stop conditions

Stop if:

acceptance criteria are met. evidence contradicts the objective (needs user clarification). chain exceeds time budget. risk exceeds tolerance without mitigation. (Order preserved.)
---

# SECTION 7 — Recovery and retry

Define:

what happens when a step fails. how to backtrack. how to revise hypotheses. (Order preserved.)
Termination:

stop when protocol is produced.

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
