---
title: "Extreme Combos — Index"
type: "index"
tags:
  - "prompt-library"
  - "combo-prompts"
  - "high-verbosity"
  - "high-complexity"
created: "2026-02-14"
---

# Extreme Combos (high-verbosity / high-complexity prompt set)

This doc indexes **intentionally overbuilt, extremely verbose** prompts that **combine** patterns from the existing library:

- **Agent Architect** style phased design (`prompts/implementation/agent_architect_10_phase_agent_systems_blueprint.md`)
- **Repo Discovery** evidence-first workflow (`prompts/discovery/repo_discovery_massive_prompt.md`)
- **Rust / Python House Style** constraints (`prompts/discovery/rust_repo_discovery_engineer.md`, `prompts/discovery/python_repo_discovery_engineer.md`, and the docs in `prompts/misc/`)
- **Terrifyingly exhaustive service industrialization** doc-corpus output (`prompts/discovery/explore_repo.md`)
- **Multimodal restoration** constraint-matrix workflow (`prompts/implementation/restore_simple_openai.md`)

These are “kitchen-sink” prompts meant for:

- writing a complete engineering plan + implementation + test + rollout pack
- turning repos into services, tools, and MCP ecosystems
- generating structured documentation corpora
- building evaluation harnesses and reliability loops
- creating multimodal pipelines (image restoration → code → reproducible notebook)

## Files

1. **omni_agent_platform.md** (canonical: `prompts/implementation/omni_agent_platform.md`)
   - The biggest combo: repo forensics → service transformation → agent/tool design → MCP tooling → knowledge graph → production deployment.

2. **evidence_driven_implementation.md** (canonical: `prompts/implementation/evidence_driven_implementation.md`)
   - “Smallest correct diff” execution prompt with explicit evidence/hypothesis loops, plus language-specific house-style gates (Python/Rust).

3. **mcp_server_factory.md** (canonical: `prompts/implementation/mcp_server_factory.md`)
   - Builds an MCP server/tool suite around a repo or capability with strict schema discipline, safety, and testing.

4. **prompt_library_composer.md** (canonical: `prompts/implementation/prompt_library_composer.md`)
   - A meta-prompt for **extracting components** from existing prompts and generating new prompts in the same “house style”.

5. **multimodal_restoration_pipeline.md** (canonical: `prompts/implementation/multimodal_restoration_pipeline.md`)
   - Combines “Restore Simple” (metadata vector + constraint matrix) with engineering deliverables: batch restoration pipeline, notebook, evaluation, and artifact export.

6. **service_industrializer.md** (canonical: `prompts/implementation/service_industrializer.md`)
   - A new, more disciplined “Explore Repo” variant that forces termination conditions, abstraction budgets, and “no speculative architecture” constraints.

7. **agent_testing_eval_gauntlet.md** (canonical: `prompts/execution/agent_testing_eval_gauntlet.md`)
   - A new prompt focused on agent/reasoning/tool testing, adversarial evaluation, and production monitoring.

8. **security_threat_model.md** (canonical: `prompts/security/security_threat_model.md`)
   - STRIDE/LINDDUN threat modeling with concrete mitigations + verification plan.

9. **migration_and_rollout.md** (canonical: `prompts/migration/migration_and_rollout.md`)
   - Backward compatibility + canary rollout + rollback planning.

10. **incident_response_and_postmortem.md** (canonical: `prompts/incident_response/incident_response_and_postmortem.md`)
    - Incident playbook + postmortem template + prevention backlog.

11. **chain_router_and_runbook.md** (canonical: `prompts/execution/chain_router_and_runbook.md`)
    - Chooses which extreme prompts to run next and produces a step-by-step chain runbook.

12. **handoff_packet_generator.md** (canonical: `prompts/execution/handoff_packet_generator.md`)
    - Packages upstream outputs into a minimal, high-fidelity context packet for the next prompt.

13. **chain_execution_protocol.md** (canonical: `prompts/execution/chain_execution_protocol.md`)
    - Governance and logging protocol for chaining: state model, approvals, quality gates, stop conditions.

## How to use

- Copy a prompt into your LLM as a **system** prompt (or top-of-chat instruction) and then answer its Phase 1 questions.
- If you’re using an agentic coding environment, keep the “Termination rule” sections intact to prevent scope creep.
- Most prompts support a **two-turn workflow**:
  1) generate evidence + plan only
  2) implement and produce deliverables

## Customization knobs

Each prompt exposes common knobs:

- `RISK_TOLERANCE`: prototype / production / regulated
- `BLAST_RADIUS`: single module / subsystem / cross-cutting
- `VERBOSITY`: keep at “max” for these prompts; reduce only if needed
- `OUTPUT_MODE`: plan-only vs plan+implementation vs full doc corpus
