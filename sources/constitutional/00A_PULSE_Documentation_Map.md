# PULSE Documentation Map

## 1. Document Status

| Field | Governance definition |
|---|---|
| **Document name** | `00A_PULSE_Documentation_Map.md` |
| **Version** | 1.0.0 |
| **Status** | **Documentation Governance Source** |
| **Owner** | Javier Forero, PULSE Methodology Owner |
| **Purpose** | Govern the architecture, authority, ownership, dependencies, lifecycle, and Knowledge Base placement of the PULSE documentation system. |
| **Intended audience** | PULSE methodology authors, editors, researchers, consultants, educators, designers, engineers, product teams, Knowledge Base administrators, and AI-system maintainers. |
| **Authority level** | Structural and editorial governance authority. It determines where knowledge belongs, which document owns each concept, and how documentation changes are controlled. |
| **Review cadence** | Quarterly during active methodology development; every six months after stabilization; immediately after any constitutional change to `00_PULSE_DNA.md`. |
| **Relationship to `00_PULSE_DNA.md`** | This map is subordinate to the DNA. It governs the documentation system but does not override, reinterpret, or replace the intellectual content of the DNA. When this map conflicts with the DNA, the DNA prevails. |
| **Source authority** | 1) `00_PULSE_DNA.md`; 2) Javier Forero’s original articles, classes, frameworks, metaphors, and explicit points of view; 3) `02_PULSE_Framework.md`; 4) `03_PULSE_Technical_Foundations.md`; 5) derived PULSE documentation; 6) general industry practices. |
| **Change class** | Controlled governance document. Changes to document ownership, authority, layer assignment, canonical filenames, or dependency order require an explicit decision record. |

> **Core governance rule:** One concept may appear in several documents, but only one document may own its formal definition.

Supporting documents may explain, apply, illustrate, operationalize, test, or implement a concept. They must cite or link to its authoritative home and must not silently redefine it.

### 1.1 Scope of authority

This document governs:

- The canonical document set.
- The purpose and boundary of each document.
- Concept ownership.
- Source precedence.
- Dependency and reading order.
- Document status and maintenance expectations.
- Knowledge Base placement.
- Creation, merge, retirement, and archival decisions.
- The documentation inputs from which PULSE agent instructions are derived.

This document does **not** govern:

- The constitutional meaning of PULSE.
- The scientific validity of an external theory.
- The final wording of the Identity, Manifesto, Framework, or other documents.
- Product-roadmap priorities outside documentation.
- Client-specific implementations, except for the rules that determine whether they may be presented as PULSE reference implementations.

### 1.2 Source and assessment note

The source set used for this version included `00_PULSE_DNA.md` and Javier Forero’s supplied articles on PULSE, technical foundations, conversational analytics, data architecture, analytical maturity, and decision-centered AI. The full current text of `00_PULSE_Identity.md` through `08_PULSE_Component_Library.md` was not present in the working set.

Accordingly:

- The architecture, ownership model, proposed document set, and dependency graph are definitive governance recommendations derived from the DNA.
- The assessment of the existing `00`–`08` documents is an **architecture-level diagnosis** based on their declared functions.
- Content-level findings for those files are explicitly marked as review tests rather than verified defects.
- Their lifecycle status remains **Pending Review** until the full files are audited against this map.

This limitation protects the governance system from false precision. An unavailable document must not be judged as though its contents had been inspected.

---

## 2. Purpose of the Documentation Map

PULSE is intended to evolve. Evolution without governance, however, produces conceptual drift: the same term acquires several definitions, examples become mistaken for rules, implementation details become permanent doctrine, and a growing Knowledge Base becomes harder—not easier—to trust.

This map exists to keep PULSE coherent while allowing it to expand.

Its functions are to:

1. **Prevent conceptual drift.** Constitutional language remains stable unless the DNA changes through an explicit constitutional review.
2. **Prevent unnecessary duplication.** Repetition is permitted for orientation and teaching, but formal definitions and normative rules have one home.
3. **Establish authoritative ownership.** Every canonical concept, method, pattern, standard, and component has an accountable document owner.
4. **Define reading and dependency order.** Authors know what must be understood before a document can be created or revised.
5. **Guide future document creation.** New files are created only when they own a genuinely distinct knowledge function.
6. **Govern Knowledge Base organization.** Retrieval systems can distinguish constitutional truth, operating methodology, standards, examples, and agent instructions.
7. **Support the GPT System Instruction.** Agent behavior is derived from governed documentation and cannot become an alternative source of methodology.
8. **Maintain consistency across channels.** Articles, classes, dashboards, executive briefs, GitHub examples, conversational systems, agents, and future PULSE products use the same conceptual spine.
9. **Preserve traceability.** A reader can move from a claim to its canonical definition, evidence basis, operational rule, implementation standard, and example.
10. **Control document growth.** The Knowledge Base expands by capability and evidence, not by generating a new file for every topic.

### 2.1 The documentation contract

Every governed PULSE document must answer six questions:

| Question | Required answer |
|---|---|
| **Why does this document exist?** | A distinct purpose that is not already owned elsewhere. |
| **What does it own?** | A bounded set of concepts, methods, standards, patterns, or artifacts. |
| **What does it only support?** | Concepts it may explain or apply but may not redefine. |
| **What does it depend on?** | Higher-authority or prerequisite documents. |
| **Who uses it?** | A primary audience and use context. |
| **How does it change?** | An owner, status, review cadence, and change class. |

A file that cannot answer these questions is not ready to enter the canonical Knowledge Base.

### 2.2 Source authority hierarchy

When sources disagree, the following order applies:

1. **`00_PULSE_DNA.md` — constitutional authority.** Owns worldview, official definition, boundaries, canonical language, non-negotiable principles, ethical position, and long-term aspiration.
2. **Javier Forero’s original intellectual material — primary evidence of authorial fidelity.** Articles, classes, frameworks, metaphors, and explicit points of view verify whether derived documentation remains faithful to the methodology’s origin and evolved direction.
3. **`02_PULSE_Framework.md` — operational methodology.** Owns how a PULSE engagement or decision system is diagnosed, designed, operated, measured, and improved.
4. **`03_PULSE_Technical_Foundations.md` — scientific and conceptual support.** Explains external theories, evidence posture, analogical limits, and intellectual lineage.
5. **Derived PULSE documentation.** Operational systems, design rules, patterns, components, standards, guides, and evaluations.
6. **General industry practices.** May improve implementation when compatible with PULSE, but never redefine PULSE.

A lower-level document may refine implementation. It may not contradict a higher-level source merely because an industry convention is more common or a tool makes another approach easier.

---

## 3. Documentation Architecture Principles

| Principle | Meaning | Practical implication | Failure mode prevented |
|---|---|---|---|
| **DNA First** | The DNA is the constitutional source of truth. | Every governed document declares its DNA dependencies and passes the DNA Decision Test before approval. | Derived documents quietly becoming the real methodology. |
| **One Authoritative Home per Concept** | A formal definition, normative rule, or canonical model has one owner. | Other documents link to the owner and use a short restatement only when necessary for comprehension. | Competing definitions, semantic fragmentation, and retrieval ambiguity. |
| **Minimal Necessary Duplication** | Repetition is allowed only when it improves orientation, teaching, or execution. | Repeated text is labeled as summary, application, or implementation—not presented as an independent definition. | Copy-paste drift and costly multi-file updates. |
| **Clear Separation of Concerns** | Constitution, beliefs, methodology, evidence, systems, patterns, components, standards, guides, and examples are different knowledge types. | A document is structured around one primary knowledge function. | Files that mix philosophy, code, marketing, and examples into an unmaintainable whole. |
| **Interface Independence** | PULSE is a decision methodology, not a dashboard, HTML, chat, or agent methodology. | Interface-specific files implement the methodology but cannot define its identity. | A temporary delivery mechanism becoming the permanent definition of PULSE. |
| **Evidence Traceability** | Claims must reveal whether they are established foundations, PULSE synthesis, practical point of view, aspiration, or hypothesis. | Technical and explanatory documents cite source material and separate evidence from analogy or prescription. | Aspirations presented as proven facts and metaphors presented as science. |
| **Progressive Disclosure** | Readers receive the minimum knowledge required for their role, with paths to greater depth. | Executive, practitioner, engineering, and agent-facing documents reference the same core without duplicating all detail. | Overloaded documents and inaccessible methodology. |
| **Stable Core, Evolving Implementation** | Constitutional concepts change slowly; patterns, components, and engineering practices may change faster. | Different document classes receive different versioning and review cadences. | Tool changes forcing unnecessary changes to the methodology. |
| **Examples Do Not Define the Methodology** | A dashboard, case, prompt, or code repository demonstrates one valid application. | Reference artifacts state the principles and constraints they instantiate and the context in which they are valid. | A successful example being generalized into an unsupported universal rule. |
| **Documentation Before Automation** | A behavior must be understood and governed before it is encoded in prompts, agents, or workflows. | The GPT System Instruction is generated from approved documentation, never used to fill conceptual gaps. | Automation freezing ambiguity, contradiction, or undocumented judgment. |
| **Governance Enables Evolution** | Governance creates safe mechanisms for change rather than preventing change. | Proposals can add, revise, merge, deprecate, or retire material through explicit impact analysis. | Either uncontrolled sprawl or a rigid Knowledge Base that cannot learn. |
| **Avoid Document Sprawl** | A new file is justified by a distinct owner, audience, lifecycle, or retrieval need. | Related topics are merged when they share authority, dependencies, and maintenance cadence. | A large collection of thin, overlapping, low-trust documents. |
| **Dependency Before Drafting** | A document should not be written before its authoritative inputs are stable enough. | Foundational documents precede systems; systems precede standards and examples; agent instructions are derived last. | Downstream rework and contradictory implementation. |
| **Normative Language Is Controlled** | “Must,” “should,” “may,” and “must not” have specific force. | Standards and governance documents distinguish requirements from recommendations and options. | Advice being mistaken for a requirement, or requirements being treated as optional. |
| **Machine Retrieval Must Preserve Authority** | Search relevance must not override source authority. | Knowledge chunks carry document layer, status, version, authority, and concept-owner metadata. | An agent retrieving a vivid example instead of the canonical rule. |
| **Deprecation Is Preferable to Silent Mutation** | Historical material remains traceable when its role changes. | Superseded files are marked, redirected, and archived rather than quietly rewritten into a different purpose. | Broken links, lost intellectual history, and uncertainty about which version governed a decision. |

### 3.1 Controlled use of duplication

Duplication is legitimate in only four forms:

- **Orientation:** a short summary that directs the reader to the canonical owner.
- **Application:** a concept is used in a domain-specific procedure.
- **Implementation:** a principle is converted into a technical requirement.
- **Illustration:** an example demonstrates the concept in context.

Whenever a concept is repeated, the document must make the relationship clear. Phrases such as “as defined in,” “operationalizes,” “implements,” or “illustrates” are preferred over language that implies independent ownership.

### 3.2 New-document admission test

A proposed document is created only when at least one of the following is true:

1. It owns a distinct normative system or method.
2. It serves a substantially different audience with a different maintenance cadence.
3. It contains implementation standards that must evolve independently from the methodology.
4. It is required as a machine-consumable artifact with controlled generation.
5. Its size or retrieval characteristics would materially degrade the parent document.

A new document is rejected or merged when the only rationale is that the topic is important. Importance does not by itself create a new ownership boundary.

---

## 4. Documentation Layers

The layers classify the **type of knowledge** a document contains. They do not create an automatic hierarchy within each layer, and they do not replace the source authority hierarchy. A Layer 4 trust requirement may be a prerequisite for a Layer 2 conversational system even though its layer number is higher.

### Layer 0 — Constitutional and Governance

| Attribute | Definition |
|---|---|
| **Purpose** | Protect the intellectual identity of PULSE and govern the documentation system that expresses it. |
| **Type of knowledge** | Constitutional definitions, boundaries, canonical language, authority rules, ownership, lifecycle, and change control. |
| **Belongs here** | `00_PULSE_DNA.md`, `00A_PULSE_Documentation_Map.md`, constitutional decision records. |
| **Must not belong here** | Detailed operating procedures, UI specifications, code standards, examples, vendor guidance, or client-specific practices. |

Layer 0 changes require the highest scrutiny because they can alter every downstream document.

### Layer 1 — Foundational

| Attribute | Definition |
|---|---|
| **Purpose** | Express what PULSE is, what it believes, how it works at the methodology level, and why its intellectual foundations are credible. |
| **Type of knowledge** | Identity, mission, vision, beliefs, methodology, evidence basis, conceptual lineage, and scope. |
| **Belongs here** | Identity, Manifesto, Framework, Technical Foundations. |
| **Must not belong here** | Detailed components, code conventions, prompt templates, galleries, or product-specific interface rules. |

Layer 1 is the minimum reading set for anyone authorized to create new PULSE methodology content.

### Layer 2 — Decision and Reasoning Systems

| Attribute | Definition |
|---|---|
| **Purpose** | Define coordinated methods for questions, reasoning, decisions, narratives, conversations, options, uncertainty, and learning. |
| **Type of knowledge** | Reasoning protocols, question structures, decision patterns, narrative logic, conversational operating rules, and learning-loop methods. |
| **Belongs here** | Decision Patterns, Narrative System, Reasoning and Question System, Conversational Analytics. |
| **Must not belong here** | Visual tokens, CSS rules, data-platform architecture, or reusable UI primitives. |

Layer 2 turns the Framework into repeatable cognitive and communicative behavior.

### Layer 3 — Experience Design

| Attribute | Definition |
|---|---|
| **Purpose** | Define how PULSE principles are experienced through visual, narrative, conversational, operational, and embedded interfaces. |
| **Type of knowledge** | Experience principles, Mobile First, accessibility, progressive disclosure, interface selection, interaction behavior, visual system, experience patterns, and components. |
| **Belongs here** | Experience Principles, Design System, Pattern Library, Component Library. |
| **Must not belong here** | Canonical methodology definitions, scientific theory, data governance policy, or application-specific code. |

Layer 3 gives form to PULSE without allowing form to define PULSE.

### Layer 4 — Data Trust and Governance

| Attribute | Definition |
|---|---|
| **Purpose** | Define the operating conditions under which evidence, analytics, conversation, and automation are sufficiently trustworthy and controlled for a given decision. |
| **Type of knowledge** | Fitness for purpose, quality, semantics, ownership, stewardship, lineage, provenance, permissions, privacy, context, traceability, uncertainty, escalation, auditability, and Human-in-Control controls. |
| **Belongs here** | Data Trust and Governance operating model, readiness criteria, control matrix, decision-risk tiers, and evidence traceability requirements. |
| **Must not belong here** | A generic enterprise data-governance handbook unrelated to decisions, or technical implementation details that belong in Engineering Standards. |

Layer 4 operationalizes Trust First and Governance Enables Speed.

### Layer 5 — Engineering

| Attribute | Definition |
|---|---|
| **Purpose** | Translate approved methodology, experience, and trust requirements into implementable technical standards. |
| **Type of knowledge** | HTML architecture, coding conventions, data contracts, semantic structures, performance, accessibility implementation, observability, security hooks, testing, and GitHub Pages deployment. |
| **Belongs here** | Engineering Standards and machine-readable schemas maintained under it. |
| **Must not belong here** | The official definition of PULSE, business methodology, or assumptions that are true only for one example repository. |

Layer 5 changes quickly enough to require independent versioning but remains subordinate to the methodology.

### Layer 6 — Application, Evaluation, and Evidence

| Attribute | Definition |
|---|---|
| **Purpose** | Demonstrate, test, audit, and improve PULSE through applied examples and reference implementations. |
| **Type of knowledge** | Evaluation rubrics, audits, galleries, recipes, templates, cases, reference repositories, implementation notes, and lessons learned. |
| **Belongs here** | Decision Experience Evaluation, Reference Implementations, approved case studies, and cookbook recipes. |
| **Must not belong here** | New canonical definitions inferred from one case or unverified examples presented as approved standards. |

Layer 6 is evidence of application, not constitutional authority.

### Layer 7 — Agent Behavior

| Attribute | Definition |
|---|---|
| **Purpose** | Govern how AI systems retrieve, reason over, communicate, evaluate, and act on PULSE knowledge. |
| **Type of knowledge** | Retrieval precedence, prompt and tool behavior, evidence handling, uncertainty, output constraints, evaluation, refusal and escalation rules, and executable system instructions. |
| **Belongs here** | Agent Operating Standard and GPT System Instruction. |
| **Must not belong here** | Undocumented methodology, autonomous authority to change PULSE, or a hidden alternative ontology. |

Layer 7 is downstream of all approved human-readable documentation. The GPT System Instruction is an executable derivative, not a source of intellectual truth.

---

## 5. Master Document Registry

### 5.1 Canonical registry

**Authority levels used below**

- **A0 — Constitutional:** governs all PULSE intellectual interpretation.
- **A0G — Governance:** governs documentation structure and lifecycle, subordinate only to the DNA on intellectual content.
- **A1 — Foundational:** authoritative for a distinct foundational function.
- **A2 — System:** authoritative for an operational or experience system within DNA boundaries.
- **A3 — Standard:** authoritative for implementation requirements.
- **A4 — Reference:** approved illustration, evaluation, or implementation evidence.
- **A5 — Executable derivative:** machine-facing behavior generated from approved sources.

| ID | File Name | Layer | Primary Purpose | Concepts Owned | Supporting Concepts | Primary Audience | Depends On | Authority Level | Current Status | Required Action | Priority | Knowledge Base Role |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| C00 | `00_PULSE_DNA.md` | 0 | Define the constitutional truth of PULSE. | Official definition; core thesis; worldview; canonical language; boundaries; non-negotiable principles; ethical position; long-term aspiration. | All PULSE systems and implementations. | All authors and systems. | Javier Forero’s original thought and explicit evolution. | A0 | Approved | Keep; change only through constitutional review. | P0 | Mandatory root source; highest retrieval authority. |
| G00A | `00A_PULSE_Documentation_Map.md` | 0 | Govern documentation architecture, ownership, dependencies, lifecycle, and KB placement. | Document roles; concept ownership; registry; dependency graph; change control. | All PULSE documentation. | Authors, editors, KB and agent maintainers. | C00. | A0G | Create | Approve as the structural source after owner review. | P0 | Governance root and routing map. |
| F00 | `00_PULSE_Identity.md` | 1 | Express what PULSE is for external and internal recognition. | Mission; vision; value proposition; audiences; positioning; identity boundaries. | Official definition and core thesis. | Executives, partners, clients, educators, authors. | C00, G00A. | A1 | Pending Review | Audit and adjust; remove independent constitutional definitions. | P1 | High-level identity and orientation source. |
| F01 | `01_PULSE_Manifesto.md` | 1 | Mobilize the beliefs and commitments of PULSE. | Manifesto propositions and commitments. | Canonical statements and non-negotiable principles. | Broad PULSE community and learners. | C00, F00. | A1 | Pending Review | Audit and adjust; distinguish belief, aspiration, and evidence. | P2 | Persuasive belief layer; not used for technical truth. |
| F02 | `02_PULSE_Framework.md` | 1 | Define how PULSE operates as a decision methodology. | Engagement lifecycle; diagnostic logic; operating stages; deliverables; roles; measures; feedback loop. | Decision Circle; PDAMR; transformation chain; five verbs. | Consultants, practitioners, product and transformation teams. | C00, G00A, F00. | A1 | Pending Review | Full methodology audit; likely controlled rewrite if pre-DNA structure conflicts. | P1 | Primary operational methodology source. |
| F03 | `03_PULSE_Technical_Foundations.md` | 1 | Explain the scientific and conceptual support for PULSE. | Evidence map; intellectual lineage; analogy limits; external theories; evidence posture. | Asymmetry; alostasis; interoception; decision science; systems thinking; learning. | Researchers, advanced practitioners, educators, skeptical reviewers. | C00, Javier Forero source material. | A1 | Pending Review | Audit evidence quality, citations, claim types, and analogy boundaries. | P1 | Evidence and credibility source. |
| X04 | `04_PULSE_Design_System.md` | 3 | Define the visual and interaction language of PULSE. | Design tokens; visual hierarchy; typography; color; layout; visualization language; states. | Mobile First; accessibility; progressive disclosure. | Designers and front-end engineers. | C00, G00A, N09. | A2 | Pending Review | Audit and adjust after Experience Principles is approved. | P3 | Design-system source; not methodology source. |
| X05 | `05_PULSE_Pattern_Library.md` | 3 | Define reusable experience patterns. | Cross-interface patterns; pattern anatomy; selection criteria; anti-patterns. | Decision and narrative patterns; components. | Designers, analysts, product teams, engineers. | C00, N09, T06, T07, X04. | A2 | Pending Review | Audit boundaries with Decision Patterns and Component Library. | P3 | Reusable experience-pattern source. |
| T06 | `06_PULSE_Decision_Patterns.md` | 2 | Define reusable approaches for recurring decision situations. | Decision-pattern taxonomy; pattern inputs; options; risks; owners; feedback structures. | Decision Circle; PDAMR; reasoning; learning. | Consultants, analysts, product owners, decision owners. | C00, F02, N12. | A2 | Pending Review | Audit and adjust; prohibit redefinition of canonical decision terms. | P2 | Decision-method reuse source. |
| T07 | `07_PULSE_Narrative_System.md` | 2 | Define how evidence becomes decision-supporting narrative. | Narrative roles; DATA → IDEA → DECISIÓN applications; evidence-to-claim rules; uncertainty language; executive structures. | Shared understanding; smart narratives; explainability. | Analysts, writers, educators, product teams, AI designers. | C00, F02, N12, N10. | A2 | Pending Review | Audit for causal overreach, unsupported certainty, and overlap with conversational responses. | P2 | Narrative-generation and review source. |
| X08 | `08_PULSE_Component_Library.md` | 3 | Define reusable experience building blocks. | Component inventory; anatomy; states; properties; accessibility behavior; composition rules. | Patterns and design tokens. | Designers and engineers. | C00, N09, X04, X05. | A2 | Pending Review | Audit and adjust; ensure components implement patterns rather than define decisions. | P3 | Component specification source. |
| N09 | `09_PULSE_Experience_Principles.md` | 3 | Operationalize the non-negotiable principles of a PULSE Decision Experience across interfaces. | Experience principles; Mobile First implementation; progressive disclosure; interface selection; accessibility baseline; action connection; replaceability. | Decision Experience; Human-in-Control; interface independence. | Designers, analysts, product owners, engineers. | C00, F02, N10. | A2 | Create | Create before revising Design System, Pattern Library, or Components. | P1 | Bridge from methodology to experience design. |
| N10 | `10_PULSE_Data_Trust_and_Governance.md` | 4 | Define the operating model for trustworthy evidence and governed decisions. | Fitness-for-purpose assessment; trust dimensions; semantic control; stewardship; lineage; permissions; traceability; decision-risk tiers; control requirements; readiness gates. | Trusted Data; Data Trust; Governance; Context First; Human-in-Control. | Data leaders, stewards, architects, risk teams, AI and analytics teams. | C00, F02, F03. | A2 | Create | Create as one integrated trust-and-governance system. | P1 | Mandatory prerequisite for governed analytics and agents. |
| N11 | `11_PULSE_Conversational_Analytics.md` | 2 | Define how governed natural-language interaction supports evidence, explanation, exploration, and action. | Conversational use cases; readiness model; answer contract; evidence citation; follow-up behavior; permissions; fallback; conversation-to-action rules. | Conversational Analytics; Decision Copilot; interface evolution. | Product teams, analysts, AI engineers, data leaders, decision owners. | C00, F02, N10, N12, T07, N09. | A2 | Create | Create after trust and reasoning systems are stable. | P2 | Conversational-system source. |
| N12 | `12_PULSE_Reasoning_and_Question_System.md` | 2 | Define disciplined questioning and reasoning for evidence-based decisions. | Question taxonomy; decision-question anatomy; hypothesis handling; assumptions; alternatives; counterarguments; uncertainty; evidence tests; learning questions. | Question First; Evidence Before Authority; decision reasoning. | Consultants, analysts, educators, product and agent designers. | C00, F02, F03, N10. | A2 | Create | Merge the proposed reasoning and question documents into one system. | P1 | Cognitive protocol for humans and agents. |
| S13 | `13_PULSE_Engineering_Standards.md` | 5 | Translate approved PULSE systems into technical implementation requirements. | HTML architecture; coding conventions; data contracts; semantic payload; accessibility implementation; performance; security hooks; observability; deployment. | Components, patterns, trust controls, conversational interfaces. | Engineers and technical reviewers. | C00, N09, N10, N11, X04, X05, X08. | A3 | Create | Merge HTML Architecture, Coding Standards, and narrative Data Model documentation; maintain schemas as companion files. | P3 | Normative implementation source. |
| E14 | `14_PULSE_Decision_Experience_Evaluation.md` | 6 | Define how PULSE experiences are reviewed, tested, and approved. | Evaluation rubric; decision-value tests; usability; trust; accessibility; narrative quality; conversational quality; learning-loop evidence; release gates. | DNA Decision Test; dashboard review; agent-output evaluation. | Reviewers, QA, product owners, consultants, clients. | C00, F02, N09, N10, N11, T07, S13. | A3 | Create | Replace dashboard-only review with interface-independent evaluation. | P2 | Quality gate and audit source. |
| E15 | `15_PULSE_Reference_Implementations.md` | 6 | Curate approved examples, recipes, cases, templates, and GitHub implementations. | Reference-entry metadata; example status; context; assumptions; version compatibility; lessons learned; reuse conditions. | All methodology and implementation systems. | Practitioners, educators, clients, developers. | Approved documents and E14. | A4 | Create | Merge Reference Gallery and Cookbook into a curated registry backed by repository folders. | P4 | Evidence and applied-learning catalog. |
| A16 | `16_PULSE_Agent_Operating_Standard.md` | 7 | Define human-readable rules for PULSE agents, prompting, retrieval, tool use, and evaluation. | Retrieval precedence; prompt patterns; source use; reasoning behavior; uncertainty; tool boundaries; escalation; agent test suite. | Human-in-Control; evidence traceability; narrative and conversational behavior. | AI system owners, prompt designers, evaluators, governance teams. | C00, G00A, F02, N10, N11, N12, T07, E14. | A3 | Create | Merge Prompting Guide with agent governance and evaluation; keep user examples as appendices or recipes. | P3 | Normative agent-design source. |
| A17 | `17_PULSE_GPT_System_Instruction.md` | 7 | Provide the executable instruction set for the official PULSE GPT. | Operational behavior of the GPT only. | All approved PULSE concepts and controls. | GPT runtime and maintainers. | All approved canonical documents, especially A16. | A5 | Create | Generate only after upstream documents are approved; maintain traceable source mapping. | P3 | Executable derivative; never an intellectual source. |

### 5.2 Disposition of proposed future files

| Proposed file | Decision | Canonical destination | Rationale |
|---|---|---|---|
| `09_PULSE_Experience_Principles.md` | **Create independently** | `09_PULSE_Experience_Principles.md` | Principles have different authority and cadence from visual design tokens and components. |
| `10_PULSE_Data_Trust_Framework.md` | **Rename and broaden** | `10_PULSE_Data_Trust_and_Governance.md` | Trust and governance are inseparable in PULSE: trust judges fitness for use; governance creates ownership, controls, permissions, and traceability. |
| `11_PULSE_Conversational_Analytics.md` | **Create independently** | `11_PULSE_Conversational_Analytics.md` | Conversational interaction has distinct readiness, evidence, permission, and fallback requirements. |
| `12_PULSE_Reasoning_Framework.md` | **Merge** | `12_PULSE_Reasoning_and_Question_System.md` | Questions are the entry structure of reasoning; separating them would create duplicate taxonomies and maintenance. |
| `16_PULSE_Question_Framework.md` | **Merge** | `12_PULSE_Reasoning_and_Question_System.md` | See above. Question structures remain an explicit owned section within the combined system. |
| `13_PULSE_HTML_Architecture.md` | **Merge** | `13_PULSE_Engineering_Standards.md` | HTML is one implementation substrate, not a distinct methodology. |
| `14_PULSE_Coding_Standards.md` | **Merge** | `13_PULSE_Engineering_Standards.md` | Coding, testing, performance, accessibility, and deployment share an engineering lifecycle. |
| `15_PULSE_Data_Model.md` | **Merge as narrative; separate schemas permitted** | `13_PULSE_Engineering_Standards.md` plus `/schemas` | A narrative data-model file would overlap with trust semantics and engineering contracts. Machine-readable schemas may evolve as companion artifacts. |
| `17_PULSE_Dashboard_Review.md` | **Rename and broaden** | `14_PULSE_Decision_Experience_Evaluation.md` | PULSE is interface-independent. Evaluation must cover dashboards, narratives, mobile, conversation, copilots, and workflows. |
| `18_PULSE_Reference_Gallery.md` | **Merge** | `15_PULSE_Reference_Implementations.md` | A gallery without context becomes aesthetic; examples and recipes need common approval metadata. |
| `20_PULSE_Cookbook.md` | **Merge** | `15_PULSE_Reference_Implementations.md` | Recipes are one reference-implementation format and should be governed with cases and repositories. |
| `19_PULSE_Prompting_Guide.md` | **Merge and defer public-facing extraction** | `16_PULSE_Agent_Operating_Standard.md` | Prompting is part of agent behavior, retrieval, and evaluation. A separate public guide may be extracted later if audience demand justifies it. |
| `21_PULSE_GPT_System_Instruction.md` | **Create separately, renumber canonically** | `17_PULSE_GPT_System_Instruction.md` | The executable instruction must remain separate from the human-readable operating standard and must be generated downstream. |

### 5.3 Smallest complete future set

The smallest complete extension required by the DNA is therefore nine documents:

1. `09_PULSE_Experience_Principles.md`
2. `10_PULSE_Data_Trust_and_Governance.md`
3. `11_PULSE_Conversational_Analytics.md`
4. `12_PULSE_Reasoning_and_Question_System.md`
5. `13_PULSE_Engineering_Standards.md`
6. `14_PULSE_Decision_Experience_Evaluation.md`
7. `15_PULSE_Reference_Implementations.md`
8. `16_PULSE_Agent_Operating_Standard.md`
9. `17_PULSE_GPT_System_Instruction.md`

This set is complete enough to operationalize the DNA without turning every subtopic into an independent file.

---
## 6. Concept Ownership Matrix

The matrix below assigns one authoritative owner to each formal concept. “Supporting Documents” may explain or operationalize the concept. “May Be Referenced In” identifies likely reuse. “Must Not Be Redefined In” identifies the highest-risk locations for conceptual drift; the prohibition also applies to every other non-owner document.

| Concept | Authoritative Document | Supporting Documents | May Be Referenced In | Must Not Be Redefined In |
|---|---|---|---|---|
| Official definition of PULSE | `00_PULSE_DNA.md` | Identity; Framework | Every PULSE document and product | Identity; Manifesto; System Instruction; marketing pages |
| Purpose of PULSE | `00_PULSE_DNA.md` | Identity; Manifesto | Articles, classes, proposals, product descriptions | Framework; examples; agent outputs |
| Mission | `00_PULSE_Identity.md` | DNA; Manifesto | External communications, partnerships, education | Manifesto; Framework; product pages |
| Vision | `00_PULSE_Identity.md` | DNA long-term aspiration; Manifesto | Strategy, roadmap, education | Manifesto; conversational or agent documents |
| Core thesis | `00_PULSE_DNA.md` | Identity; Framework | All PULSE materials | Manifesto; Technical Foundations; examples |
| Trusted Data | `00_PULSE_DNA.md` | Data Trust and Governance | Framework, Conversational Analytics, Engineering | Data Trust document; System Instruction; dashboards |
| Shared Understanding | `00_PULSE_DNA.md` | Narrative System; Framework | Decision experiences, classes, articles | Narrative System; Identity; agent outputs |
| `DATA → IDEA → DECISIÓN` | `00_PULSE_DNA.md` | Narrative System; Framework | Executive briefs, dashboards, classes, articles | Narrative templates; examples; GPT instruction |
| Expanded PULSE transformation | `00_PULSE_DNA.md` | Framework; Data Trust and Governance | Education, consulting, evaluations | Framework; Identity; reference examples |
| Decision Circle | `00_PULSE_DNA.md` | Framework; Decision Patterns; Reasoning and Question System | Diagnostics, classes, products, narratives | Decision Patterns; Framework; agent instruction |
| Five Verbs of Organizational Intelligence | `00_PULSE_DNA.md` | Framework; Evaluation | Business cases, articles, classes, metrics | Identity; Framework; examples |
| PDAMR | `00_PULSE_DNA.md` | Framework; Decision Patterns | Initiative intake, reviews, prompts, workshops | Framework; templates; GPT instruction |
| Business First | `00_PULSE_DNA.md` | Framework | Every initiative and evaluation | Experience Principles; Engineering Standards |
| Decision First | `00_PULSE_DNA.md` | Framework; Decision Patterns | Product briefs, dashboards, agents | Pattern Library; Evaluation rubric |
| Question First | `00_PULSE_DNA.md` | Reasoning and Question System | Workshops, prompts, conversational systems | Reasoning system; Prompt examples |
| Trust First | `00_PULSE_DNA.md` | Data Trust and Governance | Analytics, conversation, agents, engineering | Data Trust document; engineering rules |
| Context First | `00_PULSE_DNA.md` | Data Trust and Governance; Reasoning System | Narratives, conversation, copilots | Framework; data model; agent instruction |
| Human-in-Control | `00_PULSE_DNA.md` | Data Trust and Governance; Agent Operating Standard | Copilots, agents, workflows, evaluations | Conversational Analytics; System Instruction; product policies |
| Mobile First | `00_PULSE_DNA.md` | Experience Principles; Design System; Engineering Standards | Components, patterns, reference implementations | Design System; HTML standards; examples |
| Interface Independence | `00_PULSE_DNA.md` | Experience Principles; Framework | All interface-specific documents | Design System; Conversational Analytics; Engineering Standards |
| Dashboards as a Bridge | `00_PULSE_DNA.md` | Experience Principles; Narrative System; Reference Implementations | Classes, dashboard audits, product roadmaps | Dashboard examples; Design System |
| Conversational Analytics | `00_PULSE_DNA.md` | `11_PULSE_Conversational_Analytics.md`; Data Trust and Governance | Products, articles, agents, reference implementations | Conversational Analytics document; System Instruction; vendor descriptions |
| Conversational Analytics operating system | `11_PULSE_Conversational_Analytics.md` | Data Trust; Reasoning; Narrative; Experience Principles | Product requirements, engineering, evaluation | Agent Standard; reference examples |
| Decision Copilot | `00_PULSE_DNA.md` | Conversational Analytics; Agent Operating Standard | Product strategy, classes, reference implementations | Agent Standard; System Instruction; product marketing |
| Organizational Interoception | `00_PULSE_DNA.md` | Technical Foundations; Framework | Diagnostics, articles, classes | Technical Foundations; Decision Patterns |
| Alostasis | `00_PULSE_DNA.md` | Technical Foundations | Articles, education, diagnostic interpretation | Technical Foundations; Manifesto |
| Information Asymmetry | `00_PULSE_DNA.md` | Technical Foundations; Framework | Strategy, articles, classes | Technical Foundations; Identity |
| Decision Latency | `00_PULSE_DNA.md` | Framework; Evaluation | Metrics, audits, conversational hypotheses | Framework; Evaluation rubric; dashboards |
| Analytical Cadence | `00_PULSE_DNA.md` | Framework; Decision Patterns | Operating models, dashboard use, learning reviews | Framework; Decision Patterns |
| Organizational Learning | `00_PULSE_DNA.md` | Framework; Reasoning System; Evaluation | Decision patterns, narratives, cases | Framework; examples; agent outputs |
| Decision Experience | `00_PULSE_DNA.md` | Experience Principles; Evaluation | Design System, patterns, components, products | Experience Principles; Design System; marketing |
| Experience principles | `09_PULSE_Experience_Principles.md` | DNA; Data Trust and Governance | Design System, Pattern Library, Components, Engineering | Design System; Pattern Library; examples |
| Data Trust | `00_PULSE_DNA.md` | `10_PULSE_Data_Trust_and_Governance.md` | Framework, conversation, engineering, evaluation | Data Trust document; System Instruction |
| Data Trust operating model | `10_PULSE_Data_Trust_and_Governance.md` | DNA; Technical Foundations | Conversational Analytics, Engineering, Evaluation | Engineering Standards; agent documents |
| Governance | `00_PULSE_DNA.md` | Data Trust and Governance; Agent Operating Standard | All implementation and agent documents | Data Trust document; Engineering; System Instruction |
| Governance control model | `10_PULSE_Data_Trust_and_Governance.md` | DNA; Framework | Engineering, conversation, evaluation, agents | Agent Standard; Engineering Standards |
| Reasoning protocol | `12_PULSE_Reasoning_and_Question_System.md` | DNA; Framework; Technical Foundations | Narratives, conversation, agents, decision patterns | System Instruction; prompt recipes |
| Question taxonomy | `12_PULSE_Reasoning_and_Question_System.md` | DNA; Framework | Workshops, conversation, agents, recipes | Conversational Analytics; Prompting examples |
| Narrative System | `07_PULSE_Narrative_System.md` | DNA; Framework; Reasoning System | Dashboards, briefs, conversation, agents | Smart-narrative examples; System Instruction |
| Decision Patterns | `06_PULSE_Decision_Patterns.md` | DNA; Framework; Reasoning System | Pattern Library, cases, workshops | Experience Pattern Library; reference cases |
| Experience patterns | `05_PULSE_Pattern_Library.md` | Experience Principles; Decision Patterns; Narrative System | Components, engineering, examples | Component Library; Design System |
| Experience Components | `08_PULSE_Component_Library.md` | Design System; Pattern Library; Experience Principles | Engineering and reference implementations | Pattern Library; example code |
| Visual and interaction design tokens | `04_PULSE_Design_System.md` | Experience Principles | Components, Engineering, examples | Component Library; repositories |
| Engineering requirements | `13_PULSE_Engineering_Standards.md` | Experience, Trust, Conversation, Components | GitHub implementations and technical reviews | Example repositories; coding snippets |
| Decision Experience evaluation rubric | `14_PULSE_Decision_Experience_Evaluation.md` | DNA; Framework; Experience; Trust; Narrative | Release reviews, dashboard audits, agent tests | Reference cases; project-specific scorecards |
| Reference implementation governance | `15_PULSE_Reference_Implementations.md` | Evaluation; Engineering; all relevant systems | GitHub, classes, workshops, proposals | Individual repositories or gallery pages |
| GitHub reference implementations | `15_PULSE_Reference_Implementations.md` | Engineering Standards; Evaluation | Articles, classes, product demos | Repository README files; social posts |
| Agent operating rules | `16_PULSE_Agent_Operating_Standard.md` | DNA; Data Trust; Reasoning; Conversation; Narrative | GPT instruction, agent evaluations, prompt recipes | GPT System Instruction; ad hoc prompts |
| Official GPT behavior | `17_PULSE_GPT_System_Instruction.md` | Agent Operating Standard and all approved sources | GPT runtime only | No human-readable methodology document |

### 6.1 Ownership interpretation rules

1. **Canonical definitions remain in the DNA even when a dedicated operational document exists.** For example, the DNA owns the formal meaning of Data Trust; `10_PULSE_Data_Trust_and_Governance.md` owns the operating model used to assess and govern it.
2. **A system document owns methods, not constitutional meaning.** The Conversational Analytics document owns readiness, answer contracts, and interaction rules; it does not own the canonical definition of PULSE or the ethical position on human accountability.
3. **Patterns and components are different.** A pattern describes a reusable solution to a recurring experience or decision problem. A component is a reusable building block used to implement one or more patterns.
4. **Identity and Manifesto remain expressive layers.** Identity owns mission, vision, positioning, and audiences. The Manifesto owns the rhetorical commitments used to mobilize belief. Neither owns the constitutional definition.
5. **The GPT System Instruction owns no methodology concept.** It owns only the behavior of a specific system implementation.

---

## 7. Existing Document Assessment

### 7.1 Assessment method and confidence boundary

Because the full text of the existing `00_PULSE_Identity.md` through `08_PULSE_Component_Library.md` was not available in the working source set, the assessments below distinguish three kinds of statements:

- **Verified:** established by `00_PULSE_DNA.md` or the declared document architecture.
- **Required:** a governance condition the document must satisfy.
- **Review test:** a likely risk or question to inspect when the file becomes available; it is not presented as a confirmed defect.

No existing file should be approved, rewritten, merged, or retired solely from filename inference. The recommended status for all nine files is therefore **Pending Review**, with a specific review disposition.

### 7.2 `00_PULSE_Identity.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Express what PULSE is, for whom it exists, how it is positioned, and how it should be recognized without reproducing the full constitution. |
| **Alignment with the DNA** | Structurally aligned if it derives its definition, scope, and boundaries from the DNA. Content alignment remains unverified. |
| **Valuable content to preserve** | Distinctive mission and vision language; audience framing; positioning; concise value proposition; recognizability; any wording traceable to Javier Forero’s established voice. |
| **Conceptual conflicts — review tests** | Does it reduce PULSE to dashboards, BI, HTML, or AI? Does it define PULSE differently from the DNA? Does it present a technology maturity ladder as decision health? Does it promise autonomous decision-making as the destination? |
| **Missing concepts — review tests** | Decision-centered positioning; interface independence; trusted data and context; action and learning; Human-in-Control; dashboards as bridge rather than identity. |
| **Repeated concepts — review tests** | Full definitions of Decision Circle, PDAMR, Data Trust, or principles that should be linked to the DNA or Framework. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Conduct a line-by-line constitutional audit. Adjust rather than expand. Keep the file concise and expressive. If it contains an incompatible independent definition, rewrite that section rather than the entire document by default. |
| **Must depend on** | `00_PULSE_DNA.md`; `00A_PULSE_Documentation_Map.md`. |
| **Documents that depend on it** | Manifesto; external introductions; proposals; partner material; high-level product positioning. |

### 7.3 `01_PULSE_Manifesto.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Mobilize what PULSE believes and the commitments it asks practitioners to make. It is rhetorical and normative, not definitional or evidentiary. |
| **Alignment with the DNA** | Structurally aligned if every proposition can be traced to a DNA principle, boundary, or aspiration. Content alignment remains unverified. |
| **Valuable content to preserve** | Memorable language; emotional force; contrast between technology-centered and decision-centered practice; commitments to truth, context, responsibility, action, and learning. |
| **Conceptual conflicts — review tests** | Does it present aspirations as established outcomes? Does it imply dashboards are obsolete, conversation is always superior, speed always wins, or automation is inherently more mature? |
| **Missing concepts — review tests** | Evidence discipline; uncertainty; Human-in-Control; governance as an enabler; learning as completion of the decision cycle. |
| **Repeated concepts — review tests** | Long explanations of scientific foundations, operating stages, or component behavior. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Audit every statement against the DNA evidence posture. Preserve brevity and force. Convert unsupported universal claims into commitments, directions, or hypotheses. |
| **Must depend on** | DNA and Identity. |
| **Documents that depend on it** | Cultural onboarding, keynote material, community communication. No technical document should depend on manifesto rhetoric for a requirement. |

### 7.4 `02_PULSE_Framework.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Define how PULSE works as an operational decision methodology. This is the primary downstream methodology document. |
| **Alignment with the DNA** | It must operationalize—not redefine—the Decision Circle, PDAMR, transformation chain, five verbs, principles, decision health, value measures, and learning loop. Content alignment remains unverified. |
| **Valuable content to preserve** | Practical stages, workshop flows, diagnostics, roles, inputs, outputs, decision artifacts, measurement logic, and examples that have been used successfully in Javier Forero’s work or teaching. |
| **Conceptual conflicts — review tests** | Does it begin with dashboards or tools rather than priorities and decisions? Does it use a linear maturity ladder? Does it separate decision from action so completely that execution disappears? Does it omit risk, ownership, context, or learning? |
| **Missing concepts — review tests** | Explicit decision owner; current and target decision latency; uncertainty; internal capacity sensing; value baseline; first- and second-order risk; expected-versus-observed learning. |
| **Repeated concepts — review tests** | Constitutional definitions, scientific explanations, design rules, and implementation details. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Perform the first and deepest content audit after this map. If the existing structure predates the DNA and is dashboard-centric, use a controlled rewrite rather than incremental patching. Preserve validated methods and examples as traceable modules. |
| **Must depend on** | DNA, Documentation Map, Identity. |
| **Documents that depend on it** | Technical Foundations for methodological context; Decision Patterns; Narrative System; Reasoning and Question System; Experience Principles; Data Trust and Governance; Evaluation. |

### 7.5 `03_PULSE_Technical_Foundations.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Explain why the methodology’s foundations are credible and where PULSE is synthesis, analogy, practical judgment, aspiration, or testable hypothesis. |
| **Alignment with the DNA** | Must support the DNA’s evidence posture and preserve the limits of organizational analogies. Content alignment remains unverified. |
| **Valuable content to preserve** | Sources and explanations for information asymmetry, dispersed knowledge, alostasis, interoception, systems thinking, decision science, organizational learning, and human-centered design. |
| **Conceptual conflicts — review tests** | Does it claim PULSE invented the external theories? Does it treat organizations as literal organisms? Does it overstate empirical support for the complete PULSE synthesis? Does it use weak secondary sources where primary sources are available? |
| **Missing concepts — review tests** | Clear claim taxonomy; counterarguments; known limitations; boundary between scientific evidence and managerial analogy; falsifiable hypotheses for PULSE applications. |
| **Repeated concepts — review tests** | Full operational methodology, extensive manifesto language, or design-system rules. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Evidence audit with source quality grading. Add explicit “what is supported / what is synthesized / what remains to be tested” boundaries. |
| **Must depend on** | DNA and original source material. It should reference the Framework only to explain what requires support, not to inherit authority over external evidence. |
| **Documents that depend on it** | Framework, Reasoning and Question System, Data Trust and Governance, educational material, research notes. |

### 7.6 `04_PULSE_Design_System.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Give PULSE a coherent visual and interaction language across decision experiences. |
| **Alignment with the DNA** | Must serve clarity, trust, action, accessibility, Mobile First, progressive disclosure, and interface independence. Content alignment remains unverified. |
| **Valuable content to preserve** | Validated typography, color, spacing, layout, hierarchy, visualization grammar, interaction states, responsive behavior, and brand-recognition elements. |
| **Conceptual conflicts — review tests** | Does visual consistency take priority over decision usefulness? Does the system assume desktop dashboards as the default? Are colors or components given semantic meaning without accessibility and uncertainty safeguards? |
| **Missing concepts — review tests** | Mobile baseline; accessible contrast and non-color encoding; uncertainty display; evidence links; action states; empty/error/stale-data states; conversational and embedded-interface compatibility. |
| **Repeated concepts — review tests** | Experience principles, decision patterns, component specifications, or coding rules. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Freeze major expansion until `09_PULSE_Experience_Principles.md` is approved. Then audit every token and rule against those principles. |
| **Must depend on** | DNA, Experience Principles, Data Trust and Governance where visual states express trust or permissions. |
| **Documents that depend on it** | Pattern Library, Component Library, Engineering Standards, Reference Implementations. |

### 7.7 `05_PULSE_Pattern_Library.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Define reusable experience approaches that coordinate several components to solve recurring user and decision needs. |
| **Alignment with the DNA** | Must be interface-aware but not interface-bound; patterns should reduce uncertainty, reveal evidence, support action, and preserve control. Content alignment remains unverified. |
| **Valuable content to preserve** | Pattern anatomy, context of use, decision problem, prerequisites, interaction flow, accessibility behavior, anti-patterns, and examples. |
| **Conceptual conflicts — review tests** | Does it duplicate Decision Patterns? Does it treat a card, chart, or layout as a pattern without a recurring problem? Does it encode one dashboard layout as universal? |
| **Missing concepts — review tests** | Selection criteria; contraindications; required trust state; mobile behavior; conversation handoff; action and learning connection; version compatibility. |
| **Repeated concepts — review tests** | Component anatomy, design tokens, decision-method definitions, narrative templates. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Reclassify entries into decision patterns, experience patterns, components, or examples. Retain only cross-component experience solutions in this file. |
| **Must depend on** | DNA, Experience Principles, Decision Patterns, Narrative System, Design System. |
| **Documents that depend on it** | Component compositions, Engineering Standards, Reference Implementations, Evaluation. |

### 7.8 `06_PULSE_Decision_Patterns.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Define reusable methodological responses to recurring decision situations, such as threshold escalation, scenario comparison, prioritization, anomaly response, or capacity-constrained choice. |
| **Alignment with the DNA** | Must instantiate the Decision Circle, PDAMR, option generation, ownership, risk, action, and learning. Content alignment remains unverified. |
| **Valuable content to preserve** | Decision context, triggering question, evidence required, alternatives, constraints, accountable role, cadence, action, result metric, and learning mechanism. |
| **Conceptual conflicts — review tests** | Does it redefine the Decision Circle or PDAMR? Are patterns merely visual layouts? Do they assume prediction or automation is always superior? |
| **Missing concepts — review tests** | Reversibility; uncertainty; first- and second-order risk; stop conditions; Human-in-Control; post-decision observation. |
| **Repeated concepts — review tests** | Question taxonomy, narrative rules, component layouts, or engineering implementation. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Audit every entry against a common decision-pattern schema. Move visual-only entries to the Pattern Library and example-only entries to Reference Implementations. |
| **Must depend on** | DNA, Framework, Reasoning and Question System. |
| **Documents that depend on it** | Narrative System, Experience Pattern Library, Conversational Analytics, Reference Implementations. |

### 7.9 `07_PULSE_Narrative_System.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Define how evidence is translated into clear, contextual, decision-supporting language without overstating certainty. |
| **Alignment with the DNA** | Must preserve the distinctions among data, information, understanding, idea, recommendation, decision, action, result, and learning. Content alignment remains unverified. |
| **Valuable content to preserve** | Executive structures; DATA → IDEA → DECISIÓN applications; prioritization logic; narrative hierarchy; uncertainty language; evidence links; tone patterns; smart-narrative templates. |
| **Conceptual conflicts — review tests** | Does it infer causes from correlation? Does it turn recommendations into decisions? Does it omit evidence, uncertainty, or counterevidence? Does it allow persuasive tone to outrun analytical support? |
| **Missing concepts — review tests** | Claim-evidence contract; confidence labels; alternative explanations; audience and decision context; action owner; generated-text traceability; multilingual canonical-term handling. |
| **Repeated concepts — review tests** | Question taxonomy, conversational turn rules, design tokens, or canonical term definitions. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Audit narrative templates for claim safety and concept precision. Define interfaces with the Reasoning System and Conversational Analytics before expanding. |
| **Must depend on** | DNA, Framework, Reasoning and Question System, Data Trust and Governance. |
| **Documents that depend on it** | Design and Pattern Libraries, Conversational Analytics, Agent Operating Standard, Evaluation, Reference Implementations. |

### 7.10 `08_PULSE_Component_Library.md`

| Assessment dimension | Diagnosis |
|---|---|
| **Current role** | **Verified:** Specify reusable experience building blocks and their states, properties, accessibility behavior, and composition rules. |
| **Alignment with the DNA** | Must implement—not define—decision, trust, narrative, and experience principles. Content alignment remains unverified. |
| **Valuable content to preserve** | Component inventory; anatomy; variants; states; responsive behavior; accessibility semantics; data requirements; interaction contracts; code references. |
| **Conceptual conflicts — review tests** | Are components treated as methodology? Are chart types named as decision patterns? Are trust, uncertainty, or action states omitted? Are components desktop-only? |
| **Missing concepts — review tests** | Stale/partial/unavailable data states; provenance; confidence; permission-denied states; mobile behavior; keyboard and screen-reader support; action confirmation and rollback. |
| **Repeated concepts — review tests** | Design tokens, patterns, narrative templates, or coding standards. |
| **Recommended status** | **Pending Review** |
| **Recommended action** | Audit after Experience Principles, Design System, and Pattern Library boundaries are approved. Assign every component to at least one governed pattern and one evaluation criterion. |
| **Must depend on** | DNA, Experience Principles, Design System, Pattern Library, Data Trust and Governance. |
| **Documents that depend on it** | Engineering Standards, Evaluation, Reference Implementations. |

### 7.11 Cross-document audit priorities

When the current files become available, the audit should test these risks first:

1. **Definition drift:** multiple files independently define PULSE, Decision Intelligence, Decision Experience, Data Trust, or Human-in-Control.
2. **Dashboard centrality:** PULSE is framed as a dashboard methodology rather than a decision methodology.
3. **Technology ladder logic:** advanced interfaces are treated as inherently more mature.
4. **Missing action and learning:** documents end at analysis, visualization, or recommendation.
5. **Unsupported certainty:** narratives and technical claims blur evidence, synthesis, aspiration, and hypothesis.
6. **Pattern/component confusion:** visual building blocks, experience patterns, and decision patterns are mixed.
7. **Mobile as adaptation rather than baseline:** desktop structures are merely compressed.
8. **Agent instruction as hidden source:** prompts introduce concepts or rules that do not exist in approved documentation.

---
## 8. Required New Documents

The documents below close genuine gaps between the constitutional DNA and repeatable implementation. They are the minimum governed set, not a complete list of every artifact PULSE may eventually produce.

### 8.1 `09_PULSE_Experience_Principles.md`

| Field | Definition |
|---|---|
| **Purpose** | Translate DNA principles into non-negotiable rules for designing any PULSE Decision Experience, regardless of interface. |
| **Concepts owned** | Experience principles; smallest meaningful decision experience; Mobile First implementation; progressive disclosure; interface-selection criteria; accessibility baseline; action connection; evidence visibility; replaceability. |
| **Inputs** | DNA; Framework; Data Trust requirements; lessons from existing Design, Pattern, Narrative, and Component documents. |
| **Outputs** | Normative experience rules; design decision tests; interface-selection matrix; required experience states; handoff requirements to design and engineering. |
| **Dependencies** | `00_PULSE_DNA.md`, `00A_PULSE_Documentation_Map.md`, `02_PULSE_Framework.md`, `10_PULSE_Data_Trust_and_Governance.md`. |
| **Why it must exist separately** | Principles are more stable and authoritative than visual tokens, patterns, or components. Merging them into the Design System would make PULSE appear visual-interface dependent. |
| **What it must not repeat** | The full DNA definition of Decision Experience, detailed visual tokens, component specifications, engineering code, or client examples. |
| **Creation priority** | **P1 — Required before other experience documents are revised.** |

The central design question for this document is not “What should a PULSE interface look like?” It is “What conditions must any interface satisfy to improve a decision without weakening trust or responsibility?”

### 8.2 `10_PULSE_Data_Trust_and_Governance.md`

| Field | Definition |
|---|---|
| **Purpose** | Operationalize Trust First and Governance Enables Speed as a decision-specific control system. |
| **Concepts owned** | Data fitness-for-purpose model; trust dimensions; trust-state labels; semantic ownership; stewardship; provenance and lineage requirements; permissions; privacy; traceability; decision-risk tiers; evidence readiness; governance controls; exception and escalation paths. |
| **Inputs** | DNA; Framework; Technical Foundations; source material on data architecture, context, AI amplification, and Human-in-Control. |
| **Outputs** | Trust assessment; governance control matrix; decision-risk classification; readiness gates for dashboards, conversation, copilots, and bounded action; required metadata. |
| **Dependencies** | DNA, Documentation Map, Framework, Technical Foundations. |
| **Why it must exist separately** | Trust and governance cut across every interface and require owners, controls, and review cadence distinct from methodology, design, or engineering. |
| **What it must not repeat** | Generic enterprise data-governance theory; the DNA’s canonical definitions; platform-specific implementation; complete security or legal policies. |
| **Creation priority** | **P1 — Required before Conversational Analytics, Engineering Standards, and Agent behavior.** |

This document should treat trust as contextual. The question is not “Are these data trustworthy?” in the abstract. It is “Are these data sufficiently fit, understood, permissioned, and traceable for this decision and consequence?”

### 8.3 `11_PULSE_Conversational_Analytics.md`

| Field | Definition |
|---|---|
| **Purpose** | Define the governed operating system for asking questions of organizational evidence through natural language. |
| **Concepts owned** | Conversational use-case taxonomy; readiness model; answer contract; evidence citation; clarification behavior; follow-up context; semantic resolution; permissions; uncertainty disclosure; fallback; escalation; conversation-to-action boundary; Decision Copilot behavior at the product level. |
| **Inputs** | DNA; Framework; Data Trust and Governance; Reasoning and Question System; Narrative System; Experience Principles. |
| **Outputs** | Product requirements; conversational flows; answer-state model; safety and fallback rules; readiness checklist; evaluation criteria passed to `14_PULSE_Decision_Experience_Evaluation.md`. |
| **Dependencies** | DNA, Framework, Data Trust and Governance, Reasoning and Question System, Narrative System, Experience Principles. |
| **Why it must exist separately** | Conversation changes access, interaction, ambiguity, permissions, and failure modes. These requirements are not adequately owned by the Narrative System or Design System. |
| **What it must not repeat** | Canonical definitions; general prompting advice; detailed model orchestration code; all narrative templates; the GPT’s final system instruction. |
| **Creation priority** | **P2 — Core operational.** |

The document must preserve a critical distinction: natural language lowers interaction friction; it does not automatically increase truth, context, or legitimacy.

### 8.4 `12_PULSE_Reasoning_and_Question_System.md`

| Field | Definition |
|---|---|
| **Purpose** | Define how PULSE converts business priorities into answerable questions and evidence-based reasoning without hiding assumptions, alternatives, or uncertainty. |
| **Concepts owned** | Question taxonomy; decision-question structure; reasoning protocol; assumption register; hypothesis testing; evidence hierarchy; alternative explanations; counterargument; uncertainty treatment; option comparison; learning questions. |
| **Inputs** | DNA; Framework; Technical Foundations; Data Trust and Governance; Javier Forero’s teaching material and decision-centered examples. |
| **Outputs** | Question templates; reasoning workflow; evidence and uncertainty checks; reusable structures for human workshops, narratives, conversation, and agents. |
| **Dependencies** | DNA, Framework, Technical Foundations, Data Trust and Governance. |
| **Why it must exist separately** | Reasoning is a cross-interface cognitive system. It should not be hidden in prompts, narrative templates, or decision patterns. Questions and reasoning share one lifecycle and should remain together. |
| **What it must not repeat** | The Decision Circle definition; the entire Framework; narrative style rules; interface behavior; code or model-chain implementation. |
| **Creation priority** | **P1 — Required before Decision Patterns, Narrative System, Conversation, and agents are finalized.** |

The combined document is superior to separate Reasoning and Question files because a question taxonomy without a reasoning contract becomes a list of prompts, while a reasoning framework without question design lacks a disciplined entry point.

### 8.5 `13_PULSE_Engineering_Standards.md`

| Field | Definition |
|---|---|
| **Purpose** | Convert approved PULSE methodology, trust, experience, pattern, and component requirements into maintainable technical standards. |
| **Concepts owned** | Reference HTML architecture; coding standards; repository structure; data contracts; semantic payloads; accessibility implementation; responsive behavior; performance budgets; error and stale-data handling; observability; testing; security integration; GitHub Pages deployment. |
| **Inputs** | Experience Principles; Data Trust and Governance; Conversational Analytics; Design System; Pattern Library; Component Library; evaluation requirements. |
| **Outputs** | Normative engineering requirements; reference project structure; test checklist; schema registry; deployment and versioning rules. |
| **Dependencies** | DNA and all relevant Layer 2–4 systems. |
| **Why it must exist separately** | Engineering standards change faster than the methodology and require technical ownership, versioning, and testability. HTML, coding, and data contracts belong to one implementation lifecycle. |
| **What it must not repeat** | Methodology definitions; generic language tutorials; vendor documentation; complete component examples that belong in reference repositories. |
| **Creation priority** | **P3 — Implementation.** |

Machine-readable schemas may live in `/schemas` and be versioned independently, but their purpose, ownership, compatibility, and change rules remain governed by this document.

### 8.6 `14_PULSE_Decision_Experience_Evaluation.md`

| Field | Definition |
|---|---|
| **Purpose** | Provide an interface-independent method to determine whether a PULSE experience is useful, trustworthy, usable, governable, and ready for release. |
| **Concepts owned** | Evaluation model; acceptance gates; scoring and evidence requirements; decision-value review; trust and governance review; reasoning quality; narrative quality; accessibility; mobile baseline; action connection; learning-loop verification; agent-output evaluation interfaces. |
| **Inputs** | DNA Decision Test; Framework outcomes; Experience Principles; Data Trust and Governance; Narrative System; Conversational Analytics; Engineering Standards. |
| **Outputs** | Audit report; release decision; severity classification; remediation backlog; evidence record; approval or rejection status. |
| **Dependencies** | All normative documents relevant to the evaluated experience. |
| **Why it must exist separately** | Evaluation is a governance function with an independent reviewer audience. A dashboard-only review would contradict interface independence. |
| **What it must not repeat** | Full design rules, trust controls, or engineering standards. It references them and defines how compliance and decision value are tested. |
| **Creation priority** | **P2 — Core operational, before examples are approved.** |

The evaluation must not collapse into a cosmetic score. A visually strong artifact that does not improve a defined decision, expose evidence, support action, or preserve control must fail regardless of aesthetics.

### 8.7 `15_PULSE_Reference_Implementations.md`

| Field | Definition |
|---|---|
| **Purpose** | Curate approved examples, recipes, templates, case studies, and GitHub repositories as contextual evidence of PULSE application. |
| **Concepts owned** | Reference-entry schema; approval status; context and constraints; implemented principles; source-data status; version compatibility; known limitations; reuse conditions; lessons learned. |
| **Inputs** | Approved implementations; evaluation reports; engineering documentation; case evidence; repository metadata. |
| **Outputs** | Searchable catalog; gallery views; cookbook recipes; links to repositories; case summaries; deprecation notices. |
| **Dependencies** | Evaluation, Engineering Standards, and every system an example claims to implement. |
| **Why it must exist separately** | Examples require curation and lifecycle management but do not belong in normative documents. Combining gallery and cookbook prevents aesthetic examples from being detached from context and reuse rules. |
| **What it must not repeat** | Canonical definitions; entire codebases; unsupported success claims; client-confidential information; unreviewed experiments presented as standards. |
| **Creation priority** | **P4 — Examples and expansion.** |

The actual artifacts may live in subfolders or separate repositories. This document is the governed registry that tells users which artifacts are canonical, experimental, deprecated, or illustrative only.

### 8.8 `16_PULSE_Agent_Operating_Standard.md`

| Field | Definition |
|---|---|
| **Purpose** | Define how AI systems should retrieve, reason over, communicate, evaluate, and act on PULSE knowledge before those rules are encoded in a system instruction. |
| **Concepts owned** | Agent retrieval precedence; authority-aware grounding; prompt patterns; tool-use rules; evidence and citation behavior; uncertainty; clarification and assumption handling; Human-in-Control checkpoints; escalation; memory boundaries; output review; test suite. |
| **Inputs** | All approved constitutional, foundational, system, trust, experience, narrative, and evaluation documents. |
| **Outputs** | Human-readable agent specification; traceability matrix; prompt pattern library; evaluation cases; generation requirements for the GPT System Instruction. |
| **Dependencies** | DNA, Documentation Map, Framework, Data Trust and Governance, Conversational Analytics, Reasoning and Question System, Narrative System, Evaluation. |
| **Why it must exist separately** | Human-readable agent governance must be inspectable and discussable independently from one platform’s executable instruction syntax. Prompting, retrieval, tools, and evaluation are one operating system. |
| **What it must not repeat** | Full methodology documents; product-specific secrets; ungoverned hidden reasoning requirements; a copy of the final GPT System Instruction. |
| **Creation priority** | **P3 — Implementation, after upstream systems stabilize.** |

A public-facing Prompting Guide may later be extracted from this standard if there is a stable, distinct user audience. Until then, maintaining two parallel prompt documents would create unnecessary drift.

### 8.9 `17_PULSE_GPT_System_Instruction.md`

| Field | Definition |
|---|---|
| **Purpose** | Encode the approved behavior of the official PULSE GPT in an executable, platform-appropriate instruction artifact. |
| **Concepts owned** | No methodology concepts. It owns the runtime behavior of the official GPT implementation. |
| **Inputs** | Every approved source required by the Agent Operating Standard, with version references. |
| **Outputs** | Executable system instruction; source-mapping header; version and compatibility metadata; behavioral test results. |
| **Dependencies** | All canonical human-readable documents, especially `16_PULSE_Agent_Operating_Standard.md`. |
| **Why it must exist separately** | Executable instructions require platform-specific structure, release control, and testing. They must not clutter or replace human-readable governance. |
| **What it must not repeat** | Entire source documents; new definitions; hidden policy changes; unsupported autonomy; implementation guidance unrelated to runtime behavior. |
| **Creation priority** | **P3 — Generated last within the core documentation sequence.** |

The System Instruction must include a source mapping that identifies which approved document governs each major behavior. A behavior with no approved source is a defect, not an innovation.

### 8.10 Documents explicitly not required as independent files

The following topics are important but do not currently justify separate canonical documents:

- **A standalone Mobile First document.** Mobile First is constitutionally defined in the DNA and operationalized in Experience Principles, Design System, Components, Engineering, and Evaluation.
- **A standalone Human-in-Control document.** The definition remains in the DNA; governance controls belong in Data Trust and Governance; agent-specific implementation belongs in the Agent Operating Standard.
- **A standalone Accessibility document.** Accessibility is an experience principle and engineering requirement. A separate file may be created only if regulatory depth or organizational ownership later requires an independent lifecycle.
- **A standalone Semantic Layer document.** Semantics are governed in Data Trust and Governance and implemented through Engineering Standards and schemas.
- **A standalone GitHub Pages guide.** Deployment is one section of Engineering Standards; repositories provide implementation-specific README files.
- **A standalone Dashboard methodology.** Dashboards are one Decision Experience form and remain covered by Experience Principles, Narrative System, patterns, components, engineering, and evaluation.

---

## 9. Dependency Graph

### 9.1 Canonical dependency graph

```text
JAVIER FORERO'S ORIGINAL THOUGHT AND SOURCE MATERIAL
    |
    v
00_PULSE_DNA.md  [constitutional content]
    |
    +------------------------------+
    |                              |
    v                              v
00A_PULSE_Documentation_Map.md     00_PULSE_Identity.md
    |                              |
    |                              v
    |                          01_PULSE_Manifesto.md
    |
    +------------------------------+
    |
    v
02_PULSE_Framework.md <------ 03_PULSE_Technical_Foundations.md
    |                              |
    +---------------+--------------+
                    |
          +---------+----------+
          |                    |
          v                    v
12_PULSE_Reasoning_and_       10_PULSE_Data_Trust_
Question_System.md            and_Governance.md
          |                    |
          +----+-----------+---+
               |           |
               v           v
06_PULSE_Decision_       09_PULSE_Experience_
Patterns.md              Principles.md
               |           |
               v           +----------------+
07_PULSE_Narrative_      |                |
System.md                v                v
               |      04_PULSE_       05_PULSE_
               |      Design_System   Pattern_Library
               |                       |
               +-----------+-----------+
                           |
                           v
                08_PULSE_Component_Library.md
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
11_PULSE_Conversational_          13_PULSE_Engineering_
Analytics.md                      Standards.md
          |                                 |
          +----------------+----------------+
                           |
                           v
              14_PULSE_Decision_Experience_
              Evaluation.md
                           |
                           v
              15_PULSE_Reference_
              Implementations.md

All approved constitutional, foundational, system,
trust, experience, and evaluation documents
                           |
                           v
              16_PULSE_Agent_Operating_
              Standard.md
                           |
                           v
              17_PULSE_GPT_System_
              Instruction.md
```

### 9.2 Dependency rules

1. **The DNA precedes every document.** The Documentation Map may be created immediately after the DNA because it governs the revision sequence.
2. **The Framework and Technical Foundations are parallel but mutually informative.** The Framework owns operating methodology; Technical Foundations explains support and limits. Neither may use the other to override the DNA.
3. **Reasoning and Trust precede conversation.** A conversational system without a question/reasoning protocol and trust controls is not ready.
4. **Experience Principles precede the Design System, Pattern Library, and Component Library.** Otherwise visual precedent becomes an accidental principle.
5. **Decision Patterns precede experience patterns when the experience claims to support a recurring decision.** The decision problem must be known before its interaction pattern is standardized.
6. **Narrative System precedes generated narratives and conversational answer generation.** Evidence-to-claim rules cannot be invented inside prompts.
7. **Engineering Standards follow approved experience and trust requirements.** Code must implement governed behavior rather than define it.
8. **Evaluation precedes reference status.** An artifact may be experimental before evaluation; it becomes a PULSE reference only after passing the appropriate gate.
9. **Agent documents come last.** The Agent Operating Standard synthesizes approved sources; the GPT System Instruction encodes that standard.

### 9.3 Recommended creation and revision sequence

| Sequence | Work item | Reason |
|---:|---|---|
| 1 | Approve `00A_PULSE_Documentation_Map.md` | Establish ownership and prevent downstream rework. |
| 2 | Audit `00_PULSE_Identity.md`, `01_PULSE_Manifesto.md`, `02_PULSE_Framework.md`, and `03_PULSE_Technical_Foundations.md` | Stabilize the foundational layer. Framework receives the deepest audit. |
| 3 | Create `10_PULSE_Data_Trust_and_Governance.md` and `12_PULSE_Reasoning_and_Question_System.md` | Establish the prerequisites for trustworthy reasoning and conversation. |
| 4 | Create `09_PULSE_Experience_Principles.md` | Establish cross-interface experience rules before visual and component revisions. |
| 5 | Audit `06_PULSE_Decision_Patterns.md` and `07_PULSE_Narrative_System.md` | Align reusable decision and communication systems with the Framework, reasoning, and trust. |
| 6 | Create `11_PULSE_Conversational_Analytics.md` | Build conversation on approved trust, reasoning, narrative, and experience foundations. |
| 7 | Audit `04_PULSE_Design_System.md`, `05_PULSE_Pattern_Library.md`, and `08_PULSE_Component_Library.md` | Resolve principles, patterns, and components after upstream systems are stable. |
| 8 | Create `13_PULSE_Engineering_Standards.md` | Translate approved requirements into code, schemas, testing, and deployment. |
| 9 | Create `14_PULSE_Decision_Experience_Evaluation.md` | Establish release gates and audit methods. |
| 10 | Create `15_PULSE_Reference_Implementations.md` | Curate only evaluated examples and repositories. |
| 11 | Create `16_PULSE_Agent_Operating_Standard.md` | Define human-readable behavior and evaluation for PULSE agents. |
| 12 | Generate and test `17_PULSE_GPT_System_Instruction.md` | Produce the executable derivative last. |

---

## 10. Documentation Governance and Change Control

### 10.1 Document ownership roles

| Role | Responsibility |
|---|---|
| **Methodology Owner** | Final authority for constitutional interpretation, mission fidelity, and approval of P0/P1 changes. Initially Javier Forero. |
| **Document Owner** | Maintains the purpose, scope, accuracy, dependencies, and review cadence of one canonical document. |
| **Concept Steward** | Monitors the use of a canonical concept across documents and flags drift or duplication. One steward may cover several related concepts. |
| **Evidence Reviewer** | Assesses source quality, claim type, uncertainty, and the boundary between evidence, synthesis, analogy, aspiration, and hypothesis. |
| **Experience Reviewer** | Tests whether interfaces implement experience principles, accessibility, trust, action, and learning requirements. |
| **Engineering Maintainer** | Maintains implementation standards, schemas, test tooling, and compatibility. |
| **Knowledge Base Curator** | Maintains metadata, authority-aware retrieval, aliases, archives, and source mapping. |
| **Agent Maintainer** | Generates, tests, and releases executable agent instructions from approved sources without adding hidden methodology. |

One person may hold several roles during early development, but the responsibilities remain distinct.

### 10.2 Change classes

| Change class | Examples | Required approval | Version impact |
|---|---|---|---|
| **Constitutional** | Official definition, core thesis, principles, canonical terms, ethical boundaries, long-term aspiration. | Methodology Owner; evidence review where relevant; impact assessment across all documents. | DNA major or minor version; mandatory downstream review. |
| **Governance architecture** | Concept owner, document role, layer, canonical filename, merge/retire decision, authority level. | Methodology Owner and Documentation Map owner. | Map minor or major version; KB migration plan. |
| **Methodology** | Framework stages, decision-pattern schema, reasoning protocol, trust operating model. | Document Owner plus Methodology Owner. | Minor or major version depending compatibility. |
| **Standard** | Design tokens, component behavior, engineering requirements, evaluation thresholds. | Document Owner and affected reviewers. | Minor for additive compatible change; major for breaking change. |
| **Editorial** | Clarity, grammar, examples, non-normative explanation. | Document Owner. | Patch version. |
| **Reference** | New example, recipe, case, or repository version. | Evaluation approval and Reference curator. | Catalog patch or minor version. |
| **Executable** | GPT instruction wording, tool rule, retrieval configuration. | Agent Maintainer plus source owner for affected behavior; tests required. | Runtime release version; source mapping updated. |

### 10.3 Change proposal requirements

Every non-editorial proposal must include:

1. Problem being solved.
2. Proposed change.
3. Authoritative concept affected.
4. Current owner and proposed owner.
5. Source evidence or implementation learning.
6. Compatibility impact.
7. Documents, schemas, repositories, and agent behaviors affected.
8. First- and second-order risks.
9. Migration and deprecation plan.
10. Tests or observations that would validate the change.

A change is not approved because it sounds clearer or more modern. It must improve coherence, fidelity, usefulness, evidence, maintainability, or safety.

### 10.4 Conflict resolution protocol

When two documents conflict:

1. Identify the exact concept or requirement in conflict.
2. Consult the Concept Ownership Matrix.
3. Apply the source authority hierarchy.
4. Determine whether the lower-authority text is a legitimate implementation refinement or an actual redefinition.
5. Correct the lower-authority document.
6. Record the resolution if it changes interpretation, ownership, or downstream behavior.
7. Rebuild affected agent instructions and retrieval indexes.

When the DNA itself is ambiguous, the ambiguity must be resolved in the DNA—not patched independently in several downstream documents.

### 10.5 Versioning model

PULSE canonical documents use semantic versioning:

- **Major:** breaking change to purpose, ownership, canonical meaning, method, or required behavior.
- **Minor:** additive or materially improved content that remains compatible with prior use.
- **Patch:** editorial clarification, corrected citation, formatting, or non-normative example.

Every document header should include:

```yaml
file: 00_PULSE_DNA.md
version: 1.0.0
status: Approved
owner: Javier Forero
layer: 0
architecture_authority: A0
last_reviewed: YYYY-MM-DD
next_review: YYYY-MM-DD
supersedes: null
depends_on: []
concepts_owned: []
```

The exact serialization may change, but the metadata fields are mandatory for Knowledge Base ingestion.

### 10.6 Lifecycle states

| Status | Meaning |
|---|---|
| **Approved** | Canonical and authorized for use. |
| **Keep** | Approved content remains valid; only maintenance is required. |
| **Adjust** | Purpose remains valid; bounded revisions are required. |
| **Rewrite** | Purpose remains necessary, but the current structure or content is materially incompatible. |
| **Create** | Approved gap requiring a new document. |
| **Merge** | Content must move to a named canonical owner; the original file becomes a redirect or archive. |
| **Retire** | No longer needed and should not be used for current guidance. |
| **Archive** | Preserved for historical traceability but excluded from normal retrieval. |
| **Pending Review** | Structural role is known, but content has not been approved against current governance. |

“Keep,” “Adjust,” and “Rewrite” are action-oriented lifecycle states. Once the work is completed and approved, the document returns to “Approved.”

### 10.7 Deprecation and archival rules

A merged or retired document must contain a short tombstone header:

- Status.
- Date deprecated.
- Reason.
- Canonical replacement.
- Last valid version.
- Whether old links remain supported.

Archived material is excluded from default GPT retrieval and normal Knowledge Base search unless the user explicitly requests historical context.

---

## 11. Knowledge Base Organization

### 11.1 Recommended repository structure

```text
/pulse-docs
    /00_constitutional
        00_PULSE_DNA.md
        00A_PULSE_Documentation_Map.md
        /decision_records
    /01_foundational
        00_PULSE_Identity.md
        01_PULSE_Manifesto.md
        02_PULSE_Framework.md
        03_PULSE_Technical_Foundations.md
    /02_decision_reasoning
        06_PULSE_Decision_Patterns.md
        07_PULSE_Narrative_System.md
        11_PULSE_Conversational_Analytics.md
        12_PULSE_Reasoning_and_Question_System.md
    /03_experience_design
        09_PULSE_Experience_Principles.md
        04_PULSE_Design_System.md
        05_PULSE_Pattern_Library.md
        08_PULSE_Component_Library.md
    /04_trust_governance
        10_PULSE_Data_Trust_and_Governance.md
    /05_engineering
        13_PULSE_Engineering_Standards.md
        /schemas
        /tests
    /06_application_evidence
        14_PULSE_Decision_Experience_Evaluation.md
        15_PULSE_Reference_Implementations.md
        /cases
        /recipes
        /templates
    /07_agent_behavior
        16_PULSE_Agent_Operating_Standard.md
        17_PULSE_GPT_System_Instruction.md
        /evaluations
    /archive
```

Canonical filenames may retain their current numeric prefixes to avoid unnecessary link churn. Folder placement, metadata, and the Documentation Map provide the stronger architecture signal.

### 11.2 Required retrieval metadata

Every Knowledge Base chunk should carry:

- File name and version.
- Layer.
- Authority level.
- Approval status.
- Document owner.
- Section title.
- Concepts owned.
- Concepts supported.
- Dependencies.
- Effective date.
- Superseded or deprecated status.
- Evidence posture, where applicable.
- Intended audience.

Retrieval should rank authority before textual similarity when a query seeks a definition, principle, or rule.

### 11.3 Query routing rules

| User intent | Preferred source |
|---|---|
| “What is PULSE?” | DNA first; Identity for concise expression. |
| “What does PULSE believe?” | DNA principles, then Manifesto for rhetorical expression. |
| “How do I apply PULSE?” | Framework, then relevant decision/reasoning/trust/experience systems. |
| “Why is this credible?” | Technical Foundations and cited original sources. |
| “How should this decision be framed?” | Framework, Reasoning and Question System, Decision Patterns. |
| “How should this be narrated?” | Narrative System, with Trust and Reasoning prerequisites. |
| “How should the interface behave?” | Experience Principles, Pattern Library, Components, Design System. |
| “Can these data support this decision?” | Data Trust and Governance. |
| “How should this be built?” | Engineering Standards and approved Components. |
| “Is this a valid PULSE experience?” | Decision Experience Evaluation. |
| “Show me an example.” | Reference Implementations after normative sources are understood. |
| “How should the GPT behave?” | Agent Operating Standard; executable details in the GPT System Instruction. |

### 11.4 Retrieval anti-patterns

The Knowledge Base must prevent:

- An example outranking the DNA for a definition.
- A Manifesto sentence being treated as scientific evidence.
- An archived file being returned without a deprecation warning.
- A component description being treated as a decision pattern.
- The GPT System Instruction being cited as proof of methodology.
- General industry content overriding a canonical PULSE rule.
- A Spanish canonical expression being translated into a different concept without an explicit language note.

---

## 12. Maintenance Cadence

| Document class | Default review cadence | Triggered review events |
|---|---|---|
| DNA | Annual, unless active constitutional evolution requires more frequent review | New foundational concept; changed ethical boundary; altered official definition; accumulated unresolved conflicts. |
| Documentation Map | Quarterly during active build; semiannual after stabilization | New file proposal; merge/retire decision; concept ownership dispute; KB architecture change. |
| Identity and Manifesto | Semiannual | DNA change; positioning change; new primary audience. |
| Framework and Technical Foundations | Quarterly during development; semiannual after approval | New field evidence; validated implementation learning; method change; claim challenge. |
| Decision, reasoning, narrative, conversation, trust, and experience systems | Quarterly | New pattern class; material failure; regulatory or risk change; repeated implementation ambiguity. |
| Design, patterns, components, and engineering | At each planned release; at least quarterly | Browser/platform changes; accessibility issue; performance regression; new interface form. |
| Evaluation | Quarterly and after major upstream changes | New experience type; audit failure pattern; changed release threshold. |
| Reference Implementations | Continuous curation; quarterly status audit | Repository update; deprecated dependency; failed evaluation; broken link. |
| Agent Operating Standard and GPT Instruction | Each release; monthly during active iteration | Model/platform change; retrieval change; tool change; safety incident; upstream document update. |

A review does not require a revision. It requires an explicit decision: keep, adjust, rewrite, merge, retire, archive, or no change.

---

## 13. Governance Risks and Controls

| Risk | First-order effect | Second-order effect | Primary control |
|---|---|---|---|
| **Constitutional duplication** | Conflicting definitions. | Loss of trust in the entire Knowledge Base. | Concept Ownership Matrix and authority-aware retrieval. |
| **Document sprawl** | Harder navigation and maintenance. | More contradictions and lower agent grounding quality. | New-document admission test and merge-first policy. |
| **Over-centralization** | Every detail is forced into the DNA or Framework. | Core documents become unstable and unreadable. | Layered ownership and progressive disclosure. |
| **Over-fragmentation** | Thin files split one coherent system. | Users cannot reconstruct the method; updates become inconsistent. | Merge related topics with shared owner, audience, and cadence. |
| **Examples becoming doctrine** | Context-specific choices are generalized. | PULSE becomes aesthetically or technically narrow. | Evaluation metadata and explicit reuse conditions. |
| **Metaphor becoming proof** | Analogies are overstated. | Scientific credibility is damaged. | Technical Foundations evidence posture and analogy limits. |
| **Agent drift** | GPT behavior diverges from approved documentation. | Hidden methodology and inconsistent client advice emerge. | Agent Operating Standard, source mapping, tests, regeneration after upstream changes. |
| **Governance becoming bureaucracy** | Slow updates and abandoned maintenance. | Teams bypass the canonical system. | Proportionate change classes and clear decision rights. |
| **Silent breaking changes** | Existing examples or tools fail. | Historical decisions become unreproducible. | Semantic versioning, impact analysis, migration, deprecation. |
| **Authority confused with evidence** | High-level statements are accepted without challenge. | Confirmation bias and polished error. | Evidence Before Authority, evidence review, and challengeability. |

### 13.1 Best counterargument to this architecture

The strongest counterargument is that the proposed system remains too document-heavy for an evolving personal methodology. Nine new documents, governance metadata, versioning, and review roles could create overhead before PULSE has enough users or implementations to justify it.

That objection is valid. The response is not to produce all files at full depth immediately. The response is to preserve the **architecture now** while creating documents progressively according to dependency and use. A file may begin as a concise approved standard and expand only when evidence and implementation demand it.

The architecture should therefore be treated as a controlled roadmap, not an instruction to maximize page count.

### 13.2 Information that would change this architecture

The proposed structure should be reconsidered if:

- The current `00`–`08` files reveal that two supposedly distinct functions are already cleanly integrated without confusion.
- A separate owner or regulatory obligation requires accessibility, security, privacy, or semantic governance to have an independent lifecycle.
- PULSE expands beyond digital Decision Experiences into a formal organizational operating model requiring additional role, process, or certification documentation.
- Reference implementations become numerous enough that gallery, cookbook, cases, and repository registry require separate retrieval systems.
- Multiple agents or platforms require a platform-neutral agent standard plus distinct executable instruction files.
- Empirical evaluation produces a validated PULSE measurement instrument that deserves its own methodology and evidence document.

---

## 14. Final Governance Statement

> **PULSE should grow by deepening capability, evidence, and application—not by multiplying definitions. The DNA owns the truth of the methodology. Each downstream document owns one distinct function. Every implementation remains traceable to its principles, every example remains subordinate to the method, and every agent remains derived from approved human-readable knowledge.**

### Governance decision

The recommended architecture is approved in principle when the Methodology Owner accepts:

1. The authority hierarchy.
2. The single-owner rule for formal concepts.
3. The nine-document minimum future set.
4. The merge decisions for reasoning/questions, trust/governance, engineering, reference materials, and prompting/agent governance.
5. The requirement that the GPT System Instruction be generated last and own no methodology concepts.
6. The provisional status of existing `00`–`08` files until direct content audit.


---

## Appendix A — Source Basis for Version 1.0.0

| Source | Governance use in this map |
|---|---|
| `00_PULSE_DNA.md` | Constitutional authority for official definitions, worldview, transformation, Decision Circle, five verbs, principles, language, boundaries, ethics, interface independence, Mobile First, conversational direction, and Human-in-Control. |
| `PULSE tómale el pulso a tus decisiones.md` | Primary authorial evidence for the living-system metaphor, Decision Circle, decision health, competitive comparison, and the shift from analytical ladders to organizational responsiveness. |
| `Los fundamentos técnicos de PULSE.md` | Primary authorial evidence for information asymmetry, alostasis, organizational interoception, and the distinction between established foundations and PULSE synthesis. |
| `ia-datos-analitica-valor-decisiones.md` | Primary authorial evidence for Business First, PDAMR, five verbs, Human-in-Control, AI as amplifier, data context, capability over isolated use cases, and value as changed decisions and actions. |
| `La IA Conversacional Revoluciona Dashboards y Analítica.md` | Supporting evidence for conversational access, natural-language interaction, democratization, the changing role of dashboards, and the need to govern the transition from static views to dialogue. |
| `arquitectura-de-datos-moderna-fabula_.md` | Supporting evidence for data architecture as shared meaning, purpose, ownership, coordination, and the “village of data” metaphors. |
| `analitica-datos-5-niveles_.md` | Supporting evidence for question-led analytics, uncertainty in prediction, actionability, cognitive interfaces, governance, and the warning that complexity is not equivalent to value. |
| `Pasted markdown.md` | The commissioning brief defining the required structure, governance objective, status vocabulary, priority vocabulary, candidate document set, and assessment requirements for this map. |

The source articles support fidelity to Javier Forero’s thinking. They do not outrank the approved DNA where wording or scope has been constitutionally clarified.
