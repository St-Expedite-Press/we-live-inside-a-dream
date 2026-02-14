# prompt-ecosystem-library

This is a PROMPT ECOSYSTEM LIBRARY: not a prompt dump. Its an opinionated, production-minded system for turning vague objectives into controlled execution, with routing, chaining, governance, and artifact-first outputs.

Start here:

Book (navigation + ontology): `library/book/BOOK.md`. Canonical prompts (source of truth): `library/prompts/`.
Mental model (what this repo is and is not): `library/docs/repo_mental_model.md`. Forensic audit agent spec (top-of-chat protocol for repo diagnostics): `library/docs/agent_specs/repo_forensic_arch_diagnostic_agent_spec.md`.
## What you actually get

Canonical prompts organized by domain (`library/prompts/`). A Book view (TOC + catalog + ontology exports) (`library/book/`). Orchestration prompts for chaining + handoffs + approvals (so output stays constrained). Tooling to rebuild indexes and generate improvement artifacts. (Order preserved.)
This library is built for serious-mode prompting:

stable schemas instead of vibes. stop conditions instead of scope creep. artifacts instead of chat fog. explicit governance when chaining prompts. (Order preserved.)
## Repository map

| Item | Explanation |
|---|---|
| `library/prompts/` | `discovery/`: learn an unknown repo, build a map, find leverage points; `implementation/`: smallest-correct-diff execution, MCP tooling, platformization; `execution/`: routers, runbooks, chain protocols, eval gauntlets; `security/`, `migration/`, `incident_response/`, `misc/`: specialized operators |
| `library/book/`: index/navigation layer + ontology exports (JSON/JSON-LD/YAML) |  |
| `library/tools/`: maintenance tools (build + analysis helpers) |  |
| `library/docs/`: human docs + indexes |  |
| `library/research/`: context-engineering patterns and reference notes |  |
## Fast paths (use these first)

Repo -> plan -> smallest correct diff: `library/prompts/discovery/repo_discovery_massive_prompt.md`. Route a big objective into a safe chain: `library/prompts/execution/chain_router_and_runbook.md`. Govern a multi-prompt chain (state, artifacts, approvals): `library/prompts/execution/chain_execution_protocol.md`. Threat model a system with mitigations + verification: `library/prompts/security/security_threat_model.md`. (Order preserved.)
## How to use this library

Pick the canonical prompt from `library/prompts/` (or from the book) and run it as your top-of-chat instruction. Answer its early questions first, because those phases define the invariant constraints that keep later work deterministic. If you are chaining prompts, route the objective with the router prompt and enforce the chain state and artifact contracts with the protocol prompt so the chain stays disciplined.

## Commands

| Item | Explanation |
|---|---|
| Rebuild the book + ontology exports: | `python library/book/_build_book.py`; or `python library/library.py build-book` |
| Generate improvement artifacts for canonical prompts (writes to `library/improvements/`): | `python library/library.py improve -- --dry-run` |
