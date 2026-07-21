#!/usr/bin/env python3
"""Validate Sprint 6 conversational decision pattern boundaries and artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.8.0-rc.1"


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
    "docs/08-patterns/index.md": "knowledge-area-landing",
    "docs/08-patterns/pattern-language.md": "candidate-standard",
    "docs/08-patterns/catalog.md": "pattern-catalog",
    "docs/08-patterns/anti-patterns.md": "anti-pattern-catalog",
    "docs/08-patterns/b2b-proposal-walkthrough.md": "pattern-demonstration",
    "docs/versions/v0.8.0-rc.1.md": "release-note",
}
documents: dict[str, tuple[dict, str]] = {}
for path, artifact_type in required_docs.items():
    check((ROOT / path).exists(), f"Missing Sprint 6 document: {path}")
    if not (ROOT / path).exists():
        continue
    metadata, body = markdown(path)
    documents[path] = (metadata, body)
    check(metadata.get("version") == RELEASE, f"Wrong Sprint 6 version: {path}")
    check(metadata.get("status") == "candidate", f"Sprint 6 document must remain candidate: {path}")
    check(metadata.get("normative") is False, f"Sprint 6 document cannot be normative: {path}")
    check(metadata.get("artifact_type") == artifact_type, f"Wrong artifact type: {path}")

markers = {
    "docs/08-patterns/index.md": [
        "Un patrón no decide por ti",
        "Empieza por el bloqueo",
        "Ajusta el rigor al riesgo",
        "no autoriza a un sistema de IA",
    ],
    "docs/08-patterns/pattern-language.md": [
        "definiciones institucionales candidatas",
        "Un patrón es reusable",
        "Stop conditions",
        "candidate-synthesis",
        "mínimo suficiente",
    ],
    "docs/08-patterns/catalog.md": [
        "CDP-001",
        "CDP-002",
        "CDP-003",
        "CDP-004",
        "CDP-005",
        "Alternativa superior en ciertos contextos",
        "Qué validaría o refutaría el catálogo",
    ],
    "docs/08-patterns/anti-patterns.md": [
        "ANTI-CDI-001",
        "ANTI-CDI-002",
        "ANTI-CDI-003",
        "ANTI-CDI-004",
        "ANTI-CDI-005",
        "ANTI-CDI-006",
        "Control de segundo orden",
    ],
    "docs/08-patterns/b2b-proposal-walkthrough.md": [
        "Demostración detenida",
        "instrumented-not-executed",
        "interfaz conversacional sería **decorativa",
        "Preparado para revisión del owner; no autorizado para ejecutar",
        "todavía **no aplica**",
        "no demuestra",
    ],
    "docs/versions/v0.8.0-rc.1.md": [
        "no es una secuencia universal ni una librería de prompts",
        "Candidato implementado, no ratificado",
        "No se afirma que seguir los patrones mejore",
    ],
}
for path, expected in markers.items():
    body = documents.get(path, ({}, ""))[1]
    for marker in expected:
        check(marker.lower() in body.lower(), f"{path} misses calibrated marker: {marker}")

registry = load_yaml("governance/registries/patterns.yml")
check(registry["release"] == RELEASE, "Pattern registry release mismatch")
check(registry["governed_by"] == "ADR-023", "Pattern registry is not governed by ADR-023")
check(registry["catalog_maturity"] == "candidate-synthesis", "Pattern registry overstates maturity")
patterns = registry["patterns"]
anti_patterns = registry["anti_patterns"]
check(len(patterns) == 5, "Initial pattern catalog must contain five entries")
check(len(anti_patterns) == 6, "Initial anti-pattern catalog must contain six entries")
expected_patterns = {f"CDP-{number:03d}" for number in range(1, 6)}
expected_anti = {f"ANTI-CDI-{number:03d}" for number in range(1, 7)}
pattern_ids = {item["pattern_id"] for item in patterns}
anti_ids = {item["pattern_id"] for item in anti_patterns}
check(pattern_ids == expected_patterns, "Pattern IDs are incomplete or unexpected")
check(anti_ids == expected_anti, "Anti-pattern IDs are incomplete or unexpected")
for item in patterns:
    check(item["kind"] == "pattern", f"Wrong kind for {item['pattern_id']}")
    check(item["status"] == "candidate-synthesis", f"Maturity overstated for {item['pattern_id']}")
    check(bool(item.get("stop_condition")), f"Missing stop condition for {item['pattern_id']}")
    check(bool(item.get("output")), f"Missing output for {item['pattern_id']}")
    check(bool(item.get("source_ids")), f"Missing provenance for {item['pattern_id']}")
for item in anti_patterns:
    check(item["kind"] == "anti-pattern", f"Wrong kind for {item['pattern_id']}")
    check(item["status"] == "candidate-synthesis", f"Maturity overstated for {item['pattern_id']}")
    check(bool(item.get("observable_behavior")), f"Missing observable behavior for {item['pattern_id']}")
    check(set(item.get("repair_pattern_ids", [])).issubset(pattern_ids), f"Unknown repair pattern in {item['pattern_id']}")

template = load_yaml("docs/assets/data/conversational-decision-pattern.yml")
check(template["template_version"] == RELEASE, "Pattern template version mismatch")
check(template["record_status"] == "draft", "Pattern template must begin in draft")
pattern_template = template["pattern"]
for key in ["id", "name", "kind", "decision_moment", "decision_class", "context", "problem", "owner", "created_on", "last_reviewed"]:
    check(pattern_template[key] is None, f"Pattern template invents {key}")
for key in ["forces", "preconditions", "use_when", "do_not_use_when", "alternatives", "tested_contexts"]:
    check(pattern_template[key] == [], f"Pattern template does not begin empty: {key}")
check(pattern_template["governance"]["trace_required"] is True, "Pattern template does not require trace")
check(pattern_template["governance"]["human_commit_required"] is True, "Pattern template does not require human commitment")
check(pattern_template["conversation_contract"]["stop_or_escalate_conditions"] == [], "Template invents stop conditions")
check(pattern_template["measurement"]["review_horizon"] is None, "Template invents a review horizon")

sources = load_yaml("governance/registries/sources.yml")
source_ids = {item["source_id"] for item in sources["records"]}
for item in patterns + anti_patterns:
    for source_id in item.get("source_ids", []):
        check(source_id in source_ids, f"Unknown source {source_id} in {item['pattern_id']}")

claims = load_yaml("governance/registries/claims.yml")
claim_by_id = {item["claim_id"]: item for item in claims["claims"]}
for claim_id in ["CLAIM-CDP-CATALOG-001", "CLAIM-CDP-SELECTION-001"]:
    check(claim_id in claim_by_id, f"Missing Sprint 6 claim: {claim_id}")
    check(claim_by_id.get(claim_id, {}).get("maturity") == "candidate", f"Sprint 6 claim maturity overstated: {claim_id}")
check("no es exhaustiva" in claim_by_id["CLAIM-CDP-CATALOG-001"]["limits"].lower(), "Catalog claim lacks exhaustiveness limit")
check(claim_by_id["CLAIM-CDP-SELECTION-001"]["claim_class"] == "design-recommendation", "Selection rule is presented as empirical fact")
for claim in claims["claims"]:
    for source_id in claim.get("source_ids", []):
        check(source_id in source_ids, f"Unknown source {source_id} in {claim['claim_id']}")

concepts = load_yaml("governance/registries/concepts.yml")
concept_by_id = {item["concept_id"]: item for item in concepts["concepts"]}
for concept_id in ["CONVERSATIONAL-DECISION-PATTERN", "CONVERSATIONAL-DECISION-ANTIPATTERN"]:
    check(concept_by_id.get(concept_id, {}).get("status") == "candidate-synthesis", f"Missing or overstated concept: {concept_id}")

registries = [
    "governance/registries/sources.yml",
    "governance/registries/claims.yml",
    "governance/registries/concepts.yml",
    "governance/registries/external-demos.yml",
    "governance/registries/patterns.yml",
    "governance/adr/index.yml",
]
for path in registries:
    check(load_yaml(path).get("release") == RELEASE, f"Registry release mismatch: {path}")

adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
check(adr_by_id.get("ADR-023", {}).get("status") == "accepted", "ADR-023 is not accepted")
check((ROOT / "governance/adr/ADR-023-conversational-decision-pattern-architecture.md").exists(), "ADR-023 file is missing")

content_map = load_yaml("governance/content-map.yml")
check(content_map["release"] == RELEASE, "Content map release mismatch")
check(content_map["public_portal"]["release"] == RELEASE, "Portal content-map release mismatch")
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
check(set(required_docs).issubset(registered), "Sprint 6 documents are absent from the content map")
check("governance/registries/patterns.yml" in content_map["collections"]["registries"]["paths"], "Pattern registry is absent from the content map")

manifest = load_yaml("governance/sprint-6-manifest.yml")
check(manifest["release"] == RELEASE, "Sprint 6 manifest release mismatch")
check(manifest["status"] == "candidate-implemented-not-ratified", "Sprint 6 manifest overstates status")
check(manifest["gates"]["owner_ratification"] == "pending", "Sprint 6 invents owner ratification")
check(manifest["publication"]["status"] == "candidate-implemented-not-ratified", "Sprint 6 publication status differs")
check(manifest["publication"]["branch"] == "agent/sprint-6-conversational-patterns", "Sprint 6 branch differs")

release_registry = load_yaml("governance/releases/index.yml")
release_by_version = {item["version"]: item for item in release_registry["releases"]}
release_record = release_by_version.get(RELEASE, {})
check(release_record.get("release_class") == "release-candidate", "Sprint 6 release class differs")
check(release_record.get("status") == "candidate-implemented-not-ratified", "Sprint 6 release status differs")
check(release_record.get("tag") is None, "Sprint 6 creates an unauthorized tag")
reference = release_record.get("reference_commit", "")
check(reference == "pending-pr-head" or bool(re.fullmatch(r"[0-9a-f]{40}", reference)), "Sprint 6 reference commit is invalid")

portal_markers = {
    "mkdocs.yml": "portal: v0.8.0-rc.1",
    "overrides/main.html": "Portal v0.8.0-rc.1",
    "README.md": "`v0.8.0-rc.1`",
    "package.json": '"version": "0.8.0-rc.1"',
    "package-lock.json": '"version": "0.8.0-rc.1"',
    "docs/index.md": "Patrones candidatos v0.8.0-rc.1",
}
for path, marker in portal_markers.items():
    check(marker in (ROOT / path).read_text(encoding="utf-8"), f"Sprint 6 portal marker missing: {path}")

case = load_yaml("governance/cases/B2B-PROP-001.yml")
check(case["release"] == "0.5.0-rc.1", "Sprint 6 rewrote the historical case release")
check(case["status"] == "instrumented-not-executed", "Sprint 6 overstates case execution")
check(case["evaluation"]["action_executed"] is False, "Sprint 6 invents an executed action")
check(case["evaluation"]["outcome_observed"] is False, "Sprint 6 invents an outcome")

stable_docs = [
    "docs/00-foundation/constitution.md",
    "docs/00-foundation/cdi-scope-boundaries.md",
    "docs/00-foundation/glossary.md",
    "docs/00-foundation/domain-map.md",
    "docs/03-pulse/specification.md",
]
for path in stable_docs:
    metadata, _ = markdown(path)
    check(metadata.get("version") == "0.4.0", f"Sprint 6 altered stable core version: {path}")
    check(metadata.get("status") == "approved", f"Sprint 6 altered stable core authority: {path}")

all_new_text = "\n".join(body for _, body in documents.values()).lower()
for prohibited in [
    "los patrones garantizan",
    "taxonomía científicamente validada",
    "secuencia universal obligatoria",
    "pulse demostró que",
    "cdi demostró que",
    "la intervención produjo",
    "outcome observado en el caso b2b",
]:
    check(prohibited not in all_new_text, f"Premature or unsafe claim found: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} Sprint 6 error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 6 conversational decision patterns validated ({CHECKS} checks)")
