# Prompt Frontmatter Schema

Required keys for node prompts:

- `title`: string
- `type`: string (`prompt`, `guidelines`, `index`, `other`, `book-chapter`, `toc`, `catalog`, `ontology`, `book`)
- `tags`: list of lowercase tags matching `[a-z0-9_-]+`
- `created`: date string `YYYY-MM-DD`

Optional keys:

- additional metadata fields allowed if they are scalar strings.

Validation tooling:

- `python3 library/tools/validation/lint_frontmatter.py`
