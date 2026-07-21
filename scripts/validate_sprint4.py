#!/usr/bin/env python3
"""Validate Sprint 4 learning depth, reader outcomes and release boundaries."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.6.0-rc.1"
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
    "docs/index.md": "portal-home",
    "docs/learn/index.md": "learning-path",
    "docs/learn/01-decision-first.md": "learning-module",
    "docs/learn/02-evidence-context.md": "learning-module",
    "docs/learn/03-decision-experience.md": "learning-module",
    "docs/learn/04-human-ai-control.md": "learning-module",
    "docs/learn/05-action-learning.md": "learning-module",
    "docs/learn/decision-brief.md": "practice-template",
    "docs/versions/v0.6.0-rc.1.md": "release-note",
}

documents: dict[str, tuple[dict, str]] = {}
for path, artifact_type in required_docs.items():
    check((ROOT / path).exists(), f"Missing Sprint 4 public document: {path}")
    if not (ROOT / path).exists():
        continue
    metadata, body = markdown(path)
    documents[path] = (metadata, body)
    check(metadata.get("version") in {RELEASE, "0.7.0-rc.1", CURRENT_RELEASE}, f"Wrong Sprint 4 lineage: {path}")
    check(metadata.get("status") == "candidate", f"Sprint 4 document must remain candidate: {path}")
    check(metadata.get("normative") is False, f"Sprint 4 document cannot be normative: {path}")
    check(metadata.get("artifact_type") == artifact_type, f"Wrong artifact type: {path}")

home = documents.get("docs/index.md", ({}, ""))[1]
for marker in [
    "Convierte datos, analítica e IA en mejores decisiones",
    "Lo que podrás hacer",
    "Formular",
    "Evaluar",
    "Diseñar",
    "Gobernar",
    "Aprender",
    "Practice Lab",
    "instrumentado, no ejecutado",
]:
    check(marker.lower() in home.lower(), f"Home misses outcome or boundary marker: {marker}")

learning = documents.get("docs/learn/index.md", ({}, ""))[1]
for marker in ["Decision Brief", "cinco módulos", "Esto no garantiza una buena decisión", "Qué queda fuera"]:
    check(marker.lower() in learning.lower(), f"Learning path misses calibrated marker: {marker}")

module_markers = {
    "docs/learn/01-decision-first.md": ["PDAMR", "Costo de actuar mal", "Prueba de estrés", "Entregable"],
    "docs/learn/02-evidence-context.md": ["Hecho observado", "Contraevidencia", "Fitness for purpose", "Desconocido"],
    "docs/learn/03-decision-experience.md": ["La unidad de diseño es la decisión", "Elegir la interfaz", "Conversación con estructura", "Feedback"],
    "docs/learn/04-human-ai-control.md": ["Human-in-Control", "Derechos de decisión", "Stop condition", "Accountability"],
    "docs/learn/05-action-learning.md": ["Fijar la expectativa antes de actuar", "Resultado favorable", "Atribución prudente", "guardrails"],
    "docs/learn/decision-brief.md": ["Priority", "Evidence & context", "Human–AI control", "Challenge record"],
}
for path, markers in module_markers.items():
    body = documents.get(path, ({}, ""))[1]
    for marker in markers:
        check(marker.lower() in body.lower(), f"Learning module {path} misses: {marker}")

content_map = load_yaml("governance/content-map.yml")
check(content_map["release"] in {RELEASE, "0.7.0-rc.1", CURRENT_RELEASE}, "Content map lost Sprint 4 lineage")
check(content_map["public_portal"]["release"] in {RELEASE, "0.7.0-rc.1", CURRENT_RELEASE}, "Portal content map lost Sprint 4 lineage")
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
check(set(required_docs).issubset(registered), "Sprint 4 public documents are absent from the content map")

for registry_path in [
    "governance/registries/sources.yml",
    "governance/registries/claims.yml",
    "governance/registries/concepts.yml",
    "governance/registries/external-demos.yml",
    "governance/adr/index.yml",
]:
    check(bool(load_yaml(registry_path).get("release")), f"Current registry lacks release lineage: {registry_path}")

adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
check(adr_by_id.get("ADR-020", {}).get("status") == "accepted", "ADR-020 is not accepted")
check((ROOT / "governance/adr/ADR-020-learning-experience-architecture.md").exists(), "ADR-020 file is missing")

concepts = load_yaml("governance/registries/concepts.yml")
concept_by_id = {item["concept_id"]: item for item in concepts["concepts"]}
check(concept_by_id.get("DECISION-BRIEF", {}).get("status") == "candidate-guidance", "Decision Brief authority is overstated")

manifest = load_yaml("governance/sprint-4-manifest.yml")
check(manifest["release"] == RELEASE, "Sprint 4 manifest release mismatch")
check(manifest["status"] == "candidate-ratified-merged-deployed", "Sprint 4 closed state is not recorded")
check(manifest["gates"]["owner_ratification"] == "passed-user-ratification-2026-07-21", "Owner ratification is not recorded")
check(manifest["gates"]["post_merge_validation"] == "passed-run-29858379946", "Sprint 4 post-merge validation is not recorded")
check(manifest["gates"]["pages_deployment"] == "passed-run-29858379825", "Sprint 4 Pages deployment is not recorded")
check(manifest["publication"]["merge_commit"] == "958e2ee0c5326b2329e3f0a64259d149362571df", "Sprint 4 merge commit differs")
check(manifest["publication"]["validation_run"].endswith("/29858379946"), "Sprint 4 validation URL differs")
check(manifest["publication"]["pages_deployment_run"].endswith("/29858379825"), "Sprint 4 deployment URL differs")
check(manifest["publication"]["deployment_verification"].endswith("958e2ee0c5326b2329e3f0a64259d149362571df"), "Sprint 4 deployed commit differs")
check(manifest["publication"]["portal_position"] == "deployed-then-superseded-by-0.7.0-rc.1", "Sprint 4 current portal position is ambiguous")
check(manifest["publication"]["status"] == "candidate-ratified-merged-deployed", "Sprint 4 publication state is inaccurate")

portal_markers = {
    "mkdocs.yml": "portal: v0.8.0-rc.1",
    "overrides/main.html": "Portal v0.8.0-rc.1",
    "README.md": "`v0.6.0-rc.1`",
    "package.json": '"version": "0.8.0-rc.1"',
    "package-lock.json": '"version": "0.8.0-rc.1"',
}
for path, marker in portal_markers.items():
    check(marker in (ROOT / path).read_text(encoding="utf-8"), f"Sprint 4 portal marker missing: {path}")

portal_css = (ROOT / "docs/assets/stylesheets/cdi-bok.css").read_text(encoding="utf-8")
check('.md-nav__link[href*="learn/"]' in portal_css and "min-height: 24px" in portal_css, "Learning navigation targets are below the 24px floor")
check(".cdi-learning-step small" in portal_css and "opacity: 1" in portal_css, "Learning-step descriptions may inherit low opacity")

case = load_yaml("governance/cases/B2B-PROP-001.yml")
check(case["release"] == "0.5.0-rc.1", "Sprint 4 rewrote the historical case release")
check(case["status"] == "instrumented-not-executed", "Sprint 4 overstates case execution")
check(case["evaluation"]["action_executed"] is False, "Sprint 4 invents an executed action")
check(case["evaluation"]["outcome_observed"] is False, "Sprint 4 invents an observed outcome")

stable_docs = [
    "docs/00-foundation/constitution.md",
    "docs/00-foundation/cdi-scope-boundaries.md",
    "docs/00-foundation/glossary.md",
    "docs/00-foundation/domain-map.md",
    "docs/03-pulse/specification.md",
]
for path in stable_docs:
    metadata, _ = markdown(path)
    check(metadata.get("version") == "0.4.0", f"Sprint 4 altered stable core version: {path}")
    check(metadata.get("status") == "approved", f"Sprint 4 altered stable core authority: {path}")

all_new_text = "\n".join(body for _, body in documents.values()).lower()
for prohibited in [
    "pulse demostró que",
    "cdi demostró que",
    "garantiza mejores decisiones",
    "la intervención produjo",
    "impacto causal observado",
]:
    check(prohibited not in all_new_text, f"Premature or guaranteed claim found: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} Sprint 4 error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 4 learning experience validated ({CHECKS} checks)")
