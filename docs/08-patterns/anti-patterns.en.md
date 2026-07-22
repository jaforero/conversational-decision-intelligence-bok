---
title: Anti-pattern catalog
description: Six candidate anti-patterns for decorative conversation, semantic drift, artificial certainty, undue authority, misleading adoption metrics and retrospective learning.
status: candidate
version: 0.8.0-rc.1
artifact_type: anti-pattern-catalog
authority_level: candidate-synthesis-and-guidance
normative: false
owner: Javier Forero
domains: [Decision Anti-patterns, Conversational Decision Intelligence, Responsible AI]
source_ids: [SRC-PULSE-DNA-001, SRC-ARCH-001, SRC-ACADEMIC-OUTCOME-BIAS-001, SRC-NIST-AIRMF-001]
claim_ids: [CLAIM-CDP-CATALOG-001]
last_reviewed: 2026-07-21
---

# Anti-pattern catalog

These are **candidate diagnoses**, not universal causal relationships. One symptom does not prove harm; inspect context, frequency, stakes and consequences.

## ANTI-CDI-001 — Dashboard disguised as conversation

A chat is added to existing metrics without decision, owner, alternatives, action or horizon. It feels useful because it reduces clicks; it risks confusing information access with decision support. Detect it when no one can state what choice changed or who acts. Repair with `CDP-001`, or call it Conversational Analytics and assess accuracy and information utility. Better alerts or navigation may be simpler.

## ANTI-CDI-002 — Conversation without semantics or provenance

Figures arrive without definition, population, filters, cutoff, source or verifiable permission. Fast natural answers may hide incompatible denominators. Detect unreconcilable values for the same question. Repair with `CDP-002`, a minimum semantic layer and visible scope. A controlled report may be superior for regulated definitions.

## ANTI-CDI-003 — Fluent certainty

Inference, forecast or recommendation is expressed as fact; ranges and unknowns disappear. Persuasiveness is rewarded over calibration. Detect missing counterevidence and change conditions. Separate claim classes, expose material uncertainty and use `CDP-002` plus `CDP-003`. Abstain or seek expert review when safe recommendation is impossible.

## ANTI-CDI-004 — Authority without rights

An AI recommendation becomes a decision, or an agent executes because a user “agreed,” without explicit approval, bounds or escalation. Detect inability to distinguish recommender, decider, approver and executor. Apply `CDP-004`, least privilege and positive confirmation. Deterministic workflow with segregation and rollback may be safer.

## ANTI-CDI-005 — Adoption as impact

Sessions, questions, active users, recommendation acceptance or time reduction are reported as evidence of better decisions. These are early attributable product measures, but can optimize engagement while outcomes or risks worsen. Detect absence of decision baseline, action fidelity, outcome and guardrails. Keep adoption as use and connect it to the Measurement System; prefer a comparative pilot.

## ANTI-CDI-006 — Reconstructed expectation

After outcome, the team redefines what it “really expected,” options it “always considered” or goals it “intended.” A coherent story protects reputation but prevents calibration and confuses decision with outcome. Detect absent prior snapshots or changing history. Apply `CDP-005`, preserve snapshots and label no-preregistration reviews exploratory. Independent review or cycle aggregation may be superior.

## Second-order control

The catalog itself becomes an anti-pattern if used as a universal checklist, labels replace causal analysis, people rather than behaviors are classified, detection triggers punishment without human review, or compliance displaces outcomes and learning. Treat each entry as a diagnostic hypothesis: seek supporting and opposing evidence, record uncertainty and test a reversible intervention.
