# Graph Workflow

`library/graph/` is the consolidated orchestration layer for this repository.

## Layout
- `nodes/`: granular prompt nodes (preserved one-file-per-capability).
- `rules/`: deterministic routing and safety policy.
- `workflows/`: executable graph paths and branch definitions.

## Intended end-to-end workflow
1. Start with `workflows/initial_prompt_graph_workflow.md`.
2. Apply `rules/routing_ruleset.md`.
3. Dispatch to a primary objective path.
4. If implementation is required, select language branch:
   - `workflows/python_branch.md`
   - `workflows/rust_branch.md`
5. Execute node transitions with governance:
   - `nodes/execution/handoff_packet_generator.md`
   - `nodes/execution/chain_execution_protocol.md`
6. Enforce risk gates before any destructive mutation.

## Primary objective paths
- Research: `workflows/research_path.md`
- Objective-to-product: `workflows/objective_to_product_pipeline.md`
- Incident response: `nodes/incident_response/incident_response_and_postmortem.md`
- Security-first: `nodes/security/security_threat_model.md`
- Rollout: `nodes/migration/migration_and_rollout.md`

## Granularity guarantee
- Prompt granularity is preserved under `nodes/`.
- Orchestration composes existing nodes instead of merging them.
