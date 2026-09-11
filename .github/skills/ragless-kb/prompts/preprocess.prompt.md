---
description: Preprocess input/ into canonical Markdown, cards, topic maps, INDEX, and search.
agent: Docs Builder
---

Preprocess the knowledge base from everything currently in `input/`. Follow the `ragless-kb` skill completely (`preprocess` / full build). Use incremental processing where possible, validate extraction and provenance, regenerate navigation artifacts and search index, run this skill's `scripts/kb.py eval --k 5` if `eval/questions.json` exists, and finish with a concise ingestion report.
