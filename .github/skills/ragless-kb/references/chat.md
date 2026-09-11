# Chat protocol

Use this when the user asks about already-prepared documents. Do **not** run preprocess unless they explicitly ask to ingest or refresh.

CLI is `scripts/kb.py` in the parent skill folder. From the workspace root:

```bash
python .github/skills/ragless-kb/scripts/kb.py python
python .cursor/skills/ragless-kb/scripts/kb.py search "<question>" --limit 12
```

If this skill lives under `.cursor/skills/ragless-kb/`, use that path.

## Progressive retrieval

Do not load the whole corpus.

1. Read `knowledge/INDEX.md`.
2. Open likely `knowledge/topics/*.md` maps.
3. Run search (interpreter from `kb.py python`).
4. Use `knowledge/cards/` only to triage.
5. Read the exact supporting sections in `knowledge/docs/`.
6. Search again with synonyms, entities, dates, or exact phrases when recall may be incomplete.

Also follow [qa-protocol.md](qa-protocol.md).

## Grounding and links

Every material claim needs markdown links to the canonical doc and the original input file:

```markdown
According to the AI RMF Core, the four functions are GOVERN, MAP, MEASURE, and MANAGE
([Artificial Intelligence Risk Management Framework](knowledge/docs/nist-ai-100-1.md) — “AI RMF Core”;
original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf), source p. 25).
```

End with a **Sources** list. Cards and topic maps are not citable authorities.

If the corpus does not establish an answer, say so and name what was searched.

## Answer shape

```markdown
## Answer
<source-grounded answer; quote or paraphrase with citations inline>

## Sources
- [Title](knowledge/docs/<id>.md) — section heading (source p. N) · original [file.pdf](input/file.pdf)

## Conflicts or limits
<disagreements, stale material, extraction warnings, or "not in corpus">
```
