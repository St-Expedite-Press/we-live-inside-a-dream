#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[2] / 'graph'
name_re = re.compile(r'^[a-z0-9_]+\.md$')
bad = []
for p in sorted(root.rglob('*.md')):
    if p.name == 'README.md':
        continue
    if not name_re.match(p.name):
        bad.append(str(p))
if bad:
    print('\n'.join(bad))
    sys.exit(1)
print('name lint: ok')
