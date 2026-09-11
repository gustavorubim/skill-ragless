# Ragless Document Knowledge Base

Chat with a small document set without embeddings. The harness is **two folders**: `agents/` and `skills/`.

```text
.github/                         Copilot / VS Code
  agents/docs-builder.agent.md   preprocess
  agents/docs-chat.agent.md      custom chat
  skills/ragless-kb/             CLI + instructions

.cursor/                         Cursor (same pair)
  agents/…
  skills/ragless-kb/
```

## Workflow

1. Drop files into `input/`.
2. `./setup.ps1` or `./setup.sh` (uses **uv** for `.venv` and packages).
3. Select **Docs Builder** and send a preprocess prompt.
4. Select **Docs Chat** and ask questions.

## Sample prompts

### 1. Preprocess (Docs Builder)

Select **Docs Builder**, then send one of these:

```text
preprocess
```

```text
Preprocess everything in input/. Convert PDF, DOCX, PPTX, and other files to Markdown, enrich metadata, build INDEX.md, topic maps, and search, then validate.
```

```text
refresh
```

```text
Validate the knowledge base and tell me what is missing or weakly extracted.
```

### 2. Chat (Docs Chat)

After preprocess, select **Docs Chat**. Try:

```text
What are the four core functions of the NIST AI Risk Management Framework? Cite the files.
```

```text
Is the NIST AI RMF mandatory or voluntary?
```

```text
Are any Northwind AI systems exempt from the MEASURE function? Do the NIST documents agree?
```

```text
What is Northwind's highest-risk production model, and when was it last validated?
```

```text
Do challenger models follow the same validation cadence as production models?
```

```text
Where do the documents disagree? Quote each side and link the sources.
```

```text
Summarize the major themes in this corpus, which document is authoritative for each, and where evidence is thin.
```

Answers should include markdown links to `knowledge/docs/` and the original `input/` files.

## CLI

```bash
uv venv
uv pip install -r .github/skills/ragless-kb/requirements.txt
uv run python .github/skills/ragless-kb/scripts/kb.py python
uv run python .github/skills/ragless-kb/scripts/kb.py ingest
uv run python .github/skills/ragless-kb/scripts/kb.py search "MEASURE function exemption" --limit 12
```

Large eval (~1000 docs / ~100 questions), isolated under `eval/large/`:

```bash
uv venv
uv pip install -r .github/skills/ragless-kb/requirements.txt
uv pip install -r requirements.txt
uv run python .github/skills/ragless-kb/scripts/generate_large_eval.py --root eval/large --docs 1000 --questions 100
```

```powershell
$env:KB_ROOT = "$PWD\eval\large"
uv run python .github/skills/ragless-kb/scripts/kb.py ingest
uv run python .github/skills/ragless-kb/scripts/kb.py rebuild
uv run python .github/skills/ragless-kb/scripts/kb.py validate
uv run python .github/skills/ragless-kb/scripts/kb.py eval --k 5
```

Recipes: [cookbook.md](.github/skills/ragless-kb/cookbook.md). Design / BM25 / FTS5: [technical-background.md](.github/skills/ragless-kb/technical-background.md).
