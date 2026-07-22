---
title: Decision Brief template
description: One-page template integrating decision, evidence, experience, control, action and learning before action.
status: candidate
version: 0.7.0-rc.1
artifact_type: practice-template
authority_level: guidance-derived-from-pulse
normative: false
owner: Javier Forero
domains: [Decision Intelligence, Decision Governance, Decision Metrics]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001]
claim_ids: [CLAIM-PULSE-ROLE-001]
last_reviewed: 2026-07-21
---

# Decision Brief template

The **Decision Brief** condenses the decision contract before action. It does not replace detailed analysis; it reveals what remains implicit, ungoverned or insufficiently supported.

## Completeness criterion

Another person should be able to identify what is decided, why and by when; authority and affected groups; alternatives; supporting and weakening evidence; subsequent action; AI permissions and human control; expected result; and what would change the conclusion—without reconstructing private conversations.

## Copyable template

```markdown
Decision Brief — [decision name]

## 1. Priority
- Material priority:
- Baseline:
- Horizon:
- Consequence of no action:

## 2. Decision
- Decision sentence:
- Owner and deadline:
- Affected people or groups:
- Alternatives, including no action:
- Criteria and weights if applicable:
- Constraints:
- Cost of error / delay:
- Reversibility:

## 3. Evidence & context
- Observed facts / calculations / inferences / hypotheses:
- Material unknowns:
- Provenance and quality:
- Operational context:
- Uncertainty and counterevidence:
- Information that would change the choice:

## 4. Decision Experience
- User and moment of use:
- Signal requiring attention:
- Explanation and scenarios:
- Option comparison:
- Selected interface and rationale:
- Connected decision, action and feedback:

## 5. Human–AI control
- Permitted AI role, data and tools:
- Who proposes / decides / approves / executes:
- Escalation and stop conditions:
- Reversal and required trace:
- Accountability owner:

## 6. Action, metric & learning
- Chosen option and concrete action:
- Lower / central / upper expectation:
- Process metric / outcome / guardrails:
- Comparison or counterfactual:
- Review date:
- Hold / scale / stop / reverse rule:

## 7. Challenge record
- Weakest assumption:
- Strongest counterargument:
- First- and second-order risks:
- Potentially superior alternative:
- Confidence: high / medium / low
- Signatures or approvals:
```

## Ten-question review

1. Is there a real choice rather than a topic?
2. Can the owner commit action?
3. Do alternatives contain material trade-offs?
4. Is evidence classified and bounded?
5. Could uncertainty change the preferred option?
6. Does the experience end in assigned action?
7. Are AI permissions minimal and observable?
8. Was expectation recorded before outcome?
9. Are outcome and causality separated?
10. Is the learning review agreed?

## Recommended use

Complete the brief without AI first to expose your mental model. Then use conversation to challenge assumptions, generate alternatives or detect missing fields. Do not delegate authority to define the priority, invent evidence or approve the system's own actions.

[Return to learning path](index.md){ .md-button }
[Create the Measurement Record](../07-governance-quality/measurement-record.md){ .md-button }
