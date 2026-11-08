---
title: Decision dashboard lab
description: Practice reading an indicator, verifying its source and documenting a decision with its limits.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: experimental
normative: false
owner: Javier Forero
domains: [Conversational Analytics, Semantic Layers, Decision Patterns]
source_ids: [SRC-PRACTICE-FX-001, SRC-PRACTICE-POP-001, SRC-PRACTICE-DASH-B2B-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Decision dashboard lab

**Practice question.** What signal would warrant reviewing a foreign-currency budget exposure? In this exercise, the planning team chooses whether to open a review or keep the current assumption. The final decision requires the organization's cash flows, budget currency and exposure horizon.

[Open official exchange rates](https://dashboards.javierforero.co/tasas-cambio/?lang=en){ .md-button .md-button--primary }

## Guided exercise · Exchange rates { #fx }

1. Choose two currencies, a start date and a time horizon. Record the quotation unit, value and official date of each series. Check the [data and methodology](https://github.com/jaforero/fx-bancos-centrales).
2. In **Base 100 comparison**, identify the first official observation from your chosen date for each currency. For local currency per USD, above 100 indicates depreciation against the dollar and below 100 indicates appreciation relative to that base. Try another start date and see whether the interpretation changes.
3. Check the data table. Distinguish an official observation from a value carried forward on a non-publication day. When comparing currencies, check whether starting points and observation dates align.
4. Define a review threshold before assessing the signal. If it triggers, ask the budget owner to check it against actual exposure and record when the assumption will be reviewed.

**Deliverable.** Complete a [Decision Brief](../learn/decision-brief.en.md) with both options, the threshold, dated evidence, the owner and the review condition. Repeat the analysis using another start date. If the decision changes, record why.

**Acceptance criterion.** A colleague can reproduce your interpretation using the same pair, period and source. The brief explains what would change the action and distinguishes official reference rates from a rate the organization could negotiate.

## Other practice routes

| Decision to practice | Demo | What to record |
|---|---|---|
| Review service capacity by age and area | [Latin American population](https://dashboards.javierforero.co/poblacion-latam/?lang=en) | Age group, selected edition and series, estimated or projected years, and the effect of a source revision. Follow the [demographic exercise](../learn/02-evidence-context.en.md#demographic-planning). |
| Prioritize an intervention after a service decline | [B2B SLA](https://dashboards.javierforero.co/claude/sla-operaciones/?lang=en) | Break period, denominator, escalation rule and evidence that could change the priority. Use the demo's simulated scenario. |
| Review a financial alert before committing budget | [Financial Pulse](https://dashboards.javierforero.co/claude/pulso-financiero/?lang=en) | Horizon, forecast benchmark, observed backtest error and action owner. The demo uses simulated data. |
| Choose a reversible commercial intervention | [Commercial performance](https://dashboards.javierforero.co/claude/desempeno-comercial/?lang=en) | Options, simulated baseline and criterion for observing the outcome. Continue with the [instrumented B2B case](b2b-proposal/index.en.md). |

To pilot conversational questions, add the [reference-answer and access checks](../learn/03-decision-experience.en.md#conversational-dashboard-pilot). Use the [Practice Lab catalog](catalog.en.md) to identify what data each resource uses.
