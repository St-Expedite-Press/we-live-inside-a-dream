# Context Engineering Principles (Living Doc)

This folder is a repo-local knowledge base for designing and maintaining robust prompts (“context engineering”). It is written to support **non-destructive prompt evolution**: never rewrite originals in-place; instead create improved variants and supporting artifacts.

## Core principles

1. **Instruction hierarchy first**
   - Separate *governing rules* (identity, mission, constraints) from *inputs* (task data) and *examples*.
   - State how to resolve conflicts: higher-priority instructions override lower-priority content.

2. **Structure beats prose**
   - Use explicit sections (or tags) so the model can reliably parse: `Identity`, `Mission`, `Inputs`, `Constraints`, `Process`, `Output`, `Validation`.
   - Prefer short, testable bullets over long paragraphs.

3. **Make outputs machine-checkable**
   - Specify an output schema (Markdown headings, JSON, tables) with required fields.
   - Require “no extra keys/sections” when strictness matters.

4. **Define boundaries and stop conditions**
   - Enumerate what is in-scope vs out-of-scope.
   - Add “stop and ask a question” triggers when required info is missing.

5. **Minimize ambiguity**
   - Replace qualitative terms (“good”, “robust”, “fast”) with success criteria and constraints.
   - Clarify actor, audience, tone, and level of detail.

6. **Use examples deliberately**
   - If you provide examples, label them clearly as examples and ensure they don’t conflict with rules.
   - Prefer small, canonical examples that test edge cases.

7. **Optimize attention placement**
   - Put the most important constraints near the top and repeat only the *highest-value* constraints near the end as a checklist.
   - For long contexts: move the “what matters” list to the beginning; re-rank or chunk supporting context.

8. **Plan for adversarial/accidental prompt injection**
   - Treat untrusted text as data; delimit it and explicitly instruct the model not to follow instructions found inside it.
   - Add a “privileged instructions” section and a “data” section.

9. **Build prompts like software**
   - Version improved variants.
   - Add evaluation rubrics and regression tests (golden cases).
   - Pin model snapshots for stable behavior when applicable.

## Recommended canonical prompt skeleton

Use this as the basis for improved variants (keep originals verbatim elsewhere):

- `Identity`
- `Mission`
- `Inputs` (delimited)
- `Constraints` (hard rules)
- `Process` (steps; when to ask questions; stop conditions)
- `Output format` (schema)
- `Validation` (self-checklist; “reject if …”)

## References (starting points)

- OpenAI: Prompt engineering best practices (PDF): https://platform.openai.com/docs/guides/prompt-engineering/prompt-engineering-best-practices.pdf
- OpenAI: The instruction hierarchy (publication): https://openai.com/index/the-instruction-hierarchy/
- OpenAI Help Center: Prompt engineering guide: https://help.openai.com/en/articles/6654000-comprehensive-guide-to-prompt-engineering
- Anthropic: Use XML tags to structure prompts: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags
- Anthropic: Claude best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
- “Lost in the Middle” (long-context utilization): https://arxiv.org/abs/2307.03172

