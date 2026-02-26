# Routing Ruleset

Apply rules top-to-bottom. First terminal match wins.

## Rule 1: Incident Preemption
Condition: active outage, customer impact, or security incident in progress.
Route: `incident_response` path.

## Rule 2: Research Objective
Condition: user asks for research synthesis, evidence review, literature analysis, benchmark survey, or knowledge map.
Route: `research` path.

## Rule 3: Security-first
Condition: objective changes auth, secrets, permissions, trust boundaries, or public attack surface.
Route: `security_review` path, then continue to implementation path.

## Rule 4: Implementation
Condition: user asks for code changes, bug fixes, refactors, or feature delivery.
Route: `implementation` path.

## Rule 5: Language Branch Selection
Condition: implementation path selected and language can be inferred or specified.
Route: `python_branch` for Python-first work. `rust_branch` for Rust-first work. If unknown, route to clarification.

## Rule 6: Migration/Rollout
Condition: objective includes deployment, compatibility, data migration, canary, or rollback planning.
Route: `rollout` path.

## Rule 7: Default Clarification
Condition: objective is ambiguous or missing acceptance criteria.
Route: `clarification` path.

## Global Risk Gates
- Any destructive mutation requires explicit approval.
- Missing critical context routes to clarification.
- Contradictory constraints route to clarification.
