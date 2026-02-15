---
title: "Path: objective → product (explore → plan → implement)"
type: "path"
tags: ["paths", "pipeline", "phases", "governance", "packet"]
created: "2026-02-15"
---

# Path: objective → product (explore → plan → implement)

This path is an operational runbook for turning a defined user prompt into a concrete product by passing the prompt through a deterministic three-phase pipeline. The phases are exploratory, planning, and implementation. Each phase emits both a human-readable artifact and a machine-readable packet designed for verbatim handoff.

This path is appropriate when you want a repeatable workflow that produces inspectable artifacts rather than conversational output. It is also the recommended starting point for turning this library into a production-grade prompt infrastructure layer, because it makes intermediate representations explicit.

## Inputs

You need a user prompt. Preserve it verbatim. You also need to know whether you have repository access, because “product” means different things in different environments.

Use the following intake record. If a field is unknown, record it as unknown rather than inventing it.

| Field | Value |
|---|---|
| User prompt (verbatim) |  |
| Execution environment (local repo access, no repo access, unknown) |  |
| Target product kind (code change, new codebase, design doc, runbook, prompt pack, research synthesis, other) |  |
| Primary language (python, rust, other, unknown) |  |
| Risk level (low, medium, high, unknown) |  |

## Phase 1: exploratory

Objective: reduce ambiguity until a planner can generate a build plan without guessing.

Run the exploratory phase prompt as top-of-chat and answer its intake questions using the table above as your baseline.

Prompt to run: `library/prompts/exploratory/objective_intake_and_context_map.md`.

Required outputs: an `Exploration report` section and an `EXPLORATION_PACKET` JSON block.

Handoff: copy the entire `EXPLORATION_PACKET` block verbatim. It becomes canonical input to Phase 2.

## Phase 2: planning

Objective: compile an executable plan with acceptance criteria, artifact contracts, quality gates, and explicit stop conditions.

Run the planning phase prompt as top-of-chat. Provide the verbatim user prompt and paste the `EXPLORATION_PACKET` as the initial context.

Prompt to run: `library/prompts/planning/product_plan_compiler.md`.

Required outputs: a `Build plan` section and a `PLAN_PACKET` JSON block.

Handoff: copy the entire `PLAN_PACKET` block verbatim. It becomes canonical input to Phase 3.

## Phase 3: implementation

Objective: execute the plan and produce the product with verification evidence.

Run the implementation phase prompt as top-of-chat. Provide the verbatim user prompt and paste the `PLAN_PACKET` as the initial context. If you are operating inside a repository, also provide the repo path and the expected test and build commands.

Prompt to run: `library/prompts/implementation/product_build_executor.md`.

Required outputs: a `Delivery report` section and a `DELIVERY_PACKET` JSON block.

Completion condition: the delivery report must claim success only by referencing acceptance criteria and recorded verification, and the delivery packet must be specific enough to hand off to another engineer without re-explaining context.

## Governance notes (how to keep the pipeline deterministic)

The pipeline is deterministic only when handoffs are treated as immutable. Packets should be pasted verbatim between phases. If a phase discovers that the packet is missing required information, that discovery must become a new explicit observation or a new plan revision, not an invented assumption.

When destructive operations are required, insert explicit approval gates. The gate should name what is about to change, why it is required, and how you will verify and roll back.
