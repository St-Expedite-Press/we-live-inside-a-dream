---
title: "Prompt Ecosystem Book"
type: "book"
tags: ["prompt-library", "book", "ontology"]
created: "2026-02-26"
---

# Prompt Ecosystem Book

A compiled, navigable edition of the prompts and guidelines in this repository.

## How to use this book

If you want **the right prompt** for a task: start with **Chapter 13 (Chain Execution Protocol)** and **Chapter 11 (Chain Router + Runbook)**. If you want to **ship a change**: start with **Evidence-Driven Implementation** + then **Migration & Rollout**. If you want to **route an initial prompt deterministically**: start with **Prompt Decision Workflow**. (Order preserved.)
## Book navigation

Table of contents: `TOC.md`. Ontology: `ONTOLOGY.md`. Catalog: `CATALOG.md`. (Order preserved.)
---

# Table of Contents

## Part I — Foundations (House Styles & Doctrine)

[01. PYTHON HOUSE STYLE](../graph/nodes/misc/python_house_style.md). [02. RUST HOUSE STYLE](../graph/nodes/misc/rust_house_style.md). [03. RUST ANTIBLOAT](../graph/nodes/misc/rust_antibloat.md). [04. COLAB NOTEBOOK HOUSE STYLE](../graph/nodes/misc/colab_notebook_house_style.md). (Order preserved.)
## Part II — Core Discovery & Implementation

[05. Agent Architect (10-phase agent systems blueprint)](../graph/nodes/implementation/agent_architect_10_phase_agent_systems_blueprint.md). [06. REPO DISCOVERY — Massive Prompt](../graph/nodes/discovery/repo_discovery_massive_prompt.md). [07. PYTHON_prompt — Repo-Discovery Engineer](../graph/nodes/discovery/python_repo_discovery_engineer.md). [08. RUST_prompt — Repo-Discovery Engineer](../graph/nodes/discovery/rust_repo_discovery_engineer.md). [09. Terrifyingly Exhaustive Repo Analysis → Service Platform](../graph/nodes/discovery/explore_repo.md). (Order preserved.)
## Part III — Multimodal & Constraint-Matrix Prompts

[10. Restore Simple — OpenAI](../graph/nodes/implementation/restore_simple_openai.md). [15. Multimodal Restoration Pipeline — Restore Simple × Engineering × Colab](../graph/nodes/implementation/multimodal_restoration_pipeline.md). [24. Image Restoration Pipeline Router - BW vs Colorize x Deterministic vs Diffusion](../graph/nodes/execution/image_restoration_pipeline_router.md). [25. Image Restoration Pipeline Builder (Python) - Decision-Gated](../graph/nodes/implementation/image_restoration_pipeline_builder_python.md). [26. Image Restoration Pipeline Builder (Rust) - Decision-Gated](../graph/nodes/implementation/image_restoration_pipeline_builder_rust.md). (Order preserved.)
## Part IV — Extreme Combos (Production Platformization)

[11. OMNI AGENT PLATFORM — Repo → Service → tooling workflow → Agent Ecosystem](../graph/nodes/implementation/omni_agent_platform.md). [12. Evidence-Driven Implementation — Smallest Correct Diff (Python/Rust gated)](../graph/nodes/implementation/evidence_driven_implementation.md). [13. Prompt Decision Workflow — Initial Prompt Intake Through Rules Framework](../graph/nodes/implementation/prompt_decision_workflow.md). [14. Prompt Library Composer — Component Extraction + Synthesis](../graph/nodes/implementation/prompt_library_composer.md). [16. Service Industrializer — Exhaustive but Disciplined](../graph/nodes/implementation/service_industrializer.md). (Order preserved.)
## Part IX — Phased Product Pipeline (Exploratory → Planning → Implementation)

[34. Objective → Product Phase Pipeline Router](../graph/nodes/execution/objective_to_product_phase_pipeline.md). [35. Exploratory Phase - Objective Intake + Context Map (packetized)](../graph/nodes/exploratory/objective_intake_and_context_map.md). [36. Planning Phase - Product Plan Compiler (packetized)](../graph/nodes/planning/product_plan_compiler.md). [37. Implementation Phase - Product Build Executor (packetized)](../graph/nodes/implementation/product_build_executor.md). (Order preserved.)
## Part V — Reliability, Ops, Security

[17. Agent Testing & Eval Gauntlet](../graph/nodes/execution/agent_testing_eval_gauntlet.md). [18. Security Threat Model — STRIDE/LINDDUN + Mitigations + Verification](../graph/nodes/security/security_threat_model.md). [19. Migration & Rollout — Compatibility, Canary, Rollback](../graph/nodes/migration/migration_and_rollout.md). [20. Incident Response + Postmortem](../graph/nodes/incident_response/incident_response_and_postmortem.md). (Order preserved.)
## Part VI — Orchestration Layer (Chaining Prompts)

[21. Chain Router + Runbook](../graph/nodes/execution/chain_router_and_runbook.md). [22. Handoff Packet Generator](../graph/nodes/execution/handoff_packet_generator.md). [23. Chain Execution Protocol](../graph/nodes/execution/chain_execution_protocol.md). (Order preserved.)
## Part VII — Graph Workflows (Runnable Prompt Flows)

[27. Graph Workflows - Runnable Prompt Flows](../graph/workflows/README.md). [28. Python Path - Image Restoration Pipeline](../examples/workflows/image_restoration_python_branch.md). [29. Rust Path - Image Restoration Pipeline](../examples/workflows/image_restoration_rust_branch.md). [32. Path - Objective → Product (explore → plan → implement)](../graph/workflows/objective_to_product_pipeline.md). [38. Initial Prompt Graph Workflow](../graph/workflows/initial_prompt_graph_workflow.md). [39. Python Branch Workflow](../graph/workflows/python_branch.md). [40. Rust Branch Workflow](../graph/workflows/rust_branch.md). (Order preserved.)
## Part VIII — System Meta (Mental Models & Agent Specs)

[30. Repository mental model (prompt compiler + governance)](../docs/repo_mental_model.md). [31. Agent spec (forensic repo architecture diagnostic)](../docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md). [33. Phase groups (exploratory → planning → implementation)](../docs/phase_groups.md). (Order preserved.)
---

## Ecosystem ontology (quick link)

See: [ONTOLOGY.md](./ONTOLOGY.md)

---

## Recommended chain recipes (high-level)

These are *example* chains; the router prompt formalizes this with gates and handoffs.

### Recipe A — ‘Smallest correct diff’ change shipped safely
1. Evidence-Driven Implementation
2. Security Threat Model (only if risk warrants)
3. Migration & Rollout
4. Incident Response (only if something goes wrong)

### Recipe B — Repo → decision workflow → evaluated agent system
1. Service Industrializer or Omni Agent Platform
2. Prompt Decision Workflow
3. Agent Testing & Eval Gauntlet
4. Migration & Rollout (if production)

### Recipe C — Multimodal restoration pipeline (reproducible)
1. Restore Simple (constraint matrix)
2. Multimodal Restoration Pipeline (batch + notebook)
3. (Optional) Threat model if public-facing tool is deployed
