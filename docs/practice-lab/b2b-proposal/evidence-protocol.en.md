---
title: B2B evidence protocol
description: Reproducible baseline, evidence quality, counterfactual and attribution rules for the Proposal case.
status: candidate
version: 0.5.0-rc.1
artifact_type: evidence-protocol
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains: [Decision Metrics, Research, Decision Quality]
source_ids: [SRC-PRACTICE-B2B-001, SRC-PRACTICE-DASH-B2B-001]
claim_ids: [CLAIM-PRACTICE-B2B-001, CLAIM-PRACTICE-B2B-002, CLAIM-PRACTICE-B2B-003]
last_reviewed: 2026-07-21
---

# B2B evidence protocol

## Readiness verdict

Decision and four options are ready; the demo baseline is reproducible. Organizational fitness for purpose, owner, rights and prior expectation are **not established**. The counterfactual is designed but unassigned; no outcome is observed; causal attribution is blocked pending a comparator and 2–3 cycles.

## Reproduced baseline

Calculations derive from the simulated [commercial dashboard](https://dashboards.javierforero.co/claude/desempeno-comercial/) observed July 21, 2026. Repository CSVs are audit aggregates, not real CRM data.

### Compliance and Proposal

- June 2026: `381,061.4 / 475,657 = 80.11%`, the lowest weighted compliance from January 2025 to June 2026; all 8 demo sellers were below 90%.
- Jan–Mar 2026 Proposal baseline: `(46.5 + 50.4 + 47.2) / 3 = 48.03%`.
- Apr–Jun deterioration: `(37.4 + 34.5 + 37.7) / 3 = 36.53%`; change `−11.50 pp`.

The pre-decline window requires sensitivity against full-year 2025 and seasonality before real use.

### Channels

| Channel | Won / closed | Win rate | Wilson 95% |
|---|---:|---:|---:|
| Event / trade show | 5 / 56 | 8.93% | 3.87%–19.26% |
| Referral | 10 / 126 | 7.94% | 4.37%–13.99% |
| Digital inbound | 4 / 111 | 3.60% | 1.41%–8.90% |

The ranking favors event and referral, but intervals overlap widely. **“Significantly superior” is unsupported.** Option B remains blocked pending more observations, mix adjustment or a specific test.

## Preferred design: hold-out + difference-in-differences

Define eligible sellers, regions or portfolios; match on prior conversion, volume, ticket, channel mix and seniority; assign intervention and operational comparator; preregister action, expectation and horizon; calculate:

\[
\widehat{\tau}_{DiD}=(Y_{I,post}-Y_{I,pre})-(Y_{C,post}-Y_{C,pre})
\]

Review parallel trends, composition changes and atypical deals; report estimate, interval and sensitivity. Without hold-out, historical series or forecast is weaker and normally remains `observed-noncausal`.

## Metrics and learning

Primary: Proposal→Negotiation conversion. Secondary: sales compliance. Guardrails: quality prospects, cycle time and margin/discount. Process: 0–10 rubric. One cycle inspects implementation, not effectiveness; two is the case minimum and three preferred. Do not institutionalize good outcomes from weak process; review hypotheses after poor outcomes from sound process. Log every post-action definition, group or expectation change.

## Evidence files

- [`demo-sales-monthly.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-sales-monthly.csv)
- [`demo-funnel-2026.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-funnel-2026.csv)
- [`demo-channel-win-rate.csv`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/b2b-proposal/demo-channel-win-rate.csv)
