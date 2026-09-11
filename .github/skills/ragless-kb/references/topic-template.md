# Topic map template

Write one file per coherent topic under `knowledge/topics/<topic-slug>.md`. Prefer 5–20 maps, not dozens of keyword files.

```markdown
---
topic: <slug>
title: <human title>
aliases: []
---

# <title>

## Scope
What this topic covers and what it deliberately excludes.

## Documents
Order by likely authority and usefulness. Use markdown links.

- [Title](knowledge/docs/<id>.md) — one-line role · [original](input/<file>)

## Relationships
Dependencies, version chains, and which source to prefer.

## Disagreements and staleness
Where sources conflict or look outdated.

## Search terms
Synonyms, acronyms, and phrases to try with this skill's `scripts/kb.py search`.
```
