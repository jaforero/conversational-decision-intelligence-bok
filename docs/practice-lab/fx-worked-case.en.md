---
title: Worked case · Exchange rates
description: Rebuild two indexes, verify a carried-forward rate, and decide whether an FX signal triggers a simulated budget review.
status: candidate
version: 0.9.0
artifact_type: practice-exercise
authority_level: pedagogical
normative: false
owner: Javier Forero
domains: [Conversational Analytics, Semantic Layers, Decision Governance]
source_ids: [SRC-PULSE-DNA-001, SRC-PRACTICE-FX-001, SRC-PRACTICE-FX-SNAPSHOT-001]
claim_ids: []
last_reviewed: 2026-11-08
---

# Worked case · Exchange rates

On November 6, 2026, the USD–COP index reads **101.42** when you use the effective TRM. Match the market dates used by Mexico's FIX and the index reads **100.07**. The difference determines whether the team opens a review under the rule in this exercise.

## Decision and criterion { #decision }

The planning team at a simulated importer reviews local budgets for USD payables in Colombia and Mexico. It needs to decide which budget warrants an unscheduled review. Before calculating, the owner sets the teaching criterion **review if local currency per USD rises by at least 1% from November 3 to 6, 2026, using market dates**. The options are to review Colombia first, review Mexico first, or follow the regular schedule.

The threshold belongs to the simulated scenario. For a payment decision, the owner also checks the invoice currency, amount, date, applicable rate, and existing hedges.

## Evidence and calculation { #evidence }

The [exchange rate repository](https://github.com/jaforero/fx-bancos-centrales/tree/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series) is pinned to commit `dd7a205`. The index uses November 3 and 6, and Saturday the 7th tests the carry-forward. The effective TRM was cross-checked against [data from Colombia's Financial Superintendency](https://www.datos.gov.co/Econom-a-y-Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-TRM/32sa-8pi3). The [Bank of Mexico](https://www.banxico.org.mx/tipcamb/tipCamMIAction.do?idioma=sp) distinguishes the determination of the FIX from its official gazette publication and the rate for payments.

The index is `100 × final rate ÷ initial rate`. Rates are quoted in COP or MXN per USD. A rise means it takes more units of local currency to buy a dollar. Apply the threshold before rounding the change.

| Series and date basis | Nov. 3 | Nov. 6 | Final index | Change |
| --- | ---: | ---: | ---: | ---: |
| USD–COP · [Effective TRM](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_cop_trm.json) | 3,182.99 | 3,228.26 | 101.42 | +1.42% |
| USD–COP · [TRM aligned to market date](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_cop_trm_mkt.json) | 3,235.59 | 3,237.83 | 100.07 | +0.07% |
| USD–MXN · [FIX by determination date](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/usd_mxn_fix.json) | 18.7592 | 18.6297 | 99.31 | −0.69% |

On November 7 the FIX series shows **18.6297 MXN per USD**, carried forward from the 6th. The TRM of **3,237.83 COP per USD** is effective November 7–9 and reflects the market on the 6th. For the [November 6 MXN–COP cross-rate](https://github.com/jaforero/fx-bancos-centrales/blob/dd7a205e147ccb7c00171bbd319e4b0b5fed5e52/data/series/mxn_cop_cross.json), divide the inputs from the same market day. `3,237.83 ÷ 18.6297 = 173.7994 COP per MXN` to four decimal places.

## Observed checks { #observed-checks }

I tested the [dashboard](https://dashboards.javierforero.co/tasas-cambio/?lang=en) in Chromium using this [code revision](https://github.com/jaforero/dashboards/tree/9ba5a468627fb58136fa83febb5122c182490fd7/tasas-cambio) and data pinned to `dd7a205`. Under **Base 100 comparison**, I set November 3 as the start and read the row for the 6th. I also checked the USD–MXN history and the converter. The assisted column records an editorial run with ChatGPT using the pinned JSON files. The same review prepared and checked the cases.

| Question | Expected result | Observed in the dashboard | Observed assisted response |
| --- | --- | --- | --- |
| How much did each currency move from November 3 to 6? | State the pair and date basis. Distinguish the dashboard view from the aligned calculation. | The table shows 101.4 for effective-date COP and 99.3 for determination-date MXN. | Identified +1.42% and −0.69% in the dashboard view. With market dates aligned, recalculated COP at +0.07%. |
| How much is the dollar? | Ask for the quote currency and date before answering. | The dashboard offers a pair selector and a history by date. | “Which currency and date do you need the USD reference rate for?” |
| Was a new FIX determined on Saturday the 7th? | Identify the carry-forward and date the original observation. | The history labels the 7th as a carry-forward and the 6th as official. | Identified 18.6297 MXN per USD, determined on Friday the 6th and carried forward on Saturday the 7th. |
| How many COP was one MXN worth on the 6th? | Rebuild the cross-rate and cite both inputs from the same market day. | The converter shows 173.80 COP per MXN dated the 6th and labeled “Calculated.” | Calculated 173.7994 COP per MXN using the market-date TRM and the FIX determined on the 6th. |

The run checks these behaviors in the selected data cut. To compare times in an independent evaluation, use new questions and alternate the channel order. Time from the question to a response with a figure or clarification, unit, date, and source where applicable. To reproduce the values from the CDI-BoK root, run the [verification script](https://github.com/jaforero/conversational-decision-intelligence-bok/blob/main/evidence/fx-case/reproduce.py) with `python evidence/fx-case/reproduce.py`.

## Action and review { #review }

**Case decision.** Keep the regular review schedule. Both series fall below the threshold when compared on market dates. If the internal rule used effective dates, the COP reading would trigger a review. The budget owner should confirm which convention applies before using the criterion for a real payment.

Record the data cut and date convention. Recalculate at the next planned close or when the exposed amount changes materially. Use the [dashboard guide](dashboards.en.md#fx) and the [assistant evaluation lab](conversational-evidence.en.md#public-data-exercises) to reuse the protocol.

*Editorial note. This teaching case uses public data and a simulated budget policy. AI assisted the drafting, translation, and assisted run.*
