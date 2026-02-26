# Routing Ruleset

Apply rules top-to-bottom. First terminal match wins.

## Rule 1: Research Objective
Condition: user asks for research synthesis, evidence review, literature analysis, benchmark survey, or knowledge map.
Route: `research` path.

## Rule 2: Python Build Path
Condition: objective requires implementation and target language is Python.
Route: `python` path.

## Rule 3: Rust Build Path
Condition: objective requires implementation and target language is Rust.
Route: `rust` path.

## Rule 4: Default Clarification
Condition: objective is ambiguous or missing acceptance criteria.
Route: `clarification` path.

## Overlay gates (cross-cutting, not primary paths)
- `incident_gate`: if active outage/customer incident exists, run incident response immediately before continuing.
- `security_gate`: if auth, secrets, trust boundaries, or attack surface are affected, run threat model before mutating actions.
- `rollout_gate`: if deployment or compatibility changes are included, require migration/rollout planning before release.

## Global risk gates
- Any destructive mutation requires explicit approval.
- Missing critical context routes to clarification.
- Contradictory constraints route to clarification.
