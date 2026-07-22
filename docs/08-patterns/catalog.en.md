---
title: Conversational pattern catalog
description: Five candidate patterns for framing, grounding, deliberating, committing and learning around a decision.
status: candidate
version: 0.8.0-rc.1
artifact_type: pattern-catalog
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains: [Decision Patterns, Conversational Decision Intelligence, Decision Governance]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001, SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-OUTCOME-BIAS-001]
claim_ids: [CLAIM-CDP-CATALOG-001, CLAIM-CDP-SELECTION-001]
last_reviewed: 2026-07-21
---

# Conversational pattern catalog

These five patterns cover recurring cycle blockers—not five screens or prompts. They can guide a meeting, brief, tracked dashboard or governed assistant. None requires AI.

| ID | Pattern | Moment | Minimum output |
|---|---|---|---|
| `CDP-001` | Decision contract | Frame | Decision, owner, alternatives, date and expected action |
| `CDP-002` | Evidence boundary | Ground | Facts, inferences, unknowns and fitness for purpose |
| `CDP-003` | Option challenge | Deliberate | Comparable options, trade-offs and change conditions |
| `CDP-004` | Decision–action handoff | Commit | Authorized choice, execution, guardrails and escalation |
| `CDP-005` | Expectation–result review | Learn | Deviation, calibrated attribution and next-cycle adjustment |

## CDP-001 — Decision contract

**Use when:** conversation begins with “analyze sales” or “what should we do?” without a choice. Convert the topic to who chooses what, among which alternatives and by when; complete PDAMR; state affected people, costs and reversibility; include no action when material; confirm with the rights holder.

**Exit:** a minimum Decision Brief. **Stop:** without a real choice or owner, reclassify as information exploration. **Risk:** false legitimacy if a facilitator assigns ownership without authority; bureaucracy at second order. **Alternative:** operational rule or decision table for stable recurring choices. **PULSE:** Business First, Decision First, PDAMR, Focus.

## CDP-002 — Evidence boundary

**Use when:** figures, definitions, filters or explanations conflict. Restore population, period, unit, filters and metric; identify source, owner, lineage and permission; separate fact, calculation, inference, hypothesis, recommendation and unknown; assess fitness for purpose; expose counterevidence and sensitivity; answer, abstain or escalate with a verifiable reason.

**Exit:** bounded evidence whose conclusion does not exceed its sources. **Stop:** unreconciled material definitions, missing permissions or inadequate quality. **Risk:** over-governance and citation-as-authority. **Alternative:** controlled report for regulated recurring calculations. **PULSE:** Trust First, Context First, Evidence Before Authority, Perceive.

## CDP-003 — Option challenge

**Use when:** one dominant recommendation, false dichotomy or unstructured idea list appears. Make criteria and defensible weights explicit; create materially different alternatives including no action; state mechanism, fragile assumption, cost, delay, risk and reversibility; formulate the strongest counterargument; seek a potentially superior alternative; state what changes the ranking.

**Exit:** auditable comparison with provisional option and calibrated confidence. **Stop:** apply a preapproved emergency rule when delay would increase immediate harm. **Risk:** option theater and numerical criteria hiding political or distributional judgment. **Alternative:** facilitated workshop, formal decision analysis or multidisciplinary review. **PULSE:** Generate options, Anticipate, Evidence Before Authority.

## CDP-004 — Decision–action handoff

**Use when:** recommendation or preference exists but commitment and subsequent action are unclear. Separate recommend, decide, approve, execute, stop and answer; record chosen and rejected alternatives; translate choice into accountable action and timing; define AI permissions, review, guardrails, stop, reversal and escalation; freeze expectation and review date; require positive confirmation.

**Exit:** authorized decision and traceable action plan, or explicit abstention/escalation. **Stop:** without decision right, approval or risk-proportional reversal, only prepare the handoff. **Risk:** authority laundering, concentrated power and traces used to suppress dissent. **Alternative:** deterministic transactional workflow. **PULSE:** Decide and Act, Governance Enables Speed, Human-in-Control.

## CDP-005 — Expectation–result review

**Use when:** a decision horizon ends. Open but do not overwrite the prior snapshot; record outcomes, process measures, guardrails, unintended effects and execution quality; describe deviation before explaining; examine counterfactual, confounding and sample size; separate ex-ante quality, execution fidelity and result; decide what to hold, scale, stop, reverse or investigate.

**Exit:** learning that changes perception, criterion, action or control. **Stop:** without a prior snapshot, label the review exploratory and prohibit strong expectation-accuracy or effect claims. **Risk:** institutionalizing noise and defensive forecasting under punitive culture. **Alternative:** causal evaluation, independent audit or aggregation across cycles. **PULSE:** Learn, Value Must Be Observable, Decision Measurement Record.

## What would validate or refute the catalog

The conclusion changes if longitudinal use shows no improvement in completeness, traceability or action fidelity; materially higher latency without lower error; gaming, conformity pressure or improper delegation; missing decision classes; or better performance as non-conversational rules, forms or workflows. Until then the catalog remains `candidate-synthesis`.
