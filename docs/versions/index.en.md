---
title: Versions
description: Normative releases, portal candidates and CDI-BoK history policy.
status: candidate
version: 0.8.1
artifact_type: version-index
authority_level: guidance
normative: false
owner: Javier Forero
domains: [Decision Governance]
last_reviewed: 2026-07-21
---

# Versions

## Current status

| Component | Version | Status | Scope |
|---|---|---|---|
| Bilingual portal | [`v0.8.1`](v0.8.1.md) | Editorially and technically stable | Complete ES/EN routes, localized interface and translation-drift gates |
| Source bilingual candidate | [`v0.8.1-rc.1`](v0.8.1-rc.1.md) | Ratified, merged, deployed and promoted | Traceable source of stable `v0.8.1` |
| CDI-BoK governance | `v0.2.0` | Approved and normative | Architecture, authority, claims, brand and Sprint 0 |
| Technical portal | `v0.3.0-rc.1` | Integrated and deployed | MkDocs, navigation, CI/CD, checks and custom domain |
| Foundational core | [`v0.4.0`](v0.4.0.md) | Stable | Constitution, CDI boundaries, glossary, domains and PULSE specification |
| Practice and evidence | [`v0.5.0-rc.1`](v0.5.0-rc.1.md) | Deployed candidate, not ratified | Catalog and first instrumented B2B case, without observed outcome |
| Learning experience | [`v0.6.0-rc.1`](v0.6.0-rc.1.md) | Ratified and deployed candidate | Outcome-oriented home, five modules and Decision Brief |
| Quality and measurement | [`v0.7.0-rc.1`](v0.7.0-rc.1.md) | Ratified and deployed candidate | Decision Quality, six lenses, anti-metrics and Measurement Record |
| Conversational patterns | [`v0.8.0-rc.1`](v0.8.0-rc.1.md) | Ratified, merged and deployed candidate | Five patterns, six anti-patterns, language, template and stopped B2B demonstration |
| Stable portal baseline | [`v0.8.0`](v0.8.0.md) | Editorially and technically stable | Reproducible build, navigation, traceability, gates and authority boundaries |

The portal version does not automatically raise the doctrinal maturity of its content. Infrastructure, knowledge and evidence may evolve at different rates, but must remain traceable.

## Current policy

- Stable releases require an immutable tag and GitHub Release.
- Candidates are traced through notes, changelog, manifest, PR, merge SHA, validation and deployment. They receive a tag only when the owner explicitly authorizes freezing them as an immutable prerelease.
- Ratification, deployment and stability are different states.
- `decision.javierforero.co` displays the latest merged public build; the portal version does not raise every document's authority or evidence strength.
- Drafts do not appear in stable navigation.
- Spanish is canonical during `0.x`; English translations are versioned and linked through a controlled parity registry.

ADR-022 replaces ADR-005's initial rule and avoids ambiguous retrospective tags. `governance/releases/index.yml` preserves the complete lineage. Historical RCs remain intentionally untagged.

!!! note "Why there is no later v0.1.0"
    The initial roadmap named Sprint 2 as `v0.1.0`, but the sequence had already published `v0.2.0` and `v0.3.0-rc.1`. ADR-014 assigned `v0.4.0-rc.1`; ADR-017 records its ratification and stable promotion to `v0.4.0`.

## History

See [`CHANGELOG.md`](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/CHANGELOG.md) and the [repository releases](https://github.com/jaforero/conversational-decision-intelligence-bok/releases).
