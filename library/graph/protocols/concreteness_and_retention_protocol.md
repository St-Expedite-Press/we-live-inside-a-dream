# Concreteness and Knowledge Retention Protocol

Use this protocol in every prompt node.

## Concreteness rule

For each bullet, include:

1. `Action`: exact operation and target artifact.
2. `Evidence`: file reference, command output, or observed signal that justifies the action.
3. `Output`: exact artifact, field, or decision produced.

If all three cannot be provided, write a complete sentence containing the missing details rather than shorthand bullets.

## Knowledge retention rule (no database)

1. Create run notes under `library/graph/knowledge/runs/` using `library/graph/knowledge/templates/run_note_template.md`.
2. Append reusable lessons to `library/graph/knowledge/lessons_registry.md` using `library/graph/knowledge/templates/lessons_entry_template.md`.
3. Before each run, review the five latest run notes and latest lessons.
4. Emit `PLAN_ADJUSTMENTS_FROM_HISTORY` in the current plan.
5. If the same failure repeats three times, propose a rule/spec update.
6. Do not use databases, vector stores, or hidden memory for retention.
