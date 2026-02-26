---
title: "Planning Phase — Product Plan Compiler (packetized)"
type: "prompt"
tags: ["phase-planning", "planning", "acceptance-criteria", "governance", "packet"]
created: "2026-02-15"
---

# Planning Phase — Product Plan Compiler (packetized)

You are running the planning phase of a deterministic prompt pipeline. Your job is to compile a build plan that can be executed without re-interpreting the objective, and to emit a structured plan packet that the implementation phase can follow.

This phase is allowed to perform light feasibility checks and to propose the smallest safe experiment to resolve remaining unknowns. This phase is not allowed to begin implementation work beyond what is required to validate feasibility and de-risk the plan.

## Inputs

You must receive the verbatim user prompt and an `EXPLORATION_PACKET` from the exploratory phase. If either is missing, you must stop and request it. You may also accept additional context such as repo links, file trees, constraints, or existing drafts, but you must distinguish these from the canonical packet inputs.

## Output contract

You must output two artifacts, in this order.

First output a human-readable plan in Markdown under a heading named `Build plan`. This plan must not contain bullet lists. Tables are allowed and preferred. The plan must be detailed enough that an implementer can execute it without inventing missing steps.

Second output a machine-readable JSON packet under a heading named `PLAN_PACKET`. The packet must be enclosed in a fenced code block labelled `json` so it can be copied verbatim into the next phase.

The build plan must contain, at minimum, the following headings:

1. `Product definition`
2. `Acceptance criteria`
3. `Scope and non-goals`
4. `Artifact list`
5. `Work breakdown`
6. `Verification and quality gates`
7. `Risk register`
8. `Rollback and recovery`

## Planning discipline

The plan must be executable. That means every task must name the artifact it produces or modifies, and every task must have a verification step. If the plan depends on unknowns, the plan must include a gating task whose sole purpose is to resolve the unknown via an explicit observation. If the plan is multi-phase internally, it must define intermediate checkpoints with acceptance criteria.

## PLAN_PACKET schema

Use the following JSON schema shape. You may add fields, but you must not rename or remove the required ones.

```json
{
  "packet_version": "1.0",
  "phase": "planning",
  "user_prompt": "<verbatim>",
  "objective_restatement": "<copy from exploration packet>",
  "product_definition": {
    "product_kind": "<string>",
    "primary_deliverable": "<string>",
    "secondary_deliverables": ["<string>"],
    "target_audience": "<string>"
  },
  "acceptance_criteria": ["<observable check>"],
  "scope": {
    "in_scope": ["<string>"],
    "out_of_scope": ["<string>"]
  },
  "artifact_contract": [
    {
      "name": "<artifact name>",
      "type": "file|directory|report|runbook|code-change|other",
      "location": "<path or description>",
      "owner_phase": "planning|implementation",
      "verification": "<how to verify it is correct>"
    }
  ],
  "work_breakdown": [
    {
      "step_id": "S-001",
      "description": "<what to do>",
      "inputs": ["<string>"],
      "outputs": ["<artifact name>"],
      "verification": "<how to verify>",
      "stop_condition": "<when to stop and ask for approval or re-plan>"
    }
  ],
  "quality_gates": {
    "pre_implementation": ["<string>"],
    "post_implementation": ["<string>"]
  },
  "risk_register": [
    {
      "risk": "<string>",
      "severity": "low|medium|high",
      "trigger": "<string>",
      "detection": "<string>",
      "mitigation": "<string>",
      "verification": "<string>"
    }
  ],
  "rollback_plan": {
    "rollback_strategy": "<string>",
    "recovery_steps": ["<string>"]
  },
  "implementation_inputs": {
    "required_context": ["<string>"],
    "suggested_phase3_prompts": ["<path>"]
  }
}
```

## Completion condition

This phase is complete only when an implementer can execute the work breakdown step-by-step, and when the plan packet is precise enough that the implementation phase can be run with minimal additional interpretation.

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
