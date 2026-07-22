---
title: Practice Lab catalog
description: Verified demo inventory and assessment of readiness to become instrumented cases.
status: candidate
version: 0.5.0-rc.1
artifact_type: practice-catalog
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains: [Case Studies, Decision Patterns, Decision Metrics]
source_ids: [SRC-PRACTICE-DASH-ROOT-001, SRC-PRACTICE-GPT-ROOT-001]
claim_ids: []
last_reviewed: 2026-07-21
---

# Practice Lab catalog

This inventory records what was publicly available on **July 21, 2026**. It catalogs interfaces and does not attribute impact. Availability may change outside the CDI-BoK release cycle.

## Two portfolios, one evidence boundary

| Portfolio | Observed cases | Visible capabilities | Limit |
|---|---:|---|---|
| [Claude](https://dashboards.javierforero.co/claude/) | 3 interactive demos | Local SLA/Finance upload, deterministic Q&A, governance | Specific pages state simulated or synthetic demo data |
| [ChatGPT Work](https://javier-dashboards.jforero.chatgpt.site/) | 5 available, 1 announced | Three dashboards, predictive project, Tableau benchmark | A collection and interface do not prove decision improvement |

!!! warning "The specific statement prevails"
    The home page says “embedded real data,” while reviewed SLA, Finance and Commercial pages state simulated, synthetic or demonstration data. This catalog uses the more specific conservative statement.

## Verified inventory

| ID | Case | Portfolio | Data observed | Case readiness |
|---|---|---|---|---|
| `JF-CLAUDE-SLA` | B2B SLA compliance | Claude | Synthetic; local CSV/XLSX | Medium: visible decision and thresholds; no organizational result |
| `JF-CLAUDE-FINANCE` | Corporate Financial Pulse | Claude | Simulated demo; local CSV/XLSX | Medium: visible backtest; slow action attribution |
| `JF-CLAUDE-COMMERCIAL` | B2B Commercial Performance | Claude | Simulated sales, funnel and CRM | **High for instrumentation:** three sources, recurring choice, reversible action |
| `JF-GPT-FINANCE` | 2025 financial prediction | ChatGPT Work | Simulated financial dataset | Medium: predictive evidence; no decision learning record |
| `JF-GPT-SLA` | B2B SLA compliance | ChatGPT Work | 570 simulated records | Medium-high: signal and action; no churn/retention link |
| `JF-GPT-COMMERCIAL` | Commercial performance and sales | ChatGPT Work | Three simulated datasets | High for instrumentation; same decision family |
| `JF-GPT-WORLDCUP` | 2026 World Cup prediction | ChatGPT Work | Prediction data and models | High for calibration; low for B2B organizational action |
| `JF-GPT-TABLEAU` | Latin America inflation | ChatGPT Work | Not assessed this sprint | Low: descriptive benchmark, not instrumented cycle |
| `JF-GPT-PULSE` | PULSE Decision Intelligence | ChatGPT Work | No observable case | Not assessable |

## Why B2B Commercial was selected

It offers a material recurring monthly funnel decision, heterogeneous sales/conversion/CRM sources, a demo baseline and a reversible Proposal intervention. It lacks an observed result, confirmed real owner and assigned counterfactual; therefore instrumentation is possible but effectiveness and causal attribution remain blocked.

[Open the B2B Proposal case](b2b-proposal/index.md){ .md-button .md-button--primary }

## What would change selection

Customer-level SLA–churn data would strengthen the retention case; failure to confirm a commercial owner would keep B2B Proposal pedagogical; more channel evidence could raise demand reallocation; and a case with executed action and valid comparison could produce observable learning sooner.
