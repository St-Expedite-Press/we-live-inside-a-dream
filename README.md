# prompt-ecosystem-library

This repository is a deterministic prompt-governance and compilation system.

It is not a chatbot runtime, not an inference service, and not a UI application. It is a source-controlled prompt infrastructure layer that turns canonical prompt assets into inspectable, routable, machine-readable outputs.

If you need one sentence:

This repo is a build system for prompt chains.

## Why This Exists

Prompt systems fail when they are managed as ad hoc chat snippets. Typical failures include:

- unclear source of truth
- prompt duplication and drift
- inconsistent handoff structure
- weak routing discipline
- no deterministic artifact model
- no audit trail for prompt changes

This repo solves those failures by defining:

- canonical prompt nodes (`library/graph/nodes/`)
- deterministic graph workflows (`library/graph/workflows/`)
- explicit routing rules (`library/graph/rules/`)
- retention protocols (`library/graph/knowledge/`, `library/graph/protocols/`)
- compiled and exported views (`library/book/` + ontology exports)

## Fast Orientation

Open these in order:

1. `library/graph/minimal_execution_surface.md`
2. `library/graph/workflows/top_level_prompt_chain.md`
3. `library/graph/rules/routing_ruleset.md`
4. `library/graph/workflows/research_path.md`, `python_branch.md`, `rust_branch.md`
5. `library/book/BOOK.md` (compiled navigation)

If you are extending internals, also read:

- `library/graph/registry/artifacts_registry.json`
- `library/book/_build_book.py`
- `.github/workflows/graph_consistency.yml`

## Core Mental Model

Treat prompts as source code.

- Nodes are source files.
- Workflows are orchestration code.
- Rules are route/classifier policy.
- Book/ontology files are compiled outputs.

The runtime for this repository is the build process itself. Model execution is downstream and out of scope.

## Repository Map

```text
library/
  graph/
    nodes/                 # canonical granular prompt nodes
    workflows/             # example-agnostic top-level and branch workflows
    rules/                 # primary classifier and overlay gates
    protocols/             # shared behavioral protocols
    knowledge/             # file-based knowledge retention artifacts/templates
    registry/              # deterministic metadata source for artifacts
    minimal_execution_surface.md
  examples/
    workflows/             # example-specific paths only
  book/
    _build_book.py         # compiler for book/catalog/ontology artifacts
    BOOK.md
    TOC.md
    CATALOG.md
    ONTOLOGY.md
    ontology/
      prompt_ecosystem.json
      prompt_ecosystem.jsonld
      prompt_ecosystem.yaml
  tools/
    validation/            # lint and consistency checks
  docs/
    agent_specs/
```

## Top-Level Prompt Chain (Application Contract)

The application-facing chain is example-agnostic and strictly classifier-driven.

Input:

- one raw prompt

Primary classifier outputs (exactly one):

- `research`
- `python`
- `rust`

Overlay gates (cross-cutting, can wrap any primary path):

- `incident_gate`
- `security_gate`
- `rollout_gate`

Reference:

- `library/graph/workflows/top_level_prompt_chain.md`

Operational view:

- `library/graph/workflows/initial_prompt_graph_workflow.md`

### High-Level Execution Graph

```text
raw user prompt
  -> intake normalization
  -> route classification (research|python|rust)
  -> primary path runbook
  -> apply overlay gates if triggered
  -> iterative augmentation loop
  -> emit project-specific prompt-chain package
```

### Iterative Augmentation Loop

The system repeatedly specializes outputs for the specific project context:

1. clarify constraints and acceptance criteria
2. inject evidence-derived project details
3. refine downstream prompt packets
4. validate against gates and non-goals
5. record lessons and feed adjustments forward

This loop terminates only when package outputs are executable without missing context.

## Primary Paths

### Research Path

Use when objective is synthesis/analysis and not immediate code mutation.

- `library/graph/workflows/research_path.md`

### Python Path

Use when implementation target is Python.

- `library/graph/workflows/python_branch.md`

### Rust Path

Use when implementation target is Rust.

- `library/graph/workflows/rust_branch.md`

## Overlay Gates

These are not primary classifier outcomes.

- incident gate: `library/graph/nodes/incident_response/incident_response_and_postmortem.md`
- security gate: `library/graph/nodes/security/security_threat_model.md`
- rollout gate: `library/graph/nodes/migration/migration_and_rollout.md`

## Governance Nodes

Use these for deterministic chaining:

- `library/graph/nodes/execution/handoff_packet_generator.md`
- `library/graph/nodes/execution/chain_execution_protocol.md`
- `library/graph/nodes/execution/chain_router_and_runbook.md`

## Knowledge Retention (No Database)

Retention is file-based, auditable, and versioned.

Protocol:

- `library/graph/protocols/concreteness_and_retention_protocol.md`

Storage:

- run notes: `library/graph/knowledge/runs/`
- lessons registry: `library/graph/knowledge/lessons_registry.md`
- templates: `library/graph/knowledge/templates/`

Hard constraint:

- no DB, vector store, or hidden memory layer

## Output Schema Contract

Standard section schema is centralized in:

- `library/graph/protocols/output_schema.md`

This reduces semantic drift across nodes and workflows.

## Build and Validation Pipeline

### Build

```bash
python3 library/book/_build_book.py
```

or:

```bash
python3 library/library.py build-book
```

### Validation

```bash
python3 library/tools/validation/lint_frontmatter.py
python3 library/tools/validation/lint_graph_names.py
python3 library/tools/validation/detect_orphan_docs.py
```

### Registry Sync (if needed)

```bash
python3 library/tools/validation/sync_artifact_registry.py
```

### CI

CI workflow:

- `.github/workflows/graph_consistency.yml`

It enforces:

- frontmatter lint
- naming lint
- orphan graph-doc detection
- rebuild + deterministic diff check for `library/book`

## Determinism Rules

Determinism in this repo means same inputs -> same outputs.

Practically:

- artifact order is explicit
- source paths are stable
- compiled views are regenerated from source
- no hidden mutable state in the build

If a change requires manual output edits in `library/book` without source updates, that is considered process drift.

## Source of Truth Hierarchy

1. canonical nodes/workflows/rules/protocols in `library/graph/`
2. artifact registry in `library/graph/registry/artifacts_registry.json`
3. generated views in `library/book/`

Never treat `library/book/*` as independent canonical content.

## Example Policy

Core workflows are example-agnostic.

Example-specific paths are isolated to:

- `library/examples/workflows/`

This keeps app-level routing clean while preserving reusable demos.

## Adding or Modifying Prompts Safely

Use this sequence:

1. edit canonical files in `library/graph/nodes/` or `library/graph/workflows/`
2. run validation tools
3. rebuild book outputs
4. verify deterministic diff behavior
5. update registry/schema docs only if artifact contracts changed

## Recommended Contribution Checklist

Before pushing changes:

- [ ] all validation scripts pass
- [ ] top-level flow remains `research|python|rust`
- [ ] overlay gates are still overlays, not primary paths
- [ ] no new example-specific logic leaked into core workflows
- [ ] book outputs regenerated and consistent
- [ ] retention protocol references remain intact in nodes

## What This Repo Does Not Do

- execute prompts against model providers
- store long-term runtime memory in databases
- host an API server for inference
- replace downstream agent runtime logic

It prepares and governs the prompt infrastructure that downstream runtimes consume.

## Glossary

- Node: canonical prompt file
- Workflow: orchestrated sequence of nodes
- Rule: classifier or gate policy
- Overlay gate: cross-cutting gate applied on top of primary path
- Package suite: project-specific chain output set ready for execution
- Compiled artifacts: generated navigation/ontology files in `library/book/`

## Operator Commands (Copy/Paste)

```bash
# validate
python3 library/tools/validation/lint_frontmatter.py
python3 library/tools/validation/lint_graph_names.py
python3 library/tools/validation/detect_orphan_docs.py

# build
python3 library/book/_build_book.py

# optional: registry sync from ontology
python3 library/tools/validation/sync_artifact_registry.py
```

## Minimal Entry Surface

If you only need to run the chain, start here and nowhere else:

- `library/graph/minimal_execution_surface.md`

## Additional References

- Agent specs: `library/docs/agent_specs/`
- Mental model: `library/docs/repo_mental_model.md`
- Compiled ontology: `library/book/ONTOLOGY.md`
