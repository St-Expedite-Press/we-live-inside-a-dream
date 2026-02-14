---
title: "Prompt Ecosystem Book"
type: "book"
tags:
  - "prompt-library"
  - "book"
  - "ontology"
created: "2026-02-14"
---

# Prompt Ecosystem Book

A compiled, navigable edition of the prompts and guidelines in this repository.

## How to use this book

- If you want **the right prompt** for a task: start with **Chapter 13 (Chain Execution Protocol)** and **Chapter 11 (Chain Router + Runbook)**.
- If you want to **ship a change**: start with **Evidence-Driven Implementation** + then **Migration & Rollout**.
- If you want to **toolify a repo** for agents: start with **MCP Server Factory**.

## Book navigation

- Table of contents: `TOC.md`
- Ontology: `ONTOLOGY.md`
- Catalog: `CATALOG.md`

---

# Table of Contents

## Part I — Foundations (House Styles & Doctrine)

- [01. PYTHON HOUSE STYLE](../prompts/misc/python_house_style.md)
- [02. RUST HOUSE STYLE](../prompts/misc/rust_house_style.md)
- [03. RUST ANTIBLOAT](../prompts/misc/rust_antibloat.md)
- [04. COLAB NOTEBOOK HOUSE STYLE](../prompts/misc/colab_notebook_house_style.md)

## Part II — Core Discovery & Implementation

- [05. Agent Architect (10-phase agent systems blueprint)](../prompts/implementation/agent_architect_10_phase_agent_systems_blueprint.md)
- [06. REPO DISCOVERY — Massive Prompt](../prompts/discovery/repo_discovery_massive_prompt.md)
- [07. PYTHON_prompt — Repo-Discovery Engineer](../prompts/discovery/python_repo_discovery_engineer.md)
- [08. RUST_prompt — Repo-Discovery Engineer](../prompts/discovery/rust_repo_discovery_engineer.md)
- [09. Terrifyingly Exhaustive Repo Analysis → Service Platform](../prompts/discovery/explore_repo.md)

## Part III — Multimodal & Constraint-Matrix Prompts

- [10. Restore Simple — OpenAI](../prompts/implementation/restore_simple_openai.md)
- [15. Multimodal Restoration Pipeline — Restore Simple × Engineering × Colab](../prompts/implementation/multimodal_restoration_pipeline.md)

## Part IV — Extreme Combos (Production Platformization)

- [11. OMNI AGENT PLATFORM — Repo → Service → MCP → Agent Ecosystem](../prompts/implementation/omni_agent_platform.md)
- [12. Evidence-Driven Implementation — Smallest Correct Diff (Python/Rust gated)](../prompts/implementation/evidence_driven_implementation.md)
- [13. MCP Server Factory — Tool Suite Design + Implementation](../prompts/implementation/mcp_server_factory.md)
- [14. Prompt Library Composer — Component Extraction + Synthesis](../prompts/implementation/prompt_library_composer.md)
- [16. Service Industrializer — Exhaustive but Disciplined](../prompts/implementation/service_industrializer.md)

## Part V — Reliability, Ops, Security

- [17. Agent Testing & Eval Gauntlet](../prompts/execution/agent_testing_eval_gauntlet.md)
- [18. Security Threat Model — STRIDE/LINDDUN + Mitigations + Verification](../prompts/security/security_threat_model.md)
- [19. Migration & Rollout — Compatibility, Canary, Rollback](../prompts/migration/migration_and_rollout.md)
- [20. Incident Response + Postmortem](../prompts/incident_response/incident_response_and_postmortem.md)

## Part VI — Orchestration Layer (Chaining Prompts)

- [21. Chain Router + Runbook](../prompts/execution/chain_router_and_runbook.md)
- [22. Handoff Packet Generator](../prompts/execution/handoff_packet_generator.md)
- [23. Chain Execution Protocol](../prompts/execution/chain_execution_protocol.md)

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

### Recipe B — Repo → MCP tool suite → evaluated agent system
1. Service Industrializer or Omni Agent Platform
2. MCP Server Factory
3. Agent Testing & Eval Gauntlet
4. Migration & Rollout (if production)

### Recipe C — Multimodal restoration pipeline (reproducible)
1. Restore Simple (constraint matrix)
2. Multimodal Restoration Pipeline (batch + notebook)
3. (Optional) Threat model if public-facing tool is deployed
