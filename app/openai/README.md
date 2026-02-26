# OpenAI Module

Centralized in-repo OpenAI integration.

Current client:

- `responses_client.py`: wrapper for OpenAI Responses API text and JSON-mode generations.

Usage:

```python
from app.openai.responses_client import OpenAIResponsesClient
```

This module exists to keep LLM transport/auth/request handling out of orchestration/business logic.
