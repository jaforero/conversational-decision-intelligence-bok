#!/usr/bin/env python3
"""Validate the CDI-BoK Sprint 3 B2B Proposal practice-and-evidence contract."""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.5.0-rc.1"


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def load_yaml(relative: str):
    with (ROOT / relative).open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def markdown(relative: str) -> tuple[dict, str]:
    text = (ROOT / relative).read_text(encoding="utf-8")
    check(text.startswith("---\n"), f"Missing front matter: {relative}")
    parts = text.split("---", 2)
    check(len(parts) == 3, f"Invalid front matter boundary: {relative}")
    if len(parts) != 3:
        return {}, text
    return yaml.safe_load(parts[1]) or {}, parts[2]


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def close(actual: float, expected: float, tolerance: float = 0.011) -> bool:
    return abs(actual - expected) <= tolerance


required_docs = {
    "docs/practice-lab/index.md": "practice-landing",
    "docs/practice-lab/catalog.md": "practice-catalog",
    "docs/practice-lab/b2b-proposal/index.md": "instrumented-case",
    "docs/practice-lab/b2b-proposal/decision-contract.md": "decision-contract",
    "docs/practice-lab/b2b-proposal/evidence-protocol.md": "evidence-protocol",
    "docs/practice-lab/b2b-proposal/cycle-log.md": "learning-log",
    "docs/versions/v0.5.0-rc.1.md": "release-note",
}
documents: dict[str, tuple[dict, str]] = {}
for path, artifact_type in required_docs.items():
    check((ROOT / path).exists(), f"Missing Sprint 3 public document: {path}")
    if not (ROOT / path).exists():
        continue
    metadata, body = markdown(path)
    documents[path] = (metadata, body)
    check(metadata.get("version") == RELEASE, f"Wrong Sprint 3 version: {path}")
    check(metadata.get("status") == "candidate", f"Sprint 3 document must remain candidate: {path}")
    check(metadata.get("normative") is False, f"Sprint 3 document cannot be normative: {path}")
    check(metadata.get("artifact_type") == artifact_type, f"Wrong artifact type: {path}")

case_body = documents.get("docs/practice-lab/b2b-proposal/index.md", ({}, ""))[1]
evidence_body = documents.get("docs/practice-lab/b2b-proposal/evidence-protocol.md", ({}, ""))[1]
contract_body = documents.get("docs/practice-lab/b2b-proposal/decision-contract.md", ({}, ""))[1]
cycle_body = documents.get("docs/practice-lab/b2b-proposal/cycle-log.md", ({}, ""))[1]
for marker in ["instrumentado, no ejecutado", "80,11%", "−11,50 pp", "datos simulados"]:
    check(marker.lower() in case_body.lower(), f"Case page misses calibrated marker: {marker}")
for marker in ["Wilson 95%", "diferencia-en-diferencias", "Atribución causal", "No se sostiene"]:
    check(marker.lower() in evidence_body.lower(), f"Evidence protocol misses: {marker}")
for marker in ["Por confirmar", "Prerregistro obligatorio", "Preferencia provisional"]:
    check(marker.lower() in contract_body.lower(), f"Decision contract misses: {marker}")
for marker in ["No iniciado", "Resultado observado", "No estimable"]:
    check(marker.lower() in cycle_body.lower(), f"Cycle log misses null-state marker: {marker}")

case = load_yaml("governance/cases/B2B-PROP-001.yml")
check(case["release"] == RELEASE, "Case manifest release mismatch")
check(case["status"] == "instrumented-not-executed", "Case status overstates its evidence stage")
check(case["normative"] is False, "Experimental case cannot be normative")
check(case["decision_owner_confirmed"] is False, "Decision owner was invented")
check(case["decision"]["chosen_option"] is None, "Case records an option that has not been chosen")
check(case["decision"]["provisional_preference"] == "A", "Provisional option A is not explicit")
check(case["evidence"]["data_nature"] == "simulated-demo", "Simulated-data boundary is missing")
check(case["evidence"]["raw_organizational_data_materialized"] is False, "Case implies real CRM data are materialized")
check(case["evidence"]["channel_read"]["superiority_established"] is False, "Channel superiority is overstated")
check(case["evaluation"]["action_executed"] is False, "Case invents an executed action")
check(case["evaluation"]["outcome_observed"] is False, "Case invents an observed outcome")
check(case["evaluation"]["causal_claim_allowed"] is False, "Causal claim guard is open")
check(case["evaluation"]["minimum_cycles"] == 2, "Minimum multi-cycle rule is missing")
check(case["evaluation"]["preferred_cycles"] == 3, "Preferred multi-cycle rule is missing")
check(case["cycle_zero"]["status"] == "completed", "Evidence-review cycle zero is not recorded")
check("B y C quedan bloqueadas" in case["cycle_zero"]["decision_change"], "Cycle zero did not change the channel recommendation")
check("not evidence of commercial impact" in case["cycle_zero"]["learning_scope"], "Cycle zero overstates business impact")
check(case["readiness"]["instrumentation"] == "ready", "Instrumentation readiness is not explicit")
check(case["readiness"]["impact_evaluation"] == "blocked", "Impact evaluation must remain blocked")
check(len(case["readiness"]["blockers"]) >= 5, "Case readiness blockers are incomplete")

sales = read_csv("evidence/b2b-proposal/demo-sales-monthly.csv")
check(len(sales) == 18, f"Expected 18 monthly sales aggregates, found {len(sales)}")
sales_by_month = {row["month"]: row for row in sales}
check(len(sales_by_month) == len(sales), "Duplicate month in sales evidence")
june = sales_by_month.get("2026-06", {})
if june:
    compliance = float(june["actual"]) / float(june["target"]) * 100
    check(close(compliance, 80.11), f"June compliance differs: {compliance:.4f}")
    check(int(june["sellers_under_90"]) == 8, "June sellers-under-90 differs")
    check(int(june["sellers_total"]) == 8, "June seller denominator differs")
    minimum = min(sales, key=lambda row: float(row["compliance_pct"]))
    check(minimum["month"] == "2026-06", "June 2026 is not the minimum in the versioned aggregate")
    check(close(float(case["evidence"]["baseline"]["june_2026_sales_compliance_pct"]), compliance), "Case and sales baseline differ")

funnel = read_csv("evidence/b2b-proposal/demo-funnel-2026.csv")
check(len(funnel) == 30, f"Expected 30 funnel rows, found {len(funnel)}")
proposal = {row["month"]: float(row["conversion_pct"]) for row in funnel if row["stage"] == "Propuesta"}
check(len(proposal) == 6, "Expected six Proposal conversion observations")
baseline = sum(proposal[month] for month in ["2026-01", "2026-02", "2026-03"]) / 3
deteriorated = sum(proposal[month] for month in ["2026-04", "2026-05", "2026-06"]) / 3
change = deteriorated - baseline
check(close(baseline, 48.03), f"Proposal baseline differs: {baseline:.4f}")
check(close(deteriorated, 36.53), f"Proposal deteriorated period differs: {deteriorated:.4f}")
check(close(change, -11.50), f"Proposal change differs: {change:.4f}")
case_baseline = case["evidence"]["baseline"]
check(close(float(case_baseline["proposal_conversion_jan_mar_pct"]), baseline), "Case Proposal baseline differs")
check(close(float(case_baseline["proposal_conversion_apr_jun_pct"]), deteriorated), "Case Proposal post period differs")
check(close(float(case_baseline["proposal_change_pp"]), change), "Case Proposal change differs")

channels = read_csv("evidence/b2b-proposal/demo-channel-win-rate.csv")
check(len(channels) == 6, f"Expected six channel summaries, found {len(channels)}")
channel_by_name = {row["channel"]: row for row in channels}
for name, row in channel_by_name.items():
    n = int(row["closed"])
    won = int(row["won"])
    observed = won / n * 100
    check(close(observed, float(row["win_rate_pct"])), f"Win rate differs for {name}")
    z = 1.96
    p = won / n
    denominator = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denominator
    check(close((center - half) * 100, float(row["wilson_95_low"])), f"Wilson low differs for {name}")
    check(close((center + half) * 100, float(row["wilson_95_high"])), f"Wilson high differs for {name}")
event = channel_by_name["Evento / feria"]
referral = channel_by_name["Referido"]
inbound = channel_by_name["Inbound digital"]
check(float(event["win_rate_pct"]) > float(inbound["win_rate_pct"]), "Observed event ranking differs")
check(float(referral["win_rate_pct"]) > float(inbound["win_rate_pct"]), "Observed referral ranking differs")
check(float(event["wilson_95_low"]) < float(inbound["wilson_95_high"]), "Event and inbound intervals no longer overlap")
check(float(referral["wilson_95_low"]) < float(inbound["wilson_95_high"]), "Referral and inbound intervals no longer overlap")

decision_record = load_yaml("docs/assets/data/b2b-proposal-decision-record.yml")
check(decision_record["record_status"] == "pre-decision", "Decision record is not pre-decision")
check(decision_record["chosen_option"] is None, "Decision template invents a chosen option")
check(decision_record["expectation"]["central_estimate_pct"] is None, "Decision template invents an expectation")
check(decision_record["outcome"]["observed"] is False, "Decision template invents an outcome")
check(decision_record["outcome"]["attributable_effect_pp"] is None, "Decision template invents an effect")
check(decision_record["audit"]["owner_signoff"] is None, "Decision template invents owner signoff")
cycle_log = read_csv("docs/assets/data/b2b-proposal-cycle-log.csv")
check(len(cycle_log) == 4, "Cycle log must include four pre/post and intervention/comparison rows")
check(all(row["status"] == "not-started" for row in cycle_log), "Cycle log overstates execution")
check(all(not row["attributable_effect_pp"] for row in cycle_log), "Cycle log invents an attributable effect")

sources = load_yaml("governance/registries/sources.yml")
claims = load_yaml("governance/registries/claims.yml")
concepts = load_yaml("governance/registries/concepts.yml")
adr_index = load_yaml("governance/adr/index.yml")
external_demos = load_yaml("governance/registries/external-demos.yml")
for registry, label in [(sources, "sources"), (claims, "claims"), (concepts, "concepts"), (adr_index, "ADR"), (external_demos, "external demos")]:
    check(registry.get("release") == RELEASE, f"Current {label} registry release mismatch")
source_ids = {item["source_id"] for item in sources["records"]}
claim_by_id = {item["claim_id"]: item for item in claims["claims"]}
required_sources = {"SRC-PRACTICE-B2B-001", "SRC-PRACTICE-DASH-ROOT-001", "SRC-PRACTICE-GPT-ROOT-001", "SRC-PRACTICE-DASH-B2B-001"}
required_claims = {"CLAIM-PRACTICE-B2B-001", "CLAIM-PRACTICE-B2B-002", "CLAIM-PRACTICE-B2B-003", "CLAIM-PRACTICE-B2B-HYP-001"}
check(required_sources.issubset(source_ids), "Sprint 3 sources are incomplete")
check(required_claims.issubset(claim_by_id), "Sprint 3 claims are incomplete")
for claim in claims["claims"]:
    for source_id in claim.get("source_ids", []):
        check(source_id in source_ids, f"Unknown source {source_id} in {claim['claim_id']}")
check(claim_by_id["CLAIM-PRACTICE-B2B-HYP-001"]["evidence_status"] == "untested", "Causal hypothesis is overstated")
check("no hay acción ejecutada" in claim_by_id["CLAIM-PRACTICE-B2B-HYP-001"]["limits"].lower(), "Causal hypothesis lacks execution boundary")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
for adr_id in ["ADR-018", "ADR-019"]:
    check(adr_by_id.get(adr_id, {}).get("status") == "accepted", f"Missing accepted {adr_id}")
check(len(external_demos["demos"]) == 9, "External demo catalog does not contain nine observed/announced entries")
demo_by_id = {item["demo_id"]: item for item in external_demos["demos"]}
check(demo_by_id["JF-CLAUDE-COMMERCIAL"]["selected_case_id"] == "B2B-PROP-001", "Primary demo is not linked to the case")
check(demo_by_id["JF-GPT-COMMERCIAL"]["related_case_id"] == "B2B-PROP-001", "Related ChatGPT demo is not linked to the case")

content_map = load_yaml("governance/content-map.yml")
check(content_map["release"] == RELEASE, "Content map release mismatch")
check(content_map["public_portal"]["release"] == RELEASE, "Portal content-map release mismatch")
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
check(set(required_docs).issubset(registered), "Sprint 3 public documents are absent from the content map")

manifest = load_yaml("governance/sprint-3-manifest.yml")
check(manifest["release"] == RELEASE, "Sprint 3 manifest release mismatch")
check(manifest["status"] == "implementation-complete-awaiting-ci", "Sprint 3 manifest status is not ready for CI")
for gate in ["baseline_reproducible", "decision_record_present", "causal_claim_guard", "strict_build", "static_accessibility_audit"]:
    check(str(manifest["gates"][gate]).startswith("passed"), f"Sprint 3 local gate not recorded: {gate}")
check(manifest["gates"]["visual_regression"] == "pending-github-actions", "Visual gate must remain pending until canonical CI")
check(manifest["gates"]["owner_ratification"] == "pending", "Candidate cannot pre-record owner ratification")

portal_markers = {
    "mkdocs.yml": "portal: v0.5.0-rc.1",
    "overrides/main.html": "Portal v0.5.0-rc.1",
    "README.md": "`v0.5.0-rc.1`",
    "package.json": '"version": "0.5.0-rc.1"',
    "package-lock.json": '"version": "0.5.0-rc.1"',
}
for path, marker in portal_markers.items():
    check(marker in (ROOT / path).read_text(encoding="utf-8"), f"Sprint 3 portal marker missing: {path}")

stable_docs = [
    "docs/00-foundation/constitution.md",
    "docs/00-foundation/cdi-scope-boundaries.md",
    "docs/00-foundation/glossary.md",
    "docs/00-foundation/domain-map.md",
    "docs/03-pulse/specification.md",
]
for path in stable_docs:
    metadata, _ = markdown(path)
    check(metadata.get("version") == "0.4.0", f"Sprint 3 altered stable core version: {path}")
    check(metadata.get("status") == "approved", f"Sprint 3 demoted stable core: {path}")

all_case_text = "\n".join(body for _, body in documents.values()).lower()
for prohibited in [
    "pulse demostró que",
    "cdi demostró que",
    "la intervención produjo",
    "efecto causal observado",
    "owner confirmado: sí",
]:
    check(prohibited not in all_case_text, f"Premature practice claim found: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} Sprint 3 error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 3 B2B practice-and-evidence contract validated ({CHECKS} checks)")
