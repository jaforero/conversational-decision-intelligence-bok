---
title: The Data Village · The Missing Delivery
description: A fable about data architecture, shared definitions, and a decision with a deadline.
status: candidate
version: 0.9.0
artifact_type: learning-module
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Decision Architectures, Semantic Layers, Decision Governance]
source_ids: [SRC-JF-004, SRC-PULSE-DNA-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# The Data Village · The Missing Delivery

*A teaching sequel to [The Data Village, Javier Forero’s original fable in Spanish](https://javierforero.co/2025/04/02/arquitectura-de-datos-moderna-fabula/). The characters, places, and metaphor come from the original story. The incident and figures in this chapter are fictional.*

## Eighty in one book, seventy-six in the other { #the-decision }

The second time Adriana came to the village, Don Martín was waiting in the square with two sheets of paper and a clock.

“The schools need eighty boxes to start the day at nine,” he said. “The warehouse says it delivered eighty. The schools say they received seventy-six. We have four in reserve. Should we send them?”

Both sheets had the same heading, “Delivered.” Adriana almost asked for one of the numbers to be corrected.

“Before we decide,” she said, “what had to happen for each person to make a mark on their sheet?”

## A box’s journey

At the **Mysterious Lake**, Adriana found the records as they had arrived. The warehouse logged the time each box left. Each school signed a receipt once the box was at its door. The timestamps described different events, and the village had kept both. The keeper showed her what she could consult for the delivery and who could open the original receipts.

In the **Great Library**, the librarian looked up one of the boxes by its ID. It had a dispatch record and no receipt. Another box appeared twice in a school file. The librarian showed how the two copies referred to the same arrival. They rebuilt the count and left a trail back to each source record.

The **Specialty Shop** already had a list of boxes by school. The delivery team needed to know where boxes were missing and how long it would take a reserve box to reach them. All four were bound for the same school, ten minutes from the depot. Adriana could set aside four reserve boxes and wait until 8:45. Sending them earlier could duplicate the delivery. Waiting longer would leave little time to get there.

The warehouse lead and the school principal met in the **Collaborative Neighborhood**. Each took responsibility for their own records, and they agreed to share a box ID. The principal would be responsible for confirming receipt. They agreed that *received on time* meant a unique, expected box with a confirmed receipt at its destination school by nine.

The **Magic Loom** helped trace the thread from the Shop to the source records. The dashboard began showing “Dispatched” and “Confirmed received” separately, with a cutoff time. When Adriana asked, “How many did we deliver?”, the assistant asked whether she meant boxes that had left the warehouse or boxes the schools had received. She chose receipts and could see where the count came from and which boxes were still outstanding.

## The box that came out of reserve { #action-and-learning }

At 8:45, three receipts came in. The driver confirmed the fourth box was still on the road and would arrive after nine. Adriana, who was responsible for the delivery, authorized one reserve box for that school, linked to the original order and asked the driver to return the delayed box to the depot.

The school confirmed receipt of the reserve box before nine. The final record showed **80 of 80 boxes received on time**, one from reserve. Adriana recorded the cost of the extra trip and logged the original box’s return to the depot separately. At the next delivery, she would use the actual travel time to check whether fifteen minutes still gave the team enough time to use the reserve. One delivery gave the team a reason to review the rule. Adopting it on other routes would require more observations of delivery and travel times.

Don Martín looked at the two sheets again.

“What changed in the village?”

“Now I can follow a box from dispatch to receipt,” Adriana said. “And I know whom to call when it gets held up.”

## From story to design { #architecture-map }

| Place | Role in this case | Question for your team |
|---|---|---|
| **Lake · Data Lake** | Preserves the source records, with provenance and controlled access. | Can we recover what came from each source and when? |
| **Library · Data Warehouse** | Integrates records, distinguishes events, and documents how the duplicate was handled. | Can we reconstruct the count from its inputs? |
| **Shop · Data Mart** | Gives the delivery team a view by school. | What detail does the decision owner need to act in time? |
| **Neighborhood · Data Mesh** | Illustrates domain ownership of data and shared agreements. | Who responds when a definition changes or a record fails? |
| **Loom · Data Fabric** | Illustrates how metadata and integration can trace evidence across systems. | Can we follow the thread from the figure back to the source? |

The semantic layer applies the agreed definition of “received on time” so the dashboard and the assistant compute the same count. The places represent responsibilities and design approaches. A single platform can cover several responsibilities. Choose what you need based on the decision, the risk, and the cost of operating each piece.

## Try it with your data { #try-it }

Pick two reports that use the same label for a figure. Write down the event each counts, the unit, the cutoff time, the source, and who owns the definition. Reconstruct one record from its source. Then write down which action would change if you used one definition or the other, who would authorize it, and what outcome would lead you to review the rule.

In the [worked exchange rate case](../practice-lab/fx-worked-case.en.md), the interpretation changes depending on whether you compare by **effective date** or **market day**. Use the [evidence contract](02-evidence-context.en.md) and the [PULSE specification](../03-pulse/specification.en.md) to connect the definition and provenance to the decision and its review.

*Editorial note. Candidate teaching chapter. Drafting and translation received AI assistance.*
