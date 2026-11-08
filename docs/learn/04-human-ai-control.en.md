---
title: 4. Govern Human–AI collaboration
description: Define decision rights, automation levels, permissions, stop conditions and human accountability.
status: candidate
version: 0.6.0-rc.1
artifact_type: learning-module
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains: [Responsible AI, Decision Governance, Decision Agents]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001, SRC-JF-BLOG-2942]
claim_ids: [CLAIM-CDI-EFFECT-001]
last_reviewed: 2026-07-21
---

# 4. Govern Human–AI collaboration

**Module outcome:** a matrix defining what every actor may do, what requires approval, when escalation occurs and who answers for consequences.

## Human-in-Control, not decorative approval

Putting a person at the end does not guarantee control. Humans retain control when they can define purpose, criteria, limits, permissions, override, escalation and consequences—and have the time, information and authority to exercise them.

## Decision rights

Assign explicitly: **see**, **ask**, **propose**, **recommend**, **decide**, **approve**, **execute**, **stop**, **audit** and **answer**. An AI system may receive some permissions; good execution does not grant moral legitimacy or final accountability.

## Delegation scale

| Level | AI role | Minimum condition |
|---|---|---|
| **1. Inform** | Retrieve and summarize evidence | Visible sources, permissions and limits |
| **2. Explore** | Answer questions and generate scenarios | Shared semantics and traceability |
| **3. Recommend** | Compare alternatives | Criteria, uncertainty and counterarguments |
| **4. Prepare action** | Draft or configure execution | Effective human review and reversibility |
| **5. Bounded execution** | Act within a limit | Least privilege, observability, stop conditions and rollback |

The level is not general maturity. A mature organization may keep critical decisions at level 2 or 3.

## Increase control when

rights, safety, employment, credit, health or access are affected; irreversibility, scale or speed increase; data becomes sensitive; mechanism becomes opaque; uncertainty or context shifts; or harm becomes hard to detect and repair.

## Control matrix

```text
Action:
Proposing actor:
Deciding actor:
Approving actor:
Executing actor or system:
Permitted data:
Scope limit:
Escalation condition:
Stop condition:
Reversal mechanism:
Required trace:
Accountability owner:
```

## Applied case · Specifying what to delegate { #delegation-brief }

**Practice decision.** The operations owner must decide how to handle recurring incidents. A bounded assignment lets the team compare three options: apply a rule, use AI to prepare a human review, or authorize an agent to take a reversible action within explicit limits.

| Part of the assignment | Example for the incident log |
|---|---|
| **Context** | Consult the ticket, the current catalog and authorized prior incidents. |
| **Criteria** | Apply explicit rules for known incident types. Escalate ambiguous or high-impact cases. |
| **Tools and permissions** | May draft a classification or add an internal tag that can be removed. The responsible person authorizes any closure or external communication. |
| **Trigger** | A new in-scope ticket starts the workflow. Each event is processed once. |

**Exercise.** Record who can stop or reverse an action and what evidence remains for audit. Test a duplicate ticket, an out-of-scope ticket and one with embedded instructions that try to expand permissions. Compare with current operations using cost per incident accepted after review and the correction rate, including escalated cases. Start with a rule if it handles the expected cases within the agreed limits.

Philia Sophia reading (17 Oct 2026) · [An agent is more than its model: four parts of effective delegation](https://javierforero.co/2026/10/17/agentes-ia-delegar-con-criterio/).

## Stress test and deliverable

Ask whether approval is informed or habitual; whether many small actions can accumulate major harm; who detects context shift or degradation; what happens if the owner is unavailable; whether evidence and version can be reconstructed; and whether affected groups can appeal or correct. Complete one row per action. If **stop**, **reverse** and **answer** cannot be assigned, automation is not ready.

In [Thursday's Promise](ai-work-redesign.en.md), a service desk uses these rules to redesign its workflow, pilot an assistant, and decide whether to expand its scope.

**Next:** [connect action, result and learning →](05-action-learning.en.md)
