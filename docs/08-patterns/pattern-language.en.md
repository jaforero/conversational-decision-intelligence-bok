---
title: Pattern language and template
description: Anatomy, maturity states, selection criteria and controlled template for conversational decision patterns and anti-patterns.
status: candidate
version: 0.8.0-rc.1
artifact_type: candidate-standard
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains: [Decision Patterns, Decision Anti-patterns, Decision Governance]
source_ids: [SRC-PULSE-DNA-001, SRC-PULSE-MAP-001, SRC-ARCH-001]
claim_ids: [CLAIM-CDP-CATALOG-001, CLAIM-CDP-SELECTION-001]
last_reviewed: 2026-07-21
---

# Pattern language and template

## Candidate definitions

> A **conversational decision pattern** is a reusable structure of moves, roles, evidence, controls and outputs for a recurring problem within a decision-oriented conversation.

> A **conversational decision anti-pattern** is a recurring recognizable behavior that appears useful in the short term but tends to weaken decision, action, control or learning under stated conditions.

These candidate institutional definitions do not replace future PULSE documents `06_PULSE_Decision_Patterns.md` and `05_PULSE_Pattern_Library.md`. This language must align if those assets are approved.

## What counts as a pattern

A standalone practice such as “cite the source” is insufficient. An entry needs recurring context and decision; observable problem; forces and trade-offs; provider-independent moves; roles and decision rights; required evidence, uncertainty and abstention; auditable output linked to action or learning; consequences, risks and contraindications; distinct process and outcome measures; provenance and maturity. Reuse preserves logic across contexts, not one exact prompt.

## Controlled anatomy

| Field | Required question |
|---|---|
| ID, name, type and status | How is it identified and what maturity does it have? |
| Decision moment | Does it frame, ground, deliberate, commit or learn? |
| Context, problem and forces | When does it appear, what friction exists and why is it nontrivial? |
| Preconditions and moves | What must exist and what turns or checks occur? |
| Rights and evidence | Who may ask, recommend, decide, execute and escalate; on what basis? |
| Stop conditions | When should it abstain, escalate or change interface? |
| Consequences and measurement | What improves, what risks arise and how are process, outcome and guardrails assessed? |
| Alternatives and provenance | What simpler or safer mechanism may be better, and what is the evidence class? |

## Move contract

- **Entry:** exposes the decision or starting state.
- **Challenge:** seeks omissions, counterevidence, alternatives or definition conflicts.
- **Commitment:** records a choice, abstention or escalation under explicit rights.
- **Exit:** produces a verifiable artifact or state.

Not every pattern reaches commitment. Evidence Boundary correctly ends when data is unfit for use.

## Maturity states

| State | Minimum evidence | Permitted use |
|---|---|---|
| `candidate-synthesis` | Authorized-source coherence and editorial review | Learning, design and controlled testing |
| `tested-in-context` | Documented execution, result and limits in one context | Conditional reuse, no generalization |
| `approved-guidance` | Owner ratification and sufficient accumulated evidence | Institutional guidance within scope |
| `deprecated` | Superior alternative or unacceptable risk | History and migration only |

Use count and satisfaction do not by themselves raise maturity.

## Selection rule

Prefer the **minimum sufficient** pattern that resolves the blocker, keeps risk-proportional human control, preserves evidence and rights, changes decision/action/learning, and costs less than the error or delay it seeks to prevent.

Formalization can create bureaucracy, inhibit tacit knowledge and slow expert decisions. Therefore satisfied moves may be omitted, reversible choices may use minimal records, and rules, reports or expert review may replace conversation.

## Machine-readable template

[Download YAML template](/assets/data/conversational-decision-pattern.yml){ .md-button .md-button--primary }

The template starts empty and a pattern cannot be published without contraindications, stop conditions and provenance. Controlled entries live in [`governance/registries/patterns.yml`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/governance/registries/patterns.yml).
