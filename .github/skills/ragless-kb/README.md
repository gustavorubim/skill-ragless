# Ragless KB skill

Copy **this folder** into a project. That is the whole skill: instructions, CLI, templates, custom agents, and recipes. Nothing else from the original repo is required except an `input/` folder at the project root.

## Install

**GitHub Copilot / VS Code**

```text
<your-project>/.github/skills/ragless-kb/     ← this folder
```

Optional, so Copilot lists custom agents: copy `agents/*.agent.md` to `<your-project>/.github/agents/`. Optional prompt files: copy `prompts/` to `<your-project>/.github/prompts/`.

**Cursor**

```text
<your-project>/.cursor/skills/ragless-kb/     ← this folder
```

Enable Agent Skills in VS Code if `/ragless-kb` does not appear: `chat.useAgentSkills`.

## Quick start

1. Create `<your-project>/input/` and drop PDF, DOCX, PPTX, XLSX, CSV, HTML, or text files there.
2. Once per machine: `python -m pip install -r requirements.txt` (from this folder). A project `.venv` is preferred.
3. Preprocess: invoke `/ragless-kb preprocess`, or select **Docs Builder** and say `preprocess`.
4. Chat: select **Docs Chat**, or invoke `/ragless-kb` with a question.

Answers must be grounded in `knowledge/docs/` with markdown links to those files and to the originals in `input/`.

## This folder

```text
SKILL.md                 agent instructions (preprocess + chat routing)
README.md                this file
cookbook.md              copy, preprocess, chat, refresh, eval recipes
requirements.txt
scripts/kb.py            ingest, search, rebuild, validate, eval
scripts/fetch_eval_docs.py
scripts/make_sample_docs.py
references/              metadata, cards, topics, Q&A, chat protocol
agents/                  Docs Builder + Docs Chat (copy to .github/agents/)
prompts/                 optional Copilot prompt files
```

Workspace artifacts (`input/`, `knowledge/`) live at the **project root**, not inside this skill folder.

## CLI

```bash
python .github/skills/ragless-kb/scripts/kb.py python
python .cursor/skills/ragless-kb/scripts/kb.py python
```

Use the path that matches where you copied this folder. See [cookbook.md](cookbook.md).
