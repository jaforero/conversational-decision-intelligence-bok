#!/usr/bin/env python3
"""Validate release lineage, candidate closure and tag policy."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
CHECKS = 0


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


adr5 = text("governance/adr/ADR-005-versioning-model.md")
adr22 = text("governance/adr/ADR-022-release-identification-and-tag-policy.md")
adr_index = load_yaml("governance/adr/index.yml")
adr_by_id = {item["id"]: item for item in adr_index["decisions"]}
check("status: superseded" in adr5, "ADR-005 is not marked superseded")
check("superseded_by: ADR-022" in adr5, "ADR-005 lacks its successor")
check("status: accepted" in adr22, "ADR-022 is not accepted")
check("supersedes: ADR-005" in adr22, "ADR-022 does not declare the replaced decision")
check("Release estable" in adr22 and "Release candidate" in adr22, "ADR-022 does not distinguish release classes")
check("No se crearán tags retrospectivos" in adr22, "ADR-022 lacks the non-retroactivity rule")
check(adr_by_id.get("ADR-005", {}).get("status") == "superseded", "ADR registry keeps ADR-005 accepted")
check(adr_by_id.get("ADR-005", {}).get("superseded_by") == "ADR-022", "ADR registry lacks ADR-005 lineage")
check(adr_by_id.get("ADR-022", {}).get("status") == "accepted", "ADR-022 is absent from the registry")
check(adr_by_id.get("ADR-022", {}).get("supersedes") == "ADR-005", "ADR-022 registry lineage differs")

registry = load_yaml("governance/releases/index.yml")
check(registry["schema_version"] == "1.0.0", "Release registry schema differs")
check(registry["registry_id"] == "CDI-RELEASE-LINEAGE", "Release registry ID differs")
check(registry["governed_by"] == "ADR-022", "Release registry is not governed by ADR-022")
records = {item["version"]: item for item in registry["releases"]}
expected_versions = {
    "0.2.0",
    "0.3.0-rc.1",
    "0.4.0-rc.1",
    "0.4.0",
    "0.5.0-rc.1",
    "0.6.0-rc.1",
    "0.7.0-rc.1",
    "0.8.0-rc.1",
}
check(expected_versions == set(records), "Release registry versions are incomplete or unexpected")
for version in expected_versions:
    record = records.get(version, {})
    check(bool(record.get("reference_commit")), f"Release {version} lacks a reference commit")
    check((ROOT / record.get("manifest", "missing")).exists(), f"Release {version} manifest does not exist")

check(records["0.2.0"]["tag"] == "v0.2.0", "Governance milestone tag differs")
check(records["0.4.0"]["release_class"] == "stable-release", "v0.4.0 lost stable class")
check(records["0.4.0"]["status"] == "stable", "v0.4.0 lost stable status")
check(records["0.4.0"]["tag"] == "v0.4.0", "Stable v0.4.0 tag differs")
check(records["0.4.0"]["reference_commit"] == "6d4ae6282218918ff17f4d673a669add56397e86", "Stable tag commit differs")

candidate_versions = ["0.3.0-rc.1", "0.4.0-rc.1", "0.5.0-rc.1", "0.6.0-rc.1", "0.7.0-rc.1", "0.8.0-rc.1"]
for version in candidate_versions:
    check(records[version]["release_class"] == "release-candidate", f"{version} is not classified as a candidate")
    check(records[version]["tag"] is None, f"{version} invents a retrospective tag")
check(set(registry["tag_snapshot"]["candidates_intentionally_untagged"]) == set(candidate_versions), "Untagged candidate snapshot differs")

check(records["0.5.0-rc.1"]["status"] == "candidate-deployed-not-ratified", "Sprint 3 candidate state is overstated")
check(records["0.5.0-rc.1"]["reference_commit"] == "340efda43aec909237587a4c5747b664b107721e", "Sprint 3 implementation lineage differs")
check(records["0.5.0-rc.1"]["closure_commit"] == "a52033466a664000d385d5b7762fc062b5133380", "Sprint 3 closure lineage differs")
check(records["0.6.0-rc.1"]["status"] == "candidate-ratified-merged-deployed", "Sprint 4 closure differs")
check(records["0.7.0-rc.1"]["status"] == "candidate-ratified-merged-deployed", "Sprint 5 closure differs")
check(records["0.7.0-rc.1"]["reference_commit"] == "e84f53a6caaca696a8143a2aab2e7a24e9bdb4e8", "Sprint 5 merge lineage differs")
check(records["0.8.0-rc.1"]["status"] == "candidate-implemented-not-ratified", "Sprint 6 candidate state is overstated")
check(records["0.8.0-rc.1"]["reference_commit"] == "pending-pr-head" or len(records["0.8.0-rc.1"]["reference_commit"]) == 40, "Sprint 6 implementation reference is invalid")

sprint4 = load_yaml("governance/sprint-4-manifest.yml")
sprint5 = load_yaml("governance/sprint-5-manifest.yml")
sprint6 = load_yaml("governance/sprint-6-manifest.yml")
check(sprint4["status"] == "candidate-ratified-merged-deployed", "Sprint 4 manifest is not closed")
check(sprint4["publication"]["pages_deployment_run"].endswith("/29858379825"), "Sprint 4 Pages evidence differs")
check(sprint5["status"] == "candidate-ratified-merged-deployed", "Sprint 5 manifest is not closed")
check(sprint5["publication"]["merge_commit"] == records["0.7.0-rc.1"]["reference_commit"], "Sprint 5 registry and manifest diverge")
check(sprint5["publication"]["portal_verification"].startswith("passed-http-200"), "Sprint 5 portal verification is absent")
check(sprint6["status"] == "candidate-implemented-not-ratified", "Sprint 6 manifest overstates ratification")
check(sprint6["publication"]["status"] == records["0.8.0-rc.1"]["status"], "Sprint 6 registry and manifest diverge")

version_index = text("docs/versions/index.md")
release_note = text("docs/versions/v0.7.0-rc.1.md")
candidate_note = text("docs/versions/v0.8.0-rc.1.md")
changelog = text("CHANGELOG.md")
check("Ratificación, despliegue y estabilidad son estados diferentes" in version_index, "Public version policy conflates release states")
check("tags retrospectivos ambiguos" in version_index, "Public version policy lacks retrospective-tag caution")
check("candidato ratificado, fusionado y desplegado" in release_note, "v0.7.0-rc.1 public closure is absent")
check("No equivale a `v0.7.0` estable" in release_note, "v0.7.0 stable boundary is absent")
check("ADR-022 sustituye la regla ambigua de ADR-005" in changelog, "Changelog lacks version-governance decision")
check(not (ROOT / "governance/releases/v0.7.0.yml").exists(), "A stable v0.7.0 manifest was created prematurely")
check("Candidato implementado, no ratificado" in candidate_note, "v0.8.0-rc.1 candidate boundary is absent")
check(not (ROOT / "governance/releases/v0.8.0.yml").exists(), "A stable v0.8.0 manifest was created prematurely")
check('"version": "0.8.0-rc.1"' in text("package.json"), "Portal version differs from the active candidate")

content_map = load_yaml("governance/content-map.yml")
registry_paths = content_map["collections"]["registries"]["paths"]
check("governance/releases/index.yml" in registry_paths, "Release registry is absent from the content map")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} version-governance error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: release lineage and version governance validated ({CHECKS} checks)")
