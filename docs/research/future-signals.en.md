---
title: Future signals
description: Industry forecasts and signals governed as scenarios rather than facts or commitments.
status: candidate
version: 0.9.0-rc.1
artifact_type: future-signals-register
authority_level: bounded-forecast-synthesis
normative: false
owner: Javier Forero
domains: [Research, Future Directions, AI Agents]
claim_ids: [CLAIM-FUTURE-SIGNALS-001, CLAIM-DMN-VERSION-001, CLAIM-NIST-REVISION-001]
source_ids: [SRC-GARTNER-PREDICTIONS-001, SRC-GARTNER-VALUE-001, SRC-OMG-DMN-001, SRC-OMG-DMN-BETA-001, SRC-NIST-AIRMF-001]
as_of: 2026-07-24
last_reviewed: 2026-07-24
---

# Future signals

A future signal helps stress-test a strategy. **It is not a certain prediction,
proof of readiness or sufficient authorization for an investment.** Analyst
reports are registered by metadata and hash; their PDF files are not
redistributed.

## Signal register

| Signal | Horizon | Primary uncertainty | Decision question | Evidence that updates it |
|---|---|---|---|---|
| Conversational interfaces may absorb some exploration currently performed in dashboards | short–medium | adoption, accuracy, cost and task fit | Which decisions need conversation, visualization or both? | task-level telemetry and comparison with the current interface |
| Copilots and agents may move from explaining to proposing or executing actions | short–medium | authority, error chains, reversibility and control | Which rights can the owner delegate and under what stop conditions? | incidents, override, reversal, accuracy and outcome |
| Data and AI value may be measured closer to decisions and outcomes | medium | attribution and gameable metrics | Which decision changes and what alternative is the comparator? | baseline, counterfactual and follow-up |
| Semantic layers and explicit decision models may become more important | medium | interoperability and maintenance cost | What semantics must be governed before automation? | defects, reuse, traceability and change time |
| Governance may shift from isolated artifacts to sociotechnical systems | medium–long | regulatory maturity and fragmentation | Which controls remain effective when a system learns or acts? | audits, control failures and official versions |

## How to use a signal

1. Translate it into a concrete decision rather than a generic trend.
2. State the horizon and critical assumption.
3. Design an early indicator and abandonment condition.
4. Compare at least two plausible scenarios.
5. Record what observation would confirm, refute or make the signal irrelevant.

## Standards and framework signals

Versions also change. As of `2026-07-24`:

- OMG publishes DMN 1.5 as a formal specification and DMN 1.7 Beta 1 as an
  informational document; a conformity decision must check the current
  official inventory.
- NIST keeps AI RMF 1.0 available and states that it is under revision; this
  page does not assume the content of a future version.

## What remains prohibited

- “Gartner says it will happen” as a fact;
- treating a target year as a probability;
- turning expected adoption into expected benefit;
- presenting a beta as a formal standard;
- inferring readiness without evaluating data, process, people and control;
- presenting a signal as validation of PULSE or CDI.

<div class="cdi-risk" markdown>
**Stop condition:** if a signal changes no decision, experiment or indicator, it
is narrative context rather than decision intelligence.
</div>
