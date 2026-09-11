# Ragless KB cookbook

Copy this skill folder, drop documents, preprocess, then chat. No embeddings.

`$SKILL` below is the folder that contains this file:

- Copilot: `.github/skills/ragless-kb`
- Cursor: `.cursor/skills/ragless-kb`

```bash
python $SKILL/scripts/kb.py python          # print .venv interpreter; use it after this
python $SKILL/scripts/kb.py skill-path      # confirm which copy is running
```

---

## 1. Copy the skill into a project

Copy the entire `ragless-kb` directory (not only `SKILL.md`).

| Harness | Destination |
| --- | --- |
| VS Code / GitHub Copilot | `<project>/.github/skills/ragless-kb/` |
| Cursor | `<project>/.cursor/skills/ragless-kb/` |

You can copy it to both. The folders are identical.

For Copilot custom agents, also copy:

- `$SKILL/agents/docs-builder.agent.md` → `.github/agents/docs-builder.agent.md`
- `$SKILL/agents/docs-chat.agent.md` → `.github/agents/docs-chat.agent.md`

Optional: copy `$SKILL/prompts/` → `.github/prompts/`.

Create the drop folder if it does not exist:

```text
<project>/input/
```

Install Python packages once (prefer a project `.venv`):

```bash
python -m pip install -r $SKILL/requirements.txt
```

---

## 2. Drop documents and preprocess

Put files in `input/` (subfolders are fine). Then invoke the skill:

> /ragless-kb preprocess

Or select **Docs Builder** and say `preprocess`.

The agent will:

1. Resolve the interpreter (`kb.py python`).
2. Run `ingest` (PDF/DOCX/PPTX/XLSX/CSV/HTML/text → `knowledge/docs/`).
3. Enrich metadata, cards, topic maps, and `knowledge/INDEX.md`.
4. `rebuild` the catalog + BM25 index.
5. `validate`.
6. Report counts, warnings, and conflicts.

Supported extensions: `.md`, `.txt`, `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.csv`, `.html`. Scanned PDFs are flagged, not OCRed. `README.md` in `input/` is ignored.

---

## 3. Chat with grounded answers

Select **Docs Chat**, or:

> /ragless-kb What are the four core functions of the NIST AI RMF?

The agent must not dump the whole corpus. It should follow [references/chat.md](references/chat.md):

`INDEX.md` → topic maps → `kb.py search` → cards for triage only → `knowledge/docs/` sections.

Every material claim needs file links:

```markdown
The Core has four functions: GOVERN, MAP, MEASURE, and MANAGE
([AI RMF 1.0](knowledge/docs/nist-ai-100-1.md) — “AI RMF Core”;
original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf), source p. 25).
```

Answer shape:

```markdown
## Answer
…

## Sources
- [Title](knowledge/docs/<id>.md) — section (source p. N) · original [file](input/file)

## Conflicts or limits
…
```

If the corpus does not establish the answer, say so and name what was searched.

---

## 4. Refresh after new files

Drop more files (or replace a source) in `input/`, then:

> /ragless-kb refresh

Unchanged hashes are skipped. Semantic frontmatter on existing canonical docs is kept. Missing input files are reported as `ORPHAN`; canonical Markdown is not deleted.

---

## 5. Search and status yourself

```bash
python $SKILL/scripts/kb.py ingest
python $SKILL/scripts/kb.py rebuild
python $SKILL/scripts/kb.py search "MEASURE function exemption" --limit 12
python $SKILL/scripts/kb.py search "MEASURE function exemption" --json
python $SKILL/scripts/kb.py status
python $SKILL/scripts/kb.py validate
```

---

## 6. Eval (optional)

At the project root, `eval/questions.json` can list gold questions:

```json
{
  "questions": [
    {
      "id": "rmf-four-functions",
      "question": "What are the four core functions of the NIST AI Risk Management Framework?",
      "expected_doc_ids": ["nist-ai-100-1"],
      "must_contain": ["GOVERN", "MAP", "MEASURE", "MANAGE"]
    }
  ]
}
```

```bash
python $SKILL/scripts/kb.py eval --k 5
```

Hit@k = any `expected_doc_ids` value appears in the top-k BM25 hits. `must_contain` is checked in canonical Markdown.

Sample NIST PDFs + Northwind office fixtures (for trying the skill):

```bash
python $SKILL/scripts/fetch_eval_docs.py
python $SKILL/scripts/make_sample_docs.py
```

Then preprocess and eval.

---

## 7. Custom agents (Copilot)

After copying `$SKILL/agents/` to `.github/agents/`:

1. **Docs Builder** — preprocess only (edit + execute). Hands off to Docs Chat.
2. **Docs Chat** — Q&A only (read/search/execute, no edit). Grounded citations.

Cursor uses this skill file directly; custom Copilot agents are optional there.

---

## 8. Troubleshooting

| Symptom | What to do |
| --- | --- |
| `/ragless-kb` missing in VS Code | Set `chat.useAgentSkills` to true |
| `Cannot locate workspace root` | Create `input/` at the project root, or set `KB_ROOT` |
| `Install pypdf` / similar | `pip install -r $SKILL/requirements.txt` inside the project `.venv` |
| Empty PDF text | Likely scanned; skill flags it. OCR is out of scope |
| Search returns nothing useful | Rebuild; then ask the agent to retry synonyms. Do not add embeddings |
| Agent cites a card as proof | Correct it: only `knowledge/docs/` is evidence |

---

## 9. What not to copy

Do not copy `knowledge/` or `input/` from a demo repo unless you want that corpus. The skill creates `knowledge/` on preprocess. Keep originals in the target project's `input/`.
