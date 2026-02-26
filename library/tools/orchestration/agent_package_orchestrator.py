from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

LIBRARY_ROOT = Path(__file__).resolve().parents[2]
GRAPH_ROOT = LIBRARY_ROOT / "graph"


@dataclass
class RouteDecision:
    primary_path: str
    overlay_gates: list[str]
    rationale: str


class OpenAIResponsesClient:
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


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        raise ValueError("No JSON object found in model output")
    return json.loads(m.group(0))


def _classify_route(client: OpenAIResponsesClient | None, prompt: str, offline: bool) -> RouteDecision:
    if offline:
        p = prompt.lower()
        if any(k in p for k in ("research", "analyze", "analysis", "survey", "literature")):
            return RouteDecision("research", [], "Offline keyword classification: research intent detected.")
        if "rust" in p:
            return RouteDecision("rust", [], "Offline keyword classification: rust intent detected.")
        return RouteDecision("python", [], "Offline default classification: python path.")

    assert client is not None
    rules = _load_text(GRAPH_ROOT / "rules" / "routing_ruleset.md")
    instructions = (
        "You are a deterministic route classifier for a prompt-chain app. "
        "Choose exactly one primary_path in ['research','python','rust'] and optional overlay_gates in "
        "['incident_gate','security_gate','rollout_gate']. Return strict JSON with keys "
        "primary_path, overlay_gates, rationale."
    )
    user_input = f"Routing rules:\n{rules}\n\nUser prompt:\n{prompt}"
    raw = client.generate(instructions, user_input, json_mode=True)
    obj = _extract_json_object(raw)
    primary = str(obj.get("primary_path", "")).strip().lower()
    if primary not in {"research", "python", "rust"}:
        raise RuntimeError(f"Invalid primary_path from model: {primary}")
    gates = [g for g in obj.get("overlay_gates", []) if g in {"incident_gate", "security_gate", "rollout_gate"}]
    rationale = str(obj.get("rationale", "")).strip() or "No rationale provided"
    return RouteDecision(primary, gates, rationale)


def _workflow_for_route(route: str) -> Path:
    m = {
        "research": GRAPH_ROOT / "workflows" / "research_path.md",
        "python": GRAPH_ROOT / "workflows" / "python_branch.md",
        "rust": GRAPH_ROOT / "workflows" / "rust_branch.md",
    }
    return m[route]


def _gate_docs(gates: list[str]) -> list[Path]:
    mapping = {
        "incident_gate": GRAPH_ROOT / "nodes" / "incident_response" / "incident_response_and_postmortem.md",
        "security_gate": GRAPH_ROOT / "nodes" / "security" / "security_threat_model.md",
        "rollout_gate": GRAPH_ROOT / "nodes" / "migration" / "migration_and_rollout.md",
    }
    return [mapping[g] for g in gates]


def _stage_enrich(
    client: OpenAIResponsesClient | None,
    offline: bool,
    stage: str,
    prompt: str,
    aggregate: str,
    graph_context: str,
) -> str:
    if offline:
        return (
            f"# {stage}\n\n"
            f"This is an offline enrichment artifact.\n\n"
            f"Prompt focus: {prompt[:240]}\n\n"
            f"Aggregate context length: {len(aggregate)} characters.\n"
        )

    assert client is not None
    instructions = (
        "You are a prompt enrichment engine for an orchestration pipeline. "
        "Produce concrete Markdown with explicit sections, decisions, and artifacts. "
        "Do not output placeholders."
    )
    user_input = (
        f"Stage: {stage}\n\n"
        f"Original prompt:\n{prompt}\n\n"
        f"Current aggregate docs:\n{aggregate}\n\n"
        f"Graph context:\n{graph_context[:12000]}\n"
    )
    return client.generate(instructions, user_input, json_mode=False)


def _make_agent_specs(route: str, gates: list[str], aggregate: str) -> list[dict[str, Any]]:
    agents: list[dict[str, Any]] = [
        {
            "id": "orchestrator_agent",
            "role": "Route coordination, packetization, and chain control.",
            "inputs": ["user_prompt", "route_decision", "enrichment_docs"],
            "outputs": ["runbook", "handoff_packets", "execution_plan"],
        },
        {
            "id": "evidence_agent",
            "role": "Collects and verifies evidence used by downstream agents.",
            "inputs": ["source_docs", "project_context"],
            "outputs": ["evidence_ledger", "validation_notes"],
        },
    ]

    if route == "research":
        agents.append(
            {
                "id": "research_agent",
                "role": "Produces structured synthesis and uncertainty-aware findings.",
                "inputs": ["research_questions", "evidence_ledger"],
                "outputs": ["synthesis_report", "open_questions", "next_actions"],
            }
        )
    else:
        agents.append(
            {
                "id": "builder_agent",
                "role": f"Implements task on {route} path with smallest-correct-diff discipline.",
                "inputs": ["plan_packet", "constraints", "acceptance_criteria"],
                "outputs": ["delivery_packet", "change_log", "verification_results"],
            }
        )

    if "security_gate" in gates:
        agents.append(
            {
                "id": "security_gatekeeper_agent",
                "role": "Blocks unsafe actions and enforces threat-model mitigations.",
                "inputs": ["threat_model", "proposed_actions"],
                "outputs": ["security_decision", "required_controls"],
            }
        )

    if "rollout_gate" in gates:
        agents.append(
            {
                "id": "rollout_guardian_agent",
                "role": "Enforces compatibility, staged rollout, and rollback readiness.",
                "inputs": ["release_plan", "compatibility_contract"],
                "outputs": ["rollout_decision", "rollback_plan"],
            }
        )

    if "incident_gate" in gates:
        agents.append(
            {
                "id": "incident_response_agent",
                "role": "Executes stabilization-first incident response flow.",
                "inputs": ["incident_signals", "service_context"],
                "outputs": ["incident_timeline", "recovery_actions", "postmortem_packet"],
            }
        )

    agents.append(
        {
            "id": "qa_validation_agent",
            "role": "Verifies package completeness and readiness for framework consumption.",
            "inputs": ["agent_suite", "workflow_docs", "manifest"],
            "outputs": ["readiness_report", "blocking_gaps"],
        }
    )

    return agents


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def run_orchestration(prompt: str, out_dir: Path, model: str, offline: bool) -> Path:
    api_key = os.getenv("OPENAI_API_KEY", "")
    client: OpenAIResponsesClient | None = None
    if not offline:
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required unless --offline is used")
        client = OpenAIResponsesClient(api_key=api_key, model=model)

    decision = _classify_route(client, prompt, offline)

    top_level = _load_text(GRAPH_ROOT / "workflows" / "top_level_prompt_chain.md")
    route_doc = _load_text(_workflow_for_route(decision.primary_path))
    gate_docs = [_load_text(p) for p in _gate_docs(decision.overlay_gates)]
    graph_context = "\n\n".join([top_level, route_doc, *gate_docs])

    stages = [
        "STAGE_01_INTAKE_AND_CLASSIFICATION",
        "STAGE_02_CONTEXT_EXPANSION",
        "STAGE_03_WORKFLOW_COMPOSITION",
        "STAGE_04_AGENT_SUITE_DESIGN",
        "STAGE_05_PACKAGE_FINALIZATION",
    ]

    aggregate_parts: list[str] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    package_dir = out_dir / f"agent_package_{timestamp}_{decision.primary_path}"
    enrichment_dir = package_dir / "enrichment"
    workflow_dir = package_dir / "workflow"
    agents_dir = package_dir / "agents"

    for idx, stage in enumerate(stages, start=1):
        aggregate = "\n\n".join(aggregate_parts)
        stage_text = _stage_enrich(client, offline, stage, prompt, aggregate, graph_context)
        aggregate_parts.append(stage_text)
        p = enrichment_dir / f"{idx:02d}_{stage.lower()}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(stage_text, encoding="utf-8")

    agents = _make_agent_specs(decision.primary_path, decision.overlay_gates, "\n\n".join(aggregate_parts))
    for agent in agents:
        _write_json(agents_dir / f"{agent['id']}.json", agent)

    runbook = (
        "# Agent Package Runbook\n\n"
        f"Primary path: `{decision.primary_path}`\n\n"
        f"Overlay gates: `{', '.join(decision.overlay_gates) if decision.overlay_gates else 'none'}`\n\n"
        "## Execution sequence\n"
        "1. Read route decision\n"
        "2. Process enrichment docs in numeric order\n"
        "3. Instantiate agent specs from `agents/`\n"
        "4. Execute workflow under governance constraints\n"
        "5. Produce delivery or research packet\n"
    )
    workflow_dir.mkdir(parents=True, exist_ok=True)
    (workflow_dir / "runbook.md").write_text(runbook, encoding="utf-8")

    manifest = {
        "package_version": "1.0",
        "created_utc": timestamp,
        "primary_path": decision.primary_path,
        "overlay_gates": decision.overlay_gates,
        "route_rationale": decision.rationale,
        "model": model,
        "offline_mode": offline,
        "input_prompt": prompt,
        "artifacts": {
            "workflow": ["workflow/runbook.md", "workflow/route_decision.json"],
            "enrichment": [str(p.relative_to(package_dir)).replace("\\", "/") for p in sorted(enrichment_dir.glob("*.md"))],
            "agents": [str(p.relative_to(package_dir)).replace("\\", "/") for p in sorted(agents_dir.glob("*.json"))],
        },
    }

    _write_json(workflow_dir / "route_decision.json", {
        "primary_path": decision.primary_path,
        "overlay_gates": decision.overlay_gates,
        "rationale": decision.rationale,
    })
    _write_json(package_dir / "manifest.json", manifest)

    overview = (
        "# Agent Package Suite\n\n"
        "This directory contains a generated package suite for agentic frameworks.\n\n"
        f"Primary path: `{decision.primary_path}`\n"
        f"Overlay gates: `{', '.join(decision.overlay_gates) if decision.overlay_gates else 'none'}`\n\n"
        "## Contents\n"
        "- `manifest.json`\n"
        "- `workflow/`\n"
        "- `enrichment/`\n"
        "- `agents/`\n"
    )
    (package_dir / "README.md").write_text(overview, encoding="utf-8")

    return package_dir


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Generate an agent package suite from a prompt.")
    parser.add_argument("--prompt", help="Raw user prompt to orchestrate.")
    parser.add_argument("--prompt-file", help="Path to file containing prompt text.")
    parser.add_argument("--out-dir", default="outputs", help="Directory where package output will be written.")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"), help="OpenAI model for Responses API.")
    parser.add_argument("--offline", action="store_true", help="Run without API calls using deterministic local stubs.")
    ns = parser.parse_args(argv)

    prompt = (ns.prompt or "").strip()
    if ns.prompt_file:
        prompt = Path(ns.prompt_file).read_text(encoding="utf-8").strip()
    if not prompt:
        raise SystemExit("Provide --prompt or --prompt-file")

    out = Path(ns.out_dir)
    package = run_orchestration(prompt=prompt, out_dir=out, model=ns.model, offline=ns.offline)
    print(f"Generated package: {package}")
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
