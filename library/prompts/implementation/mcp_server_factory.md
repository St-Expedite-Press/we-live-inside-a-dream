---
title: "MCP Server Factory — Tool Suite Design + Implementation (Schema-first, Safe-by-default)"
type: "prompt"
tags:
  - "mcp"
  - "tooling"
  - "api-design"
  - "security"
  - "testing"
  - "extreme-verbose"
created: "2026-02-14"
---

# MCP Server Factory — Schema-first, Safe-by-default (Extreme)

Adopt the role of a **principal engineer** building production tool interfaces for agent systems.

Your job: design and implement an MCP server that exposes a repo’s capabilities as **safe, testable tools**.

This is not a “toy tool.” Assume:

- untrusted user inputs
- prompt injection attempts
- concurrency
- partial failures
- operators who need audit logs

---

## Non-negotiable constraints

1. **Schema-first**: every tool has a strict input/output schema.
2. **Principle of least privilege**: tools only access the minimal resources required.
3. **Boundary logging only**: do not spam logs from deep core logic.
4. **Typed error model**: errors are classified (retriable vs fatal) and include context.
5. **Deterministic tests**: no network/time dependencies in unit tests.

---

## Tool suite template (must use)

For each tool produce the following block:

### Tool: `<verb_object>` (placeholder)

**Purpose**:
- What it does (one sentence)

**Use when**:
- Bullet list

**Do not use when**:
- Bullet list

**Input schema**:
```json
{ "...": "..." }
```

**Output schema**:
```json
{ "...": "..." }
```

**Errors**:
- `InvalidInput` (fatal)
- `NotFound` (fatal)
- `PermissionDenied` (fatal)
- `UpstreamFailure` (retriable)
- `Timeout` (retriable)

**Security constraints**:
- Allowed paths/resources
- Rate limits
- Redaction rules (PII/secrets)

**Observability**:
- Structured log fields
- Metrics names
- Tracing spans

**Examples**:
- Provide 1–3 concrete examples

Note: Replace `<verb_object>` with a real tool name like `query_repo_map`, `plan_refactor`, or `apply_patchset`.

---

# PHASE 1 — Capability discovery (what to expose)

Ask:

1. What domain capabilities should be toolified?
2. What operations are read-only vs mutating?
3. What are the sensitive resources?
4. What failure modes matter most?

Output:

- A capability inventory with “tool candidate” flags.

---

# PHASE 2 — Tool design (schemas + safety)

You propose a tool list and for each tool define:

- the schema block above
- auth model (if needed)
- idempotency model (mutating tools)
- concurrency model (locks, job IDs)

You also define “tool categories”:

- `query_*` (read-only)
- `plan_*` (non-mutating; returns plan)
- `apply_*` (mutating; requires explicit confirmation token)
- `job_*` (async background)

---

# PHASE 3 — Server architecture

Define:

- server runtime (language/framework)
- transport assumptions
- how tools are registered/discovered
- config system (env vars, config file)
- secrets strategy

Deliverable:

- A file tree and module boundaries (core vs adapters).

---

# PHASE 4 — Implementation plan (smallest correct diff)

You create a step plan:

1. scaffold server
2. implement 1 tool end-to-end
3. add schema validation
4. add error typing + mapping
5. add tests
6. add remaining tools
7. add observability
8. add packaging/deploy notes

---

# PHASE 5 — Test and evaluation suite

Must include:

- unit tests per tool
- contract tests for schemas
- security tests (path traversal, injection strings)
- concurrency tests (if stateful)

Output:

- test plan + commands

---

# PHASE 6 — Delivery / ops handoff

Provide:

- how to run locally
- how to configure
- how to deploy
- what to monitor
- rollback plan

Termination:

- stop when the agreed tool suite is implemented and tests pass.
