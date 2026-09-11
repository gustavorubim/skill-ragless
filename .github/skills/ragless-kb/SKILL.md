---
name: ragless-kb
description: Build and query a local document knowledge base without embeddings or vector RAG. Converts PDF, DOCX, PPTX, XLSX, HTML, and text dropped into input/; then answers questions with source-grounded citations and file links. Use when the user says preprocess, ingest, build, refresh, index, validate, or asks questions about the documents, corpus, policies, or knowledge base.
disable-model-invocation: true
argument-hint: preprocess | refresh | validate | chat
---

# Ragless KB

Self-contained skill. This folder is the package: copy it to `.github/skills/ragless-kb/` (VS Code / Copilot) or `.cursor/skills/ragless-kb/` (Cursor).

Human docs: [README.md](README.md) · recipes: [cookbook.md](cookbook.md)

Do not introduce embeddings or a vector database. Canonical evidence is Markdown in `knowledge/docs/` plus provenance back to `input/`.

## Skill CLI

CLI is [scripts/kb.py](scripts/kb.py) in **this folder**. From the workspace root:

```bash
python .github/skills/ragless-kb/scripts/kb.py python
python .cursor/skills/ragless-kb/scripts/kb.py python
```

Use the copy you loaded. If this `SKILL.md` lives under `.cursor/skills/ragless-kb/`, substitute `.cursor/skills/ragless-kb` for `.github/skills/ragless-kb` in every command. Use the printed interpreter for later `kb.py` commands. `skill-path` prints this script's location.

Dependencies: [requirements.txt](requirements.txt)

## Route the request

| Argument / intent | Action |
| --- | --- |
| `preprocess`, `build`, `ingest`, empty build request | [Preprocess workflow](#preprocess-workflow) |
| `refresh` | Ingest, then re-enrich only changed/new docs |
| `validate` | Run `validate` and spot-check INDEX/cards |
| a question about the documents, or `chat` | Read [references/chat.md](references/chat.md) and [references/qa-protocol.md](references/qa-protocol.md) |

## Workspace layout (not inside this skill)

Created next to the project that copied this skill, not inside the skill folder:

```text
input/                 # drop originals here
knowledge/
  docs/                # canonical Markdown + provenance
  cards/               # navigation cards
  topics/              # topic maps
  INDEX.md             # corpus map (start of every Q&A turn)
  catalog.json
  .kb/                 # manifest + disposable SQLite FTS5 index
```

## Preprocess workflow

### 1. Deterministic extraction

```bash
python .github/skills/ragless-kb/scripts/kb.py ingest
```

(`preprocess` is an alias.) Discovers supported files in `input/` (dotfiles and `README.md` ignored); hashes and skips unchanged conversions; writes `knowledge/docs/`; preserves agent-filled semantic frontmatter on re-extract; reports missing sources as `ORPHAN` without deleting canonical Markdown.

Supported: Markdown/text, PDF, DOCX, PPTX, XLSX/CSV, HTML.

Do not summarize from filenames. Inspect extracted content.

### 2. Check extraction quality

For each new/changed doc, skim for empty/short extraction, broken encoding, missing headings/tables, scrambled pages, scanned/image-only PDFs, duplicates. Record warnings in metadata/cards.

### 3. Enrich metadata

Edit frontmatter in `knowledge/docs/*.md` using [references/metadata-schema.md](references/metadata-schema.md). Infer conservatively. Do not strip `source_file`, `source_sha256`, `id`, or `extraction_warnings`.

### 4. Document cards

Create `knowledge/cards/<id>.md` for every canonical doc using [references/card-template.md](references/card-template.md). Cards are navigation aids, not evidence.

### 5. Topic maps

Write `knowledge/topics/` maps using [references/topic-template.md](references/topic-template.md). Prefer 5–20 coherent maps.

### 6. Corpus INDEX

Keep `knowledge/INDEX.md` compact: size, last refresh, topic links, authoritative docs with links to `knowledge/docs/` and `input/`, conflicts, search reminder, ingestion warnings.

### 7. Rebuild catalog and search

```bash
python .github/skills/ragless-kb/scripts/kb.py rebuild
python .github/skills/ragless-kb/scripts/kb.py search "validation frequency" --limit 12
python .github/skills/ragless-kb/scripts/kb.py status
```

Natural-language questions become OR terms (longest distinctive words first), ranked with BM25.

### 8. Validate

```bash
python .github/skills/ragless-kb/scripts/kb.py validate
```

Confirm: every supported input file is represented or failed; orphans reported; every canonical doc has a card; topic coverage; provenance present; search hits sensible.

### 9. Optional eval

If `eval/questions.json` exists at the workspace root:

```bash
python .github/skills/ragless-kb/scripts/kb.py eval --k 5
```

### 10. Report

Counts (added/updated/unchanged/failed/unsupported/orphaned), extraction caveats, topic changes, conflicts, validation/eval, user actions. Then the user can chat (invoke this skill with a question, or select **Docs Chat**).

## Chat (summary)

Do not load the whole corpus. Follow [references/chat.md](references/chat.md). Cite markdown links to `knowledge/docs/<id>.md` and the original `input/` file.

## Hard rules

- Never delete originals in `input/` unless the user explicitly asks.
- Never delete canonical Markdown just because a source went missing; report `ORPHAN`.
- Canonical `knowledge/docs/` outranks cards, topics, and the search index.
