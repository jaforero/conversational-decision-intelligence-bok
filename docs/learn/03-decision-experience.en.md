---
title: 3. Design the Decision Experience
description: Select the interface and structure the experience around attention, understanding, options, decision, action and feedback.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains: [Decision Architectures, Decision Narratives, Conversational Analytics]
source_ids: [SRC-PULSE-DNA-001, SRC-JF-002, SRC-ARCH-001]
claim_ids: [CLAIM-PULSE-ROLE-001, CLAIM-CDI-EFFECT-001]
last_reviewed: 2026-07-21
---

# 3. Design the Decision Experience

**Module outcome:** a blueprint connecting user, evidence, uncertainty, alternatives, decision, action, risk and feedback through the least complex interface that solves the need.

## The design unit is the decision

A correct dashboard may change nothing. A fluent conversation may create false confidence. Define user and context, decision and owner, subsequent action, required evidence, visible uncertainty, risks and permissions, outcome metric and learning feedback before drawing screens.

## Select the interface

| Dominant need | Initial interface | Frequent risk |
|---|---|---|
| Controlled repeatable facts | **Report** | Information without a decision |
| Monitoring and detection | **Dashboard** | KPI excess and no actionable thresholds |
| Executive interpretation | **Narrative** | Hidden counterevidence or causal overclaim |
| Question exploration | **Conversation** | Fluency without semantics, source or limits |
| Synthesis and preparation | **Copilot** | Criteria-free recommendations or diffuse accountability |
| Action coordination | **Workflow** | Automating an ill-defined process |
| Bounded execution | **Agent** | Excess authority and weak stop conditions |

There is no required progression toward agents. A brief report may be superior for a stable, low-ambiguity decision.

## Sequence the experience

1. **Attention:** what needs attention now?
2. **Importance:** why and for whom?
3. **Change:** what moved against baseline, target or expectation?
4. **Explanation:** what is known, inferred and unknown?
5. **Future:** what scenarios are plausible under what uncertainty?
6. **Options:** what alternatives and trade-offs exist?
7. **Decision and action:** who chooses, what follows and when?
8. **Risk:** what can fail, how is it stopped, who answers?
9. **Learning:** what result will be observed and how will the next cycle change?

Progressive disclosure may reduce load but must never hide a limitation that could change the choice.

## Structured conversation

Each material answer should expose metric definition and provenance; filters, population and period; calculation or method; uncertainty and assumptions; counterevidence; applied permissions; link to the decision; and authorized next action. Conversation is an interface over data, semantics, context and governance—not a source of truth.

## Minimum blueprint

| Layer | Question | Possible component |
|---|---|---|
| **Signal** | What changed? | Alert, headline, comparison |
| **Understanding** | Why might it matter? | Breakdown, narrative, conversation |
| **Criterion** | How do we compare options? | Matrix, scenarios, constraints |
| **Commitment** | Who decides what? | Decision Brief, approval, signature |
| **Action** | What happens next? | Workflow, task, rule, accountable actor |
| **Feedback** | What will we learn? | Outcome, guardrail, scheduled review |

## Stress test and deliverable

Ask whether the logic remains clear without AI, whether the interface supports choice rather than only exploration, whether attention can be captured by unimportant content, whether recommendations expose alternatives and change conditions, whether a safe exit exists, and whether feedback returns to the originating system. Draw the six layers and annotate content, actor, permission and risk before choosing components.

**Next:** [define human control and AI boundaries →](04-human-ai-control.md)
