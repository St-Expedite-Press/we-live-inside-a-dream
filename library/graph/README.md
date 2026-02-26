# Graph Workflow

`library/graph/` is the consolidated orchestration layer for this repository.

## Layout
- `nodes/`: granular prompt nodes (preserved one-file-per-capability).
- `rules/`: deterministic routing and safety policy.
- `workflows/`: executable graph paths and branch definitions.
- `registry/`: deterministic artifact and schema metadata for build tooling.
- `minimal_execution_surface.md`: minimal files required to run the chain.

## Intended end-to-end workflow
1. Start with `workflows/initial_prompt_graph_workflow.md`.
2. Apply `rules/routing_ruleset.md`.
3. Classify to exactly one primary path: `research`, `python`, or `rust`.
4. Apply overlay gates (`incident_gate`, `security_gate`, `rollout_gate`) when triggered.
5. Execute node transitions with governance:
   - `nodes/execution/handoff_packet_generator.md`
   - `nodes/execution/chain_execution_protocol.md`
6. Enforce risk gates before any destructive mutation.

## Primary paths
- Research: `workflows/research_path.md`
- Python: `workflows/python_branch.md`
- Rust: `workflows/rust_branch.md`

## Overlay gates
- Incident gate: `nodes/incident_response/incident_response_and_postmortem.md`
- Security gate: `nodes/security/security_threat_model.md`
- Rollout gate: `nodes/migration/migration_and_rollout.md`

## Granularity guarantee
- Prompt granularity is preserved under `nodes/`.
- Orchestration composes existing nodes instead of merging them.
