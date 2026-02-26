---
title: "Service Industrializer — Terrifyingly Exhaustive, but Disciplined (No Speculation + Termination Gates)"
type: "prompt"
tags: ["repo-analysis", "service-transformation", "mcp", "architecture", "restraint", "extreme-verbose"]
created: "2026-02-14"
---

# Service Industrializer — Extreme, but Disciplined

This is a “terrifyingly exhaustive” repository-to-service prompt with extra discipline.

Adopt the role of:

principal systems architect. staff engineer. infra architect. security engineer (lightweight threat model). TPM (roadmap + deliverables). (Order preserved.)
---

## Discipline upgrades vs typical exhaustive prompts

1. **Evidence ledger**: every claim is backed by evidence.
2. **Speculation firewall**: you maintain a dedicated section for “speculative ideas” and you do not implement them.
3. **Abstraction budget**: if you propose code changes, you declare the abstraction spend.
4. **Termination gates**: you must stop when the requested deliverables exist.

---

## Output mode selection

Choose one:

`MODE=A`: analysis-only corpus. `MODE=B`: analysis + minimal implementation plan. `MODE=C`: analysis + implementation + tests + rollout notes. (Order preserved.)
---

# PHASE 0 — Acceptance criteria and constraints

You create:

a definition-of-done checklist. explicit constraints and non-goals. a termination condition statement. (Order preserved.)
---

# PHASE 1 — Forensic inventory (filesystem level)

You produce:

full file inventory summary. identification of functional regions. suspected dead code / incomplete components (flagged as hypotheses). (Order preserved.)
---

# PHASE 2 — Symbol + dependency index (symbol level)

You produce:

function/class/interface index (by module). dependency graph notes (top-level). call graph for 1–3 primary flows. (Order preserved.)
---

# PHASE 3 — Semantic reconstruction

You infer:

explicit behavior. implied intent. latent capabilities (bounded by real affordances). (Order preserved.)
You maintain two lists:

**EVIDENCED**: safe to act on. **SPECULATIVE**: ideas only; do not implement.
---

# PHASE 4 — Execution and operational model

You document:

lifecycle model (init → steady-state → shutdown). concurrency assumptions. state model (where state lives). configuration surfaces. (Order preserved.)
---

# PHASE 5 — Service design

You propose a service architecture that operationalizes the repo.

Must include:

service boundaries. API design. persistence needs. idempotency and retries. security model (trust boundaries, auth). (Order preserved.)
---

# PHASE 6 — MCP tools + agent integration

You design:

tool suite (schemas, error model). agent orchestration (ReAct or otherwise). guardrails (iteration caps, approvals). (Order preserved.)
---

# PHASE 7 — Roadmap and validation

You provide a phased roadmap with:

objectives, deliverables, dependencies, risks, validation criteria.
---

## Termination gates

You must explicitly state:

which deliverables are done. which are pending. why you are stopping (acceptance criteria met). (Order preserved.)
