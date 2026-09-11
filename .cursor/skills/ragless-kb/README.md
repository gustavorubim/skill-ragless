# Ragless KB skill

This folder is `skills/ragless-kb/`. It is meant to sit next to `agents/` — those two folders are the whole harness.

## Use both agents

**Docs Builder** and **Docs Chat** are a pair. Copy and use both; one agent is not enough.

| Agent | File | When to select it |
| --- | --- | --- |
| **Docs Builder** | `agents/docs-builder.agent.md` | Preprocess, ingest, refresh, index, validate |
| **Docs Chat** | `agents/docs-chat.agent.md` | Questions about the documents |

Do not ask Docs Builder domain questions, and do not ask Docs Chat to ingest. Builder prepares `knowledge/`; Chat is the only agent that answers from it. After a successful preprocess, switch to **Docs Chat** (Builder can hand off).

```text
.github/                    # Copilot / VS Code
  agents/docs-builder.agent.md
  agents/docs-chat.agent.md
  skills/ragless-kb/        ← this folder

.cursor/                    # Cursor (same agent pair + this skill)
  agents/docs-builder.agent.md
  agents/docs-chat.agent.md
  skills/ragless-kb/        ← copy this folder here too
```

No prompts, instructions, or extra Copilot files are required.

## Quick start

1. Create `input/` at the project root and drop PDF, DOCX, PPTX, XLSX, CSV, HTML, or text files.
2. Use **uv** for the venv and packages: `uv venv` then `uv pip install -r requirements.txt`.
3. Select **Docs Builder** → `preprocess`.
4. Switch to **Docs Chat** and ask questions. Do not stay on Builder for Q&A.

Answers must be grounded in `knowledge/docs/` with markdown links to those files and to `input/` originals.

How search and the ragless design work (BM25, SQLite FTS5, why not vector RAG): [technical-background.md](technical-background.md).

VS Code: enable `chat.useAgentSkills` if `/ragless-kb` does not appear.

## Sample prompts

### 1. Preprocess (Docs Builder)

Select **Docs Builder**, then send:

```text
preprocess
```

```text
Preprocess everything in input/. Convert PDF, DOCX, PPTX, and other files to Markdown, enrich metadata, build INDEX.md, topic maps, and search, then validate.
```

```text
refresh
```

### 2. Chat (Docs Chat)

Select **Docs Chat**, then try:

```text
What are the four core functions of the NIST AI Risk Management Framework? Cite the files.
```

```text
Are any Northwind AI systems exempt from the MEASURE function? Do the NIST documents agree?
```

```text
What is Northwind's highest-risk production model, and when was it last validated?
```

```text
Where do the documents disagree? Quote each side and link the sources.
```

```text
Summarize the major themes in this corpus, which document is authoritative for each, and where evidence is thin.
```


## This folder

```text
SKILL.md
README.md
cookbook.md
technical-background.md
requirements.txt
scripts/kb.py
scripts/fetch_eval_docs.py
scripts/make_sample_docs.py
scripts/generate_large_eval.py
references/
```

`input/` and `knowledge/` stay at the project root.

## CLI

```bash
uv venv
uv pip install -r requirements.txt
uv run python .github/skills/ragless-kb/scripts/kb.py python
uv run python .cursor/skills/ragless-kb/scripts/kb.py python
```

See [cookbook.md](cookbook.md) and [technical-background.md](technical-background.md).
