#!/usr/bin/env python3
"""Validate the bounded stable promotion contract for CDI-BoK v0.8.1."""

from __future__ import annotations

import json
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
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


manifest = load_yaml("governance/releases/v0.8.1.yml")
registry = load_yaml("governance/releases/index.yml")
records = {item["version"]: item for item in registry["releases"]}
candidate = load_yaml("governance/sprint-6-1-manifest.yml")
content_map = load_yaml("governance/content-map.yml")
adr_index = load_yaml("governance/adr/index.yml")
package = json.loads(text("package.json"))

check(package["version"] in {"0.8.1", "0.8.2", "0.9.0-rc.1"}, "Package is older than stable 0.8.1")
check(manifest["release"] == "0.8.1", "Stable manifest release differs")
check(manifest["tag"] == "v0.8.1", "Stable tag differs")
check(manifest["status"] == "stable", "Stable manifest status differs")
check(manifest["reference"] == "refs/tags/v0.8.1", "Stable reference is not tag-resolvable")
check(manifest["source_candidate"] == "0.8.1-rc.1", "Source candidate differs")
check(manifest["source_candidate_commit"] == "655e3b80ad1cbd8b443b6339358996f9fe656083", "PR #12 merge lineage differs")
check(manifest["interface_hotfix_commit"] == "5837657f6bfe0627f5bd0c8ada13640dba9a0a4b", "PR #13 merge lineage differs")
check(manifest["ratification"]["governed_by"] == "ADR-026", "Stable ratification is not governed by ADR-026")
check(manifest["notes_path"] == "governance/releases/v0.8.1-notes.md", "Stable notes path differs")

stable = records.get("0.8.1", {})
source = records.get("0.8.1-rc.1", {})
check(stable.get("release_class") == "stable-release", "Registry lacks stable v0.8.1")
check(stable.get("reference_commit") == "refs/tags/v0.8.1", "Registry stable reference differs")
check(source.get("status") == "candidate-ratified-merged-deployed-promoted", "Source candidate is not closed")
check(source.get("superseded_by") == "0.8.1", "Source candidate promotion differs")
check(source.get("reference_commit") == manifest["source_candidate_commit"], "Manifest and registry candidate commits diverge")
check(source.get("interface_hotfix_commit") == manifest["interface_hotfix_commit"], "Manifest and registry hotfix commits diverge")

authorized = {item["tag"]: item for item in registry["tag_snapshot"]["authorized_for_post_merge_creation"]}
check(authorized.get("v0.8.1", {}).get("target") == "validated-main-sha", "v0.8.1 tag is not restricted to validated main")
check(authorized.get("v0.8.1", {}).get("governed_by") == "ADR-026", "v0.8.1 tag authorization differs")

check(candidate["status"] == "candidate-ratified-merged-deployed-promoted", "Sprint 6.1 manifest is not closed")
check(candidate["publication"]["promoted_to"] == "0.8.1", "Sprint 6.1 promotion target differs")
check(candidate["publication"]["portal_verification"].startswith("passed-http-200"), "Public English verification is absent")

check(content_map["release"] in {"0.8.1", "0.8.2", "0.9.0-rc.1"}, "Content map is older than v0.8.1")
check(content_map["public_portal"]["release"] in {"0.8.1", "0.8.2", "0.9.0-rc.1"}, "Public portal is older than v0.8.1")
navigation = {item["path"]: item for item in content_map["public_portal"]["navigation"]}
check(navigation.get("docs/versions/v0.8.1.md", {}).get("status") == "approved", "Stable ES note is not approved in navigation")
check((ROOT / "docs/versions/v0.8.1.en.md").exists(), "Stable English note is absent")

decisions = {item["id"]: item for item in adr_index["decisions"]}
check(decisions.get("ADR-026", {}).get("status") == "accepted", "ADR-026 is absent or not accepted")
check("portal: v0.9.0-rc.1" in text("mkdocs.yml"), "MkDocs active portal marker is absent")
check("portal bilingüe ES/EN como línea base editorial y técnica estable" in text("docs/versions/v0.8.1.md"), "Historical v0.8.1 stable boundary is absent")

for limitation in ["scientifically validated", "instrumented and not executed", "WCAG 2.2 AA"]:
    check(limitation.lower() in " ".join(manifest["limitations"]).lower(), f"Stable limitation missing: {limitation}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"FAILED: {len(ERRORS)} v0.8.1 promotion error(s) across {CHECKS} checks", file=sys.stderr)
    raise SystemExit(1)

print(f"PASS: v0.8.1 stable promotion validated ({CHECKS} checks)")
