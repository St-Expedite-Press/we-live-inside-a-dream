---
title: "RUST HOUSE STYLE"
type: "guidelines"
tags: ["rust", "code-style", "rustfmt", "clippy"]
created: "2026-02-05"
---

# RUST HOUSE STYLE

A project-agnostic house style for writing **idiomatic, reviewable Rust**.

This complements (but does not replace) “anti-bloat” or architecture rules. This document is about day-to-day code shape: naming, layout, APIs, errors, and tests.

## Table of contents

[Core doctrine](#core-doctrine). [Formatting & layout](#formatting--layout). [Modules & visibility](#modules--visibility). [Naming](#naming). [Types & APIs](#types--apis). [Ownership & borrowing](#ownership--borrowing). [Error handling](#error-handling). [Traits, generics, and macros](#traits-generics-and-macros). [Async & concurrency](#async--concurrency). [Docs & comments](#docs--comments). [Testing](#testing). [House self-audit (pre-commit)](#house-self-audit-pre-commit). (Order preserved.)
---

## Core doctrine

**R-00 — `rustfmt`/Clippy define the baseline**: argue with configuration, not with hand-styling. **R-01 — Make invalid states unrepresentable** when feasible (newtypes, enums, `NonZero*`, etc.). **R-02 — Prefer explicitness over cleverness**: future readers should not need to “decode” intent. **R-03 — Keep the happy path obvious**: structure functions so success flow reads top-to-bottom. (Order preserved.)
---

## Formatting & layout

**F-01 — Run `rustfmt`** and do not fight it. **F-02 — Keep functions small**: if a function has multiple conceptual phases, split. **F-03 — Prefer `?`** for propagation; avoid nested `match`/`if let` error pyramids. **F-04 — Pattern match for clarity**: use `match` when it improves readability and enforces exhaustiveness. (Order preserved.)
---

## Modules & visibility

**M-01 — Default to private**: `pub` is part of your API contract. **M-02 — Minimize `pub use` re-exports**: re-export only to shape a deliberate public surface. **M-03 — Keep module names semantic**: avoid `utils`/`common` unless the project explicitly defines them. **M-04 — Keep types near their usage**: locality beats speculative organization. (Order preserved.)
---

## Naming

| Item | Explanation |
|---|---|
| **N-01 — Standard Rust conventions**: | modules/crates: `snake_case`; types/traits/enums: `PascalCase`; functions/vars: `snake_case`; constants: `SCREAMING_SNAKE_CASE` |
| **N-02 — Boolean names**: prefer predicates (`is_valid`, `has_items`) over ambiguous nouns. |  |
| **N-03 — Error types**: `FooError` with variants that read like sentences. |  |
---

## Types & APIs

| Item | Explanation |
|---|---|
| **A-01 — Prefer `&str`/`String` correctly**: | accept `impl AsRef<str>` only when ergonomics matter and you’ve measured the cost in complexity; otherwise accept `&str` and allocate at boundaries |
| **A-02 — Choose return types that communicate intent**: | `Option<T>` for “missing is normal”; `Result<T, E>` for failures |
| **A-03 — Avoid overloading with flags**: use enums for mode/state. |  |
| **A-04 — Builder pattern** only when there are enough optional fields to justify it. |  |
---

## Ownership & borrowing

**O-01 — Borrow by default**: take `&T`/`&mut T` unless you truly need ownership. **O-02 — Avoid `.clone()` in core logic**: treat clones as explicit costs and justify them at boundaries. **O-03 — Prefer iterators, but keep them readable**: long iterator chains should be broken into named steps. **O-04 — Lifetimes**: avoid explicit lifetimes until needed; when needed, name them meaningfully. (Order preserved.)
---

## Error handling

**E-01 — Errors should be actionable**: include context (which id/path/operation failed). **E-02 — Don’t log and return the same error** (avoid double-reporting). Decide where logging lives: typically at the boundary. **E-03 — Use domain error enums** for libraries and core logic; use `anyhow` primarily at application boundaries. **E-04 — Avoid `unwrap`/`expect`** outside tests and truly impossible states. If used, the message must explain the invariant. (Order preserved.)
---

## Traits, generics, and macros

**G-01 — Generics are a cost**: use them when they reduce duplication without harming readability. **G-02 — Prefer concrete types in internal modules**; generic interfaces belong at boundaries. **G-03 — Macros**: avoid unless they substantially reduce boilerplate and remain transparent. **G-04 — Trait objects vs generics**: choose based on ergonomics and compile-time bloat; keep the simplest that works. (Order preserved.)
---

## Async & concurrency

**C-01 — Avoid mixing sync/async implicitly**: keep async boundaries explicit. **C-02 — Don’t block in async**: use async-aware primitives. **C-03 — Cancellation matters**: think about drop semantics and shutdown paths. **C-04 — Prefer structured concurrency patterns** over detached tasks. (Order preserved.)
---

## Docs & comments

**D-01 — Public items get rustdoc**: types/functions/traits in public API. **D-02 — Examples compile**: use rustdoc tests when examples are non-trivial. **D-03 — Comments explain why**: use comments to justify invariants, unsafe blocks, or non-obvious tradeoffs. (Order preserved.)
---

## Testing

**T-01 — Unit tests near the code**: test modules next to what they verify. **T-02 — Integration tests for API surfaces** (`tests/`), especially for error behavior. **T-03 — Prefer deterministic tests**: avoid sleeps/timeouts; use fakes. **T-04 — Property tests** when invariants are important and input space is large. (Order preserved.)
---

## House self-audit (pre-commit)

1. Would `cargo fmt` and `cargo clippy` pass without suppressions?
2. Did I introduce a `pub` item? If yes, is it intentional and documented?
3. Are errors typed and contextual (no vague strings)?
4. Did I add clones/allocations? If yes, are they justified at the boundary?
5. Are tests present for the new behavior and the failure mode?
