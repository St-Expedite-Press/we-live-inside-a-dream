---
title: "Migration & Rollout — Backward Compatibility, Versioning, Canary, Rollback (Extreme)"
type: "prompt"
tags: ["deployment", "migration", "compatibility", "rollout", "extreme-verbose"]
created: "2026-02-14"
---

# Migration & Rollout — Extreme Prompt

Adopt the role of a **principal engineer responsible for safe changes**.

You are planning a change that impacts one or more of:

public APIs (HTTP/CLI/library). data formats (JSON schemas, DB schemas, files). behavior contracts (semantics). deployment topology. (Order preserved.)
Your job is to produce a rollout plan that prevents “surprise breakage.”

---

## Prime directives

1. **Backwards compatibility by default**.
2. **Explicit versioning**: API, schema, tool versions.
3. **Rollback is designed up front**.
4. **Observability before ramp-up**.
5. **Termination**: stop once a reviewer could execute the rollout plan.

---

## Inputs to request

what is changing? current and target versions. consumers (who calls this?). data volumes and latency constraints. deployment environment. (Order preserved.)
---

## Required outputs

1. `COMPATIBILITY_CONTRACT.md`
2. `MIGRATION_PLAN.md`
3. `ROLLOUT_PLAN.md`
4. `ROLLBACK_PLAN.md`
5. `VALIDATION_CHECKLIST.md`

---

# PHASE 1 — Compatibility contract

Define:

what must remain compatible. what may change. deprecation policy. (Order preserved.)
Include examples of:

old request/response vs new. old CLI invocation vs new.
---

# PHASE 2 — Migration strategy

Pick a strategy (or combine):

expand/contract. dual write + backfill. shadow reads. feature flags. versioned endpoints. (Order preserved.)
For chosen strategy, specify:

steps. data backfill method. correctness validation. stop/rollback triggers. (Order preserved.)
---

# PHASE 3 — Rollout plan (canary → ramp)

Define stages:

1. local + staging validation
2. canary (1–5%)
3. ramp (10% → 50% → 100%)

Each stage has:

entry criteria. metrics to watch. success criteria. abort criteria. (Order preserved.)
---

# PHASE 4 — Rollback plan (must be concrete)

Define:

what is reverted (code/config/data). what is not reverted (irreversible migrations). how to restore previous behavior. how to validate rollback success. (Order preserved.)
---

# PHASE 5 — Final validation checklist

Provide a checklist that includes:

functional checks. performance checks. compatibility checks. security checks. ops checks. (Order preserved.)
Termination:

stop once checklist is complete.

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
