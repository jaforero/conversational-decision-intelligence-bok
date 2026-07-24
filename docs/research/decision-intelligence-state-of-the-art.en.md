---
title: Decision Intelligence state of the art
description: A traceable candidate assessment of the foundations, boundaries, evidence and gaps of Decision Intelligence and PULSE.
status: candidate
version: 0.9.0-rc.1
artifact_type: state-of-the-art
authority_level: bounded-evidence-synthesis
normative: false
owner: Javier Forero
domains: [Research, Decision Intelligence, Human-AI Collaboration]
claim_ids: [CLAIM-DI-MATURITY-001, CLAIM-DI-LAYERS-001, CLAIM-PULSE-SYNTHESIS-001, CLAIM-PULSE-BIOLOGICAL-LENSES-001, CLAIM-HUMAN-AI-EVIDENCE-001]
source_ids: [SRC-ACADEMIC-DECISION-ANALYSIS-001, SRC-OMG-DMN-001, SRC-NIST-AIRMF-001, SRC-ACADEMIC-INFOQUALITY-001, SRC-ACADEMIC-ORGLEARNING-001, SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-AIEVAL-001, SRC-ACADEMIC-RUDIN-001, SRC-PULSE-DNA-001, SRC-PULSE-IDENTITY-002, SRC-JF-005, SRC-ARCH-001]
as_of: 2026-07-24
last_reviewed: 2026-07-24
---

# Decision Intelligence state of the art

<span class="cdi-release">Candidate v0.9.0-rc.1 · Focused assessment, not a systematic review</span>

## Executive conclusion

Decision Intelligence (DI) is treated here as an **emerging integrative field
of practice**: it brings mature disciplines and practices together around the
full decision cycle, but the review does not support presenting it as a
consolidated scientific discipline with universally accepted boundaries,
methods and a corpus of its own.

This is a dated, falsifiable candidate assessment. Absence of evidence in this
corpus is not evidence that no such work exists.

## 1. What is DI and where does it come from?

DI shifts attention from producing information or models to designing,
executing and learning from decisions. Its lineage does not begin with one
technology:

| Layer | Contribution to DI | Boundary |
|---|---|---|
| Decision theory and analysis | Alternatives, uncertainty, preferences, value and process quality | Do not cover continuous operations or conversation by themselves |
| Operations research and DSS | Models, optimization and computational support | An optimum does not guarantee adoption, control or learning |
| Data and information quality | Fitness of evidence for use | Data quality is not decision quality |
| Modeling and automation | Explicit decisions, rules and reproducible execution | Automation does not resolve legitimacy, accountability or causality |
| Organizational learning | Feedback, exploration and exploitation | Recording decisions does not prove that an organization learns |
| Human–AI Interaction | Collaboration, deliberation and control design | Effects depend on task, interface, user and comparator |

## 2. How does it differ from adjacent fields?

| Field | Primary question | Relationship to DI |
|---|---|---|
| Business Intelligence | What happened and how can it be observed? | Provides visibility; DI connects evidence to decision and action |
| Analytics and Data Science | What pattern, forecast or effect can be estimated? | Provide models; DI adds authority, alternatives, guardrails and follow-through |
| Decision Analysis | How should a decision under uncertainty be structured? | A direct foundation, not a predecessor that DI replaces |
| Decision Support Systems | How can systems support a decision? | Provides a sociotechnical and operational tradition |
| EDM and DMN | How can repeatable decisions be modeled, managed and automated? | Mature evolving practices in the map, not synonyms for DI |
| Conversational Analytics | How can data be explored with natural language? | Conversation is an interface; it does not guarantee a governed decision |
| AI agents | What tasks can a system plan or execute? | Agency increases the need for rights, stop conditions and traceability |

## 3. What is established?

“Established” does not mean infallible or universal. It means that the component
has its own lineage and verifiable primary or official sources:

- decision analysis and structuring under uncertainty;
- operations research and decision support systems;
- use-dependent data and information quality;
- outcome bias and separation of process from result;
- scoring rules for repeated probabilistic forecasts;
- decision modeling through the formal DMN specification;
- AI risk management through public frameworks such as NIST AI RMF;
- organizational learning as a feedback and adaptation problem.

## 4. What remains emerging or contested?

- what boundary separates DI from a well-governed integration of existing
  disciplines;
- when conversational interfaces improve deliberation or merely increase
  fluency and confidence;
- how to compare human, human+AI and AI alone without mistaking acceptance for
  quality;
- what meaningful human control means when an agent can act;
- how to measure outcome contribution without attributing causality to the
  interface;
- whether DI has its own cumulative corpus and under which criteria.

The human–AI evidence reviewed is context-dependent. An exploratory
deliberation study does not authorize a universal effect; an evaluation in
another domain may find no improvement. In high-stakes decisions, model
interpretability may be a preferable design property to a post-hoc explanation
of a black box.

## 5. What does PULSE integrate?

PULSE organizes its own synthesis around:

- **PDAMR:** Priority, Decision, Action, Metric and Risk;
- **Decision Circle:** reality, decision, action, result and learning;
- **five verbs:** frame, understand, decide, act and learn;
- **Human-in-Control:** explicit authority, escalation and accountability;
- **Decision Experience:** evidence and context turned into an action-oriented
  experience.

Constitutional sources govern this identity. The author's texts explain its
lineage and purpose. Neither source type proves by itself that PULSE produces
better outcomes than an alternative.

## 6. What has not been validated?

It has not been established that:

- CDI is a mature scientific discipline or that the project coined the term;
- PULSE is superior, universal or causally effective;
- the L0–L7 architecture is approved doctrine;
- interoception, allostasis or a “decision organism” are literal organizational
  mechanisms;
- five levels of analytics form a universal maturity scale;
- conversation, copilots or agents always improve a decision;
- the B2B case represents an executed intervention or attributable outcome.

## 7. What evidence would change the conclusion?

Claim strength should increase or decrease in response to:

1. a reproducible systematic review of the DI corpus;
2. multi-context comparisons of human, human+AI and AI alone;
3. published replications and null or adverse results;
4. preregistered PULSE pilots with baseline, comparator, guardrails and
   follow-up;
5. external evidence about the validity, usefulness and cost of its artifacts;
6. new official versions of registered standards and frameworks;
7. independent academic and professional review of the map.

<div class="cdi-risk" markdown>
**Decision boundary:** this map supports decisions about what to investigate and
how to communicate precisely. It does not authorize saying that CDI or PULSE
has already been scientifically validated.
</div>

## Selected primary sources

- [Decision Analysis: Practice and Promise](https://doi.org/10.1287/mnsc.34.6.679)
- [OMG Decision Model and Notation 1.5](https://www.omg.org/spec/DMN/1.5/About-DMN)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Human–AI deliberation, CHI 2025](https://doi.org/10.1145/3706598.3713423)
- [Evaluation of human, human+AI and AI alone](https://arxiv.org/abs/2403.12108)
- [Interpretable models for high-stakes decisions](https://doi.org/10.1038/s42256-019-0048-x)

Continue with the [PULSE evidence map](pulse-evidence-map.md) or the
[research agenda](research-agenda.md).
