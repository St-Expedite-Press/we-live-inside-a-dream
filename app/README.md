# App Directory

All application scripting for prompt orchestration lives under `app/`.

## Submodules

- `app/orchestration/`: CLI orchestration pipeline logic and package generation.
- `app/openai/`: OpenAI Responses API integration wrappers.

## Entry command

```bash
python3 library/library.py orchestrate -- --prompt "<your prompt>" --out-dir outputs
```
