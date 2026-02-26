# prompt-ecosystem-library

A deterministic prompt-governance and compilation repository.

This repository defines, organizes, validates, and compiles prompt-chain assets.
It is designed for teams building controlled prompt workflows that must be inspectable, reproducible, and evolvable.

It is not:

- a model-inference runtime
- a hosted API
- an agent execution engine
- a chat product

It is:

- a source-of-truth prompt graph
- a routing and governance framework
- a compiler for human and machine-readable prompt artifacts

---

## 1. What This Repo Does

At a high level, the repo converts canonical prompt assets into standardized outputs.

Input layer:

- prompt nodes (`library/graph/nodes/`)
- workflows (`library/graph/workflows/`)
- route rules (`library/graph/rules/`)
- protocols (`library/graph/protocols/`)
- registry metadata (`library/graph/registry/`)

Compilation layer:

- `library/book/_build_book.py`

Output layer:

- `library/book/BOOK.md`
- `library/book/TOC.md`
- `library/book/CATALOG.md`
- `library/book/ONTOLOGY.md`
- `library/book/ontology/prompt_ecosystem.json`
- `library/book/ontology/prompt_ecosystem.jsonld`
- `library/book/ontology/prompt_ecosystem.yaml`

The build output gives both human navigation and machine-consumable ontology metadata.

---

## 2. Top-Level Architecture

```text
User/Operator Prompt
  -> Graph Entry Workflow
  -> Rule-Based Classification
  -> Primary Path Execution
  -> Overlay Gate Evaluation
  -> Handoff/Chain Governance
  -> Project-Specific Prompt Package Outputs

Canonical Sources
  -> Build Compiler
  -> Book + Catalog + Ontology Exports
```

Core principle: deterministic prompt infrastructure.

Given the same source files and tooling, outputs should be stable and reproducible.

---

## 3. Canonical Prompt Chain Contract

The application-facing flow is in:

- `library/graph/workflows/top_level_prompt_chain.md`

Classifier outputs (exactly one primary path):

- `research`
- `python`
- `rust`

Cross-cutting overlay gates (can wrap any primary path):

- `incident_gate`
- `security_gate`
- `rollout_gate`

Operational view of same flow:

- `library/graph/workflows/initial_prompt_graph_workflow.md`

Minimal required files for execution:

- `library/graph/minimal_execution_surface.md`

---

## 4. Directory-by-Directory Explanation

### `library/graph/`

This is the canonical source layer.

- `nodes/`: atomic prompt building blocks
- `workflows/`: route and orchestration documents
- `rules/`: classifier policy and gate rules
- `protocols/`: shared behavioral/output rules
- `knowledge/`: file-based retention templates and lessons
- `registry/`: deterministic artifact metadata
- `minimal_execution_surface.md`: reduced execution surface for operators

### `library/examples/`

Example-specific flows only.

Purpose:

- keep core graph example-agnostic
- isolate demonstrations from primary production flow

### `library/book/`

Compiled view layer.

- generated navigation and ontology artifacts
- should not be treated as the source-of-truth authoring layer

### `library/tools/validation/`

Consistency and policy validators.

### `library/docs/`

Supporting design docs and agent specs.

### `library/research/`

Reference notes for prompt design patterns, not runtime execution code.

---

## 5. Key Files and Their Responsibilities

### Graph execution and routing

- `library/graph/workflows/top_level_prompt_chain.md`
  - canonical classifier and augmentation flow

- `library/graph/rules/routing_ruleset.md`
  - deterministic route rules + overlay gate triggers

- `library/graph/workflows/research_path.md`
  - research-first execution path

- `library/graph/workflows/python_branch.md`
  - Python implementation branch

- `library/graph/workflows/rust_branch.md`
  - Rust implementation branch

### Governance nodes

- `library/graph/nodes/execution/handoff_packet_generator.md`
  - structured context handoff between steps

- `library/graph/nodes/execution/chain_execution_protocol.md`
  - chain-state discipline and gate handling

- `library/graph/nodes/execution/chain_router_and_runbook.md`
  - orchestration-level route/runbook generation prompt

### Shared protocols

- `library/graph/protocols/concreteness_and_retention_protocol.md`
  - required concreteness standard and no-database retention behavior

- `library/graph/protocols/output_schema.md`
  - standard output section contracts

### Knowledge retention (file-based)

- `library/graph/knowledge/templates/run_note_template.md`
- `library/graph/knowledge/templates/lessons_entry_template.md`
- `library/graph/knowledge/lessons_registry.md`
- `library/graph/knowledge/runs/`

### Compiler and registry

- `library/book/_build_book.py`
  - reads canonical artifacts
  - uses registry when present
  - generates book/catalog/ontology outputs

- `library/graph/registry/artifacts_registry.json`
  - deterministic artifact list metadata

- `library/graph/registry/frontmatter_schema.md`
  - required prompt frontmatter contract

---

## 6. Exact Build Pipeline Behavior

When you run the build:

1. source artifacts are loaded from graph/registry + canonical files
2. artifact list is ordered deterministically by `order`
3. TOC, CATALOG, ONTOLOGY.md, BOOK.md are rendered
4. ontology exports (JSON / JSON-LD / YAML) are emitted
5. formatting post-processing runs for book artifacts

Build command:

```bash
python3 library/book/_build_book.py
```

Equivalent entrypoint:

```bash
python3 library/library.py build-book
```

---

## 7. Validation and CI

Local validators:

```bash
python3 library/tools/validation/lint_frontmatter.py
python3 library/tools/validation/lint_graph_names.py
python3 library/tools/validation/detect_orphan_docs.py
```

Registry sync utility:

```bash
python3 library/tools/validation/sync_artifact_registry.py
```

CI workflow:

- `.github/workflows/graph_consistency.yml`

CI enforces:

- frontmatter validity
- naming consistency
- orphan-graph-doc detection
- deterministic book rebuild (diff must be clean)

---

## 8. How Routing Works in Practice

Routing has two layers.

Layer A: primary path classifier

- choose one of `research | python | rust`

Layer B: overlay gates

- incident gate applies when active incidents/outages exist
- security gate applies when trust boundary/secret/auth scope changes
- rollout gate applies when release/migration/compatibility concerns exist

Overlay gates do not replace the primary path. They wrap or prepend required controls.

---

## 9. How Knowledge Retention Works (and Why)

Retention is intentionally file-based.

Mechanism:

1. each run creates a run note in `knowledge/runs/`
2. reusable lessons are appended to `lessons_registry.md`
3. subsequent runs read recent run notes + lessons
4. plan adjusts via explicit `PLAN_ADJUSTMENTS_FROM_HISTORY`

Why this design:

- auditable in git history
- deterministic
- no hidden state
- no infrastructure dependency

Hard rule:

- no database/vector-store retention in this repo

---

## 10. Source-of-Truth Hierarchy

Use this strict precedence:

1. canonical graph assets (`library/graph/*`)
2. registry metadata (`library/graph/registry/artifacts_registry.json`)
3. compiled outputs (`library/book/*`)

If compiled artifacts diverge from canonical graph source, canonical graph source wins.

---

## 11. How to Add New Prompt Capabilities Safely

Recommended change sequence:

1. create/modify canonical node/workflow/rule under `library/graph/`
2. ensure frontmatter follows schema
3. run validators
4. rebuild book outputs
5. inspect generated diffs
6. update docs only where behavior changed

Do not add example-specific behavior to core graph workflows.
Place examples in `library/examples/workflows/`.

---

## 12. How to Evolve the Top-Level Chain

If classifier logic changes:

1. update `library/graph/rules/routing_ruleset.md`
2. update `library/graph/workflows/top_level_prompt_chain.md`
3. update `library/graph/workflows/initial_prompt_graph_workflow.md`
4. update `library/graph/minimal_execution_surface.md`
5. run validation + rebuild

Keep primary classifier outputs explicit and minimal.

---

## 13. Agent Specs and Their Role

Agent specs in `library/docs/agent_specs/` are operating instructions for prompt-driven agents.

They define:

- route/orchestration behavior
- branch-specific execution behavior
- security/rollout gate behaviors
- self-improvement and retention instructions

They are guidance assets that operate on the graph architecture, not independent runtime services.

---

## 14. Security and Safety Boundaries

This repository should not:

- store secrets in tracked files
- embed credentials in compiled outputs
- trigger destructive actions without explicit gate/approval semantics

If secrets are exposed, rotate and revoke immediately.

---

## 15. Operational Commands

```bash
# 1) Validate
python3 library/tools/validation/lint_frontmatter.py
python3 library/tools/validation/lint_graph_names.py
python3 library/tools/validation/detect_orphan_docs.py

# 2) Build outputs
python3 library/book/_build_book.py

# 3) Optional registry sync helper
python3 library/tools/validation/sync_artifact_registry.py
```

---

## 16. Troubleshooting

### Build outputs changed unexpectedly

- verify registry and canonical source edits
- rerun validators
- inspect artifact order and source path changes

### Route behavior feels ambiguous

- check `routing_ruleset.md`
- ensure objective includes explicit language/goal cues
- enforce clarification route when under-specified

### Prompt outputs are too vague

- verify shared concreteness protocol is referenced
- enforce `Action/Evidence/Output` bullet discipline

---

## 17. Determinism Guarantees and Limits

Guaranteed by design:

- stable artifact ordering
- explicit source paths
- explicit classifier rules
- file-based retention policy

Not guaranteed by this repo:

- downstream model behavior
- external tool runtime stability
- cloud/network-dependent variability

This repo governs prompt artifacts and chain structure. Execution variability downstream must be handled by consumer systems.

---

## 18. Minimal Start for New Operators

If you are onboarding and want the shortest path:

1. read `library/graph/minimal_execution_surface.md`
2. run validators
3. run build
4. inspect `library/book/BOOK.md`

Then branch into the relevant path (`research`, `python`, or `rust`).

---

## 19. Glossary

- Node: atomic prompt asset
- Workflow: orchestration sequence of nodes
- Rule: deterministic classifier/gate condition
- Overlay gate: cross-cutting governance stage
- Registry: deterministic artifact metadata catalog
- Compiled book: generated navigation and ontology outputs
- Prompt package suite: project-specific output set after augmentation

---

## 20. Final Boundary Statement

This repository is the prompt infrastructure control plane.

It defines how prompts are authored, routed, constrained, retained, validated, and compiled.

It does not execute model inference itself.
