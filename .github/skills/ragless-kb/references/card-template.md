# Document card template

Write `knowledge/cards/<id>.md` using this shape. Keep it roughly 150–500 words. Cards are navigation aids, not evidence.

```markdown
---
id: <same as canonical doc>
title: <human title>
source: knowledge/docs/<id>.md
original: input/<filename>
authority: formal-primary | official-guidance | secondary | reference | unknown
status: current | superseded | draft | historical | unknown
topics: []
---

# <title>

## Purpose
What this document is and who it is for.

## Authority and recency
Formality, date, version, and whether anything newer supersedes it.

## Major topics
- …

## Key definitions, rules, or findings
- …

## Notable entities and dates
- …

## Related documents
- [Title](knowledge/docs/…) — relationship

## Conflicts or caveats
Extraction warnings, disagreements, or missing evidence.

## Canonical source
[knowledge/docs/<id>.md](knowledge/docs/<id>.md) · original [input/<file>](input/<file>)
```
