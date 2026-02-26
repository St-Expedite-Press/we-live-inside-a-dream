---
title: "RUST ANTIBLOAT"
source: "RUST ANTIBLOAT.pdf"
type: "guidelines"
tags: ["rust", "code-review", "architecture", "restraint"]
created: "2026-02-05"
---

# RUST ANTIBLOAT

A compact rulebook aimed at **restraint, clarity, and maintainability** when writing Rust.

## Table of contents

[Table 1 — Global Agent Constraints](#table-1--global-agent-constraints). [Table 2 — Rust Idiomaticity & Language Discipline](#table-2--rust-idiomaticity--language-discipline). [Table 3 — Abstraction Budget System](#table-3--abstraction-budget-system). [Table 4 — Code Locality & Modularity](#table-4--code-locality--modularity). [Table 5 — Dependency Governance](#table-5--dependency-governance). [Table 6 — Error Semantics & Logging](#table-6--error-semantics--logging). [Table 7 — Complexity Management](#table-7--complexity-management). [Table 8 — Professional Readability Standard](#table-8--professional-readability-standard). [Table 9 — Agent Self‑Audit Checklist (Pre‑Commit)](#table-9--agent-self-audit-checklist-pre-commit). [Table 10 — Core System Doctrine (Canonical)](#table-10--core-system-doctrine-canonical). (Order preserved.)
---

## Table 1 — Global Agent Constraints

| Item | Explanation |
|---|---|
| **G-01 — Mission Constraint** *(Scope Control, Hard)* | Description: Agents may only act in service of the explicitly stated objective. Any action without direct task contribution is forbidden.; Violation signal: Code added without traceable task linkage |
| **G-02 — Termination Condition** *(Lifecycle, Hard)* | Description: Agents must halt when objectives are met or remaining work is subjective or aesthetic.; Violation signal: Continued diffs after acceptance criteria met |
| **G-03 — No Speculative Architecture** *(Architecture, Hard)* | Description: Agents may not design for hypothetical scale, plugins, or futures not evidenced by current requirements.; Violation signal: Unused extension points, empty traits |
| **G-04 — Diff Discipline** *(Process, Hard)* | Description: All changes must be small, focused, and reversible.; Violation signal: Large diffs with mixed concerns |
---

## Table 2 — Rust Idiomaticity & Language Discipline

| Item | Explanation |
|---|---|
| **R-01 — Ownership First** *(Memory)* | Requirement: Prefer borrowing and ownership transfer over cloning.; Rationale: Prevents hidden cost and semantic ambiguity.; Heuristic: Detect `.clone()` outside boundary types. |
| **R-02 — Enum Semantics** *(Control Flow)* | Requirement: Use enums instead of boolean flags or magic numbers.; Rationale: Encodes state meaning in the type system.; Heuristic: Multiple booleans in structs. |
| **R-03 — Pattern Matching** *(Logic)* | Requirement: Prefer `match` over nested conditionals.; Rationale: Exhaustiveness and clarity.; Heuristic: Nested `if let` chains. |
| **R-04 — Error Typing** *(Errors)* | Requirement: Use typed errors (`thiserror`, `anyhow`) over strings.; Rationale: Preserves semantic intent.; Heuristic: `Result<T, String>` usage. |
| **R-05 — Unsafe Prohibition** *(Safety)* | Requirement: `unsafe` requires written justification and audit.; Rationale: Prevents silent invariants.; Heuristic: Presence of `unsafe` blocks. |
---

## Table 3 — Abstraction Budget System

| Rule ID | Abstraction type | Budget unit | Default allowance | Approval requirement | Notes |
|---|---|---:|---|---|---|
| A-01 | New Trait | 1 | 2 per agent task | Explicit justification | Traits imply long-term contracts |
| A-02 | Generic Parameter | 1 | 3 per module | None if local | Generics amplify cognitive load |
| A-03 | Macro | 2 | 1 per crate | Mandatory | Macros obscure control flow |
| A-04 | Wrapper / Adapter | 1 | 2 per crate | Implicit | Must demonstrate necessity |
| A-05 | New Dependency | 3 | 1 per task | Mandatory | Dependencies are irreversible costs |

**Budget Exhaustion Rule:** If an agent exceeds its abstraction budget, it must delete or collapse existing abstractions before proceeding.

---

## Table 4 — Code Locality & Modularity

| Item | Explanation |
|---|---|
| **L-01 — Proximity Principle** | Constraint: Code must live near the use site.; Disallowed pattern: Premature shared modules.; Enforcement: Static analysis of cross-module imports. |
| **L-02 — One Concept per Module** | Constraint: Single noun-phrase responsibility.; Disallowed pattern: `utils.rs`, `helpers.rs`, `common.rs`.; Enforcement: Module name linting. |
| **L-03 — Reuse Evidence** | Constraint: Reuse requires ≥ 2 real call sites.; Disallowed pattern: Hypothetical reuse.; Enforcement: Call-graph inspection. |
---

## Table 5 — Dependency Governance

| Item | Explanation |
|---|---|
| **D-01 — Std Sufficiency** | Requirement: Prove `std` is insufficient.; Failure condition: Convenience usage.; Automated signal: External crate mirrors `std`. |
| **D-02 — Dependency Graph** | Requirement: Minimize depth and breadth.; Failure condition: Feature creep.; Automated signal: Transitive dependency explosion. |
| **D-03 — Maintenance** | Requirement: Must be actively maintained.; Failure condition: Abandoned crates.; Automated signal: No commits ≥ 12 months. |
| **D-04 — Feature Flags** | Requirement: Enable minimal features only.; Failure condition: Default-all features.; Automated signal: Cargo feature over-enablement. |
---

## Table 6 — Error Semantics & Logging

| Item | Explanation |
|---|---|
| **E-01 — Error Meaning** | Requirement: Domain-specific error enums.; Prohibited: Generic catch-alls.; Detection: Broad `anyhow::Error`. |
| **E-02 — Error Propagation** | Requirement: No silent recovery.; Prohibited: Swallowing errors.; Detection: Empty `match Err(_) => {}`. |
| **E-03 — Logging Scope** | Requirement: Log only at system boundaries.; Prohibited: Deep-logic logging.; Detection: Logger calls in core modules. |
---

## Table 7 — Complexity Management

| Item | Explanation |
|---|---|
| **C-01 — Refactor First** | Required action order: Delete → Simplify → Collapse → Add; Disallowed shortcut: Immediate expansion |
| **C-02 — Type Strengthening** | Principle: Encode invariants in types; Disallowed shortcut: Runtime checks first |
| **C-03 — Expressive Code** | Principle: Prefer clarity over compression; Disallowed shortcut: Clever one-liners |
---

## Table 8 — Professional Readability Standard

**P-01 — Naming:** Descriptive, domain-accurate (no decoding required). **P-02 — Comments:** Only where behavior is non-obvious (code should explain itself). **P-03 — Control Flow:** Linear and explicit (no hidden side effects). **P-04 — Review Readiness:** Senior-level clarity (adversarial review assumed). (Order preserved.)
---

## Table 9 — Agent Self‑Audit Checklist (Pre‑Commit)

| Check ID | Question | Required answer type | Blocking |
|---|---|---|:---:|
| S-01 | What can be deleted? | Concrete code reference | Yes |
| S-02 | What abstraction can collapse? | Trait / module name | Yes |
| S-03 | What dependency could be removed? | Crate name or “none” | Yes |
| S-04 | What assumption lacks evidence? | Explicit statement | Yes |

---

## Table 10 — Core System Doctrine (Canonical)

| Axis | Value |
|---|---|
| Primary optimization | Restraint |
| Secondary optimization | Clarity |
| Tertiary optimization | Maintainability |
| Explicit anti-goal | Framework accretion |
| Cultural bias | Deletion over addition |

---

## Enrichment: how to apply this in practice

Treat the **abstraction budget** like a forcing function: if you add a trait/generic/macro, *delete something else* or collapse an existing abstraction. Consider adding a review checklist item: **“Show the simplest version that works”** before accepting any design. Pinpoint boundaries (I/O edges, API surfaces) where `.clone()` and `anyhow` are acceptable; ban them elsewhere. (Order preserved.)
