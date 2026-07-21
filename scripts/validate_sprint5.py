#!/usr/bin/env python3
"""Validate Sprint 5 decision quality and measurement boundaries."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.7.0-rc.1"
CURRENT_RELEASE = "0.8.0-rc.1"


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


required_docs = {
    "docs/07-governance-quality/index.md": "knowledge-area-landing",
    "docs/07-governance-quality/decision-quality.md": "domain-guide",
    "docs/07-governance-quality/decision-measurement-system.md": "candidate-framework",
    "docs/07-governance-quality/measurement-record.md": "practice-template",
    "docs/versions/v0.7.0-rc.1.md": "release-note",
}
documents: dict[str, tuple[dict, str]] = {}
for path, artifact_type in required_docs.items():
    check((ROOT / path).exists(), f"Missing Sprint 5 document: {path}")
    if not (ROOT / path).exists():
        continue
    metadata, body = markdown(path)
    documents[path] = (metadata, body)
    check(metadata.get("version") == RELEASE, f"Wrong Sprint 5 version: {path}")
    check(metadata.get("status") == "candidate", f"Sprint 5 document must remain candidate: {path}")
    check(metadata.get("normative") is False, f"Sprint 5 document cannot be normative: {path}")
    check(metadata.get("artifact_type") == artifact_type, f"Wrong artifact type: {path}")

markers = {
    "docs/07-governance-quality/index.md": [
        "antes de decidir",
        "durante la ejecución",
        "después del horizonte",
        "No existe una métrica universal",
    ],
    "docs/07-governance-quality/decision-quality.md": [
        "Fundamento establecido y síntesis candidata",
        "outcome bias",
        "snapshot de decisión",
        "Desconocido",
        "bloqueador material",
        "no presenta el perfil como instrumento psicométrico validado",
    ],
    "docs/07-governance-quality/decision-measurement-system.md": [
        "Seis lentes",
        "Contrato de cada métrica",
        "Brier score",
        "No uses Brier score para una decisión única",
        "Anti-métricas",
        "Tasa de override aislada",
        "Puntuación sintética universal",
    ],
    "docs/07-governance-quality/measurement-record.md": [
        "Dos snapshots",
        "debe permanecer `null`",
        "no eficacia",
        "sin sobrescritura",
    ],
}
for path, expected in markers.items():
    body = documents.get(path, ({}, ""))[1]
    for marker in expected:
        check(marker.lower() in body.lower(), f"{path} misses calibrated marker: {marker}")

record = load_yaml("docs/assets/data/decision-measurement-record.yml")
check(record["template_version"] == RELEASE, "Measurement Record template version mismatch")
check(record["record_status"] == "draft", "Measurement Record must start in draft")
snapshot = record["decision_snapshot"]
review = record["outcome_review"]
check(snapshot["frozen_at"] is None, "Template invents a frozen timestamp")
check(snapshot["chosen_option"] is None, "Template invents a chosen option")
check(snapshot["expectation"]["central"] is None, "Template invents a central expectation")
check(review["status"] == "not-observed", "Template overstates outcome status")
check(review["outcome_observed"] is None, "Template invents an observed outcome")
check(review["claim_strength"] == "not-assessed", "Template invents claim strength")
profile = snapshot["quality_profile"]
check(len([key for key in profile if key != "scale"]) == 7, "Decision Quality profile must have seven dimensions")
check(all(value["rating"] == "unknown" for key, value in profile.items() if key != "scale"), "Quality profile must begin unknown")

registries = [
    "governance/registries/sources.yml",
    "governance/registries/claims.yml",
    "governance/registries/concepts.yml",
    "governance/registries/external-demos.yml",
    "governance/adr/index.yml",
]
for path in registries:
    check(load_yaml(path).get("release") == CURRENT_RELEASE, f"Registry release mismatch: {path}")

sources = load_yaml("governance/registries/sources.yml")
source_ids = {item["source_id"] for item in sources["records"]}
required_sources = {
    "SRC-DQ-SDP-001",
    "SRC-ACADEMIC-OUTCOME-BIAS-001",
    "SRC-ACADEMIC-SCORING-RULES-001",
    "SRC-NIST-AIRMF-001",
}
check(required_sources.issubset(source_ids), "Sprint 5 sources are incomplete")

claims = load_yaml("governance/registries/claims.yml")
claim_by_id = {item["claim_id"]: item for item in claims["claims"]}
required_claims = {
    "CLAIM-DQ-OUTCOME-001",
    "CLAIM-DQ-PROFILE-001",
    "CLAIM-DM-SYSTEM-001",
    "CLAIM-DM-CALIBRATION-001",
}
check(required_claims.issubset(claim_by_id), "Sprint 5 claims are incomplete")
check(claim_by_id["CLAIM-DQ-PROFILE-001"]["claim_class"] == "design-recommendation", "Quality profile is presented as empirical fact")
check(claim_by_id["CLAIM-DM-SYSTEM-001"]["maturity"] == "candidate", "Measurement system authority is overstated")
check("repetid" in claim_by_id["CLAIM-DM-CALIBRATION-001"]["limits"].lower(), "Calibration claim lacks repetition boundary")
for claim in claims["claims"]:
    for source_id in claim.get("source_ids", []):
        check(source_id in source_ids, f"Unknown source {source_id} in {claim['claim_id']}")

concepts = load_yaml("governance/registries/concepts.yml")
concept_by_id = {item["concept_id"]: item for item in concepts["concepts"]}
for concept_id in ["DECISION-QUALITY-PROFILE", "DECISION-MEASUREMENT-SYSTEM", "DECISION-MEASUREMENT-RECORD"]:
    check(concept_by_id.get(concept_id, {}).get("status", "").startswith("candidate"), f"Missing or overstated concept: {concept_id}")

adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
check(adr_by_id.get("ADR-021", {}).get("status") == "accepted", "ADR-021 is not accepted")
check((ROOT / "governance/adr/ADR-021-decision-measurement-architecture.md").exists(), "ADR-021 file is missing")

content_map = load_yaml("governance/content-map.yml")
check(content_map["release"] == CURRENT_RELEASE, "Content map release mismatch")
check(content_map["public_portal"]["release"] == CURRENT_RELEASE, "Portal content-map release mismatch")
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
check(set(required_docs).issubset(registered), "Sprint 5 documents are absent from the content map")

manifest = load_yaml("governance/sprint-5-manifest.yml")
check(manifest["release"] == RELEASE, "Sprint 5 manifest release mismatch")
check(manifest["status"] == "candidate-ratified-merged-deployed", "Sprint 5 closure state is not recorded")
check(manifest["gates"]["owner_ratification"] == "passed-user-ratification-2026-07-21", "Owner ratification is not recorded")
check(manifest["gates"]["final_pull_request_validation"] == "passed-run-29862965428", "Final PR validation is not recorded")
check(manifest["gates"]["final_pull_request_browser_quality"] == "passed-run-29862965289", "Final PR browser quality is not recorded")
check(manifest["gates"]["post_merge_validation"] == "passed-run-29863235105", "Post-merge validation is not recorded")
check(manifest["gates"]["pages_deployment"] == "passed-run-29863234835", "Pages deployment is not recorded")
check(manifest["publication"]["merge_commit"] == "e84f53a6caaca696a8143a2aab2e7a24e9bdb4e8", "Sprint 5 merge commit differs")
check(manifest["publication"]["portal_verification"] == "passed-http-200-0.7.0-rc.1-2026-07-21", "Portal verification is not recorded")
check(manifest["publication"]["status"] == "candidate-ratified-merged-deployed", "Sprint 5 publication state is inaccurate")

portal_markers = {
    "mkdocs.yml": "portal: v0.8.0-rc.1",
    "overrides/main.html": "Portal v0.8.0-rc.1",
    "README.md": "`v0.7.0-rc.1`",
    "package.json": '"version": "0.8.0-rc.1"',
    "package-lock.json": '"version": "0.8.0-rc.1"',
}
for path, marker in portal_markers.items():
    check(marker in (ROOT / path).read_text(encoding="utf-8"), f"Sprint 5 portal marker missing: {path}")

sprint4 = load_yaml("governance/sprint-4-manifest.yml")
check(sprint4["gates"]["owner_ratification"] == "passed-user-ratification-2026-07-21", "Sprint 4 owner ratification is not closed")
check(sprint4["publication"]["merge_commit"] == "958e2ee0c5326b2329e3f0a64259d149362571df", "Sprint 4 merge commit is not recorded")
check(sprint4["publication"]["status"] == "candidate-ratified-merged-deployed", "Sprint 4 deployment closure is absent")

case = load_yaml("governance/cases/B2B-PROP-001.yml")
check(case["release"] == "0.5.0-rc.1", "Sprint 5 rewrote the historical case release")
check(case["status"] == "instrumented-not-executed", "Sprint 5 overstates case execution")
check(case["evaluation"]["action_executed"] is False, "Sprint 5 invents an executed action")
check(case["evaluation"]["outcome_observed"] is False, "Sprint 5 invents an outcome")

stable_docs = [
    "docs/00-foundation/constitution.md",
    "docs/00-foundation/cdi-scope-boundaries.md",
    "docs/00-foundation/glossary.md",
    "docs/00-foundation/domain-map.md",
    "docs/03-pulse/specification.md",
]
for path in stable_docs:
    metadata, _ = markdown(path)
    check(metadata.get("version") == "0.4.0", f"Sprint 5 altered stable core version: {path}")
    check(metadata.get("status") == "approved", f"Sprint 5 altered stable core authority: {path}")

all_new_text = "\n".join(body for _, body in documents.values()).lower()
for prohibited in [
    "pulse demostró que",
    "cdi demostró que",
    "garantiza mejores decisiones",
    "instrumento científicamente validado",
    "decision health score:",
    "menor latencia siempre es mejor",
    "los overrides siempre deben minimizarse",
]:
    check(prohibited not in all_new_text, f"Premature or unsafe claim found: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} Sprint 5 error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 5 decision measurement validated ({CHECKS} checks)")
