---
title: Redesigning Work with AI · Thursday's Promise
description: A story about when to bring AI into a workflow, how to assign decision rights, and what evidence would justify expanding a pilot.
status: candidate
version: 0.9.0
artifact_type: learning-module
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Architectures, Decision Governance, AI Native Analytics]
source_ids: [SRC-PULSE-DNA-001, SRC-JF-BLOG-1973, SRC-JF-BLOG-2705, SRC-JF-BLOG-2529, SRC-JF-BLOG-2748, SRC-JF-BLOG-2806, SRC-JF-BLOG-2828, SRC-JF-BLOG-2942]
claim_ids: []
last_reviewed: 2026-11-08
---

# Redesigning Work with AI · Thursday's Promise

*A narrative chapter based on Javier Forero’s Philia Sophia articles. The company, characters, policies, and pilot results are fictional.*

## A flawless reply { #the-decision }

At 8:12 on Thursday morning, the assistant drafted its first test reply to a customer waiting for a spare part. “We can confirm that your order will ship today.”

The email was ready in seconds. Lucía, the service shift lead, opened the inventory record. There was one unit left. On another screen, she found the detail missing from the draft. The unit was reserved for a different order.

“Who promised it would ship?” asked Mateo, the new analyst.

“No one yet,” Lucía said, closing the draft. “We’re testing. If we send it, it’s our promise.”

On Friday, Irene, the operations lead, had to decide **whether to change how spare-part requests were handled and which part of the work to entrust to AI**. She wanted customers to get a reply sooner and the team to be able to honor it. Getting it wrong could mean reworking a case, displacing another order, or breaking a promise. Waiting had a cost, too. The customer still had to plan a repair.

## AI predicts, you think { #prediction-and-judgment }

When they looked at the draft together, Lucía asked Mateo to separate three things. The text was **a proposal**. The warehouse reservation was **evidence**. Committing to a date was **a decision** that affected both the customer and the order already assigned the part.

The model could draft a plausible reply from the context it received. Checking the order, weighing what to do when records disagreed, and taking responsibility for a promise required access, time, and authority. Irene made sure the team had all three. Lucía could reject a draft, request confirmation, and keep serving the customer through the regular workflow.

Javier Forero makes this distinction in [AI predicts, you think](https://javierforero.co/2025/11/28/ia-predice-tu-piensas-hype-tecnologico/). At the service desk, keeping control of the decision meant being able to change the criteria or stop the action before a proposal became a commitment.

## The delay lived between two desks { #the-workflow }

Lucía and Mateo retraced a request. The service desk read the email, asked for an ID, checked the policy, and asked the warehouse about inventory. The warehouse replied when someone could step away from their shift duties. The service desk returned to the email and made a promise. Sometimes the team asked twice because the first message was buried in someone’s inbox.

“The assistant can read the email,” Mateo said. “What do we do about the wait?”

The team first tried a shared form, one ID per case, and an authorized lookup that distinguished **stock on record** from **units available for that order**. Incomplete requests stayed open with a named owner and a deadline for the next update. The team could operate this way using rules and templates.

They agreed on where AI could help in that workflow. The system would check required fields and route standard cases using explicit rules. The model would extract details from free text and prepare a draft with references to the order and the current policy. If the warehouse had yet to confirm the reservation, the draft could request confirmation or propose an update without a shipping date. The policy and order status were the evidence behind any promise.

## Who holds the keys { #decision-rights }

In the pilot, the identity of the person handling a case determined which records could be retrieved **before** any context went to the model. The lookup had read access to the assigned order and current policy. Inventory discrepancies, special contract terms, and records outside scope went to manual review. The draft showed its source and when it was retrieved. The warehouse confirmed the reservation in the order system. The service desk checked that confirmation before committing to a date.

| Judgment zone | What the system does | How the role changes |
|---|---|---|
| **Delegate** | Organizes the request and extracts fields for review. Rules check structured fields and apply standard routing. | Mateo spends less time copying details between screens and learns to check where each field came from. |
| **Co-create** | Drafts a reply the team can check against the order and policy. | The service desk verifies the evidence, edits or rejects the draft, and logs why when it finds an error. |
| **Protect** | Sends exceptions to a person and surfaces the facts that person is authorized to see. | The warehouse confirms the reservation. The service desk can commit to a date within policy. Irene approves exceptions and is accountable for the process. |

Mateo suggested that the assistant might eventually move requests between internal queues. Irene asked him to spell out what he would delegate. The **trigger** would be a validated standard case. The **context** would include the case ID, current status, and applicable rules. The **criteria** would specify the destination and when to send an ambiguous case for review. The **hands** would be permission to change only the internal queue, with a log and a way to reverse the move. If a rule could choose the queue, conventional automation could handle it. The pilot kept the assistant in read and draft mode.

Lucía also set aside time for new staff to handle cases without the assistant and compare their judgment with someone on the shift. In one exercise, she showed them two equally convincing drafts and asked them to decide which could be sent by tracing each statement to its source. The team would investigate draft errors as potential failures of the process or system. Pilot records would help improve the workflow and train the team.

## Four weeks to test the change { #pilot-and-learning }

Irene weighed three options. **Keeping the redesigned workflow with rules** was the simplest option and the operational fallback. **Adding an assistant to that workflow** would let the team test whether reading free text and drafting replies added value. **Authorizing autonomous execution** called for evidence and controls the team still needed, including the ability to detect and reverse an incorrect action. She chose to pilot the assistant.

The team first ran in shadow mode, keeping drafts out of customer replies. It then randomly assigned standard cases within each shift and request type over four weeks. One group used the redesigned workflow with rules and templates. The other used the same workflow with an assistant and human review. Both had the same access to the sources. Special cases stayed on the manual workflow. A first verifiable reply had to give a confirmed status or state the next step, its owner, and its deadline. Each case had seven full days of follow-up.

Before the pilot, Irene set teaching thresholds of at least three minutes saved per case and a reopening increase of at most two percentage points. Data exposure, an unapproved message, or a commitment without a confirmed reservation would trigger an immediate pause, a return to the fallback workflow, and a review of the logs by Operations and the access owner. The team had to be able to keep working with the assistant switched off.

| Simulated observation | Workflow with rules and templates | Same workflow with an assistant |
|---|---:|---:|
| Standard cases assigned | 120 | 120 |
| Mean staff time per case, including review | 14 min | 10 min |
| Median time to first verifiable reply, during business hours | 90 min | 74 min |
| Cases reopened within seven days | 6 of 120 (5.0%) | 7 of 120 (5.8%) |
| Incidents that would trigger a pause | 0 observed | 0 observed |

The four-minute difference translated into **eight staff hours across the 120 cases in the assisted group**. The team spent some of that time reviewing its backlog. To establish the benefit actually captured, it still had to measure the effect on the backlog and account for integration, training, support, and operating costs. The observed increase in reopening was 0.8 percentage points. With so few cases, it remained unclear whether the true increase was within the limit. Observing zero incidents told the team little about rare failures.

**Irene’s decision.** Keep the assistant at the pilot desk and retain the rules-based workflow as a fallback. At the next four-week review, Irene would examine the reasons for reopening by shift and case type, total cost per closed case, hours spent on the backlog, and tests of blocking and escalation. She would consider expanding to another desk if there was enough evidence that quality held and the team could show the value it captured from the time saved.

Mateo returned to Thursday’s case. He knew where to look before promising a ship date. In his notebook, he wrote a question for the next shift.

“If two sources disagree, who can check what happened?”

## Take the case into your company { #try-it }

Choose a workflow where delay or rework matters. Use the [Decision Brief](decision-brief.en.md) to document these five PULSE points before choosing what to change.

| Point | Question for your team |
|---|---|
| **Priority** | What outcome matters, and who currently experiences the delay or error? |
| **Decision** | Who chooses among keeping the workflow, simplifying it with rules, adding AI assistance, or delegating a bounded action? |
| **Action** | What changes in each person’s work? Who keeps the authority to commit resources, resolve exceptions, and stop execution? |
| **Metric** | What comparable baseline will you use for total time, quality, and cost? Who will turn the time saved into an observable outcome? |
| **Risk** | What evidence and permissions does each action require? What triggers a pause, and who can restore the fallback workflow? |

Map the path a case takes before and after the change. Rehearse a standard request, an exception, and an attempt to retrieve a record outside scope. Ask the person doing the work to show when they would correct the assistant and how they would record the correction. Set a review date and identify the evidence that would lead you to expand, limit, or suspend the change.

Trace evidence back to its source in [The Data Village](data-architecture-fable.en.md), assign authority with the [human–AI control module](04-human-ai-control.en.md), and prepare the review with [action and learning](05-action-learning.en.md). The [assistant evaluation lab](../practice-lab/conversational-evidence.en.md) has exercises for testing response quality. Use the [bridge from the five levels of analytics to PULSE](../03-pulse/from-five-levels.en.md) to identify the analysis you need before acting.

## The readings behind the case { #source-readings }

| Article by Javier Forero | Contribution to the chapter |
|---|---|
| [AI predicts, you think](https://javierforero.co/2025/11/28/ia-predice-tu-piensas-hype-tecnologico/) | The central idea separates the generated proposal from the evidence and the decision the team owns. |
| [AI-native and redesigning work](https://javierforero.co/2026/07/11/ai-native-redisenar-trabajo-empresa/) | Provides the narrative arc. AI capabilities, human judgment, the platform, workflow, and learning explain what changed at the service desk. |
| [AI literacy and judgment](https://javierforero.co/2026/06/11/alfabetizacion-ia-delegar-cocrear-proteger/) | Provides the delegate, co-create, and protect zones and informs the practice through which Mateo develops his judgment. |
| [Enterprise RAG and permissions](https://javierforero.co/2026/07/28/rag-empresarial-permisos/) | Motivates retrieving evidence under the person’s access rights before sending it to the model. |
| [Two maps for using AI with judgment](https://javierforero.co/2026/08/16/triangulo-ia-modelo-prompt-contexto/) | Helps separate stable rules from tasks that involve interpreting ambiguous text. |
| [Four parts of effective delegation](https://javierforero.co/2026/10/17/agentes-ia-delegar-con-criterio/) | Provides the vocabulary of context, criteria, hands, and trigger for bounding an action before authorizing it. |
| [How to measure returns on AI](https://javierforero.co/2026/08/30/roi-ia-medir-retorno-valor/) | Separates time saved from value captured and makes quality part of the decision to expand. |

*Editorial note. Candidate teaching chapter. The articles provide the author’s perspective. The case and figures were created for practicing design decisions. Drafting and translation received AI assistance.*
