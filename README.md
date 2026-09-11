# Ragless Document Knowledge Base

Skill-first kit for chatting with a small document set (about 20–30 files) without embeddings or a vector database.

The skill is a **self-contained folder**. Copy it; do not hunt for files elsewhere.

| Harness | Copy this folder to |
| --- | --- |
| VS Code / GitHub Copilot | `.github/skills/ragless-kb/` |
| Cursor | `.cursor/skills/ragless-kb/` |

Inside that folder: `SKILL.md`, [README.md](.github/skills/ragless-kb/README.md), [cookbook.md](.github/skills/ragless-kb/cookbook.md), CLI, templates, agents, and prompts.

## Workflow

1. Copy the skill folder (see above). This demo repo already has both copies.
2. Drop files into `input/` (subfolders are fine).
3. Install deps once: `./setup.ps1` or `./setup.sh`, or `pip install -r .github/skills/ragless-kb/requirements.txt`.
4. Preprocess: select **Docs Builder** and say `preprocess`, or `/ragless-kb preprocess`.
5. Chat: select **Docs Chat**, or `/ragless-kb` plus a question. Answers include links to `knowledge/docs/` and `input/`.

Enable Agent Skills in VS Code if the slash command does not appear: `chat.useAgentSkills`.

Step-by-step recipes: [cookbook.md](.github/skills/ragless-kb/cookbook.md).

## Why this is not RAG

The skill converts sources into readable Markdown, then builds `INDEX.md`, document cards, topic maps, and a disposable SQLite FTS5/BM25 index. The chat agent navigates those files. Evidence stays in git-friendly Markdown with provenance.

## Layout

```text
.github/skills/ragless-kb/   Copilot copy of the skill (self-contained)
.cursor/skills/ragless-kb/   Cursor copy of the skill (identical)
.github/agents/              Docs Builder + Docs Chat (copied from the skill)
input/                       drop originals here
knowledge/                   generated corpus map, docs, cards, topics
eval/questions.json          optional retrieval eval
```

## CLI

From this demo repo you can still run `python scripts/kb.py` (wrapper). After copying only the skill, use the skill path:

```bash
python .github/skills/ragless-kb/scripts/kb.py python
python .github/skills/ragless-kb/scripts/kb.py ingest
python .github/skills/ragless-kb/scripts/kb.py search "MEASURE function exemption" --limit 12
python .github/skills/ragless-kb/scripts/kb.py eval --k 5
```

## Sample corpus and eval

```bash
python .github/skills/ragless-kb/scripts/fetch_eval_docs.py
python .github/skills/ragless-kb/scripts/make_sample_docs.py
```

Then preprocess and `eval --k 5`. Bundled sample: **12/12 hit@5** and **12/12 gold snippets**. Grounded Q&A examples: [eval/chat-results.md](eval/chat-results.md).

NIST publications used for eval are U.S. government works.
