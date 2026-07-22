---
title: Decision quality and measurement
description: Candidate system for evaluating process before a decision, observing execution and learning from outcomes without confusing outcome with quality.
status: candidate
version: 0.7.0-rc.1
artifact_type: knowledge-area-landing
authority_level: candidate-synthesis
normative: false
owner: Javier Forero
domains: [Decision Quality, Decision Metrics, Decision Governance]
source_ids: [SRC-PULSE-DNA-001, SRC-DQ-SDP-001, SRC-ACADEMIC-OUTCOME-BIAS-001, SRC-ACADEMIC-SCORING-RULES-001]
claim_ids: [CLAIM-DQ-OUTCOME-001, CLAIM-DQ-PROFILE-001, CLAIM-DM-SYSTEM-001]
last_reviewed: 2026-07-21
---

# Decision quality and measurement

Measuring a decision is not asking whether it “turned out well.” A material decision must be examined at three moments:

1. **before deciding:** framing, alternatives, evidence, values, reasoning and commitment;
2. **during execution:** latency, action fidelity, escalation, overrides and guardrails;
3. **after the horizon:** outcome, deviation from expectation, prudent attribution and next-cycle change.

Sprint 5's candidate system connects these moments without collapsing them into a universal score.

<div class="cdi-grid cdi-grid--3">
<a class="cdi-card" href="decision-quality/"><span class="cdi-card__index">BEFORE</span><h3>Decision Quality</h3><p>Review defensibility before the outcome introduces hindsight bias.</p></a>
<a class="cdi-card" href="decision-measurement-system/"><span class="cdi-card__index">CYCLE</span><h3>Decision Measurement System</h3><p>Select a minimum metric portfolio for priority, quality, action, time, risk and learning.</p></a>
<a class="cdi-card" href="measurement-record/"><span class="cdi-card__index">ARTIFACT</span><h3>Measurement Record</h3><p>Preregister expectation and measurement, then add outcome without rewriting what was known.</p></a>
</div>

## Problem addressed

A dashboard can show results and a meeting can produce a decision, but neither necessarily preserves prior expectation, process weakness, authorized execution, distributed cost, compatibility of outcome with expectation or next-cycle change. Without separation, a good outcome may legitimize a weak process and a bad outcome may punish a reasonable decision under uncertainty.

## Unit of measurement

The minimum unit is an **identified decision cycle**, not a tool, person or AI initiative. It states owner, date, options, action, expectation, horizon and review. Portfolio aggregation becomes meaningful only after comparable cycles exist.

!!! warning "No universal metric"
    Quality depends on stakes, reversibility, frequency, uncertainty and affected people. This system proposes an architecture and measurement contracts—not a universal benchmark or validated organizational-maturity test.

## Relationship with PULSE

PULSE requires observable value and learning that compares expectation with result. This section operationalizes those requirements for the CDI-BoK; it neither redefines PULSE nor proves that instrumentation improves outcomes.

[Design decision measurement →](decision-measurement-system.md){ .md-button .md-button--primary }
