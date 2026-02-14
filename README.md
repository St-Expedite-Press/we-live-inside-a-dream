# prompt-ecosystem-library

This is a PROMPT ECOSYSTEM LIBRARY: not a prompt dump. Its an opinionated, production-minded system for turning vague objectives into controlled execution, with routing, chaining, governance, and artifact-first outputs.

Start here:

- Book (navigation + ontology): `library/book/BOOK.md`
- Canonical prompts (source of truth): `library/prompts/`

## What you actually get

- Canonical prompts organized by domain (`library/prompts/`)
- A Book view (TOC + catalog + ontology exports) (`library/book/`)
- Orchestration prompts for chaining + handoffs + approvals (so output stays constrained)
- Tooling to rebuild indexes and generate improvement artifacts

This library is built for serious-mode prompting:

- stable schemas instead of vibes
- stop conditions instead of scope creep
- artifacts instead of chat fog
- explicit governance when chaining prompts

## Repository map

- `library/prompts/`
  - `discovery/`: learn an unknown repo, build a map, find leverage points
  - `implementation/`: smallest-correct-diff execution, MCP tooling, platformization
  - `execution/`: routers, runbooks, chain protocols, eval gauntlets
  - `security/`, `migration/`, `incident_response/`, `misc/`: specialized operators
- `library/book/`: index/navigation layer + ontology exports (JSON/JSON-LD/YAML)
- `library/tools/`: maintenance tools (build + analysis helpers)
- `library/docs/`: human docs + indexes
- `library/research/`: context-engineering patterns and reference notes

## Fast paths (use these first)

- Repo -> plan -> smallest correct diff: `library/prompts/discovery/repo_discovery_massive_prompt.md`
- Route a big objective into a safe chain: `library/prompts/execution/chain_router_and_runbook.md`
- Govern a multi-prompt chain (state, artifacts, approvals): `library/prompts/execution/chain_execution_protocol.md`
- Threat model a system with mitigations + verification: `library/prompts/security/security_threat_model.md`

## How to use this library

1. Pick the canonical prompt from `library/prompts/` (or from the book).
2. Run it as your top-of-chat instruction.
3. Answer its Phase 1 questions.
4. If you are chaining prompts, use the router + protocol prompts to keep the chain disciplined.

## Commands

- Rebuild the book + ontology exports:
  - `python library/book/_build_book.py`
  - or `python library/library.py build-book`
- Generate improvement artifacts for canonical prompts (writes to `library/improvements/`):
  - `python library/library.py improve -- --dry-run`
