# Grounded chat eval

Sample corpus: 3 NIST PDFs + 4 Northwind fixtures. Retrieval eval (`python scripts/kb.py eval --k 5`): **12/12 hit@5** and **12/12 gold snippets** present in canonical Markdown.

These answers were produced with the Docs Chat protocol: `knowledge/INDEX.md` → topic map → `kb.py search` → canonical `knowledge/docs/` → citations with file links. Cards were not used as evidence.

## Q1. What are the four core functions of the NIST AI RMF?

### Answer
The AI RMF Core is composed of four functions: GOVERN, MAP, MEASURE, and MANAGE ([Artificial Intelligence Risk Management Framework (AI RMF 1.0)](knowledge/docs/nist-ai-100-1.md) — “AI RMF Core”; original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf), source p. 25).

### Sources
- [AI RMF 1.0](knowledge/docs/nist-ai-100-1.md) — AI RMF Core (source p. 25) · original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf)

### Conflicts or limits
None. Companion materials reuse the same four functions.

## Q2. Are any Northwind AI systems exempt from MEASURE?

### Answer
Yes, as an **internal Northwind rule only**. The Northwind AI Governance Policy says AI systems with forecast annual spend under USD 250,000 are exempt from the MEASURE function; GOVERN, MAP, and MANAGE still apply. The policy itself states this is a Northwind cost-control choice and is **not stated in NIST AI RMF 1.0** ([Northwind AI Governance Policy](knowledge/docs/northwind-ai-governance-policy.md) — “MEASURE function exemption”; original [northwind-ai-governance-policy.docx](input/northwind-ai-governance-policy.docx)).

NIST AI RMF 1.0 describes MEASURE as one of the four Core functions and does not grant a spend-based exemption ([AI RMF 1.0](knowledge/docs/nist-ai-100-1.md) — “AI RMF Core”; original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf), source p. 25).

### Sources
- [Northwind AI Governance Policy](knowledge/docs/northwind-ai-governance-policy.md) — MEASURE function exemption · original [northwind-ai-governance-policy.docx](input/northwind-ai-governance-policy.docx)
- [AI RMF 1.0](knowledge/docs/nist-ai-100-1.md) — AI RMF Core · original [NIST.AI.100-1.pdf](input/NIST.AI.100-1.pdf)

### Conflicts or limits
The two sources disagree. Internal policy does not supersede NIST; it records a local exemption.

## Q3. What is Northwind's highest-risk production model, and when was it last validated?

### Answer
Credit-Decision-v4 (NW-001) is the highest-risk production model. Last independent validation: 2025-11-02; next due: 2026-11-02 ([Q3 2026 Model Inventory Briefing](knowledge/docs/q3-model-inventory.md) — Slide 2; original [q3-model-inventory.pptx](input/q3-model-inventory.pptx), source-slide 2). The inventory table lists the same model, owner (Retail Credit), high risk tier, production status, and 2025-11-02 last validation ([Northwind Model Inventory](knowledge/docs/model-inventory.md); original [model-inventory.csv](input/model-inventory.csv)).

### Sources
- [Q3 2026 Model Inventory Briefing](knowledge/docs/q3-model-inventory.md) — Slide 2 · original [q3-model-inventory.pptx](input/q3-model-inventory.pptx)
- [Northwind Model Inventory](knowledge/docs/model-inventory.md) · original [model-inventory.csv](input/model-inventory.csv)

### Conflicts or limits
The briefing reports 47 production models; the CSV is a five-row extract. Both agree on NW-001's last validation date.

## Q4. Do challenger models follow the same validation cadence?

### Answer
Yes. Challenger models follow the same annual independent validation cadence as production models unless an emergency exception is approved by the Model Risk Committee ([Northwind Model Risk FAQ](knowledge/docs/faq-model-risk.md) — “Validation cadence”; original [faq-model-risk.txt](input/faq-model-risk.txt)).

### Sources
- [Northwind Model Risk FAQ](knowledge/docs/faq-model-risk.md) — Validation cadence · original [faq-model-risk.txt](input/faq-model-risk.txt)

### Conflicts or limits
None versus the internal policy's annual-validation rule.

## Q5. What is Northwind's CEO compensation?

### Answer
The knowledge base does not establish this. Search over CEO / compensation / salary and the Northwind topic map did not yield a compensation figure. Hits on “compensation” in NIST AI 600-1 refer to human-subjects research practices, not executive pay.

### Sources
- Searched: `knowledge/INDEX.md`, `knowledge/topics/northwind-model-risk.md`, `python scripts/kb.py search "Northwind CEO compensation salary"`
- No canonical document states CEO compensation.

### Conflicts or limits
Not in corpus.

## Efficiency notes

- Progressive navigation kept context small: INDEX + one topic map + 1–2 canonical files per question.
- BM25 search returned the gold document in the top 3 for every factual question above.
- Canonical Markdown contained every gold snippet in `eval/questions.json`.
- No embeddings were used.
