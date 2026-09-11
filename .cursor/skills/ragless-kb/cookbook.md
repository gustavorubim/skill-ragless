# Ragless KB cookbook

The product is two folders: `agents/` and `skills/`. Drop documents in `input/`, preprocess with **Docs Builder**, chat with **Docs Chat**.

`$SKILL` is this folder:

- Copilot: `.github/skills/ragless-kb`
- Cursor: `.cursor/skills/ragless-kb`

```bash
python $SKILL/scripts/kb.py python
python $SKILL/scripts/kb.py skill-path
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

Then create `input/` at the project root and install:

```bash
python -m pip install -r $SKILL/requirements.txt
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
python $SKILL/scripts/kb.py ingest
python $SKILL/scripts/kb.py rebuild
python $SKILL/scripts/kb.py search "MEASURE function exemption" --limit 12
python $SKILL/scripts/kb.py status
python $SKILL/scripts/kb.py validate
python $SKILL/scripts/kb.py eval --k 5
```

---

## 6. Troubleshooting

| Symptom | What to do |
| --- | --- |
| `/ragless-kb` missing in VS Code | `chat.useAgentSkills` |
| Agent missing from picker | Confirm `agents/docs-builder.agent.md` and `agents/docs-chat.agent.md` sit next to `skills/` |
| `Cannot locate workspace root` | Create `input/` at the project root |
| Missing extractor package | `pip install -r $SKILL/requirements.txt` |
| Agent cites a card as proof | Only `knowledge/docs/` is evidence |
