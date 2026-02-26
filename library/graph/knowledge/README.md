# Knowledge Retention (File-based)

This directory defines no-database knowledge retention methods for graph workflows.

## Method

1. For each execution, create a run note under `runs/` from the run template.
2. Append reusable lessons to `lessons_registry.md`.
3. Before a new run, read the five most recent run notes and the latest lessons.
4. Emit `PLAN_ADJUSTMENTS_FROM_HISTORY` in the next run plan.

## Required artifacts

- `templates/run_note_template.md`
- `templates/lessons_entry_template.md`
- `lessons_registry.md`
- `runs/` directory (created during execution)

## Constraints

- No databases.
- No hidden memory stores.
- Retention must be human-auditable in versioned Markdown files.
