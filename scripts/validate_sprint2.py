#!/usr/bin/env python3
"""Validate the ratified CDI-BoK Sprint 2 core and stable v0.4.0 contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.4.0"


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
    "docs/00-foundation/constitution.md": {
        "artifact_type": "constitution",
        "authority_level": "foundational-approved",
        "normative": True,
    },
    "docs/00-foundation/cdi-scope-boundaries.md": {
        "artifact_type": "scope-standard",
        "authority_level": "institutional-approved",
        "normative": True,
    },
    "docs/00-foundation/glossary.md": {
        "artifact_type": "controlled-glossary",
        "authority_level": "approved-controlled",
        "normative": True,
    },
    "docs/00-foundation/domain-map.md": {
        "artifact_type": "knowledge-map",
        "authority_level": "approved-controlled",
        "normative": True,
    },
    "docs/03-pulse/specification.md": {
        "artifact_type": "framework-specification",
        "authority_level": "constitutional-derived-approved",
        "normative": False,
    },
}
documents: dict[str, tuple[dict, str]] = {}
for path, expected in required_docs.items():
    check((ROOT / path).exists(), f"Missing Sprint 2 document: {path}")
    if not (ROOT / path).exists():
        continue
    metadata, body = markdown(path)
    documents[path] = (metadata, body)
    check(metadata.get("version") == RELEASE, f"Wrong Sprint 2 version: {path}")
    check(metadata.get("status") == "approved", f"Ratified document must be approved: {path}")
    check(metadata.get("normative") is expected["normative"], f"Wrong normative flag: {path}")
    check(metadata.get("artifact_type") == expected["artifact_type"], f"Wrong artifact type: {path}")
    check(metadata.get("authority_level") == expected["authority_level"], f"Wrong authority level: {path}")
    check(bool(metadata.get("source_ids")), f"Missing source_ids: {path}")

definition = (
    "Conversational Decision Intelligence (CDI) es el dominio de práctica interdisciplinar propuesto "
    "que estudia y diseña cómo personas y sistemas de inteligencia artificial colaboran mediante "
    "conversaciones para convertir evidencia confiable y contexto en decisiones explícitas, acción "
    "responsable y aprendizaje medible."
)
constitution = documents.get("docs/00-foundation/constitution.md", ({}, ""))[1]
scope = documents.get("docs/00-foundation/cdi-scope-boundaries.md", ({}, ""))[1]
check(definition in constitution, "CDI definition differs in Constitution")
check(definition in scope, "CDI definition differs in scope standard")
check("no reclama haber acuñado la expresión" in scope, "Prior-art no-coinage boundary is missing")
check("dominio de práctica interdisciplinar propuesto" in scope, "CDI maturity boundary is missing")

pulse_definition = (
    "PULSE is a human-centered Decision Intelligence methodology and operating philosophy that reduces "
    "the distance between organizational reality and better decisions by turning trusted data and context "
    "into shared understanding, action, and measurable learning."
)
pulse_spec = documents.get("docs/03-pulse/specification.md", ({}, ""))[1]
pulse_dna = (ROOT / "sources/constitutional/00_PULSE_DNA.md").read_text(encoding="utf-8")
check(pulse_definition in pulse_spec, "Official PULSE definition is absent from public specification")
check(pulse_definition in pulse_dna, "Public PULSE definition does not exist in canonical DNA")
for term in ["PDAMR", "Decision Circle", "Human-in-Control", "Interface Independence", "Value Must Be Observable"]:
    check(term in pulse_spec, f"PULSE specification omits {term}")
check("No redefine PULSE" in pulse_spec, "PULSE projection boundary is missing")

concepts = load_yaml("governance/registries/concepts.yml")
expected_domains = concepts["domains"]
domain_body = documents.get("docs/00-foundation/domain-map.md", ({}, ""))[1]
table_domains = re.findall(r"^\| \*\*([^*]+)\*\* \|", domain_body, flags=re.MULTILINE)
check(len(table_domains) == 29, f"Expected 29 domain rows, found {len(table_domains)}")
check(set(table_domains) == set(expected_domains), "Public domain map differs from concept registry")
check(len(set(table_domains)) == len(table_domains), "Duplicate domain in public map")

glossary_body = documents.get("docs/00-foundation/glossary.md", ({}, ""))[1]
glossary_terms = re.findall(r"^\| \*\*([^*]+)\*\* \|", glossary_body, flags=re.MULTILINE)
check(len(glossary_terms) >= 25, f"Initial glossary is too small: {len(glossary_terms)} terms")
check(len(glossary_terms) == len(set(glossary_terms)), "Duplicate controlled glossary term")
for term in ["Conversational Decision Intelligence (CDI)", "PULSE", "Human-in-Control", "Decisión", "Resultado"]:
    check(term in glossary_terms, f"Required glossary term is missing: {term}")

concept_by_id = {item["concept_id"]: item for item in concepts["concepts"]}
for concept_id in ["PULSE", "PDAMR", "PULSE-DECISION-CIRCLE", "DECISION-EXPERIENCE", "HUMAN-IN-CONTROL"]:
    check(
        concept_by_id[concept_id]["canonical_definition_location"] == "sources/constitutional/00_PULSE_DNA.md",
        f"PULSE-owned concept points outside DNA: {concept_id}",
    )
check(concept_by_id["CDI"]["canonical_definition_location"] == "docs/00-foundation/cdi-scope-boundaries.md", "CDI canonical location is wrong")

sources = load_yaml("governance/registries/sources.yml")["records"]
source_ids = {item["source_id"] for item in sources}
required_sources = {
    "SRC-PRIOR-CDI-001",
    "SRC-PRIOR-CDI-002",
    "SRC-ACADEMIC-HAI-001",
    "SRC-ACADEMIC-AIEVAL-001",
}
check(required_sources.issubset(source_ids), "Sprint 2 research sources are incomplete")

claims = load_yaml("governance/registries/claims.yml")["claims"]
claim_by_id = {item["claim_id"]: item for item in claims}
for claim_id in ["CLAIM-CDI-001", "CLAIM-CDI-PRIOR-001", "CLAIM-CDI-EFFECT-001", "CLAIM-DOMAINS-001", "CLAIM-PULSE-ROLE-001"]:
    check(claim_id in claim_by_id, f"Missing Sprint 2 claim: {claim_id}")
for claim in claims:
    for source_id in claim.get("source_ids", []):
        check(source_id in source_ids, f"Unknown source {source_id} in {claim['claim_id']}")

adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
for adr_id in ["ADR-014", "ADR-015", "ADR-016", "ADR-017"]:
    check(adr_by_id.get(adr_id, {}).get("status") == "accepted", f"Missing accepted {adr_id}")

content_map = load_yaml("governance/content-map.yml")
check(content_map["release"] == RELEASE, "Content map registry release mismatch")
check(content_map["public_portal"]["release"] == RELEASE, "Content map portal release mismatch")
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
check(set(required_docs).issubset(registered), "Sprint 2 documents are absent from public content map")
check("docs/versions/v0.4.0.md" in registered, "Stable release note is absent from public content map")

manifest = load_yaml("governance/sprint-2-manifest.yml")
check(manifest["release"] == RELEASE, "Sprint 2 manifest release mismatch")
check(manifest["source_candidate"] == "0.4.0-rc.1", "Sprint 2 source candidate is missing")
check(manifest["gates"]["pages_live"] == "passed-http-200", "Sprint 1 deployment is not recorded as verified")
check(manifest["gates"]["owner_ratification"] == "passed-2026-07-21", "Owner ratification is not recorded")
check(manifest["ratification"]["ratified_by"] == "Javier Forero", "Ratifier differs from the owner decision")
check(manifest["ratification"]["governed_by"] == "ADR-017", "Ratification lacks ADR-017")

release_manifest = load_yaml("governance/releases/v0.4.0.yml")
check(release_manifest["release"] == RELEASE, "Stable release manifest version mismatch")
check(release_manifest["tag"] == f"v{RELEASE}", "Stable release tag mismatch")
check(release_manifest["status"] == "stable", "Release manifest is not stable")
check(release_manifest["source_candidate"] == "0.4.0-rc.1", "Release lineage is incomplete")
check(release_manifest["ratification"]["governed_by"] == "ADR-017", "Release manifest lacks ADR-017")
promotion_by_path = {item["path"]: item for item in release_manifest["promotions"]}
for path, expected in required_docs.items():
    promotion = promotion_by_path.get(path, {})
    check(promotion.get("status") == "approved", f"Release promotion status mismatch: {path}")
    check(promotion.get("authority_level") == expected["authority_level"], f"Release promotion authority mismatch: {path}")
    check(promotion.get("normative") is expected["normative"], f"Release promotion normative mismatch: {path}")

for registry_path in [
    "governance/registries/concepts.yml",
    "governance/registries/claims.yml",
    "governance/registries/sources.yml",
    "governance/adr/index.yml",
]:
    check(load_yaml(registry_path)["release"] == RELEASE, f"Registry release mismatch: {registry_path}")

check(concept_by_id["CDI"]["status"] == "approved", "CDI concept was not promoted")
check(claim_by_id["CLAIM-CDI-001"]["maturity"] == "approved-project-definition", "CDI definition claim was not promoted")
check(claim_by_id["CLAIM-DOMAINS-001"]["maturity"] == "approved-institutional-taxonomy", "Domain taxonomy claim was not promoted")
check(claim_by_id["CLAIM-PULSE-ROLE-001"]["maturity"] == "approved-derived", "PULSE role claim was not promoted")

portal_files = {
    "mkdocs.yml": "portal: v0.4.0",
    "overrides/main.html": "Portal v0.4.0",
    "README.md": "`v0.4.0`",
    "package.json": '"version": "0.4.0"',
}
for path, marker in portal_files.items():
    check(marker in (ROOT / path).read_text(encoding="utf-8"), f"Stable portal marker missing: {path}")

all_foundational_text = "\n".join(body for _, body in documents.values()).lower()
for prohibited in [
    "cdi es una disciplina científica consolidada",
    "el cdi-bok es el estándar internacional",
    "pulse garantiza mejores decisiones",
    "acuñamos conversational decision intelligence",
]:
    check(prohibited not in all_foundational_text, f"Premature claim found: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} Sprint 2 error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 2 stable foundational core validated ({CHECKS} checks)")
