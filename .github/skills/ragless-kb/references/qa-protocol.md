# Q&A Protocol

## Progressive retrieval

1. If the question is broad or topic-oriented, inspect `knowledge/INDEX.md`.
2. Inspect one or more relevant topic maps.
3. Use cards to shortlist sources, not to prove claims.
4. Search with this skill's `scripts/kb.py search "..."` plus repo text search where useful.
5. Read canonical Markdown sections that support the answer.
6. Search again using synonyms, acronyms, entities, dates, and contrary terms if omission risk is material.

## Source hierarchy

Prefer, in order when applicable:

1. formal/primary/current source;
2. official implementation guidance;
3. secondary/reference material;
4. topic maps/cards only for navigation.

Recency does not automatically beat authority. Explain the relationship.

## Conflict handling

If two sources differ:

- quote or paraphrase each position separately;
- identify dates/versions/authority;
- state whether one explicitly supersedes the other;
- otherwise preserve the ambiguity.

Do not collapse disagreement into a false consensus.

## Citation style

Use markdown links to both the canonical conversion and the original input file:

```markdown
([Title](knowledge/docs/<id>.md) — “Section heading”; original [file.pdf](input/file.pdf), source p. 14)
```

For slides use `source-slide`; for spreadsheets use sheet names.

End answers with a **Sources** list of those links.

Never cite a card or topic map as the underlying authority when a canonical source exists.

## Completeness

For narrow factual questions, 1–3 strong sources can be enough.
For comparisons, policy interpretation, historical change, or “what do all documents say?”, inspect the full candidate set from the topic map/catalog and mention scope.

If evidence is absent, say the KB does not establish the answer and identify the searches/topics checked.
