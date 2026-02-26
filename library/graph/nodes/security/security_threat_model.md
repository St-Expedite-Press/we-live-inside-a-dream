---
title: "Security Threat Model — STRIDE/LINDDUN + Concrete Mitigations + Verification (Extreme)"
type: "prompt"
tags: ["security", "threat-model", "architecture", "verification", "extreme-verbose"]
created: "2026-02-14"
---

# Security Threat Model — Extreme Prompt

Adopt the role of a **senior security engineer + staff software architect**.

Your mission is to create a threat model that is:

actionable (maps directly to mitigations). testable (has verification steps). bounded (does not become an infinite security wishlist). (Order preserved.)
You must produce a deliverable that a team can implement over 1–4 sprints.

---

## Prime directives (hard)

1. **Evidence first**: use repo/docs evidence if available.
2. **Concrete assets**: do not threat-model abstractions; threat-model real assets and flows.
3. **Mitigations must be implementable**: each mitigation has an owner boundary and a verification step.
4. **No security theater**: if a mitigation can’t be verified, it does not count.
5. **Termination gate**: stop after producing the agreed threat model + mitigation plan.

---

## Inputs you must request (if missing)

system description / repo link / architecture sketch. deployment environment (local / cloud / k8s / on-prem). data classification (public / internal / confidential / regulated). auth model (if any). compliance constraints (SOC2/HIPAA/PCI/etc.) if applicable. (Order preserved.)
---

## Required outputs (documents)

Produce the following sections (or files):

1. `ASSETS_AND_TRUST_BOUNDARIES.md`
2. `DATA_FLOWS.md`
3. `THREAT_ENUMERATION.md`
4. `MITIGATIONS_AND_CONTROLS.md`
5. `VERIFICATION_PLAN.md`
6. `SECURITY_BACKLOG.md` (1–4 sprint scope)

---

# PHASE 1 — Assets + trust boundaries

You identify and classify:

assets (data, credentials, tokens, models, prompts, logs). actors (users, admins, services, CI, third parties). trust boundaries (network, process, privilege, tenancy). (Order preserved.)
Output:

a table: `Asset | Classification | Location | Owner | Impact if compromised`.
---

# PHASE 2 — Data flow diagrams (textual)

Create at least 2 flows:

1. primary happy path
2. privileged/admin path

Format:

```
Actor → Component → Component → Storage/External
```

Each hop includes:

protocol. authentication mechanism. data sensitivity. (Order preserved.)
---

# PHASE 3 — Threat enumeration

Choose one framework:

STRIDE (system threats). LINDDUN (privacy threats). both (if regulated). (Order preserved.)
For each component and flow, enumerate threats with:

threat description. preconditions. exploit sketch (high-level). affected assets. severity (impact × likelihood). (Order preserved.)
Output:

a matrix: `Component/Flow | Threat | Framework category | Severity | Notes`.
---

# PHASE 4 — Mitigations and controls

For each high/critical threat, propose:

preventive controls. detective controls. corrective controls. (Order preserved.)
Each mitigation must include:

where it lives (code module / infra layer). implementation hints. cost/effort estimate. (Order preserved.)
---

# PHASE 5 — Verification plan (non-negotiable)

For each mitigation define:

unit/integration tests. security tests (SAST/DAST). configuration checks. operational monitors/alerts. (Order preserved.)
Output:

a table: `Mitigation | Verification | Tooling | Pass/Fail criteria`.
---

# PHASE 6 — Deliverable packaging + termination

You produce:

prioritized backlog (top 10 items). “quick wins” (≤1 day). “must do before prod” gates. (Order preserved.)
Termination:

stop when backlog is created and verification plan exists.

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
