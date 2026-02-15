---
title: "Prompt Ecosystem Ontology"
type: "ontology"
tags: ["ontology", "prompt-library"]
created: "2026-02-15"
---

# Prompt Ecosystem Ontology

This ontology models the library as a **directed ecosystem**:

artifacts (prompts/guidelines/indexes). domains (what the artifact is about). techniques (what the artifact *does*). relationships (how artifacts compose into chains). (Order preserved.)
The goal is not academic purity; it’s practical routing: **given an objective, pick the right prompt(s) and order them safely**.

---

## 1) Core entity types

### 1.1 Artifact
An **Artifact** is any first-class Markdown object in the library:

prompts (procedural, phased, actionable). guidelines (constraints/standards). indexes/readmes (navigation). intermediate orchestrators (routers/handoffs/protocols). (Order preserved.)
Minimum fields:

`id`: stable identifier (e.g. `EC-03`). `title`: human label. `kind`: prompt | guidelines | index. `domain_tags`: e.g. `repo-analysis`, `mcp`, `security`. `techniques`: e.g. `phases`, `evidence-ledger`, `schema-first`. `inputs`: what it requires to run. `outputs`: deliverables it promises. (Order preserved.)
### 1.2 Domain
A **Domain** is a topical cluster:

`repo-analysis` / `implementation`. `agent-systems`. `mcp` / `tooling`. `knowledge-graph`. `multimodal` / `image-restoration`. `security`. `ops` / `observability`. `meta-orchestration`. (Order preserved.)
### 1.3 Technique
A **Technique** is a reusable behavioral primitive (components you can compose):

phased workflow. evidence → hypothesis → next-actions loop. constraint matrices. schema-first tool design. termination gates / stop conditions. abstraction budgets (anti-bloat). safety/approval gates (mutations). regression/eval harness design. (Order preserved.)
### 1.4 Relationship
Relationships are edges between artifacts:

`COMBINES_WITH` (A is a combo of B+C). `ENFORCES` (A enforces guideline G). `ROUTES_TO` (A selects and dispatches to B). `PRECEDES` (A should run before B). `PRODUCES_INPUT_FOR` (A outputs data B requires). (Order preserved.)
---

## 2) Canonical ecosystem graph (high-level)

```mermaid
graph TD
  HS[House Styles & Discipline] --> IMPL[Evidence-Driven Implementation]
  HS --> SRV[Service Industrializer / Omni Platform]
  IMPL --> ROL[Migration & Rollout]
  SRV --> MCP[MCP Server Factory]
  MCP --> EVAL[Agent Testing & Eval]
  SRV --> SEC[Security Threat Model]
  SEC --> IMPL
  ROL --> OPS[Incident Response & Postmortem]
  ROUTER[Chain Router + Runbook] --> IMPL
  ROUTER --> SRV
  ROUTER --> MCP
  ROUTER --> SEC
  ROUTER --> ROL
  ROUTER --> EVAL
  HANDOFF[Handoff Packet Generator] --> ROUTER
  PROTO[Chain Execution Protocol] --> ROUTER
```

Interpretation:

**House styles** constrain implementation prompts. **Security** often precedes implementation for high-risk objectives. **Rollout** precedes production deploy. **Incident response** is an interrupt handler: it can preempt the chain. (Order preserved.)
---

## 3) Artifact IDs included in this book

`F-01` → `prompts/misc/python_house_style.md`. `F-02` → `prompts/misc/rust_house_style.md`. `F-03` → `prompts/misc/rust_antibloat.md`. `F-04` → `prompts/misc/colab_notebook_house_style.md`. `C-01` → `prompts/implementation/agent_architect_10_phase_agent_systems_blueprint.md`. `C-02` → `prompts/discovery/repo_discovery_massive_prompt.md`. `C-03` → `prompts/discovery/python_repo_discovery_engineer.md`. `C-04` → `prompts/discovery/rust_repo_discovery_engineer.md`. `C-05` → `prompts/discovery/explore_repo.md`. `M-01` → `prompts/implementation/restore_simple_openai.md`. `EC-01` → `prompts/implementation/omni_agent_platform.md`. `EC-02` → `prompts/implementation/evidence_driven_implementation.md`. `EC-03` → `prompts/implementation/mcp_server_factory.md`. `EC-04` → `prompts/implementation/prompt_library_composer.md`. `EC-05` → `prompts/implementation/multimodal_restoration_pipeline.md`. `EC-06` → `prompts/implementation/service_industrializer.md`. `EC-07` → `prompts/execution/agent_testing_eval_gauntlet.md`. `EC-08` → `prompts/security/security_threat_model.md`. `EC-09` → `prompts/migration/migration_and_rollout.md`. `EC-10` → `prompts/incident_response/incident_response_and_postmortem.md`. `EC-11` → `prompts/execution/chain_router_and_runbook.md`. `EC-12` → `prompts/execution/handoff_packet_generator.md`. `EC-13` → `prompts/execution/chain_execution_protocol.md`. `IR-01` → `prompts/execution/image_restoration_pipeline_router.md`. `IR-02` → `prompts/implementation/image_restoration_pipeline_builder_python.md`. `IR-03` → `prompts/implementation/image_restoration_pipeline_builder_rust.md`. `P-01` → `paths/README.md`. `P-02` → `paths/python/image_restoration_pipeline.md`. `P-03` → `paths/rust/image_restoration_pipeline.md`. `META-01` → `docs/repo_mental_model.md`. `META-02` → `docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md`. `P-04` → `paths/common/objective_to_product_pipeline.md`. `META-03` → `docs/phase_groups.md`. `PH-01` → `prompts/execution/objective_to_product_phase_pipeline.md`. `PH-02` → `prompts/exploratory/objective_intake_and_context_map.md`. `PH-03` → `prompts/planning/product_plan_compiler.md`. `PH-04` → `prompts/implementation/product_build_executor.md`. (Order preserved.)
---

## 4) Prompt selection heuristics (routing rules)

Use these rules when deciding what to run:

1. If there is an active outage or customer incident → run **Incident Response** first.
2. If the objective is a small feature/bugfix → run **Evidence-Driven Implementation**.
3. If the objective is ‘turn repo into a service/tool platform’ → run **Omni Agent Platform** or **Service Industrializer**.
4. If you are exposing capabilities to agents → run **MCP Server Factory**.
5. If anything touches prod → run **Migration & Rollout**.
6. If agents/tools must be reliable → run **Agent Testing & Eval Gauntlet**.

---

## 5) Ontology exports

See `book/ontology/` for machine-readable exports:

`prompt_ecosystem.json`. `prompt_ecosystem.jsonld`. `prompt_ecosystem.yaml`. (Order preserved.)
