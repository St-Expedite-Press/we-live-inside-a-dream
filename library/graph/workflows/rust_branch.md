# Rust Branch Workflow

Use this branch when the target implementation language is Rust.

## Entry criteria
- User specifies Rust, or repository evidence indicates Rust primary runtime.
- Objective requires implementation, not analysis-only.

## Node sequence
1. `library/graph/nodes/misc/rust_house_style.md`
2. `library/graph/nodes/misc/rust_antibloat.md`
3. `library/graph/nodes/discovery/rust_repo_discovery_engineer.md`
4. `library/graph/nodes/planning/product_plan_compiler.md`
5. `library/graph/nodes/implementation/evidence_driven_implementation.md`
6. `library/graph/nodes/implementation/product_build_executor.md`

## Optional side branches
- Security: `library/graph/nodes/security/security_threat_model.md`
- Rollout: `library/graph/nodes/migration/migration_and_rollout.md`
- Eval hardening: `library/graph/nodes/execution/agent_testing_eval_gauntlet.md`

## Exit criteria
- Acceptance criteria met and verified.
- Required tests and validations executed.
- Delivery packet produced.

## Output Schema

Follow `library/graph/protocols/output_schema.md` for final response structure.
