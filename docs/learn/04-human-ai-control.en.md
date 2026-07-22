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
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001]
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

## Stress test and deliverable

Ask whether approval is informed or habitual; whether many small actions can accumulate major harm; who detects context shift or degradation; what happens if the owner is unavailable; whether evidence and version can be reconstructed; and whether affected groups can appeal or correct. Complete one row per action. If **stop**, **reverse** and **answer** cannot be assigned, automation is not ready.

**Next:** [connect action, result and learning →](05-action-learning.md)
