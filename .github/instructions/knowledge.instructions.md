---
applyTo: "knowledge/**"
---

Files under `knowledge/cards/`, `knowledge/topics/`, `knowledge/INDEX.md`, `knowledge/catalog.json`, and `knowledge/.kb/` are derived artifacts and may be regenerated.
Canonical converted text lives under `knowledge/docs/`; preserve source provenance and do not replace it with summaries.
When editing generated knowledge artifacts, keep paths repository-relative and deterministic so regeneration produces stable diffs.
Do not delete input originals or canonical docs unless the user explicitly asks. Missing input files should be reported as orphans.
