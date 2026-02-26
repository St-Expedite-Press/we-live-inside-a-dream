# Orchestration CLI

This module powers the `library.py orchestrate` command.

Behavior:

1. Takes a raw prompt.
2. Classifies primary path (`research`, `python`, `rust`).
3. Applies overlay gates (`incident_gate`, `security_gate`, `rollout_gate`) when triggered.
4. Runs staged enrichment through OpenAI Responses API.
5. Generates an agent package suite directory with workflow, enrichment docs, agent specs, and manifest.

Command:

```bash
python3 library/library.py orchestrate -- --prompt "<your prompt>" --out-dir outputs
```

Offline smoke mode:

```bash
python3 library/library.py orchestrate -- --prompt "<your prompt>" --offline --out-dir outputs
```
