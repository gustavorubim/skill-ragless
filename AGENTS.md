# Agent Guide: Ragless Document Knowledge Base

Two workflows: **preprocess/build** and **question answering**. No embeddings or vector RAG.

The skill is self-contained. Use the copy in this repo:

- Copilot: `.github/skills/ragless-kb/SKILL.md`
- Cursor: `.cursor/skills/ragless-kb/SKILL.md`

Recipes: `.github/skills/ragless-kb/cookbook.md` (identical under `.cursor/skills/ragless-kb/`).

## Build / preprocess

Follow the skill (`/ragless-kb preprocess`). New files go in `input/`. CLI:

```bash
python .github/skills/ragless-kb/scripts/kb.py python
```

## Question answering

Select **Docs Chat**, or follow `.github/skills/ragless-kb/references/chat.md`.

`knowledge/INDEX.md` → topics → cards (triage) → `knowledge/docs/`. Search with the skill CLI. Cite markdown links to `knowledge/docs/` and `input/`.
