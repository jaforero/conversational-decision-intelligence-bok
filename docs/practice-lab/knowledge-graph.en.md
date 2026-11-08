---
title: Knowledge graph lab
description: Explore the CDI-BoK as a document network and turn a verifiable finding into an editorial improvement.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: experimental
normative: false
owner: Javier Forero
domains: [Knowledge Graphs, Semantic Layers, Decision Governance]
source_ids: [SRC-PRACTICE-GRAPH-001, SRC-JF-BLOG-3248]
claim_ids: []
last_reviewed: 2026-11-08
---

# Knowledge graph lab

**Practice question.** Which link, reference or reading path should the CDI-BoK maintainer fix first? Prioritize changes that help readers reconstruct evidence or reach an application from its guidance.

[Open the CDI-BoK in the explorer](https://dashboards.javierforero.co/claude/grafo-conocimiento/?repo=jaforero%2Fconversational-decision-intelligence-bok&ref=main&path=docs&lang=en){ .md-button .md-button--primary }

## Load the book and follow a relationship

1. The link loads the CDI-BoK directly. To load it manually or pin a different version, choose **Load another vault → GitHub**. Enter `jaforero/conversational-decision-intelligence-bok` and set the subfolder to `docs` under Options. Use `main` for the current corpus or a tag to reproduce a historical version. The repository is public and loads without a token, subject to GitHub API limits.
2. Open `learn/02-evidence-context.md` and follow the link to the experience design module. At the destination, inspect the backlink and its context. Repeat with `research/research-agenda.md` and find the candidate GraphRAG protocol.
3. Classify one finding. A **broken link** points to a target that fails to resolve. A **page without inbound content links** can still be reachable through navigation. An **implicit relationship** requires checking both documents before adding an editorial link.
4. Verify in the portal and on GitHub. MkDocs conventions and `.en.md` translations may behave differently in a generic Markdown explorer. Record the source page, expected target, edition, evidence, owner and proposed correction. Verify both editions after the change.

**Deliverable.** Prepare one reproducible finding and a small correction. If a relationship already exists, use it as a control and record what you checked.

## Inspect the CDI-BoK editorial graph { #editorial-graph }

On each build, the site generates a JSON inventory from registered canonical pages, their rendered links, and the source and claim registries. It distinguishes four relationships: page links to page, page lists source, page lists claim, and claim lists source. Each label describes what the repository records.

<a href="/assets/data/cdi-knowledge-graph.json" download>Download the editorial graph as JSON</a>

The `pages_without_inbound_content_links` field lists review candidates, excluding the home page. Navigation links are excluded and each page is counted once, in the canonical Spanish edition. A declared reference helps trace provenance. Its relevance and strength require [reviewing the evidence](../governance/claims-evidence.md).

**Acceptance criterion.** Trace a path from a page to a source or claim, check it against the original file, and document what editorial action would change. The [GraphRAG protocol](../research/research-agenda.md#graphrag-evaluation) describes the additional test for relationship-based retrieval.
