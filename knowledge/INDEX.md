# Knowledge base index

Last refresh: 2026-09-11 · 7 canonical documents (3 NIST PDFs + 4 Northwind fixtures)

Start here, then open a topic map, then search, then read `knowledge/docs/`.

```bash
uv run python .github/skills/ragless-kb/scripts/kb.py search "your question" --limit 12
```

## Topic maps

- [NIST AI RMF Core](topics/ai-rmf-core.md) — GOVERN, MAP, MEASURE, MANAGE; voluntary framework
- [Generative AI](topics/generative-ai.md) — NIST 600-1 profile and Northwind GenAI controls
- [Bias and fairness](topics/bias-and-fairness.md) — SP 1270 and harmful-bias characteristic
- [Northwind model risk](topics/northwind-model-risk.md) — validation, exceptions, inventory

## Authoritative documents

| Role | Canonical | Original |
| --- | --- | --- |
| NIST primary framework | [AI RMF 1.0](docs/nist-ai-100-1.md) | [NIST.AI.100-1.pdf](../input/NIST.AI.100-1.pdf) |
| GAI profile | [NIST AI 600-1](docs/nist-ai-600-1.md) | [NIST.AI.600-1.pdf](../input/NIST.AI.600-1.pdf) |
| Bias guidance | [SP 1270](docs/nist-sp-1270.md) | [NIST.SP.1270.pdf](../input/NIST.SP.1270.pdf) |
| Internal policy | [Northwind AI Governance Policy](docs/northwind-ai-governance-policy.md) | [northwind-ai-governance-policy.docx](../input/northwind-ai-governance-policy.docx) |
| Internal FAQ | [Model Risk FAQ](docs/faq-model-risk.md) | [faq-model-risk.txt](../input/faq-model-risk.txt) |
| Inventory briefing | [Q3 2026 briefing](docs/q3-model-inventory.md) | [q3-model-inventory.pptx](../input/q3-model-inventory.pptx) |
| Inventory table | [Model inventory](docs/model-inventory.md) | [model-inventory.csv](../input/model-inventory.csv) |

## Known conflicts

- Northwind exempts AI systems under USD 250,000 annual spend from **MEASURE**. NIST AI RMF 1.0 does not grant that exemption.
- The Q3 briefing reports **47 production models**; the CSV is a **five-row extract**.

## Date range

NIST: 2022 (SP 1270) through July 2024 (GAI profile). Northwind: April–September 2026.

## Ingestion notes

Text PDFs extracted cleanly. NIST 600-1 has some hyphenation/ligature artifacts (`proﬁle`). No scanned/image-only files in this sample set.
