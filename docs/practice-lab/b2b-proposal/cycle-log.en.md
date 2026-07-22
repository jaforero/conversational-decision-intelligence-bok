---
title: B2B cycle record
description: Current state, pending fields and monthly ritual for turning the decision into traceable learning.
status: candidate
version: 0.5.0-rc.1
artifact_type: learning-log
authority_level: experimental-candidate
normative: false
owner: Javier Forero
domains: [Decision Metrics, Decision Quality, Enterprise Implementation]
source_ids: [SRC-PRACTICE-B2B-001]
claim_ids: [CLAIM-PRACTICE-B2B-HYP-001]
last_reviewed: 2026-07-21
---

# B2B cycle record

## Current state

| Field | Value |
|---|---|
| Decision | `DEC-2026-07-COMM-PROPUESTA-01` |
| Cycle | `CYCLE-01` |
| Status | **Not started** |
| Chosen option | Pending |
| Action executed | No |
| Expectation frozen | No |
| Outcome observed | No |
| Attributable effect | Not estimable |
| Learning | Pending |

Unknowns are not encoded as zero: `0` is data; blank means no observation exists.

## Before action

Confirm owner and rights; choose an option and record rejections; define intervention, comparator and assignment; approve baseline and sensitivity; freeze lower/central/upper expectation and horizon; score process quality before the future is known; lock timestamp and obtain sign-off.

## Monthly review

Verify execution fidelity; calculate identically defined intervention and comparison measures; record mix, people, pricing, seasonality and atypical deals; estimate difference-in-differences where permitted; compare expected range with result; separate process, outcome and attribution; decide continue, adapt, stop or escalate.

## State gate

| Next state | Minimum condition |
|---|---|
| `observed-noncausal` | Action and result recorded, insufficient comparator |
| `evaluated` | Preregistered expectation, defensible comparator, 2–3 cycles and analyzed limits |
| `blocked` | No owner, fit-for-purpose data or measurable design |

[Download CSV log](/assets/data/b2b-proposal-cycle-log.csv){ .md-button .md-button--primary }
[Download YAML record](/assets/data/b2b-proposal-decision-record.yml){ .md-button }

!!! note "First useful evidence"
    Before conversion is measured, the cycle can show whether the contract is understandable, the owner can state an expectation and the ritual fits operations. That is method usability evidence, not commercial-impact evidence.
