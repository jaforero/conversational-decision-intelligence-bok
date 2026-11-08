---
title: Practice Lab catalog
description: Find a lab by decision and distinguish public data, simulated demos and instrumented cases.
status: candidate
version: 0.5.0-rc.1
artifact_type: practice-catalog
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains: [Case Studies, Decision Patterns, Decision Metrics]
source_ids: [SRC-PRACTICE-DASH-ROOT-001, SRC-PRACTICE-GPT-ROOT-001, SRC-PRACTICE-FX-001, SRC-PRACTICE-POP-001, SRC-PRACTICE-GRAPH-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Practice Lab catalog

Choose a resource based on the decision you want to practice. The labs guide the exercise within the CDI-BoK and link to tools in [Javier Forero's portfolio](https://dashboards.javierforero.co/?lang=en).

| Start with | What you produce |
|---|---|
| [Decision dashboards](dashboards.md) | A brief with a verifiable indicator, an action criterion and a review date. |
| [Knowledge graphs](knowledge-graph.md) | A reproducible traceability finding and a proposed CDI-BoK improvement. |
| [B2B case · Proposal](b2b-proposal/index.md) | A protocol for evaluating a commercial intervention using simulated data. |

## Resources with public sources

Routes checked against the portfolio on **November 8, 2026**.

| Resource | What to practice | Data type |
|---|---|---|
| [Exchange rates](https://dashboards.javierforero.co/tasas-cambio/?lang=en) | Interpret base 100 and distinguish official publications from carried-forward values | Series from seven central banks and calculated crosses |
| [Latin American population](https://dashboards.javierforero.co/poblacion-latam/?lang=en) | Compare composition, areas and horizons | Official series and projections for 20 countries |
| [Cost of living by city](https://dashboards.javierforero.co/claude/costo-vida-colombia/?lang=en) | Interpret a benchmark relative to the average | Public indicators for Colombia, with methodology on the page |
| [AI training compute](https://dashboards.javierforero.co/ia-compute/?lang=en) | Check a trend against its levels of evidence | Public compilation of models with reported or estimated values |
| [Graph explorer](https://dashboards.javierforero.co/claude/grafo-conocimiento/?lang=en) | Follow links and inspect their context | User-selected corpus. The lab loads the public CDI-BoK |

## Consulting demos

| Practice decision | Claude | ChatGPT Work | Data |
|---|---|---|---|
| Prioritize an operational intervention | [B2B SLA](https://dashboards.javierforero.co/claude/sla-operaciones/?lang=en) | [B2B SLA](https://javier-dashboards.jforero.chatgpt.site/dashboards/sla) | Simulated. Claude supports local uploads. |
| Evaluate a budget alert | [Financial Pulse](https://dashboards.javierforero.co/claude/pulso-financiero/?lang=en) | [Financial forecast](https://javier-dashboards.jforero.chatgpt.site/dashboards/finanzas) | Simulated. Claude supports local uploads. |
| Choose a funnel intervention | [Commercial performance](https://dashboards.javierforero.co/claude/desempeno-comercial/?lang=en) | [Commercial and sales](https://javier-dashboards.jforero.chatgpt.site/dashboards/comercial) | Simulated sales, funnel and CRM. |

The [ChatGPT Work collection](https://javier-dashboards.jforero.chatgpt.site/en) also links to external work on sports prediction and inflation. The [demo registry](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/governance/registries/external-demos.yml) retains the July observation and the resources added since then.

## Instrumented case

The CDI-BoK selected **B2B Commercial · Proposal** for its recurring decision, three simulated sources, available baseline and reversible intervention. Running it requires a confirmed owner and a viable comparison. The [instrumented, not executed](b2b-proposal/index.md) status distinguishes the protocol from results of a real pilot.
