---
title: "PYTHON HOUSE STYLE"
type: "guidelines"
tags: ["python", "code-style", "linting", "typing"]
created: "2026-02-05"
---

# PYTHON HOUSE STYLE

A project-agnostic house style for writing **readable, maintainable Python**.

This is optimized for:

Correctness and clarity over cleverness. Tool-friendly code (formatters/linters/type-checkers). Changes that are easy to review. (Order preserved.)
## Table of contents

[Core doctrine](#core-doctrine). [Formatting & layout](#formatting--layout). [Imports](#imports). [Naming](#naming). [Types & interfaces](#types--interfaces). [Error handling](#error-handling). [Data modeling](#data-modeling). [Functions & control flow](#functions--control-flow). [Comments & docstrings](#comments--docstrings). [Testing](#testing). [Dependency & environment discipline](#dependency--environment-discipline). [House self-audit (pre-commit)](#house-self-audit-pre-commit). (Order preserved.)
---

## Core doctrine

**P-00 — One obvious way**: prefer straightforward, idiomatic Python over micro-optimizations. **P-01 — Make invariants explicit**: validate at boundaries; encode in types/dataclasses when possible. **P-02 — Prefer pure functions**: keep side effects at the edges (I/O, DB, network). **P-03 — Readability is a feature**: code is written for the next reader, not the compiler. (Order preserved.)
Recommended tool baseline (not mandatory, but assumed by this style):

Formatter: **Black**. Linter: **Ruff** (including import sorting). Type checker: **Pyright** or **mypy**. (Order preserved.)
---

## Formatting & layout

**F-01 — Formatter is law**: do not hand-format around a formatter. If you need a different look, change configuration, not code style ad hoc. **F-02 — Line length**: pick one and stick to it (Black default 88 is fine). Wrap long expressions rather than using backslashes. **F-03 — Early returns**: reduce indentation; avoid deep nesting. **F-04 — Small units**: functions should usually fit on one screen. (Order preserved.)
---

## Imports

**I-01 — Absolute imports preferred** (unless a package intentionally uses relative imports for internal cohesion). **I-02 — No star imports** (`from x import *`) except in explicit re-export modules with justification. **I-03 — Import order**: stdlib → third-party → local; one import per line when it improves diffs. **I-04 — Optional dependencies**: isolate behind boundary modules; fail with actionable messages. (Order preserved.)
---

## Naming

| Item | Explanation |
|---|---|
| **N-01 — Be boring**: | modules: `snake_case`; functions/variables: `snake_case`; classes/exceptions: `PascalCase`; constants: `SCREAMING_SNAKE_CASE` |
| **N-02 — Domain words first**: name things after the domain, not their implementation (`invoice_total`, not `sum_2`). |  |
| **N-03 — Avoid abbreviations** unless universally obvious (`id`, `url`, `db`). |  |
---

## Types & interfaces

**T-01 — Type at boundaries**: type public functions/methods and module boundaries first. **T-02 — Prefer concrete types** over `Any`. If `Any` is necessary, isolate it and document why. **T-03 — Use `Protocol` for structural interfaces** when you need “duck typing” with type safety. **T-04 — Avoid overly clever generics**: keep type parameters minimal. **T-05 — Return types**: always specify for public APIs; avoid returning “sometimes” `None` unless modeled as `T | None`. (Order preserved.)
---

## Error handling

**E-01 — Exceptions for exceptional situations**: don’t use exceptions for normal control flow. **E-02 — Raise specific exceptions**: prefer custom exceptions for domain failures. **E-03 — Add context, don’t destroy it**: use `raise ... from e` when wrapping. **E-04 — Boundary translation**: translate low-level exceptions into domain errors at module/service boundaries. (Order preserved.)
---

## Data modeling

**D-01 — Prefer `dataclasses` / `attrs` / Pydantic** for structured data instead of “dicts everywhere”. **D-02 — Make invalid states unrepresentable** where practical (enums, constrained types). **D-03 — Avoid “stringly typed” APIs**: use enums / constants, not magic strings. **D-04 — `datetime` discipline**: timezone-aware at the boundaries; document timezone assumptions. (Order preserved.)
---

## Functions & control flow

**C-01 — Prefer guard clauses** over nested `if` pyramids. **C-02 — Comprehensions**: fine for simple transforms; switch to loops when logic becomes non-trivial. **C-03 — Avoid side effects in comprehensions**. **C-04 — Prefer `pathlib.Path`** for filesystem paths. **C-05 — Avoid mutating arguments** unless explicitly documented. (Order preserved.)
---

## Comments & docstrings

| Item | Explanation |
|---|---|
| **S-01 — Code explains what; comments explain why**. |  |
| **S-02 — Docstrings for public surfaces**: | modules with non-trivial behavior; public classes and their invariants; public functions with tricky inputs/outputs |
| **S-03 — Examples beat prose**: include small usage examples for complex APIs. |  |
Docstring style:

Use a consistent style (Google or NumPy style) within a codebase. Keep docstrings short and factual; avoid re-stating obvious parameter names.
---

## Testing

**Q-01 — Test behavior, not implementation**. **Q-02 — Arrange/Act/Assert** structure; keep tests readable. **Q-03 — Determinism**: avoid time/network; use fakes or fixtures. **Q-04 — Boundary tests**: verify error translation at boundaries. (Order preserved.)
---

## Dependency & environment discipline

**G-01 — Minimum dependencies**: add a dependency only when stdlib is materially worse. **G-02 — Pin with intent**: pin versions for applications; for libraries, use compatible ranges but test broadly. **G-03 — No hidden global state**: avoid reliance on process-wide globals unless it’s a deliberate singleton. **G-04 — Secrets**: never hard-code; fetch from environment/secret manager; keep tests free of secrets. (Order preserved.)
---

## House self-audit (pre-commit)

Answer these before merging:

1. **What did I delete or simplify?**
2. **What is the smallest unit I can test here?**
3. **Are boundary types explicit (inputs/outputs/errors)?**
4. **Did I introduce `Any` / untyped dictionaries? If yes, why is it contained?**
5. **Will Black/Ruff/Pyright agree with this without per-line ignores?**
