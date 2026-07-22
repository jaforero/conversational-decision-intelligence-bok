---
title: Decision Measurement Record
description: Versioned template that freezes a measurement plan before action and adds outcomes later without rewriting the original decision.
status: candidate
version: 0.7.0-rc.1
artifact_type: practice-template
authority_level: candidate-guidance
normative: false
owner: Javier Forero
domains: [Decision Metrics, Decision Quality, PULSE]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001, SRC-PRACTICE-B2B-001]
claim_ids: [CLAIM-DM-SYSTEM-001, CLAIM-DQ-PROFILE-001]
last_reviewed: 2026-07-21
---

# Decision Measurement Record

This record complements the [Decision Brief](../learn/decision-brief.md). The Brief structures the choice; the Measurement Record preserves the observation plan and later review.

## Two snapshots, one history

| Snapshot | Closed when | May later change? |
|---|---|---|
| **Decision snapshot** | Before first action | No. Add dated, reasoned amendments. |
| **Outcome review** | When the defined horizon closes | Yes, as versioned reviews; never overwrite the original. |

This prevents retrospective adaptation of baseline, expectation or success criterion.

## Before acting

Complete ID, decision, owner, date and chosen option; sourced baseline; expected outcome with range and uncertainty; fidelity metric and denominator; guardrails, thresholds and response; horizon, comparison and attribution limits; ex-ante profile and blockers; approvals and freeze timestamp. Keep unknowns `null` with an explicit blocker—never invent estimates to make the record look ready.

## After the horizon

Add actual action and exceptions, outcomes and guardrails, deviation from range, concurrent changes and alternatives, claim strength permitted by the design, hold/scale/stop/reverse/investigate choice, and concrete next-cycle change.

## Reusable template

[Download YAML template](/assets/data/decision-measurement-record.yml){ .md-button .md-button--primary }

The template preserves unknowns as `null` and results as `not-observed`. Production use requires context-appropriate permissions, retention, sensitive-information handling and traceability.

## Review ritual

1. Verify the snapshot was frozen before action.
2. Review process quality before seeing outcome.
3. Open outcome and guardrails by relevant segment.
4. Compare with expectation, not only prior period.
5. Examine fidelity, shocks and alternatives.
6. Calibrate claim strength.
7. Record next-cycle change and owner.

## Publishing rule

A complete record proves **traceability**, not effectiveness. Causal claims need a defensible identification design, adequate data and explicit limits. Claims that CDI or PULSE improve decisions require multiple cases and external evaluation; this template does not provide that evidence.

[Return to the measurement system](decision-measurement-system.md){ .md-button }
