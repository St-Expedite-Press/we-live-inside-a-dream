---
title: "Chain Execution Protocol — Logging, State, Stop Conditions, and Human Approvals (Intermediate)"
type: "prompt"
tags:
  - "orchestration"
  - "protocol"
  - "governance"
  - "meta"
  - "extreme-verbose"
created: "2026-02-14"
---

# Chain Execution Protocol — Intermediate Prompt

Adopt the role of a **governance layer** for a multi-prompt chain.

Your job is to define:

- how each step records outputs
- how decisions are versioned
- when human approvals are required
- when the chain must stop

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

- `stepNN_<artifact_name>.md`
- stable ordering
- separate `analysis/` vs `implementation/` if needed

---

# SECTION 3 — Step log template

Every step log must include:

- start timestamp
- inputs used
- outputs produced
- decisions made
- open questions
- next step chosen

---

# SECTION 4 — Approval gates

Define when explicit human approval is required:

- writing/deleting files
- changing dependencies
- deploying
- running commands that mutate state
- accessing secrets

---

# SECTION 5 — Quality gates

Define quality bars:

- schema validation passes
- tests pass
- threat model reviewed (if required)
- rollout plan includes rollback
- observability in place before ramp-up

---

# SECTION 6 — Stop conditions

Stop if:

- acceptance criteria are met
- evidence contradicts the objective (needs user clarification)
- chain exceeds time budget
- risk exceeds tolerance without mitigation

---

# SECTION 7 — Recovery and retry

Define:

- what happens when a step fails
- how to backtrack
- how to revise hypotheses

Termination:

- stop when protocol is produced.
