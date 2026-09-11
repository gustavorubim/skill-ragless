# Knowledge Base Repository Instructions

This repository is an agent-navigable document knowledge base. Do not use embeddings or a vector database.

## Operating model

- `input/` contains newly dropped source files.
- `knowledge/docs/` contains canonical Markdown conversions. Treat these as the primary textual sources for answering questions.
- `knowledge/cards/` contains compact document cards for fast triage; cards are navigation aids, not authoritative sources.
- `knowledge/topics/` contains topic maps and cross-document syntheses; these are navigation aids.
- `knowledge/INDEX.md` is the corpus map and normal starting point.
- `knowledge/catalog.json` is the machine-readable document catalog.
- `knowledge/.kb/search.sqlite3` is a disposable derived lexical/BM25 search index.
- Original source files remain in `input/` unless the user explicitly asks to move or delete them.

## Answering questions

For substantive knowledge-base questions:

1. Read `knowledge/INDEX.md` first unless the question already names a specific source.
2. Use topic maps and document cards to narrow likely sources.
3. Run the skill CLI `python .github/skills/ragless-kb/scripts/kb.py search "<query>"` (or the `.cursor/skills/ragless-kb/` copy) for targeted lexical/BM25 search when helpful.
4. Open the relevant canonical Markdown documents and inspect the exact supporting sections.
5. Expand the search when evidence is incomplete, ambiguous, contradictory, or likely to exist under different terminology.
6. Prefer primary, newer, and higher-authority sources over summaries or derivative guidance.
7. State disagreements, stale sources, and uncertainty explicitly.
8. Cite answers with markdown links to `knowledge/docs/` and the original `input/` file, plus section headings and page/slide/sheet provenance when present.
9. Never cite a document card or topic map as though it were the underlying authority when a canonical source exists.
10. For broad synthesis questions, sample all relevant documents listed in the topic map instead of stopping at the first plausible hit.

Follow `.github/skills/ragless-kb/references/chat.md` and `.github/skills/ragless-kb/references/qa-protocol.md`.

## Building or refreshing the KB

When asked to preprocess, build, ingest, refresh, index, organize, or prepare the knowledge base, follow `.github/skills/ragless-kb/SKILL.md`. Resolve the interpreter with `python .github/skills/ragless-kb/scripts/kb.py python` first. Do not invent summaries from filenames alone. Do not load the build workflow merely to answer a question about an already-prepared corpus.

## Safety and fidelity

- Never silently delete source material.
- Preserve tables, headings, lists, URLs, dates, definitions, and qualifiers during conversion as faithfully as practical.
- Preserve provenance to original filename and page/slide/sheet where extractors provide it.
- Do not collapse conflicting source statements into a false consensus.
- Derived indexes (`INDEX.md`, cards, topics, catalog, SQLite) may be regenerated; canonical source Markdown should not be overwritten from a lower-fidelity derivative.
