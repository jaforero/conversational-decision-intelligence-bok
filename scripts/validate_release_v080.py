#!/usr/bin/env python3
"""Validate the bounded stable promotion contract for CDI-BoK v0.8.0."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0
RELEASE = "0.8.0"
SOURCE_CANDIDATE = "0.8.0-rc.1"
ACTIVE_PORTAL = "0.9.0-rc.1"


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def load_yaml(relative: str):
    with (ROOT / relative).open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def markdown(relative: str) -> tuple[dict, str]:
    value = text(relative)
    check(value.startswith("---\n"), f"Missing front matter: {relative}")
    parts = value.split("---", 2)
    check(len(parts) == 3, f"Invalid front matter boundary: {relative}")
    if len(parts) != 3:
        return {}, value
    return yaml.safe_load(parts[1]) or {}, parts[2]


required_files = [
    "governance/adr/ADR-024-v080-stable-promotion.md",
    "governance/releases/v0.8.0.yml",
    "governance/releases/v0.8.0-notes.md",
    "docs/versions/v0.8.0.md",
    "docs/versions/v0.8.0-rc.1.md",
    ".github/workflows/release.yml",
]
for path in required_files:
    check((ROOT / path).exists(), f"Stable promotion file is missing: {path}")

adr = text("governance/adr/ADR-024-v080-stable-promotion.md")
for marker in [
    "id: ADR-024",
    "status: accepted",
    "línea base editorial y técnica estable",
    "no cambia en bloque el estado editorial",
    "refs/tags/v0.8.0",
    "Estabilidad técnica no es validación científica",
]:
    check(marker in adr, f"ADR-024 misses stable boundary: {marker}")

adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
check(adr_index["release"] in {RELEASE, ACTIVE_PORTAL}, "ADR registry lost stable release lineage")
check(adr_by_id.get("ADR-024", {}).get("status") == "accepted", "ADR-024 is not accepted in the registry")

manifest = load_yaml("governance/releases/v0.8.0.yml")
check(manifest["schema_version"] == "1.0.0", "Stable manifest schema differs")
check(manifest["release"] == RELEASE, "Stable manifest release differs")
check(manifest["tag"] == f"v{RELEASE}", "Stable manifest tag differs")
check(manifest["status"] == "stable", "Stable manifest status differs")
check(manifest["source_candidate"] == SOURCE_CANDIDATE, "Stable manifest source candidate differs")
check(manifest["source_candidate_commit"] == "bbc5c0583b28bbc3d4d2b6a2aedf28f8df336347", "Stable source candidate commit differs")
check(manifest["reference"] == "refs/tags/v0.8.0", "Stable manifest reference is not tag-resolvable")
check(manifest["notes_path"] == "governance/releases/v0.8.0-notes.md", "Stable release notes path differs")
check(manifest["ratification"]["ratified_by"] == "Javier Forero", "Stable ratifier differs")
check(str(manifest["ratification"]["ratified_on"]) == "2026-07-21", "Stable ratification date differs")
check(manifest["ratification"]["governed_by"] == "ADR-024", "Stable ratification lacks ADR-024")

scope = {item["component"]: item for item in manifest["stable_scope"]}
expected_scope = {
    "integrated-portal": "stable",
    "governance-v0.2.0": "approved",
    "foundational-core-v0.4.0": "approved",
    "practice-v0.5.0-rc.1": "candidate-instrumented-not-executed",
    "learning-v0.6.0-rc.1": "candidate-ratified",
    "measurement-v0.7.0-rc.1": "candidate-synthesis-ratified",
    "patterns-v0.8.0-rc.1": "candidate-synthesis-ratified",
}
check(set(scope) == set(expected_scope), "Stable scope components are incomplete or unexpected")
for component, status in expected_scope.items():
    check(scope.get(component, {}).get("status") == status, f"Stable scope status differs: {component}")
    check(bool(scope.get(component, {}).get("authority_effect")), f"Stable scope lacks authority effect: {component}")

quality = manifest["quality_evidence"]
check(quality["candidate_pull_request"].endswith("/pull/10"), "Stable manifest candidate PR differs")
check(quality["candidate_merge_commit"] == manifest["source_candidate_commit"], "Stable manifest candidate lineage diverges")
check(quality["post_merge_validation"].endswith("/29871891960"), "Stable post-merge validation differs")
check(quality["pages_deployment"].endswith("/29871892015"), "Stable Pages deployment differs")
check(quality["portal_verification"].startswith("passed-http-200"), "Stable portal verification is absent")
check(quality["stable_gate"] == ".github/workflows/release.yml", "Stable gate path differs")
check(len(manifest["limitations"]) >= 6, "Stable manifest lacks calibrated limitations")

sprint6 = load_yaml("governance/sprint-6-manifest.yml")
check(sprint6["release"] == SOURCE_CANDIDATE, "Sprint 6 historical release differs")
check(sprint6["status"] == "candidate-ratified-merged-deployed", "Sprint 6 is not closed")
check(sprint6["gates"]["owner_ratification"] == "passed-user-ratification-2026-07-21", "Sprint 6 owner ratification is absent")
check(sprint6["gates"]["post_merge_validation"] == "passed-run-29871891960", "Sprint 6 post-merge validation differs")
check(sprint6["gates"]["pages_deployment"] == "passed-run-29871892015", "Sprint 6 deployment differs")
check(sprint6["publication"]["merge_commit"] == manifest["source_candidate_commit"], "Sprint 6 and stable manifest lineage diverge")

registry = load_yaml("governance/releases/index.yml")
records = {item["version"]: item for item in registry["releases"]}
authorized_tags = {item["tag"]: item for item in registry["tag_snapshot"]["authorized_for_post_merge_creation"]}
stable_record = records.get(RELEASE, {})
candidate_record = records.get(SOURCE_CANDIDATE, {})
check(stable_record.get("release_class") == "stable-release", "v0.8.0 release class differs")
check(stable_record.get("status") == "stable", "v0.8.0 registry status differs")
check(stable_record.get("tag") == "v0.8.0", "v0.8.0 registry tag differs")
check(stable_record.get("reference_commit") == "refs/tags/v0.8.0", "v0.8.0 registry reference differs")
check(stable_record.get("source_candidate") == SOURCE_CANDIDATE, "v0.8.0 registry source candidate differs")
check(candidate_record.get("status") == "candidate-ratified-merged-deployed-promoted", "Source candidate closure differs")
check(candidate_record.get("tag") is None, "Source candidate received an unauthorized retrospective tag")
check(candidate_record.get("reference_commit") == manifest["source_candidate_commit"], "Source candidate merge reference differs")
check(candidate_record.get("superseded_by") == RELEASE, "Source candidate promotion lineage differs")
check(authorized_tags.get("v0.8.0", {}).get("target") == "validated-main-sha", "Stable tag target authorization differs")
check(authorized_tags.get("v0.8.0", {}).get("governed_by") == "ADR-024", "Stable tag authorization lacks ADR-024")

for path in [
    "governance/registries/sources.yml",
    "governance/registries/claims.yml",
    "governance/registries/concepts.yml",
    "governance/registries/external-demos.yml",
    "governance/registries/patterns.yml",
]:
    check(load_yaml(path).get("release") == ACTIVE_PORTAL, f"Current registry release differs: {path}")

check(load_yaml("governance/adr/index.yml").get("release") == ACTIVE_PORTAL, "ADR registry active release differs")
check(load_yaml("governance/content-map.yml").get("release") == ACTIVE_PORTAL, "Content map active release differs")

content_map = load_yaml("governance/content-map.yml")
check(content_map["public_portal"]["release"] == ACTIVE_PORTAL, "Public portal content-map release differs")
navigation = {item["path"]: item for item in content_map["public_portal"]["navigation"]}
check(navigation.get("docs/versions/v0.8.0.md", {}).get("status") == "approved", "Stable public release note is not registered")
check(navigation.get("docs/versions/v0.8.0-rc.1.md", {}).get("status") == "candidate", "Source candidate note lost candidate status")

stable_metadata, stable_body = markdown("docs/versions/v0.8.0.md")
check(stable_metadata.get("version") == RELEASE, "Stable public note version differs")
check(stable_metadata.get("status") == "approved", "Stable public note is not approved")
check(stable_metadata.get("normative") is False, "Stable public note became normative")
for marker in [
    "Qué se estabiliza",
    "Autoridad preservada por componente",
    "línea base integrada",
    "Qué no significa “estable”",
    "no aporta impacto observado",
]:
    check(marker.lower() in stable_body.lower(), f"Stable public note misses boundary: {marker}")

candidate_metadata, candidate_body = markdown("docs/versions/v0.8.0-rc.1.md")
check(candidate_metadata.get("version") == SOURCE_CANDIDATE, "Source candidate public note version differs")
check(candidate_metadata.get("status") == "candidate", "Source candidate public note status differs")
check("Candidato ratificado, fusionado y desplegado" in candidate_body, "Source candidate public closure is absent")
check("permanece sin tag" in candidate_body.lower(), "Source candidate tag boundary is absent")

candidate_artifacts = {
    "docs/learn/index.md": "0.7.0-rc.1",
    "docs/07-governance-quality/index.md": "0.7.0-rc.1",
    "docs/08-patterns/index.md": "0.8.0-rc.1",
    "docs/08-patterns/catalog.md": "0.8.0-rc.1",
    "docs/08-patterns/anti-patterns.md": "0.8.0-rc.1",
}
for path, version in candidate_artifacts.items():
    metadata, _ = markdown(path)
    check(metadata.get("version") == version, f"Candidate artifact lineage changed: {path}")
    check(metadata.get("status") == "candidate", f"Bundle stability promoted candidate artifact: {path}")
    check(metadata.get("normative") is False, f"Bundle stability made candidate artifact normative: {path}")

stable_core = [
    "docs/00-foundation/constitution.md",
    "docs/00-foundation/cdi-scope-boundaries.md",
    "docs/00-foundation/glossary.md",
    "docs/00-foundation/domain-map.md",
    "docs/03-pulse/specification.md",
]
for path in stable_core:
    metadata, _ = markdown(path)
    check(metadata.get("version") == "0.4.0", f"v0.8.0 rewrote stable core lineage: {path}")
    check(metadata.get("status") == "approved", f"v0.8.0 altered stable core authority: {path}")

case = load_yaml("governance/cases/B2B-PROP-001.yml")
check(case["release"] == "0.5.0-rc.1", "Stable bundle rewrote the B2B case release")
check(case["status"] == "instrumented-not-executed", "Stable bundle overstates B2B execution")
check(case["evaluation"]["action_executed"] is False, "Stable bundle invents a B2B action")
check(case["evaluation"]["outcome_observed"] is False, "Stable bundle invents a B2B outcome")

portal_markers = {
    "mkdocs.yml": "portal: v0.9.0-rc.1",
    "overrides/main.html": "Candidato de evidencia v0.9.0-rc.1",
    "README.md": "Candidato activo: `v0.9.0-rc.1`",
    "package.json": '"version": "0.9.0-rc.1"',
    "package-lock.json": '"version": "0.9.0-rc.1"',
    "docs/index.md": "Portal candidato v0.9.0-rc.1",
    "CHANGELOG.md": "## [0.8.0] - 2026-07-21",
}
for path, marker in portal_markers.items():
    check(marker in text(path), f"Stable portal marker is missing: {path}")

workflow = text(".github/workflows/release.yml")
for marker in [
    '"governance/releases/v*.yml"',
    'package = json.loads(Path("package.json")',
    'manifest_path = Path(f"governance/releases/v{version}.yml")',
    'notes_path = Path(manifest["notes_path"])',
    '--target "${GITHUB_SHA}"',
    '--title "${RELEASE_TITLE}"',
]:
    check(marker in workflow, f"Stable release workflow misses dynamic control: {marker}")
check('Path("governance/releases/v0.4.0.yml")' not in workflow, "Stable workflow remains hard-coded to v0.4.0")
check("python scripts/preflight_release.py" in workflow, "Stable workflow omits preflight")
check("npx playwright install --with-deps chromium" in workflow, "Stable workflow omits canonical Chromium")
check("npm test" in workflow, "Stable workflow omits browser and Axe gates")

release_text = "\n".join([
    stable_body.lower(),
    text("governance/releases/v0.8.0-notes.md").lower(),
    adr.lower(),
])
for prohibited in [
    "pulse está científicamente validado",
    "los patrones garantizan mejores decisiones",
    "el caso b2b demuestra impacto",
    "cdi es una disciplina científica consolidada",
    "conforme con wcag 2.2 aa",
]:
    check(prohibited not in release_text, f"Stable promotion contains premature claim: {prohibited}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} v0.8.0 stable-promotion error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: v0.8.0 stable promotion validated ({CHECKS} checks)")
