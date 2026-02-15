---
title: "Phase groups: exploratory → planning → implementation (overlay taxonomy)"
type: "docs"
tags: ["meta", "taxonomy", "phases", "governance", "orchestration"]
created: "2026-02-15"
---

# Phase groups: exploratory → planning → implementation

This document introduces a phase-based overlay taxonomy for this prompt library. The goal is to make the library composable as a deterministic pipeline that takes a defined user prompt as input and produces a concrete product as output, with explicit intermediate artifacts that can be inspected, versioned, and handed off between phases.

The phase model does not replace the existing folder taxonomy immediately. It sits on top of it. Existing directories such as `library/prompts/discovery/`, `library/prompts/execution/`, and `library/prompts/implementation/` remain useful as a domain-oriented organization. The overlay answers a different question: “What prompt should run next, given where I am in a production workflow?”

## The phase pipeline (high-level)

The intended workflow is a deterministic chain with explicit handoff packets.

```text
User prompt
  ->
Exploratory phase (reduce unknowns and define the problem)
  ->
Planning phase (compile the plan and acceptance criteria)
  ->
Implementation phase (build the product and verify it)
  ->
Delivery packet (what shipped, how to verify, what changed)
```

The output of each phase is both human-readable and machine-readable. Human-readable artifacts are Markdown reports and runbooks. Machine-readable artifacts are phase packets in JSON, designed to be passed forward without re-interpretation.

## Phase definitions (what each phase is responsible for)

The phase model is intentionally strict about responsibilities so that later phases do not silently invent context.

| Phase | Primary responsibility | Must output | Must not do |
|---|---|---|---|
| Exploratory | Eliminate ambiguity and surface unknowns with evidence-first questions | A context map and an exploration packet | Implement solutions or commit to architectures without evidence |
| Planning | Compile a plan into an execution contract | A build plan and a plan packet | Start “doing the work” beyond light feasibility checks |
| Implementation | Execute the plan and produce the product | A delivery report and delivery packet | Re-scope the objective without producing a new plan packet |

## Handoff artifact contract (the “packet” concept)

The system becomes composable when each phase outputs a packet with the same stable structure. Packets are meant to be copy-pasted verbatim into the next phase as the starting context, or stored as files when running inside a repo.

The canonical schema is defined in the phase prompts themselves. The core idea is that the user prompt is preserved verbatim, while the phase adds structured decisions, constraints, and references that the next phase can rely on without inference.

## Mapping existing prompts into the phase model

The following table is a pragmatic mapping of the current library into the phase overlay. It is not exclusive, and some prompts span phases. The purpose is to provide a default routing strategy that can be made more granular over time.

| Existing area | Phase alignment | Why it fits |
|---|---|---|
| `library/prompts/discovery/` | Exploratory | Discovery prompts are designed to reduce unknowns, build maps, and find leverage points before committing to a plan. |
| `library/prompts/execution/` | Planning and governance | Execution prompts define how to route objectives, generate runbooks, and enforce chain state and stop conditions. |
| `library/prompts/implementation/` | Implementation | Implementation prompts focus on building the smallest correct diff, designing tool suites, and shipping with verification. |
| `library/prompts/security/` | Cross-cutting | Security work can occur as part of exploration, planning, or implementation depending on risk, but should be explicit when it preempts other work. |
| `library/prompts/migration/` | Planning and release | Migration and rollout are planning and execution governance for shipping changes safely. |
| `library/prompts/incident_response/` | Interrupt handler | Incident response can preempt any phase and must produce stabilization artifacts and postmortem outputs. |

## Why this is the “next big leap”

The phase overlay turns a collection of strong individual prompts into a product pipeline. The difference is not rhetorical, it is contractual. A pipeline is defined by the shape of its intermediate representations and by the invariants it preserves. Once the library can carry a user prompt through exploration, planning, and implementation with stable handoff packets, downstream automation becomes possible without turning the library into a brittle monolith.

In practical terms, this enables a consistent “objective → artifacts → verification → delivery” flow for many kinds of work, including software builds, prompt tooling, documentation generation, and operational playbooks.

