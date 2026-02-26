# Evaluation Methods for Prompt Ecosystems

## 1) Rubric-based review

Score each prompt (0–10) on:
clarity. determinism. ambiguity (lower is better). robustness (conflict handling, injection resistance). (Order preserved.)
Add a short justification and top failure risks.

## 2) Golden test cases (regression)

Maintain a small set of representative inputs:
“happy path”. missing info (should ask questions). adversarial injection attempt. conflicting requirements. long context / noisy context. (Order preserved.)
Expected outputs should be schema-valid and constraint-compliant.

## 3) Format conformance checks

If outputs are structured (JSON/Markdown sections), validate automatically:
JSON schema validation. required headings present. forbidden sections absent. (Order preserved.)
## 4) Comparative evaluation

Compare original vs improved variants:
success rate on golden cases. formatting adherence. time-to-completion (if relevant). (Order preserved.)
## 5) Change control

When updating improved variants:
bump version file names (no overwrites by default). record rationale in `context_engineering_notes.md`. update metadata deltas. (Order preserved.)
