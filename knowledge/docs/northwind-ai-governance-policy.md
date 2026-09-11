---
id: "northwind-ai-governance-policy"
title: "Northwind AI Governance Policy"
source_file: "input/northwind-ai-governance-policy.docx"
source_sha256: "c6082c656039b523d2079b030ea53e617b3626155d553db96b5451db6f82a987"
document_type: "policy"
date: "2026-04-01"
version: "3.2"
authority: "formal-primary"
status: "current"
topics: ["northwind", "validation", "governance", "ai-risk"]
entities: ["Northwind Bank", "Model Risk Committee", "MRC"]
summary: "Internal Northwind policy: annual independent validation, 90-day emergency exceptions, and a cost-based MEASURE exemption that is not in NIST AI RMF 1.0."
extraction_warnings: []
---

# northwind ai governance policy

# Northwind AI Governance Policy

Document ID: NW-AIGP-3.2

Version: 3.2

Effective date: 2026-04-01

Classification: Internal policy

## Purpose

This policy governs how Northwind Bank develops, validates, and operates artificial intelligence and machine learning systems. It is an internal control standard. Where this policy is quieter than applicable law or a formal regulator framework, the stricter requirement wins.

## Independent validation

Every model in production must receive independent validation at least annually. The Model Risk Committee (MRC) is the approval authority for production use, material change, and retirement.

## Emergency exceptions

The MRC may approve an emergency production exception. Emergency exceptions expire after ninety (90) days and cannot be silently renewed. A written close-out or a full validation is required before expiry.

## MEASURE function exemption

AI systems with forecast annual spend under USD 250,000 are exempt from the MEASURE function of the NIST AI Risk Management Framework. GOVERN, MAP, and MANAGE still apply. This exemption is a Northwind cost-control choice and is not stated in NIST AI RMF 1.0.

## Generative AI

Generative AI systems that draft customer-facing content require human review before send. The GenAI-Contract-Summarizer (NW-044) is in scope.
