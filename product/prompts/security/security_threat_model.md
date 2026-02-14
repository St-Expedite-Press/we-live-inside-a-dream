---
title: "Security Threat Model — STRIDE/LINDDUN + Concrete Mitigations + Verification (Extreme)"
type: "prompt"
tags:
  - "security"
  - "threat-model"
  - "architecture"
  - "verification"
  - "extreme-verbose"
created: "2026-02-14"
---

# Security Threat Model — Extreme Prompt

Adopt the role of a **senior security engineer + staff software architect**.

Your mission is to create a threat model that is:

- actionable (maps directly to mitigations)
- testable (has verification steps)
- bounded (does not become an infinite security wishlist)

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

- system description / repo link / architecture sketch
- deployment environment (local / cloud / k8s / on-prem)
- data classification (public / internal / confidential / regulated)
- auth model (if any)
- compliance constraints (SOC2/HIPAA/PCI/etc.) if applicable

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

- assets (data, credentials, tokens, models, prompts, logs)
- actors (users, admins, services, CI, third parties)
- trust boundaries (network, process, privilege, tenancy)

Output:

- a table: `Asset | Classification | Location | Owner | Impact if compromised`

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

- protocol
- authentication mechanism
- data sensitivity

---

# PHASE 3 — Threat enumeration

Choose one framework:

- STRIDE (system threats)
- LINDDUN (privacy threats)
- both (if regulated)

For each component and flow, enumerate threats with:

- threat description
- preconditions
- exploit sketch (high-level)
- affected assets
- severity (impact × likelihood)

Output:

- a matrix: `Component/Flow | Threat | Framework category | Severity | Notes`

---

# PHASE 4 — Mitigations and controls

For each high/critical threat, propose:

- preventive controls
- detective controls
- corrective controls

Each mitigation must include:

- where it lives (code module / infra layer)
- implementation hints
- cost/effort estimate

---

# PHASE 5 — Verification plan (non-negotiable)

For each mitigation define:

- unit/integration tests
- security tests (SAST/DAST)
- configuration checks
- operational monitors/alerts

Output:

- a table: `Mitigation | Verification | Tooling | Pass/Fail criteria`

---

# PHASE 6 — Deliverable packaging + termination

You produce:

- prioritized backlog (top 10 items)
- “quick wins” (≤1 day)
- “must do before prod” gates

Termination:

- stop when backlog is created and verification plan exists.
