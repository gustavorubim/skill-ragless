# Ragless KB cookbook

The product is two folders: `agents/` and `skills/`. **Docs Builder** and **Docs Chat** are a pair — use both. Drop documents in `input/`, preprocess with **Docs Builder**, then switch to **Docs Chat** for questions. Design, BM25, and FTS5: [technical-background.md](technical-background.md).

`$SKILL` is this folder:

- Copilot: `.github/skills/ragless-kb`
- Cursor: `.cursor/skills/ragless-kb`

```bash
uv venv
uv pip install -r $SKILL/requirements.txt
uv run python $SKILL/scripts/kb.py python
uv run python $SKILL/scripts/kb.py skill-path
```

---

## 1. Install the two folders

Copy the pair into the harness root:

```text
<harness>/
  agents/docs-builder.agent.md
  agents/docs-chat.agent.md
  skills/ragless-kb/          # this entire directory
```

`<harness>` is `.github` (Copilot / VS Code) or `.cursor` (Cursor). Copy into both if you use both.

Then create `input/` at the project root. Use **uv** (not pip / `python -m venv`):

```bash
uv venv
uv pip install -r $SKILL/requirements.txt
```

---

## 2. Preprocess

Select **Docs Builder** and say `preprocess` (or `/ragless-kb preprocess`).

The agent reads `$SKILL/SKILL.md`, runs `ingest`, writes `knowledge/docs/`, builds cards, topic maps, `INDEX.md`, BM25 search, and validates.

Supported: `.md`, `.txt`, `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.csv`, `.html`. Scanned PDFs are flagged, not OCRed.

---

## 3. Chat

Select **Docs Chat**. It reads `$SKILL/references/chat.md` and searches with `$SKILL/scripts/kb.py`.

`INDEX.md` → topics → search → cards (triage) → `knowledge/docs/`.

```markdown
## Answer
…

## Sources
- [Title](knowledge/docs/<id>.md) — section (source p. N) · original [file](input/file)

## Conflicts or limits
…
```

---

## 4. Refresh

Drop or replace files in `input/`. Select **Docs Builder** and say `refresh`.

---

## 5. CLI

```bash
uv run python $SKILL/scripts/kb.py ingest
uv run python $SKILL/scripts/kb.py rebuild
uv run python $SKILL/scripts/kb.py search "MEASURE function exemption" --limit 12
uv run python $SKILL/scripts/kb.py status
uv run python $SKILL/scripts/kb.py validate
uv run python $SKILL/scripts/kb.py eval --k 5
```

Large eval (isolated workspace, does not touch the sample `input/` corpus):

```bash
uv run python $SKILL/scripts/generate_large_eval.py --root eval/large --docs 1000 --questions 100
KB_ROOT=eval/large uv run python $SKILL/scripts/kb.py ingest
KB_ROOT=eval/large uv run python $SKILL/scripts/kb.py rebuild
KB_ROOT=eval/large uv run python $SKILL/scripts/kb.py eval --k 5
```

On PowerShell set `$env:KB_ROOT = "$PWD\eval\large"` before the ingest/rebuild/eval commands.

---

## 6. Troubleshooting

| Symptom | What to do |
| --- | --- |
| `/ragless-kb` missing in VS Code | `chat.useAgentSkills` |
| Agent missing from picker | Confirm `agents/docs-builder.agent.md` and `agents/docs-chat.agent.md` sit next to `skills/` |
| `Cannot locate workspace root` | Create `input/` at the project root |
| `uv` not found | Install from https://docs.astral.sh/uv/getting-started/installation/ |
| Missing extractor package | `uv pip install -r $SKILL/requirements.txt` |
| Agent cites a card as proof | Only `knowledge/docs/` is evidence |
