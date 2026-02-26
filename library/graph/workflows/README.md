# Graph Workflows

This folder defines the executable, example-agnostic prompt-chain graph for the repository.

## Workflow hierarchy

1. Canonical top-level chain: `top_level_prompt_chain.md`
2. Derived operational view: `initial_prompt_graph_workflow.md`
3. Rules engine: `../rules/routing_ruleset.md`.
4. Primary paths:
   - `research_path.md`
   - `python_branch.md`
   - `rust_branch.md`
5. Optional non-core workflow:
   - `objective_to_product_pipeline.md`
6. Example-specific workflows:
   - `library/examples/workflows/image_restoration_python_branch.md`
   - `library/examples/workflows/image_restoration_rust_branch.md`
   - index: `examples.md`
7. Templates: `templates/`.

## Branching policy

- Prompt granularity is preserved at node level under `library/graph/nodes/`.
- Workflows only orchestrate nodes; they do not collapse or merge prompts.
- Research, Python, and Rust are the only primary classifier outputs.
- Security, rollout, and incident are overlay gates that can wrap any primary path.
- Example-specific paths live under `library/examples/workflows/`.

## Start order

1. Run `initial_prompt_graph_workflow.md`.
2. Apply routing rules.
3. Select exactly one primary path (`research`, `python`, or `rust`).
4. Apply overlay gates if triggered.
5. Execute nodes with handoff and chain protocol.
