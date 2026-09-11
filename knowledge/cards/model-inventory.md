---
id: model-inventory
title: Northwind Model Inventory
source: knowledge/docs/model-inventory.md
original: input/model-inventory.csv
authority: secondary
status: current
topics: [northwind, model-inventory]
---

# Northwind Model Inventory

## Purpose
Tabular inventory of selected Northwind models (id, owner, risk tier, status, last validation).

## Authority and recency
Operational extract. Pair with the Q3 briefing for counts and ownership narrative.

## Major topics
- Production vs validation-queue models
- High-risk systems including GenAI and HR screening

## Key definitions, rules, or findings
- Credit-Decision-v4 (NW-001): high, production, last validation 2025-11-02.
- HR-Screening-Assist (NW-031): high, validation-queue, last validation never.
- GenAI-Contract-Summarizer (NW-044): high, production, last validation 2026-03-01.

## Notable entities and dates
- Five models listed; 2026-09 snapshot implied by the briefing.

## Related documents
- [Q3 briefing](knowledge/docs/q3-model-inventory.md)
- [Northwind policy](knowledge/docs/northwind-ai-governance-policy.md) — NW-044 in scope for GenAI human review

## Conflicts or caveats
CSV lists five named models; the briefing states 47 production models. Treat the CSV as a sample extract, not the full inventory.

## Canonical source
[knowledge/docs/model-inventory.md](knowledge/docs/model-inventory.md) · original [input/model-inventory.csv](input/model-inventory.csv)
