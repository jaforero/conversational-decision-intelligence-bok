#!/usr/bin/env python3
"""Validate the bounded stable promotion contract for CDI-BoK v0.9.0."""

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

manifest = load_yaml("governance/releases/v0.9.0.yml")
registry = load_yaml("governance/releases/index.yml")
records = {item["version"]: item for item in registry["releases"]}
content_map = load_yaml("governance/content-map.yml")
translations = load_yaml("governance/registries/translations.yml")
adr_index = load_yaml("governance/adr/index.yml")
package = json.loads(text("package.json"))
candidate = records.get("0.9.0-rc.1", {})
stable = records.get("0.9.0", {})

check(package["version"] == "0.9.0", "Package does not declare stable 0.9.0")
check(manifest["release"] == "0.9.0", "Stable manifest release differs")
check(manifest["tag"] == "v0.9.0", "Stable tag differs")
check(manifest["status"] == "stable", "Stable manifest status differs")
check(manifest["reference"] == "refs/tags/v0.9.0", "Stable reference is not tag-resolvable")
check(manifest["source_candidate"] == "0.9.0-rc.1", "Source candidate differs")
check(manifest["source_candidate_commit"] == candidate.get("reference_commit"), "Candidate lineage diverges")
check(manifest["closure_commit"] == "a2965f352664bbfa05b94b91f358e261aaa2bc54", "Ratified closure lineage differs")
check(manifest["ratification"]["governed_by"] == "ADR-029", "Stable promotion is not governed by ADR-029")
check(manifest["notes_path"] == "governance/releases/v0.9.0-notes.md", "Stable notes path differs")
check(candidate.get("release_class") == "release-candidate", "Source candidate class differs")
check(candidate.get("status") == "candidate-ratified-merged-deployed-promoted", "Source candidate is not promoted")
check(candidate.get("tag") is None, "Source candidate invents a tag")
check(candidate.get("superseded_by") == "0.9.0", "Candidate promotion target differs")
check(stable.get("release_class") == "stable-release", "Registry lacks stable v0.9.0")
check(stable.get("status") == "stable", "Registry stable status differs")
check(stable.get("reference_commit") == "refs/tags/v0.9.0", "Registry stable reference differs")
check(stable.get("source_candidate") == "0.9.0-rc.1", "Registry source candidate differs")
check(stable.get("source_candidate_commit") == candidate.get("reference_commit"), "Registry candidate commit differs")
authorized = {item["tag"]: item for item in registry["tag_snapshot"]["authorized_for_post_merge_creation"]}
check(authorized.get("v0.9.0", {}).get("target") == "validated-main-sha", "v0.9.0 tag is not restricted to validated main")
check(authorized.get("v0.9.0", {}).get("governed_by") == "ADR-029", "v0.9.0 tag authorization differs")
check(content_map["release"] == "0.9.0", "Content map release differs")
check(content_map["public_portal"]["release"] == "0.9.0", "Public portal release differs")
navigation = {item["path"]: item for item in content_map["public_portal"]["navigation"]}
check(navigation.get("docs/versions/v0.9.0.md", {}).get("status") == "approved", "Stable v0.9.0 note is not approved")
check((ROOT / "docs/versions/v0.9.0.en.md").exists(), "Stable English note is absent")
check(translations["release"] == "0.9.0", "Translation registry release differs")
check("TR-VERSIONS-V0-9-0" in {item["id"] for item in translations["pairs"]}, "Stable translation pair is absent")
decisions = {item["id"]: item for item in adr_index["decisions"]}
check(decisions.get("ADR-029", {}).get("status") == "accepted", "ADR-029 is absent or not accepted")
check("portal: v0.9.0" in text("mkdocs.yml"), "MkDocs portal release differs")
check("Portal estable v0.9.0" in text("overrides/main.html"), "Spanish stable banner is absent")
check("Stable portal v0.9.0" in text("overrides/main.html"), "English stable banner is absent")
check("CDI-BoK · v0.9.0" in text("overrides/main.html"), "Stable footer is absent")
check("Portal estable v0.9.0" in text("docs/index.md"), "Spanish home stable marker is absent")
check("Stable portal v0.9.0" in text("docs/index.en.md"), "English home stable marker is absent")
limitations = " ".join(manifest["limitations"]).lower()
for marker in ["provisional", "does not scientifically validate cdi or pulse", "source-quality", "instrumented and not executed", "wcag 2.2 aa"]:
    check(marker in limitations, f"Stable limitation missing: {marker}")
stable_note = text("docs/versions/v0.9.0.md")
for marker in ["sigue siendo provisional", "no queda científicamente validado", "no demuestra eficacia", "no establecen conformidad completa WCAG 2.2 AA"]:
    check(marker in stable_note, f"Public stable boundary missing: {marker}")
if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"FAILED: {len(ERRORS)} v0.9.0 promotion error(s) across {CHECKS} checks", file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: v0.9.0 stable promotion validated ({CHECKS} checks)")
