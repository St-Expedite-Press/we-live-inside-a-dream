#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
TARGETS = [ROOT / 'graph' / 'nodes']
REQUIRED = {'title', 'type', 'tags', 'created'}
ALLOWED_TAG = re.compile(r'^[a-z0-9][a-z0-9_-]*$')
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)

errors = []
for t in TARGETS:
    for p in sorted(t.rglob('*.md')):
        txt = p.read_text(encoding='utf-8')
        m = FM_RE.match(txt)
        if not m:
            errors.append(f'{p}: missing frontmatter')
            continue
        fm = m.group(1)
        keys = {line.split(':',1)[0].strip() for line in fm.splitlines() if ':' in line}
        missing = REQUIRED - keys
        if missing:
            errors.append(f"{p}: missing keys {sorted(missing)}")
        for line in fm.splitlines():
            if line.strip().startswith('tags:'):
                continue
            s = line.strip().lstrip('-').strip().strip('"').strip("'")
            if s and 'tags' in line and not ALLOWED_TAG.match(s):
                errors.append(f'{p}: invalid tag token {s}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('frontmatter lint: ok')
