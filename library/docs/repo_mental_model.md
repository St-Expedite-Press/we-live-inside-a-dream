# Repository mental model: deterministic prompt compilation and governance

This repository is a deterministic prompt compilation and governance system. It turns a collection of canonical prompt files into structured, indexed, and analyzable artifacts, including a compiled “book”, ontology exports, and improvement analyses.

The simplest correct mental model is that it is a build system for prompts. It is not a runtime service, not a chatbot, not an app, and not a model-inference wrapper. It prepares and governs prompt infrastructure for use elsewhere.

## Primary function (what it actually does)

The canonical prompt source of truth lives here:

```text
library/prompts/
```

The compiler pipeline emits structured artifacts here:

```text
library/book/           (compiled prompt book: TOC, catalog, linked chapters)
library/book/ontology/  (ontology exports: JSON, JSON-LD, YAML)
library/improvements/   (analysis and improved prompt variants; typically git-ignored)
```

Nothing runs automatically. The system only produces outputs when invoked via its CLI entrypoints.

## Primary execution flow (runtime model of the build)

The control surface is the CLI, most commonly via `library/library.py`. The conceptual flow is:

```text
User or agent
  |
  v
library/library.py (CLI)
  |
  +--> build-book
  |      |
  |      v
  |  library/book/_build_book.py
  |      |
  |      v
  |  reads canonical prompt files + metadata
  |      |
  |      v
  |  writes book artifacts + ontology exports
  |
  +--> improve
         |
         v
     library/tools/context_engineering/generate_prompt_improvements.py
         |
         v
     analyzes canonical prompts and emits improvement artifacts
```

This is intentionally compiler-like: the “runtime” here is the build, not prompt execution against a model.

## Classification (what it fundamentally is)

The repo fits multiple architecture labels at once. The following table is the intended, explicit classification vocabulary for this codebase.

| Classification | Meaning in this repo |
|---|---|
| Static prompt artifact compiler | Canonical Markdown prompts are compiled into book-like artifacts and exports. |
| Deterministic build pipeline | Outputs are designed to be reproducible given the same inputs and tooling. |
| Filesystem-based knowledge pipeline | Inputs and outputs are directories on disk with stable contracts. |
| Prompt governance and catalog system | Prompts are organized, indexed, and constrained so they do not drift into “prompt chaos”. |
| Prompt ontology generator | Prompts are exported as structured entities with IDs, tags, and relationships. |

## The problem it solves (why it exists)

Prompt libraries tend to degrade without governance. Prompts drift, duplicate, contradict, lose structure, and become hard to discover. This repo imposes discipline by treating prompts as versioned assets that must be indexable, analyzable, and safe to compose into execution chains.

## The outputs (what you get after running the build)

The “book” output under `library/book/` exists to make the library navigable, reviewable, and machine-readable. It is a view layer over canonical prompts rather than a second source of truth. The ontology exports under `library/book/ontology/` encode prompts as structured entities, which enables programmatic routing and tooling integration outside this repo.

The improvement artifacts under `library/improvements/` exist to support systematic prompt refinement without contaminating the canonical prompt sources. In typical usage they remain separate, and are treated as build products rather than hand-edited source files.

## What it is not (boundary definition)

This repository does not run prompts against any model provider. It does not host an API. It does not provide a deployed agent runtime. Those are downstream concerns. This repo is upstream, and its product is prompt infrastructure.

## Where it fits in a broader stack

This repository is designed to sit upstream of runtime agents and services. A typical operational chain is:

```text
prompt authoring
  ->
prompt governance
  ->
prompt compilation
  ->
prompt analysis and improvement
  ->
prompt export
  ->
deployment into runtime agents and services (outside this repo)
```

The guiding principle is to keep canonical prompts stable and auditable, and to treat composition, routing, and governance as first-class build artifacts.

