---
title: "Agent Testing & Eval Gauntlet — Reasoning, Tooling, Safety, Regression"
type: "prompt"
tags: ["agent-systems", "testing", "evaluation", "observability", "safety", "extreme-verbose"]
created: "2026-02-14"
---

# Agent Testing & Eval Gauntlet — Extreme Prompt

Adopt the role of a **reliability engineer for agent systems**.

Your mission: design a test/eval harness that makes it difficult for an agent system to fail silently.

You assume:

nondeterministic outputs. tool failures. partial observability. prompt injection attempts. regressions due to prompt/model/tool changes. (Order preserved.)
---

## What you are testing (define the system)

You must define:

agent interface (inputs/outputs). tool inventory and schemas. orchestration loop (ReAct/ToT/etc.). memory system (if any). grounding sources (if any). (Order preserved.)
Deliverable:

`SYSTEM_UNDER_TEST.md` describing these precisely.
---

# PHASE 1 — Failure mode inventory (before tests)

You build a failure mode list:

## Reasoning failures
wrong decomposition. premature conclusion. infinite loop. tool avoidance. tool misuse. (Order preserved.)
## Tool failures
timeouts. schema mismatch. partial failures. idempotency violations. (Order preserved.)
## Safety failures
prompt injection tool escalation. data exfiltration attempts. unauthorized file access. unsafe command generation. (Order preserved.)
Deliverable:

`FAILURE_MODES.md` with severity/likelihood.
---

# PHASE 2 — Test taxonomy and coverage map

You define a coverage matrix:

Unit tests (tool functions). Contract tests (schema validation). Integration tests (tool composition). Scenario tests (end-to-end tasks). Adversarial tests (injection + malformed inputs). Regression suite (pinned scenarios with expected outcomes). (Order preserved.)
Deliverable:

`COVERAGE_MATRIX.md` mapping failure modes → tests.
---

# PHASE 3 — Golden scenarios (deterministic-ish)

Create 10–30 scenarios with:

input prompt. required tools to call (or “must not call tools”). success criteria (observable). allowed variance band (what can differ). (Order preserved.)
Deliverable:

`SCENARIOS.md`.
---

# PHASE 4 — Evaluation metrics

Define metrics (with computation method):

task completion rate. tool selection precision/recall (if definable). schema conformance rate. hallucination rate (proxy definitions). latency p50/p95. token/cost per scenario. safety incident count. (Order preserved.)
Deliverable:

`METRICS.md`.
---

# PHASE 5 — Observability plan

You specify required telemetry:

trace spans per tool call. structured logs with correlation IDs. metrics naming conventions. dashboards and alert thresholds. (Order preserved.)
Deliverable:

`OBSERVABILITY.md`.
---

# PHASE 6 — Regression and change management

Define:

prompt versioning policy. model version pinning policy. tool schema versioning and deprecation. rollback strategy. (Order preserved.)
Deliverable:

`CHANGE_MANAGEMENT.md`.
---

## Termination

Stop when:

failure modes are enumerated. coverage matrix exists. scenarios exist. metrics exist. observability and change mgmt exist. (Order preserved.)

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
