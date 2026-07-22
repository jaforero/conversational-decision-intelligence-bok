---
title: Decision Measurement System
description: Candidate six-lens architecture for measuring priority, quality, execution, time, risk and learning around an explicit decision.
status: candidate
version: 0.7.0-rc.1
artifact_type: candidate-framework
authority_level: candidate-synthesis
normative: false
owner: Javier Forero
domains: [Decision Metrics, Decision Quality, Responsible AI]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001, SRC-ACADEMIC-SCORING-RULES-001, SRC-NIST-AIRMF-001]
claim_ids: [CLAIM-DM-SYSTEM-001, CLAIM-DM-CALIBRATION-001, CLAIM-DQ-PROFILE-001]
last_reviewed: 2026-07-21
---

# Decision Measurement System

The **Decision Measurement System** is a CDI-BoK candidate synthesis for instrumenting a decision from baseline through review. It makes the cycle observable without reducing it to adoption, speed or isolated ROI.

## Six lenses

| Lens | Observes | Examples | When |
|---|---|---|---|
| **1. Priority and outcome** | Material change justifying the decision | revenue, cost, service, error, retention | Before and after |
| **2. Ex-ante quality** | Process integrity before outcome | dimension profile, blockers, independent review | Before |
| **3. Action and execution** | Whether decision became authorized behavior | start, completion, fidelity, relevant adoption | During |
| **4. Time and friction** | Whether perception, decision and action were timely | decision/action/escalation latency | During |
| **5. Risk and guardrails** | Costs, harm and limits | incidents, equity, load, quality, privacy, reversal | During and after |
| **6. Calibration and learning** | Expectation–result fit and later change | forecast error, revised hypotheses, review closure | After and between cycles |

No lens substitutes for another. Fast action may be wrong; a positive outcome may hide harm; a complete process may create no value.

## Metric contract

Do not add a metric without name and definition; decision use; unit, population and denominator; baseline and expected range; source and owner; cadence and horizon; required segmentation; guardrail; attribution limit; and response rule for hold, scale, stop, reverse or investigate.

## Conditional metrics

### Latency

\[
L_{decision}=t_{commitment}-t_{eligible\ signal}
\]

\[
L_{action}=t_{first\ action}-t_{commitment}
\]

Record signal, evidence availability, commitment and action separately. Lower latency is improvement only if quality, rights and risk do not deteriorate.

### Execution fidelity

\[
F=\frac{\text{eligible actions executed under protocol}}{\text{eligible actions planned}}
\]

The denominator needs prior rules and explicit exceptions. Unequal action importance may require components or preregistered weights.

### Learning closure

\[
C=\frac{\text{due cycles with documented review and change or confirmation}}{\text{cycles whose horizon closed}}
\]

A “lesson” is insufficient unless what changed or remained and why are recorded.

### Probabilistic calibration

For repeated comparable binary events:

\[
BS=\frac{1}{N}\sum_{i=1}^{N}(p_i-y_i)^2
\]

Lower Brier score is better. Do not use it for one decision, post-hoc redefined events, incomparable probabilities or samples too small for calibration inference. Preserve resolution, baseline and segment analysis.

## Human–AI collaboration

Measure the sociotechnical system, not only the model. Override requires reason, context, result and evidence that control worked; lower is not always better. Agreement is diagnostic alongside accuracy and difficulty, not a trust proxy. Correct escalation should not be penalized. Incidents and near misses need severity, population, response and learning. Recommendation use shows workflow integration, not impact or correctness.

NIST AI RMF reinforces context-specific measures, documented limits, performance, risk, feedback and monitoring. It governs the AI component; it does not turn this CDI system into a NIST standard.

## Minimum viable set

For low- or medium-risk decisions begin with one priority-linked outcome, one execution-fidelity signal, one material guardrail, one expected range and horizon, one review date and owner, and any ex-ante blocker. Add measures only when they change a decision, control or learning question.

## Anti-metrics

Avoid decision count, speed without quality or risk, adoption or query volume, ROI without baseline and attribution, isolated override rate, and universal synthetic scores. They reward volume, confuse use with consequence or let irrelevant strengths compensate for blockers.

## Portfolio aggregation and counterargument

Aggregate only comparable definitions, horizons, stakes and populations; show distributions and segments before means. Rare critical decisions require case review. Six-lens instrumentation can cost more than the decision's value and become ritual. The answer is proportionality and a minimum set. Longitudinal real-decision data could test reliability, context sensitivity, gaming and outcome relation—and simplify or replace this candidate.

[Create a Measurement Record →](measurement-record.md){ .md-button .md-button--primary }
