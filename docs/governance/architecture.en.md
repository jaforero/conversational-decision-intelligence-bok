---
id: CDI-GOV-001
title: CDI-BoK editorial architecture and governance
description: Normative architecture governing authority, knowledge, claims, brand, publishing and evolution of the CDI-BoK.
status: approved
version: 0.2.0
artifact_type: governance-standard
authority_level: foundational
normative: true
owner: Javier Forero
domains: [Foundations, Decision Governance]
last_reviewed: 2026-07-21
---

# CDI-BoK editorial architecture and governance

## 0. Status and authority rule

This is the normative root document for CDI-BoK architecture and editorial governance. It governs how the project separates institutional authority from empirical evidence, organizes knowledge, controls claims, applies the brand, publishes the portal and evolves versions. When a derived page conflicts with this document, the governed source or a later accepted ADR prevails.

### Changes incorporated in v0.2.0

`v0.2.0` consolidated the constitutional sources, authority hierarchy, controlled registries, brand system, publication architecture, accessibility contract, source/claim discipline and executable Sprint 0 controls.

## 1. Decision governed by this document

### Editorial PDAMR

| Element | Governance decision |
|---|---|
| **Priority** | Build credible, cumulative and challengeable knowledge about CDI and PULSE |
| **Decision** | Determine what may be published, with what authority, evidence, status and owner |
| **Action** | Accept, revise, reject, supersede or deprecate versioned assets |
| **Metric** | Traceability, integrity, build quality, source coverage, claim calibration and observed use |
| **Risk** | Inflated authority, duplicated concepts, fabricated evidence, brand inconsistency and uncontrolled publication |

### Governing decision

The CDI-BoK is maintained as a public, versioned knowledge system whose unit of control is the **knowledge asset**, not the page count or interface. Every material asset must expose ownership, authority, maturity, version, evidence and relationships.

## 2. Calibrated ecosystem identity

### 2.1 Conversational Decision Intelligence

CDI is the proposed interdisciplinary domain of practice studying and designing how people and AI systems collaborate through conversation to turn trustworthy evidence and context into explicit decisions, responsible action and measurable learning. “Proposed” is mandatory until external recognition and evidence justify a different status.

### 2.2 CDI-BoK

The CDI-BoK is the official public, governed and versioned knowledge system of this project. “Body of Knowledge” states the intended architecture; it does not claim international standard status.

### 2.3 PULSE

PULSE is a human-centered Decision Intelligence methodology and operating philosophy and the framework of practice for this ecosystem. Its constitutional meaning is controlled by `00_PULSE_DNA.md`, `00A_PULSE_Documentation_Map.md` and `00_PULSE_Identity.md`. CDI-BoK applies and projects PULSE but cannot silently redefine it.

### 2.4 Official portal and practice labs

`decision.javierforero.co` is the public knowledge portal. External dashboards and galleries are practice extensions. A link to a demo does not convert it into an evaluated case; admission requires status, evidence and lifecycle controls.

### 2.5 Brand architecture

The institutional balance is:

1. **Conversational Decision Intelligence** — proposed domain;
2. **CDI-BoK** — governed knowledge system;
3. **PULSE** — framework of practice;
4. **Javier Forero** — founder, author and accountable owner.

No layer should visually erase the others or imply that the portal itself validates the doctrine.

#### Institutional balance rule

The portal must make the subject, artifact, methodological relationship and authorship visible without turning every page into advertising. Brand authority lives in `brand/brand-source.yml`; derived tokens and components must remain reproducible.

### 2.6 Brand-system authority

Source order: brand source → token registry → generated CSS/JSON → components → page composition. Manual divergence from tokens is prohibited unless documented by ADR or reviewed exception.

### 2.7 Binding visual and editorial principles

- decision content before decoration;
- clear hierarchy and sufficient contrast;
- color with semantic purpose;
- mobile-first responsive behavior;
- explicit states, evidence and uncertainty;
- reusable components rather than page-specific improvisation;
- visible focus and keyboard operation;
- calibrated, plain language rather than unsubstantiated superlatives.

### 2.8 Minimum visual contract

Every public page must remain usable in light and dark themes, desktop and mobile, with heading hierarchy, readable measure, accessible focus, target sizes, link meaning and no horizontal overflow. Visual snapshots detect change; they do not prove usability or WCAG conformance.

### 2.9 Identity of knowledge components

Definitions, warnings, evidence, hypotheses, recommendations, patterns, cases and version records require visually distinguishable but consistent treatment. Decoration may not elevate a hypothesis to a fact or candidate guidance to normative authority.

### 2.10 Accessibility and MkDocs adaptation

The implementation uses Material for MkDocs with project overrides. Accessibility controls include semantic landmarks, keyboard navigation, contrast, target size, responsive tables, reduced ambiguity and automated Axe checks. Full WCAG 2.2 AA conformance requires deployed-release audit beyond automated scans.

## 3. Knowledge architecture

### 3.1 Four strata

| Stratum | Purpose | Typical authority |
|---|---|---|
| **Constitutional** | Identity, doctrine and non-negotiable boundaries | Highest within the owning system |
| **Normative** | Architecture, controlled definitions and binding rules | Ratified project authority |
| **Guidance** | Frameworks, patterns, learning and implementation advice | Approved or candidate, scope-bound |
| **Evidence and practice** | Research, cases, demonstrations and observations | Strength determined by design and provenance |

Authority and evidence are independent. Constitutional wording may have high project authority with no empirical-effect claim; external evidence may be strong without becoming project doctrine.

### 3.2 Knowledge areas and domains

Eight areas organize 29 domains: Foundations and Identity; Decisions and Intelligence; Conversations and Human–AI Collaboration; Data, Semantics and Knowledge; Narratives and Communication; Systems, Agents and Architectures; Governance, Quality and Responsibility; Adoption, Maturity and Evidence.

#### Domain rules

A domain owns a bounded intellectual question, not merely a navigation label. New domains require an unmet conceptual need, distinct ownership, dependencies, evidence plan and ADR. Navigation may group domains without changing conceptual ownership.

### 3.3 Asset types

Controlled asset types include constitution, standard, definition, framework, guide, pattern, anti-pattern, template, research note, source, claim, ADR, case study, demonstration, registry and release record. Type determines minimum metadata and review, not automatic authority.

### 3.4 Documentation map as duplication control

The documentation map identifies concept owners, dependencies and boundaries. Derived assets link to canonical definitions instead of creating near-synonyms. A duplicate definition must be removed, labeled as a quotation or governed as a deliberate translation.

## 4. Authority hierarchy

### 4.1 Order

1. Ratified CDI-BoK architecture and governance decisions.
2. PULSE constitutional DNA for PULSE-owned meaning.
3. PULSE Documentation Map for documentation governance.
4. PULSE Identity for official public identity.
5. Approved CDI-BoK foundational assets.
6. Approved derived standards and guidance.
7. Controlled evidence, cases and demonstrations within scope.
8. Historical, superseded or exploratory materials.
9. Assistant-generated proposals not adopted by the owner.

### 4.2 Conflict rule

Conflicts are resolved by conceptual ownership, authority, version and evidence class—not by recency or repetition alone. Evidence may challenge a doctrine and trigger review, but cannot silently rewrite it.

### 4.3 Incorporated constitutional sources

The repository preserves identifiable canonical PULSE files. Their content must not be replaced by summaries. Derived pages explicitly state that the constitutional source prevails.

## 5. Initial corpus audit

The initial corpus included Javier Forero's original points of view, PULSE constitutional and derived documents, AI-assisted research, analyst reports and demonstrations. It contained valuable material but uneven authority, incomplete provenance, repeated definitions and claims whose strength exceeded available evidence.

### Audit conclusion

The corpus was sufficient to establish a governed architecture and research agenda, but insufficient to claim academic originality, generalized effectiveness or standard status. The response was stronger metadata and claim discipline, not deletion of useful hypotheses.

## 6. Claims and evidence discipline

### 6.1 Claim classes

Minimum classes are project definition, empirical, causal, comparative, forecast, aspiration and original-contribution proposal. Pages must distinguish fact, calculation, inference, hypothesis, recommendation, metaphor and unknown.

### 6.2 Evidence strength

Evidence is assessed by source type, provenance, method, population, period, directness, uncertainty, consistency and fitness for purpose. AI synthesis is a discovery aid, not primary validation. Vendor or analyst forecasts remain forecasts.

### 6.3 Claim registry

Material claims receive an ID, owner, class, wording, scope, evidence links, counterevidence, status, review date and change condition. Registries are controlled metadata and must agree with public text.

### 6.4 Editorial prohibitions

The project must not present aspiration as evidence, metaphor as mechanism, internal repetition as validation, possibility as readiness, pilot as universal proof, branding as scientific originality, correlation as causality, or technological fluency as decision quality.

## 7. Original contributions

### 7.1 Contribution states

An idea may move from proposed contribution to comparative review, tested-in-context and approved contribution. “Original Contribution” without qualifier requires sufficient documented comparison and owner ratification.

### 7.2 Minimum requirements

State the problem, prior art, proposed difference, mechanism, scope, assumptions, strongest counterargument, risks, evidence, validation design, failure condition and evolution path. Authorship alone is not novelty evidence.

## 8. Editorial models by content type

### 8.1 Normative concept or standard

Requires conceptual owner, canonical definition, scope, requirements, prohibited interpretations, dependencies, impact analysis and ratification.

### 8.2 Framework

Requires purpose, components, sequence or relationships, entry and exit conditions, trade-offs, boundaries, evidence class and application example.

### 8.3 Research Note

Requires question, search scope, source-quality assessment, findings, disagreement, uncertainty, references and research implications. It must not imply systematic-review status unless the method supports it.

### 8.4 Pattern / Anti-pattern

Requires recurring context, observable problem, forces, moves, rights, evidence, stop conditions, consequences, measurement, alternatives, provenance and maturity.

### 8.5 Case Study

Requires real context, decision, owner, baseline, intervention, action, observed result, attribution limits, learning and consent/security controls. A simulation is not a case study.

### 8.6 Demonstration

A demonstration may prove interface or implementation capability. It must label simulated or synthetic data, state missing owners and outcomes, and avoid impact claims.

## 9. Required metadata

Public artifacts carry title, description, status, version, artifact type, authority level, normative flag, owner, domains and review date. Material assets add source and claim IDs. Controlled records must support machine validation.

## 10. Editorial governance

### 10.1 Roles

The owner ratifies constitutional and major normative changes. Authors draft; reviewers challenge evidence, structure, language, accessibility and implementation; maintainers preserve builds and registries; contributors follow `CONTRIBUTING.md`. AI may assist but cannot ratify or own accountability.

### 10.2 Decision rights

Only authorized humans may approve doctrine, release state, original-contribution status, exceptions, public claims and irreversible publication decisions. Automation may validate and deploy within explicit workflows.

### 10.3 Editorial flow

`idea → draft → review → candidate → approved`, with `deprecated` and `superseded` for lifecycle control. Publication status and authority are distinct: a candidate may be public without becoming approved.

#### Criteria by state

Idea identifies a need; draft has provisional content; review has metadata and sources; candidate passes defined gates and awaits ratification or evidence; approved is ratified within scope; deprecated remains for transition; superseded points to a valid successor.

### 10.4 Normative changes

Changes to definitions, authority, domains, brand architecture, lifecycle, language policy or publication rules require an ADR, impact analysis, migration where necessary and explicit ratification.

## 11. Versioning

### 11.1 Three distinct versions

The project separates governance version, knowledge-asset version and integrated portal release. They may evolve at different rates but remain linked.

### 11.2 Release semantics

Stable releases identify an editorially and technically reproducible baseline; they do not upgrade every included asset's evidence maturity. Release candidates are traceable, reviewable bundles and remain candidates unless promoted.

### 11.3 Git policy

Changes flow through branches and pull requests. `main` is production. Stable tags are created only after post-merge gates on the exact SHA. Historical candidate tags are not fabricated retrospectively.

## 12. Technical publishing architecture

### 12.1 Recommended decision

Use a static MkDocs portal built from the repository, validated in GitHub Actions and deployed to GitHub Pages under the custom domain. This keeps content, governance and release history inspectable.

### 12.2 GitHub is not an application backend

GitHub stores versioned source and orchestrates builds. The portal is static; interactive or sensitive workloads require separately governed services. No page should imply that repository storage provides application authorization, runtime intelligence or private data handling.

### 12.3 Publishing flow

Pull request → validation and visual review → merge to `main` → strict build and checks → Pages deployment → public verification. Pull requests do not deploy production.

### 12.4 Visible and archived versions

Initially the portal shows the current integrated build and public version history. A multi-version selector is introduced only when at least two historical releases are useful to readers. Git tags and releases preserve immutable stable references.

### 12.5 Repository structure

`docs/` contains public pages and assets; `sources/` canonical sources; `governance/` ADRs, manifests, registries and templates; `brand/` source and generated tokens; `evidence/` controlled case data; `scripts/` gates; `tests/` browser checks; `.github/workflows/` automation.

### 12.6 Public navigation

Navigation starts from reader needs and decisions, while preserving access to foundational architecture, PULSE, practice, research, governance and versions. Omitted drafts must not be reachable as stable knowledge.

### 12.7 Design-system implementation

Brand tokens have one repository source and generated outputs. The minimum component system includes hero, cards, calls to action, evidence/insight/risk panels, status language, tables and footer. IgraSans use follows licensing and distribution controls. Dark theme is a first-class state. Images require provenance, purpose, accessibility text and versioned ownership.

## 13. Integration with dashboards.javierforero.co

The dashboard gallery is a practical extension, not the CDI-BoK's evidence authority. Integration uses explicit links, consistent identity and case admission rules. External availability or visual quality does not raise a demo's maturity. Domains remain separately deployable to avoid technical coupling and allow independent governance.

## 14. Automated controls

CI validates frontmatter, content-map registration, authority and version invariants, source and claim references, ADR lifecycle, brand synchronization, dependencies, secrets, strict MkDocs build, links, semantic HTML, visual regression, responsive behavior and automated accessibility rules.

### Editorial Definition of Done

An asset is done for its declared state only when ownership, authority, evidence, uncertainty, counterargument, risks, links, metadata, language status, build and relevant tests are complete. Passing automation does not replace owner judgment.

## 15. Languages, licenses and transparency

### 15.1 Language

Spanish is canonical during `0.x`. English pages are identified translations linked to the canonical source and version. Translation does not create an independent doctrine. Every public page must have a registered English pair, source hash, review date, status and owner; CI blocks missing or stale pairs. Co-canonical bilingual governance would require demonstrated editorial capacity and a new ADR.

### 15.2 Licenses

Repository, content, code, fonts, images and external sources may have different licenses. Publication must not imply rights beyond those documented. IgraSans distribution follows the approved licensing posture.

### 15.3 AI-assisted authorship

AI assistance is disclosed as part of the production process where material. The accountable human owner remains responsible for selection, verification, claims, publication and consequences. AI output is not a source merely because it appears in a project document.

## 16. Knowledge-system metrics

### 16.1 Editorial health

Track registered assets, stale reviews, unresolved sources or claims, broken links, translation parity, build failures, deprecated items and time to close governance decisions.

### 16.2 Portal utility

Usage analytics may show discoverability and behavior but do not prove decision impact. Use privacy-conscious aggregate measures such as entry paths, successful navigation, search gaps and task completion where available.

### 16.3 Impact evidence

Impact requires instrumented decisions, owners, actions, outcomes, comparison and learning. Page views, session duration and satisfaction are adoption signals—not proof that decisions improved.

## 17. Risks and mitigations

| Risk | First-order effect | Second-order effect | Mitigation |
|---|---|---|---|
| Inflated authority | Readers treat proposals as facts | External credibility erodes | Visible status, claim classes and evidence gates |
| Concept duplication | Definitions drift | Retrieval and teaching become inconsistent | Canonical owners and documentation map |
| Governance overload | Publishing slows | Contributors bypass controls | Proportional review and automation |
| Tool-led design | Pages optimize features | Decision purpose disappears | Decision First and interface independence |
| AI hallucination | False content is published | Errors become internal “sources” | Human verification and source registry |
| Metric gaming | Teams optimize proxies | Learning becomes defensive | Guardrails, segmentation and review |
| Translation drift | ES and EN diverge | Different doctrines emerge by language | Canonical Spanish, hashes and blocking parity gate |
| Brand inconsistency | Fragmented identity | Trust and maintainability decline | Single token source and visual review |

## 18. Open decisions requiring ADR

Future ADRs are required for bilingual co-canonicity, historical multi-version deployment, professional translation management, major domain changes, new licensing posture, external contribution governance, analytics expansion and any agent capable of publishing or acting autonomously.

## 19. Implementation sequence

Sprint 0 established constitution and control; Sprint 1 the publishable infrastructure; Sprint 2 the minimum foundational core; Sprint 3 practice and evidence. Later sprints added learning experience, decision measurement, conversational patterns, stable `v0.8.0`, and the controlled ES/EN portal candidate.

## 20. Ratification record

Javier Forero ratified this architecture as normative project governance in `v0.2.0`. Subsequent accepted ADRs may supersede specific provisions while preserving traceable lineage.

## 21. Technical publishing references

Implementation decisions use official MkDocs, Material for MkDocs, GitHub Actions and GitHub Pages documentation; dependency versions are locked. Tool documentation supports implementation and does not provide evidence for CDI's theoretical or practical claims.

## 22. Executive conclusion

The CDI-BoK is governed as a decision-centered knowledge system. Its credibility depends on keeping institutional authority, external evidence, maturity, publication status and practical outcomes distinct. The bilingual portal extends access while keeping Spanish canonical and making divergence mechanically visible.

### Confidence level

High for the governance and publishing architecture; medium for its long-term editorial efficiency; low where CDI or PULSE effectiveness remains empirically untested.

### Factors that could change the conclusion

External review, adoption across real cases, evidence of control burden, repeated translation drift, licensing constraints or a superior publishing architecture could justify revision.

### Recommended action

Apply the smallest governed change that improves a real decision, preserve evidence and uncertainty, validate both language editions, and close the learning loop before expanding complexity.
