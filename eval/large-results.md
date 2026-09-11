# Large eval results

Run with **uv** 0.12.13 (`uv venv`, `uv pip install -r`, `uv run python`). Isolated workspace `eval/large/` (`KB_ROOT`); the sample NIST/Northwind corpus was not modified.

Generator:

```bash
uv run python .github/skills/ragless-kb/scripts/generate_large_eval.py --root eval/large --docs 1000 --questions 100 --seed 42
```

## Corpus

| | |
| --- | --- |
| Documents | 1000 (`record-0001` … `record-1000`) |
| Questions | 100 |
| Formats | 840 `.txt`, 50 `.md`, 50 `.html`, 50 `.csv`, 10 `.docx` |
| Search index | 1.5 MB SQLite FTS5 |
| Catalog | 538 KB JSON |

Each file repeats shared Northwind policy language and plants one unique token (`qkassetNNNN`, `ownerNNNNname`, `ctlNNNNzeta`, or `siteNNNNriver`). Questions include that token so BM25 can pick the row out of 999 near-duplicates.

## Timings (Windows, uv-managed `.venv`)

| Step | Seconds |
| --- | --- |
| Generate corpus | 4.5 |
| `ingest` (1000 files, 0 failed) | 6.8 |
| `rebuild` catalog + FTS5 | 8.9 |
| `validate` | 1.0 |
| `eval --k 5` (100 questions) | 0.38 |

## Retrieval

| Metric | Result |
| --- | --- |
| hit@1 | **100/100** |
| hit@5 | **100/100** |
| Gold snippet coverage | **100/100** |
| Mean rank of gold doc | 1.0 |
| `validate` | VALID |

## Sample corpus (unchanged, also via uv)

| Check | Result |
| --- | --- |
| Unit tests | **14 passed** (`uv run python -m pytest tests/test_kb.py`) |
| Sample `validate` | VALID (7 docs) |
| Sample retrieval | **12/12 hit@5**, **12/12 gold snippets** |
