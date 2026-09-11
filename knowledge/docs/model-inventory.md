---
id: "model-inventory"
title: "Northwind Model Inventory"
source_file: "input/model-inventory.csv"
source_sha256: "ea658bc40655a6c3ae6f13a06b9606e10edbe07a009f569d1c7672778cdae272"
document_type: "inventory"
date: "2026-09"
version: null
authority: "secondary"
status: "current"
topics: ["northwind", "model-inventory"]
entities: ["Credit-Decision-v4", "GenAI-Contract-Summarizer"]
summary: "Tabular inventory of five Northwind models including Credit-Decision-v4 (last validated 2025-11-02) and GenAI-Contract-Summarizer."
extraction_warnings: []
---

# model inventory

| model_id | name | owner | risk_tier | status | last_validation |
| NW-001 | Credit-Decision-v4 | Retail Credit | high | production | 2025-11-02 |
| NW-014 | Fraud-Graph-v2 | Payments | high | production | 2026-01-18 |
| NW-022 | Marketing-Propensity-v9 | Growth | medium | production | 2025-08-30 |
| NW-031 | HR-Screening-Assist | People Analytics | high | validation-queue | never |
| NW-044 | GenAI-Contract-Summarizer | Legal Ops | high | production | 2026-03-01 |
