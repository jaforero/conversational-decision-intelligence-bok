---
title: Worked Decision Brief · Delivery SLA
description: A complete example of how to act on an SLA decline, decide whether a forecast is needed, and review the outcome.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Intelligence, Decision Governance, Decision Metrics]
source_ids: [SRC-PULSE-DNA-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Worked Decision Brief · Delivery SLA

**Example with simulated data.** The routes, figures and decisions on this page were created for the exercise. It follows the [Decision Brief template](../learn/decision-brief.en.md) and develops the SLA case from the [dashboard lab](dashboards.en.md).

**Decision recorded on Friday of week 4.** Move one dispatch window per working day from route B to route A during week 5, with a rollback ready and a daily review.

## 1. Priority

Restore on-time delivery on A to **95%** while keeping B at or above **97%**, the pilot's protection threshold. Over the previous four weeks, A achieved **92%** and B **98%**. Waiting leaves A exposed to another week below target. The trial lasts one week.

## 2. Decision and alternatives

The operations lead approves on Friday before scheduling closes. The dispatch coordinator executes and can return the window to B on the next working day. Both routes and their customers are affected.

| Alternative | Expected benefit | Cost or condition |
|---|---|---|
| **A. Move one window per day for five working days** | A gets capacity before cutoff using existing resources. | B gives up headroom. Move the window only if B's confirmed orders fit and it keeps one window in reserve. |
| **B. Keep the current allocation and wait for another reporting period** | B keeps its headroom and there is no reallocation cost. | A remains exposed to late deliveries. Choose this if B's reserve cannot be verified. |
| **C. Add a window using overtime** | A gains capacity while B keeps its reserve. | Requires budget and approval. Remains an option if both routes need capacity. |

## 3. Evidence and context available before acting

**Definition.** SLA = eligible deliveries on time ÷ eligible deliveries promised for the week. The same rule applies to both routes and all reporting periods. Each cell shows on-time deliveries over eligible deliveries.

| Reporting period | Route A | Route B |
|---|---:|---:|
| Week 1 | 94/100 | 98/100 |
| Week 2 | 93/100 | 98/100 |
| Week 3 | 91/100 | 98/100 |
| Week 4 | 90/100 | 98/100 |
| **Four-week baseline** | **368/400 = 92%** | **392/400 = 98%** |

- **Scenario facts.** The dashboard was reconciled with the dispatch log and the capacity plan. A fell below target in all four weeks, and 23 of its 32 late deliveries left after the hub cutoff. Week 5's plan allows one window to be moved each day while keeping one window in reserve on B for the confirmed order book.
- **Inference and hypothesis.** The concentration of late departures justifies testing capacity before cutoff. Loading or on-route delays could also contribute. The available records cannot separate those mechanisms.
- **What was sufficient.** The recurring gap, a plausible mechanism and verifiable capacity justify a bounded, reversible change. If B loses its reserve or the logs show delays occurring after dispatch, the preferred option changes.

## 4. Decision experience and the threshold for forecasting

The operations lead uses the dashboard to locate the gap and the capacity plan to compare the three options. The daily log records whether the window was used and whether B retained its reserve. Confirmed orders, daily checks and the rollback option are sufficient for this trial.

**When would a forecast be needed?** If a material share of demand is unconfirmed and could consume B's reserve, or if the transfer must last several weeks and becomes more costly to reverse. In that case, estimate demand ranges by route and compare them with capacity after the transfer. If even the high scenario fits with the agreed reserve, option A remains viable. If a plausible scenario consumes the reserve, keep the allocation or request overtime based on the cost of waiting.

## 5. Human control and execution

Operations decides and approves, and Dispatch executes from Monday. In this exercise, AI could summarize aggregate metrics and flag differences for review. Shift changes, overtime approval and instructions remain with authorized people. The record retains the reporting period, approved option, transferred windows and any exceptions.

## 6. Action, metrics and agreed review rule

- **Process.** Record how many of the five planned windows were used. Review confirmed orders and B's reserve daily. If the reserve is lost, stop the transfer and restore the window on the next working day.
- **Outcome expected before acting.** A's weekly SLA is **92% / 95% / 97%** in low, central and high scenarios. These are working assumptions for the review. B's floor is **97%**.
- **Review at the end of week 5.** Keep the transfer for another bounded cycle if A reaches **95%** and B stays at or above **97%**. If A misses target and B remains protected, check whether the window was used and where the delay persists before repeating. If B falls below **97%**, reverse the transfer even if A reaches its target.
- **Comparison.** Use each route's baseline to compare performance. B is also affected because it gives up capacity, so it cannot serve as a control group.

## 7. Simulated outcome and revised decision

| Route | Baseline | Week 5 | Change | Reading against the rule |
|---|---:|---:|---:|---|
| A | 92% | 96/100 = **96%** | **+4 pp** | Meets target. |
| B | 98% | 96/100 = **96%** | **−2 pp** | Breaches the protection threshold. |

Dispatch used **5 of 5** windows and B's reserve was retained in the daily plan. Even so, B finished below the threshold. **Operations reverses the transfer on Monday of week 6** and checks whether B's operating reserve covers weekly variability. A's improvement and B's decline are observed changes in the simulation. Comparing one post-intervention week with the baseline cannot attribute them to the transfer.

**Challenge record.** The most fragile assumption was that one reserve window was sufficient to protect B. Order mix or dispatch incidents could also have changed the results. Keeping the transfer despite the threshold could compound late deliveries on B and erode service for its customers. Confidence is **moderate for trying a reversible action** and **low for attributing the outcome to it**. Before scaling, compare like-for-like reporting periods and assess overtime or a staggered trial with a comparable route that retains its capacity.
