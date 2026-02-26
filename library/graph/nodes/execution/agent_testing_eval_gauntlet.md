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

Apply the shared protocol in `library/graph/protocols/concreteness_and_retention_protocol.md`. This protocol is mandatory for this node.
