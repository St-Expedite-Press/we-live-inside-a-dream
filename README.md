# prompt-ecosystem-library

This repository is a deterministic prompt compilation and governance system. It is not a chatbot, not a runtime service, and not an “app”. It is a compiler-like pipeline that consumes canonical prompt definitions and emits structured prompt infrastructure: a compiled book, a catalog, ontology exports, and (optionally) improvement artifacts. If you want a single sentence that is operationally correct, use this one.

It is a build system for prompts.

The intent is to eliminate “prompt chaos” by turning prompts into governed, versioned assets with explicit structure, stable routing and chaining semantics, and predictable artifact outputs that downstream agents and services can consume without re-inventing prompt organization on every project.

## Start here (minimal navigation to get oriented)

The fastest orientation path is to read the compiled navigation layer, then jump into the canonical prompts.

| What you want | Open this |
|---|---|
| Book view of the entire library (TOC, catalog links, parts) | `library/book/BOOK.md` |
| Table of contents only (quick scan) | `library/book/TOC.md` |
| Catalog (table-form index of every artifact) | `library/book/CATALOG.md` |
| Ontology overview (human-readable) | `library/book/ONTOLOGY.md` |
| Canonical prompt source of truth | `library/prompts/` |
| Mental model and boundary definition (what the repo is and is not) | `library/docs/repo_mental_model.md` |
| Forensic audit agent spec (evidence-only repo diagnostics protocol) | `library/docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md` |

## The simplest correct mental model

Prompts are treated as source code. This repo is the compiler, linker, and indexer for that source code.

Inputs are canonical Markdown prompt files under `library/prompts/` plus a curated artifact registry inside the book builder. The build transforms that source into navigation outputs (book, TOC, catalog) and machine-readable exports (ontology JSON, JSON-LD, YAML) under `library/book/ontology/`.

Nothing runs automatically. You invoke a command, the pipeline reads inputs, generates artifacts, and exits. The “runtime” here is the build, not model inference.

## Repository structure (what exists and why)

The library is intentionally split into canonical sources, compiled outputs, and tooling. The split prevents “shadow sources of truth” and makes it obvious which files are meant to be edited by humans and which files are meant to be emitted by the build.

| Location | Purpose | How to treat it |
|---|---|---|
| `library/prompts/` | Canonical prompt source of truth, organized by domain | Hand-edit these as the primary assets |
| `library/book/` | Compiled navigation view (TOC, catalog, book) and human-readable ontology summary | Treat as build artifacts, regenerate as needed |
| `library/book/ontology/` | Machine-readable exports (JSON, JSON-LD, YAML) | Treat as build artifacts, consume downstream |
| `library/tools/` | Build and maintenance tools, including improvement generators and format normalizers | Run these from CLI, keep deterministic |
| `library/docs/` | Human docs about the system itself, including mental models and agent specs | Hand-edit, keep consistent with behavior |
| `library/research/` | Context engineering notes and patterns to guide prompt design | Hand-edit, treat as reference corpus |
| `library/paths/` | Runnable prompt flows (runbooks) that route decisions into concrete step plans | Hand-edit, treat as operational playbooks |

## What you get after a build (outputs that matter)

The build emits a navigable representation of the library. The point is not aesthetic documentation, it is controlled discoverability and governance: a predictable place to look up “the prompt we consider canonical for this objective”, plus structured exports that allow programmatic routing.

| Output | Where it lives | What it is for |
|---|---|---|
| Book index | `library/book/BOOK.md` | Human navigation, organized into parts with chapter links |
| Table of contents | `library/book/TOC.md` | Fast scan and jumping-off point |
| Catalog | `library/book/CATALOG.md` | One-table index of everything included in the compiled book |
| Ontology (human) | `library/book/ONTOLOGY.md` | The vocabulary: artifacts, tags, relationships, composition semantics |
| Ontology exports | `library/book/ontology/prompt_ecosystem.json` and siblings | Machine consumption, indexing, routing, metadata tooling |
| Improvement artifacts (optional) | `library/improvements/` | Analyses and improved variants generated from canonical prompts |

## The execution model (what actually happens when you run it)

The build is CLI-driven and deterministic by intent. The conceptual flow is shown here as a simple graph.

```text
Operator or agent
  |
  v
library/library.py (CLI entrypoint)
  |
  +--> build-book
  |      |
  |      v
  |  library/book/_build_book.py
  |      |
  |      v
  |  reads canonical prompt sources
  |      |
  |      v
  |  writes book artifacts and ontology exports
  |
  +--> improve
         |
         v
     library/tools/context_engineering/generate_prompt_improvements.py
         |
         v
     writes analyses and improved variants under library/improvements/
```

This repo intentionally stops here. Prompt execution against a model is a downstream responsibility. The contract this repo offers is structured prompt infrastructure, not inference.

## What makes this “serious-mode” prompting infrastructure

The library is built around a small set of operational commitments. These are not slogans; they are behavioral constraints that make chained prompting usable in real engineering workflows.

Deterministic constraints are preferred over “be helpful” vibes. Prompts are written to force explicit inputs, explicit outputs, explicit stop conditions, and explicit acceptance criteria. When chaining prompts, the system pushes you toward stable state objects and stable artifact naming so that intermediate work is inspectable and the chain can recover from failure without hallucinating missing context.

Artifacts are preferred over conversational fog. Prompts in this library generally aim to produce files, runbooks, schemas, command sequences, decision records, and verification steps that can be diffed, reviewed, and audited. When a prompt is forced to choose between being inspirational and being inspectable, it should be inspectable.

Governance is preferred over accidental composition. Multi-prompt chains can fail silently by drifting scope, re-interpreting objectives, or inventing constraints. The orchestration prompts exist to pin down state, approvals, and invariants so the chain remains controlled.

## Canonical prompt domains (how prompts are organized)

The directory structure under `library/prompts/` is a practical taxonomy. It is not meant to be academically perfect. It is meant to answer the question “which prompt do I use next” in a way that produces correct execution under pressure.

| Domain | When to use it | Typical deliverables |
|---|---|---|
| `discovery/` | When the codebase or domain is unknown | Repo maps, entrypoints, hypotheses and validation plans, smallest-diff change plans |
| `implementation/` | When you need to ship changes with discipline | Work plans, diffs, test plans, safe refactors, tool design (including MCP) |
| `execution/` | When you must route objectives and govern chains | Routers, runbooks, chain state schemas, stop conditions, handoff packets |
| `security/` | When correctness includes adversaries and failure | Threat models, mitigations, verification plans, secrets hygiene guidance |
| `migration/` | When changes must be staged safely | Compatibility strategy, rollout, canary, rollback, validation checklists |
| `incident_response/` | When production is on fire | Triage, stabilization, root cause, postmortem, prevention backlog |
| `misc/` | When you need cross-cutting house style and doctrine | Language house styles, notebook discipline, anti-bloat rules |

## Fast operational entrypoints (which prompt to run first)

If the objective is “understand an unknown repo, form a plan, and make the smallest correct change”, start with `library/prompts/discovery/repo_discovery_massive_prompt.md`. If the objective is “route a big task into a disciplined multi-prompt chain”, start with `library/prompts/execution/chain_router_and_runbook.md` and then enforce chain invariants with `library/prompts/execution/chain_execution_protocol.md`. If the objective is “evaluate and control security risk while building”, start with `library/prompts/security/security_threat_model.md` early rather than late.

For a concrete example of decision-gated flows, the image restoration pipeline router and builders show how the library expresses branching logic and stop conditions in a way that remains auditable.

| Objective | Router or runbook | Builder prompt(s) |
|---|---|---|
| Image restoration pipeline with decision gates | `library/prompts/execution/image_restoration_pipeline_router.md` | `library/prompts/implementation/image_restoration_pipeline_builder_python.md` and `library/prompts/implementation/image_restoration_pipeline_builder_rust.md` |

## How to use this repository in practice (a workflow that stays deterministic)

Treat a canonical prompt as a top-of-chat “instruction header” for a working session. The early questions in most prompts are there to establish invariants: objective, constraints, acceptance criteria, environment, and stop conditions. If those invariants are not provided, later phases become underdetermined and the chain becomes vulnerable to scope leakage.

When you need multiple prompts, use routing and governance prompts rather than ad-hoc “now do the next thing” handoffs. The governance layer exists to ensure that each phase produces explicit artifacts and that approvals are requested before destructive operations.

When you modify this library, prefer changing canonical prompts and then regenerating the book. Treat the book and ontology outputs as compiled views of canonical source, not as independent canonical content.

## Commands (the only way anything “runs”)

All primary operations are CLI-invoked. The following table is the minimal operational surface you need to remember.

| Task | Command |
|---|---|
| Rebuild book, TOC, catalog, ontology exports | `python library/book/_build_book.py` |
| Same rebuild via the library CLI entrypoint | `python library/library.py build-book` |
| Generate improvement artifacts (dry-run suggested first) | `python library/library.py improve -- --dry-run` |

## Determinism and reproducibility (what “deterministic” means here)

The repo aims to produce stable outputs given stable inputs. That includes stable ordering, stable artifact identifiers, stable source links, and stable export structures. Where nondeterminism can sneak in, it is treated as a bug rather than as a “nice-to-have improvement”. Examples of nondeterminism that this system is designed to avoid include filesystem traversal order differences across platforms, timestamp injection into artifacts without clear contracts, and output generation that depends on locale-specific encoding behavior.

In practice, determinism is enforced through explicit artifact ordering in the book builder and through predictable source paths. When you add a new canonical prompt that must be visible in the compiled book, you do not rely on directory listing order; you add the artifact intentionally and verify the resulting catalog and ontology exports.

## Governance and safety boundaries (what this repo will and will not do)

This repository prepares prompts for use elsewhere. It does not make provider calls. It does not embed API keys into outputs. It should never commit secrets. Files like `.env` must remain untracked and must be treated as local-only configuration. If secrets are ever found in version history, treat that as an incident requiring revocation and rotation rather than as “cleanup work”.

This governance stance extends to prompt design. Prompts that are intended to change code or infrastructure should include explicit mutation boundaries, explicit “stop and ask for approval” gates, and explicit verification steps so that a chain cannot accidentally drift into destructive behavior.

## Contribution model (how to evolve the library without breaking it)

The library is meant to be extended continuously. The healthy pattern is to add or revise canonical prompts under `library/prompts/`, add or revise relevant docs under `library/docs/` when behavior changes, then rebuild the compiled book outputs. When adding new prompts, prefer explicit frontmatter metadata and stable naming. When adding new flows under `library/paths/`, prefer decision points with explicit criteria and explicit output artifacts so that downstream use remains inspectable.

If you want a structured protocol for diagnosing and industrializing an unfamiliar repository, use the forensic audit agent spec as a top-of-chat instruction and require evidence-backed claims. That spec exists to prevent “architecture vibes” and replace them with a concrete execution model and a concrete risk register tied to observed code paths.

## If you are trying to production-harden this repo (what to improve next)

The current design already has the core shape of a production-grade prompt infrastructure layer: canonical sources, compiled navigation outputs, and machine-readable exports. The next steps, if you want to raise maturity, are the same steps you would take for any build system: add CI checks that enforce determinism and forbid secrets, add smoke tests that verify build outputs exist and are stable, add explicit versioning for ontology schemas, and document the artifact contract so downstream consumers can rely on it safely.
