# Graph Workflows

This folder defines the executable workflow graph for the repository.

## Workflow hierarchy

1. Entry workflow: `initial_prompt_graph_workflow.md`.
2. Rules engine: `../rules/routing_ruleset.md`.
3. Objective paths:
   - `research_path.md`
   - `objective_to_product_pipeline.md`
   - `image_restoration_python_branch.md`
   - `image_restoration_rust_branch.md`
4. Language branches:
   - `python_branch.md`
   - `rust_branch.md`
5. Templates: `templates/`.

## Branching policy

- Prompt granularity is preserved at node level under `library/graph/nodes/`.
- Workflows only orchestrate nodes; they do not collapse or merge prompts.
- Python and Rust are first-class branches selected by explicit rules.

## Start order

1. Run `initial_prompt_graph_workflow.md`.
2. Apply routing rules.
3. Select objective path.
4. Select language branch (`python_branch.md` or `rust_branch.md`) when implementation is required.
5. Execute nodes with handoff and chain protocol.
