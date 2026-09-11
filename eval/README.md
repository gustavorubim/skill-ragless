# Eval sets

- `questions.json` — 12 gold questions for the bundled NIST + Northwind sample corpus.
- `chat-results.md` — grounded-chat checks on that sample set.
- `large/` — generated synthetic corpus (~1000 docs / ~100 questions). Gitignored. Create it with `scripts/generate_large_eval.py` and set `KB_ROOT` to `eval/large`.
- `large-results.md` — last timed uv run of the large eval.
