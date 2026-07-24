---
title: CDI scope and boundaries
description: Official project definition of Conversational Decision Intelligence, adjacent fields and inclusion and exclusion criteria.
status: approved
version: 0.4.0
artifact_type: scope-standard
authority_level: institutional-approved
normative: true
owner: Javier Forero
domains: [Conversational Decision Intelligence, Decision Intelligence, Conversational Analytics, Responsible AI]
source_ids: [SRC-PRIOR-CDI-001, SRC-PRIOR-CDI-002, SRC-ACADEMIC-HAI-001, SRC-ACADEMIC-AIEVAL-001]
claim_ids: [CLAIM-CDI-001, CLAIM-CDI-PRIOR-001, CLAIM-CDI-EFFECT-001]
last_reviewed: 2026-07-21
---

# CDI scope and boundaries

## Official project definition

> **Conversational Decision Intelligence (CDI) is the proposed interdisciplinary domain of practice that studies and designs how people and artificial intelligence systems collaborate through conversations to turn trustworthy evidence and context into explicit decisions, responsible action and measurable learning.**

This is the **official project definition from `v0.4.0`**, not a universally accepted definition. CDI is presented as an emerging domain of practice while comparative review, applied evidence and external evaluation develop.

## What makes CDI specific

A core CDI experience integrates five conditions:

1. **Iterative conversation:** supports questions, clarification, challenge, depth and revision—not only commands.
2. **Explicit decision object:** identifies decision, owner, alternatives, criteria, constraints and cost of error or delay.
3. **Evidence contract:** connects answers to data, definitions, scope, provenance, uncertainty and permissions.
4. **Governed transition to action:** separates explanation, recommendation, decision and execution; preserves decision rights and escalation.
5. **Learning loop:** records expectation, result, deviation and next-cycle adjustment.

Without a decision object, the experience is usually Conversational Analytics or information assistance. Without conversation, it may be Decision Intelligence but not CDI. Without evidence and governance, it is a fluent interface, not a trustworthy decision experience.

## Boundary matrix

| Field or artifact | Primary unit | Conversation | Explicit decision | Action and learning | Relationship to CDI |
|---|---|---:|---:|---:|---|
| **Business Intelligence** | Metric or indicator | Optional | Not necessarily | Limited | Supplies evidence and monitoring |
| **Conversational AI** | Language interaction or task | Yes | Not necessarily | Optional | Supplies dialogue capabilities |
| **Conversational Analytics** | Question about data | Yes | May be implicit | Not necessarily | Analytical interface within or outside CDI |
| **Decision Support System** | Semi-structured problem | Optional | Yes | Variable | Important functional predecessor |
| **Decision Intelligence** | Decision system | Optional | Yes | Yes | Integrating field from which CDI takes decision orientation |
| **Human–AI deliberation** | Disagreement, reasons and revision | Yes | Yes | Design-dependent | Supplies evidence and collaboration patterns |
| **CDI** | Conversation around a decision | Required | Required | Required and governed | Integrates prior capabilities under one contract |
| **PULSE** | Health and cycle of a decision | Optional | Yes | Yes | Ecosystem framework of practice, not a CDI synonym |

## In scope

- conversational exploration of evidence for an identifiable decision;
- clarification of questions, metrics, entities, periods and constraints;
- comparison of alternatives, scenarios, trade-offs and reversibility;
- Human–AI deliberation exposing disagreement and reasons;
- evidence synthesis with uncertainty and provenance;
- copilots supporting preparation, recommendation or workflow under human control;
- bounded, observable and preferably reversible agents proportional to risk;
- measurement of process quality, outcome, appropriate trust and learning.

## Outside the core

- service chatbots without an explicit organizational decision;
- text-to-SQL or conversational search disconnected from options, owner or action;
- dashboards that only add a question box;
- automatic narratives without traceability or claim control;
- recommenders hiding criteria, uncertainty or conflicts;
- open-goal agents with undefined authority;
- irreversible or rights-affecting automation without legitimate human authority;
- systems judged only by use, fluency, engagement or answer volume.

## Prior art and calibrated originality

**Conversational Decision Intelligence** had public uses before this CDI-BoK: a 2022 conversational inference platform and a 2025 decision-oriented dialogue category. Therefore the project does **not** claim to have coined the expression. Terminological overlap does not prove conceptual equivalence. The candidate contribution lies in the integrated decision, evidence, action, governance and learning contract and its connection to PULSE. Novelty claims require explicit comparison with academic, industry and practice antecedents.

## Central hypothesis and test

**Candidate hypothesis:** for a specific decision and context, a governed conversational experience may reduce friction or latency and improve understanding, exploration or process quality without reducing accuracy, control, equity or accountability.

One correct response does not confirm it. Testing requires a relevant comparison—human alone, dashboard, analyst-mediated workflow or non-conversational system—and separation of model performance, human performance, Human–AI team performance, process quality, decision outcome, and introduced cost and risk. Existing findings are heterogeneous; the proper conclusion is conditional, not universal.

## Open questions

- When does conversation improve reasoning, and when does it only increase persuasion or overconfidence?
- What mix of visualization and dialogue best serves each decision?
- How should decision quality be measured separately from luck and outcome?
- How can tacit context, disagreement and organizational power be preserved?
- Which decisions should remain simple, non-conversational or unautomated?
- What makes delegation real rather than nominal supervision?
- What evidence would support moving CDI from proposed domain to recognized discipline?

## Direct references

- Martin Schoeman, [“Conversational Decision Intelligence (CDI) Strategy Begins in Conversation”](https://medium.com/@mschoeman3/conversational-decision-intelligence-cdi-strategy-begins-in-conversation-0f2d1fc50381), 2025.
- Akeel Attar, [“Turbo charge your Conversational AI with Conversational Decision Intelligence”](https://www.linkedin.com/pulse/turbo-charge-your-conversational-ai-decision-akeel-attar), 2022.
- Ma et al., [“Towards Human-AI Deliberation”](https://doi.org/10.1145/3706598.3713423), CHI 2025.
- Ben-Michael et al., [“Does AI help humans make better decisions?”](https://arxiv.org/abs/2403.12108), 2024.
