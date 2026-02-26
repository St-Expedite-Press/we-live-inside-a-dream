from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


class OpenAIResponsesClient:
    """Thin wrapper around OpenAI Responses API for in-repo orchestration calls."""

    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model

    def generate(self, instructions: str, input_text: str, json_mode: bool = False) -> str:
        payload: dict[str, Any] = {
            "model": self.model,
            "input": [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": instructions}],
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": input_text}],
                },
            ],
        }
        if json_mode:
            payload["text"] = {"format": {"type": "json_object"}}

        req = urllib.request.Request(
            "https://api.openai.com/v1/responses",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"OpenAI API error {e.code}: {detail}") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"OpenAI API connection error: {e}") from e

        data = json.loads(body)
        output = data.get("output", [])
        chunks: list[str] = []
        for item in output:
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    chunks.append(content.get("text", ""))
        text = "\n".join(chunks).strip()
        if not text and data.get("output_text"):
            text = str(data["output_text"]).strip()
        if not text:
            raise RuntimeError("OpenAI response did not contain output text")
        return text
