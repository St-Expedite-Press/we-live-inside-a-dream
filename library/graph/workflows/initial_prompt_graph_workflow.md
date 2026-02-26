# Initial Prompt Graph Workflow

Derived operational view of `library/graph/workflows/top_level_prompt_chain.md`.

This workflow is example-agnostic. It classifies an initial prompt into one of three primary paths and then applies overlay gates.

## Step 1: Intake
Input: verbatim user prompt.
Output: normalized objective, constraints, and risk flags.
Primary node: `library/graph/nodes/implementation/prompt_decision_workflow.md`.

## Step 2: Rule Evaluation
Apply `library/graph/rules/routing_ruleset.md` in strict order.
Output: selected path ID and justification.

## Step 3: Path Dispatch
- `research`: `library/graph/workflows/research_path.md`
- `python`: `library/graph/workflows/python_branch.md`
- `rust`: `library/graph/workflows/rust_branch.md`
- `clarification`: request missing information then re-run Step 2.

## Step 4: Overlay Gates
Apply these when triggered by rules:
- `incident_gate`: `library/graph/nodes/incident_response/incident_response_and_postmortem.md`
- `security_gate`: `library/graph/nodes/security/security_threat_model.md`
- `rollout_gate`: `library/graph/nodes/migration/migration_and_rollout.md`

## Step 5: Governance
Apply handoff packaging and chain protocol before each node transition:
- `library/graph/nodes/execution/handoff_packet_generator.md`
- `library/graph/nodes/execution/chain_execution_protocol.md`

## Step 6: Termination
Stop when path acceptance criteria are satisfied and required approvals are recorded.
