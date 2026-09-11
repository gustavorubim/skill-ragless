# Metadata schema

Recommended canonical document frontmatter:

```yaml
---
id: nist-ai-100-1
title: Artificial Intelligence Risk Management Framework (AI RMF 1.0)
source_file: input/NIST.AI.100-1.pdf
source_sha256: "..."
document_type: framework
date: 2023-01-26
version: "1.0"
authority: formal-primary
status: current
topics: [ai-risk, governance, trustworthy-ai]
entities: [NIST, AI RMF]
summary: Voluntary framework for identifying, assessing, and managing AI risks.
extraction_warnings: []
---
```

Use stable IDs. Prefer lowercase kebab-case based on title; add a short hash only to resolve collisions.

Suggested `authority` vocabulary:

- `formal-primary`
- `official-guidance`
- `secondary`
- `reference`
- `unknown`

Suggested `status` vocabulary:

- `current`
- `superseded`
- `draft`
- `historical`
- `unknown`
