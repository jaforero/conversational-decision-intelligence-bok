---
title: 2. Ground in evidence and context
description: Assess whether evidence fits the decision and separate facts, inferences, hypotheses and unknowns.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains: [Decision Intelligence, Foundations, Data Storytelling]
source_ids: [SRC-PULSE-DNA-001, SRC-JF-005, SRC-ARCH-001]
claim_ids: [CLAIM-PULSE-001]
last_reviewed: 2026-07-21
---

# 2. Ground in evidence and context

**Module outcome:** a contract stating what evidence the decision needs, its reliability, what it cannot establish and what information would change the choice.

## Data is not reality

Data is recorded evidence about part of reality. It may be accurate but irrelevant, timely but wrongly defined, or associative without establishing causality. Ask: **Is it trustworthy and relevant enough for this decision, horizon and cost of error?**

## Six labels that prevent reasoning drift

| Label | Example | Required discipline |
|---|---|---|
| **Observed fact** | “420 applications were recorded.” | Source, period, population, definition |
| **Calculation** | “The rate was 12.4%.” | Formula, numerator, denominator, missingness |
| **Inference** | “The decline appears concentrated in one segment.” | Method, uncertainty, alternatives |
| **Hypothesis** | “Shorter response time might improve retention.” | Plausible mechanism and future test |
| **Recommendation** | “Prioritize segment A.” | Criteria, trade-offs, risk, authority |
| **Unknown** | “We do not know whether customer mix changed.” | Decision impact and gap-reduction plan |

The error occurs when a correlation becomes cause, a hypothesis becomes recommendation, or an AI recommendation becomes fact without notice.

## Evidence contract

For every material signal document: **provenance**, **definition**, **quality**, **population**, **context**, **uncertainty**, **fitness for purpose**, **counterevidence**, and **change condition**—the information that would change conclusion or action.

## Context outside the table

Context includes operational history, local definitions, incentives, capacity constraints, prior choices, exceptions and power. Capture provenance: “the team said so” is neither an approved rule nor quantitative evidence. Separate stable context, temporary context, local knowledge, and interests or incentives.

## When to stop a conclusion

Do not advance to recommendation when a material denominator cannot be reconstructed; definitions changed unadjusted; affected segments are missing; a model is out of population; causal explanation rests only on timing; sensitive data lacks legitimate permission or purpose; or uncertainty changes option ordering. Stopping a conclusion need not stop the decision—it may require a smaller, more reversible option or guardrail.

## Stress test

- What is the strongest counterargument?
- Which conclusion depends on one assumption?
- Could the pattern arise without the proposed mechanism?
- What group, period or outcome is invisible?
- Does the source define the concept or only report an observation?
- What uncertainty makes options indistinguishable?

## Deliverable

Build one row per material item using the nine contract fields. End with three lists: **we know**, **we infer**, **we do not yet know**.

**Next:** [design the experience connecting evidence to action →](03-decision-experience.md)
