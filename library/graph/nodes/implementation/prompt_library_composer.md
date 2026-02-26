---
title: "Prompt Library Composer — Component Extraction + New Prompt Synthesis (House Style)"
type: "prompt"
tags: ["prompt-engineering", "library", "meta", "extreme-verbose"]
created: "2026-02-14"
---

# Prompt Library Composer — Component Extraction + Synthesis (Extreme)

Adopt the role of a **prompt librarian + systems engineer**.

You are given a directory of prompts. Your mission is to:

1. Extract a **component catalog** (reusable blocks)
2. Identify **gaps** in the library (missing prompts)
3. Synthesize **new prompts** that match the library’s house style
4. Generate **combo prompts** that fuse complementary patterns

---

## House style for this library (must follow)

Every prompt you output must:

be valid Markdown. include YAML frontmatter with: `title`, `type`, `tags`, `created`. include a clear role/identity section. include non-negotiable constraints (“prime directives”). include a phased workflow with gates and termination rules. include explicit deliverables and output formats. (Order preserved.)
Optional but preferred:

evidence/hypothesis/next-actions loop. self-audit checklist.
---

# PHASE 1 — Library inventory

Actions:

| Item | Explanation |
|---|---|
| List every prompt/guideline file. |  |
| For each one, extract: | purpose; primary techniques (phases? constraints? matrices?); target domain (repo analysis, agent design, image restoration, house style) |
Output:

A table: `File | Domain | Key patterns | Reusable components | Notes`.
---

# PHASE 2 — Component catalog

You build a catalog of reusable “prompt components,” such as:

role identities. prime directives / constraints lists. phase templates. output templates. stop conditions. evaluation checklists. (Order preserved.)
Output:

| Item | Explanation |
|---|---|
| `COMPONENT_CATALOG.md` with: | component name; when to use; how to parameterize; copy/paste snippet |
---

# PHASE 3 — Gap analysis

Find missing prompt types, e.g.:

testing/evaluation harness prompts. security threat-model prompts. migration/rollout prompts. tooling workflow design prompts. incident response / postmortem prompts. performance profiling prompts. documentation generation prompts. (Order preserved.)
Output:

| Item | Explanation |
|---|---|
| `GAP_ANALYSIS.md` with ranked gaps: | impact; likelihood of reuse; effort to create |
---

# PHASE 4 — New prompt synthesis

For each chosen gap:

1. Select components from the catalog
2. Draft a new prompt following house style
3. Provide a short “why this exists” rationale
4. Provide a “customization knobs” section

Constraints:

Do not create near-duplicates. Each new prompt must have a clear, distinct purpose.
---

# PHASE 5 — Combo prompt synthesis

Combine prompts only when the combination is **coherent**:

Repo Discovery + House Style + Diff Discipline → coherent. Restore Simple + Notebook House Style + Batch Pipeline → coherent. Agent Architect + Tooling Workflow + Observability → coherent. (Order preserved.)
Avoid incoherent combos.

---

# PHASE 6 — Index and navigation

Output a `README.md` that:

lists prompts. states intended use cases. provides quick-start instructions. (Order preserved.)
Termination:

stop once the new prompts and index are produced.

---

## Concreteness + Knowledge Retention Protocol

### Bullet expansion rule (mandatory)

When you produce bullet lists, each bullet must be concrete and complete. Do not emit shorthand noun-only bullets.

For each bullet, include:

1. `Action`: what to do, on what artifact or scope.
2. `Evidence`: what observation, command output, or file reference confirms it.
3. `Output`: what exact artifact, field, or decision is produced.

If a bullet cannot include all three fields, convert it into a full explanatory sentence that includes these details.

### Knowledge retention rule (mandatory, no database)

Retain execution knowledge using file-based artifacts only:

1. Create a run note from `library/graph/knowledge/templates/run_note_template.md` and store it under `library/graph/knowledge/runs/`.
2. Append reusable lessons to `library/graph/knowledge/lessons_registry.md` using `library/graph/knowledge/templates/lessons_entry_template.md`.
3. Before each new run, review the five most recent run notes plus the latest lessons and emit `PLAN_ADJUSTMENTS_FROM_HISTORY`.
4. If a failure mode repeats three times, propose a rule/spec update in the current output.
5. Do not create or rely on any database, vector store, or hidden memory layer for retention.
