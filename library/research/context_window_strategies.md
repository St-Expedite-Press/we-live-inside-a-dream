# Context Window Strategies (Long Prompts / Long Inputs)

## Key idea: placement matters

Models can show “primacy/recency” bias: information at the beginning or end of a long context can be used more reliably than information buried in the middle.

## Practical strategies

1. **Front-load what matters**
Put objectives, constraints, and output schema early.
2. **Tail-load the checklist**
End the prompt with a short validation checklist and stop conditions.
3. **Chunk and label**
Use clear section headers or tags for each chunk. Provide a “map” (table of contents or bullet index) for long inputs.
4. **Summarize inputs before acting**
Require a brief “salient facts” extraction step, then operate on that summary.
5. **Re-rank context**
If you control retrieval: put most relevant chunks first (or last), not in the middle.
6. **Avoid redundant verbosity**
Prefer one authoritative constraint list plus a small end-of-prompt checklist.
## References

Lost in the Middle (2023): https://arxiv.org/abs/2307.03172. Found in the Middle (2024): https://arxiv.org/abs/2406.16008.
