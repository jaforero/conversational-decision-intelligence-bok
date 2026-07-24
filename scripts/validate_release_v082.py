#!/usr/bin/env python3
"""Validate the bounded stable patch contract for CDI-BoK v0.8.2."""

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


manifest = load_yaml("governance/releases/v0.8.2.yml")
registry = load_yaml("governance/releases/index.yml")
records = {item["version"]: item for item in registry["releases"]}
content_map = load_yaml("governance/content-map.yml")
adr_index = load_yaml("governance/adr/index.yml")
package = json.loads(text("package.json"))

check(package["version"] in {"0.8.2", "0.9.0-rc.1", "0.9.0"}, "Package is older than stable 0.8.2")
check(manifest["release"] == "0.8.2", "Stable patch manifest release differs")
check(manifest["tag"] == "v0.8.2", "Stable patch tag differs")
check(manifest["status"] == "stable", "Stable patch status differs")
check(manifest["reference"] == "refs/tags/v0.8.2", "Stable patch reference is not tag-resolvable")
check(manifest["source_release"] == "0.8.1", "Stable patch source release differs")
check(manifest["localization_fix_commit"] == "1f81e2ad26b42da4959744733ad8261dfd188f81", "PR #15 merge lineage differs")
check(manifest["ratification"]["governed_by"] == "ADR-027", "Stable patch is not governed by ADR-027")
check(manifest["notes_path"] == "governance/releases/v0.8.2-notes.md", "Stable patch notes path differs")

stable = records.get("0.8.2", {})
check(stable.get("release_class") == "stable-release", "Registry lacks stable v0.8.2")
check(stable.get("reference_commit") == "refs/tags/v0.8.2", "Registry v0.8.2 reference differs")
check(stable.get("source_release") == "0.8.1", "Registry v0.8.2 source differs")
check(stable.get("localization_fix_commit") == manifest["localization_fix_commit"], "Manifest and registry fix commits diverge")

authorized = {item["tag"]: item for item in registry["tag_snapshot"]["authorized_for_post_merge_creation"]}
check(authorized.get("v0.8.2", {}).get("target") == "validated-main-sha", "v0.8.2 tag is not restricted to validated main")
check(authorized.get("v0.8.2", {}).get("governed_by") == "ADR-027", "v0.8.2 tag authorization differs")

check(content_map["release"] in {"0.8.2", "0.9.0-rc.1", "0.9.0"}, "Content map is older than v0.8.2")
check(content_map["public_portal"]["release"] in {"0.8.2", "0.9.0-rc.1", "0.9.0"}, "Public portal is older than v0.8.2")
navigation = {item["path"]: item for item in content_map["public_portal"]["navigation"]}
check(navigation.get("docs/versions/v0.8.2.md", {}).get("status") == "approved", "Stable v0.8.2 note is not approved")
check((ROOT / "docs/versions/v0.8.2.en.md").exists(), "Stable v0.8.2 English note is absent")

decisions = {item["id"]: item for item in adr_index["decisions"]}
check(decisions.get("ADR-027", {}).get("status") == "accepted", "ADR-027 is absent or not accepted")
check("CDI-BoK · v0.9.0" in text("overrides/main.html"), "Active stable footer is absent")
check("portal: v0.9.0" in text("mkdocs.yml"), "MkDocs portal release differs")
check("Release v0.8.2" in text("docs/versions/v0.8.2.en.md"), "English historical release is absent")
check("Release v0.8.2" in text("docs/versions/v0.8.2.md"), "Spanish historical release is absent")
check("línea base estable" in text("docs/versions/v0.8.2.md"), "Historical v0.8.2 stable boundary is absent")
check("Buscar en español" in text("docs/assets/javascripts/site.js"), "Spanish search label is absent")
check("/en/search/search_index.json" in text("overrides/main.html"), "English search routing is absent")

for limitation in ["do not validate CDI", "not guarantee perfect ranking", "instrumented and not executed", "WCAG 2.2 AA"]:
    check(limitation.lower() in " ".join(manifest["limitations"]).lower(), f"Stable limitation missing: {limitation}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"FAILED: {len(ERRORS)} v0.8.2 promotion error(s) across {CHECKS} checks", file=sys.stderr)
    raise SystemExit(1)

print(f"PASS: v0.8.2 stable patch validated ({CHECKS} checks)")
