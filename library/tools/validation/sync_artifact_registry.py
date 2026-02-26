#!/usr/bin/env python3
from pathlib import Path
import json

repo = Path(__file__).resolve().parents[3]
ontology = repo / 'library' / 'book' / 'ontology' / 'prompt_ecosystem.json'
registry = repo / 'library' / 'graph' / 'registry' / 'artifacts_registry.json'

data = json.loads(ontology.read_text(encoding='utf-8'))
out = {'version': '1.0', 'artifacts': data.get('artifacts', [])}
registry.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(f'wrote {registry}')
