# Top-Level Prompt Chain (Example-Agnostic)

This is the canonical classifier and execution flow for the client application.

## Contract

Input: one raw user prompt.
Output: one customized prompt-chain package for the selected path.

## Classifier outputs (only these primary paths)

- `research`
- `python`
- `rust`

## Flow

1. Intake raw prompt and normalize objective.
2. Classify to exactly one primary path (`research`, `python`, or `rust`).
3. Build path runbook from the selected primary path.
4. Apply overlay gates when triggered:
   - `incident_gate`
   - `security_gate`
   - `rollout_gate`
5. Execute augmentation loop until outputs are project-specific and complete.
6. Emit final prompt-chain package with runbook + handoff packets + retained lessons references.

## Augmentation loop

Repeat until termination criteria are met:

1. Expand constraints and acceptance criteria.
2. Add project-specific context from evidence.
3. Refine node prompts and handoff packets.
4. Validate against gates and non-goals.
5. Record reusable lessons in file-based retention artifacts.

## Termination

Stop when:

- selected path outputs satisfy acceptance criteria,
- required gates are resolved,
- package is executable without missing context.

## Output Schema

Follow `library/graph/protocols/output_schema.md` for final response structure.
