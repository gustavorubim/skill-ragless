# Ragless KB skill

This folder is `skills/ragless-kb/`. It is meant to sit next to `agents/` — those two folders are the whole harness.

```text
.github/                    # Copilot / VS Code
  agents/docs-builder.agent.md
  agents/docs-chat.agent.md
  skills/ragless-kb/        ← this folder

.cursor/                    # Cursor (same pair)
  agents/docs-builder.agent.md
  agents/docs-chat.agent.md
  skills/ragless-kb/        ← copy this folder here too
```

No prompts, instructions, or extra Copilot files are required.

## Quick start

1. Create `input/` at the project root and drop PDF, DOCX, PPTX, XLSX, CSV, HTML, or text files.
2. `python -m pip install -r requirements.txt` (prefer a project `.venv`).
3. Select **Docs Builder** → `preprocess`.
4. Select **Docs Chat** and ask questions.

Answers must be grounded in `knowledge/docs/` with markdown links to those files and to `input/` originals.

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
requirements.txt
scripts/kb.py
scripts/fetch_eval_docs.py
scripts/make_sample_docs.py
references/
```

`input/` and `knowledge/` stay at the project root.

## CLI

```bash
python .github/skills/ragless-kb/scripts/kb.py python
python .cursor/skills/ragless-kb/scripts/kb.py python
```

See [cookbook.md](cookbook.md).
