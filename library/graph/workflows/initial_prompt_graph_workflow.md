# Initial Prompt Graph Workflow

This workflow shepherds an initial prompt through routing rules and into a deterministic node path.

## Step 1: Intake
Input: verbatim user prompt.
Output: normalized objective, constraints, and risk flags.
Primary node: `library/graph/nodes/implementation/prompt_decision_workflow.md`.

## Step 2: Rule Evaluation
Apply `library/graph/rules/routing_ruleset.md` in strict order.
Output: selected path ID and justification.

## Step 3: Path Dispatch
- `research`: `library/graph/workflows/research_path.md`
- `implementation`: `library/graph/workflows/objective_to_product_pipeline.md`
- `python_branch`: `library/graph/workflows/python_branch.md`
- `rust_branch`: `library/graph/workflows/rust_branch.md`
- `security_review`: `library/graph/nodes/security/security_threat_model.md`
- `rollout`: `library/graph/nodes/migration/migration_and_rollout.md`
- `incident_response`: `library/graph/nodes/incident_response/incident_response_and_postmortem.md`
- `clarification`: request missing information then re-run Step 2.

## Step 4: Governance
Apply handoff packaging and chain protocol before each node transition:
- `library/graph/nodes/execution/handoff_packet_generator.md`
- `library/graph/nodes/execution/chain_execution_protocol.md`

## Step 5: Termination
Stop when path acceptance criteria are satisfied and required approvals are recorded.
