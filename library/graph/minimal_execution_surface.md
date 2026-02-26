# Minimal Execution Surface

Use only these files to run the prompt chain:

1. Entry flow: `library/graph/workflows/top_level_prompt_chain.md`
2. Rules: `library/graph/rules/routing_ruleset.md`
3. Primary paths:
   - `library/graph/workflows/research_path.md`
   - `library/graph/workflows/python_branch.md`
   - `library/graph/workflows/rust_branch.md`
4. Overlay gates:
   - `library/graph/nodes/incident_response/incident_response_and_postmortem.md`
   - `library/graph/nodes/security/security_threat_model.md`
   - `library/graph/nodes/migration/migration_and_rollout.md`
5. Governance nodes:
   - `library/graph/nodes/execution/handoff_packet_generator.md`
   - `library/graph/nodes/execution/chain_execution_protocol.md`
