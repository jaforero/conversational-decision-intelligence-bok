#!/usr/bin/env python3
"""Fail-fast integrity checks for the CDI-BoK Sprint 0 contract."""

from __future__ import annotations

import hashlib
import json
import subprocess
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


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


required_paths = [
    "README.md",
    "CHANGELOG.md",
    "governance/00_CDI-BoK_Architecture_and_Editorial_Governance.md",
    "governance/content-map.yml",
    "governance/sprint-0-manifest.yml",
    "governance/registries/concepts.yml",
    "governance/registries/claims.yml",
    "governance/registries/sources.yml",
    "governance/registries/brand-assets.yml",
    "governance/registries/external-demos.yml",
    "governance/adr/index.yml",
    "brand/brand-source.yml",
    "brand/tokens.json",
    "brand/tokens.css",
    "brand/asset-manifest.yml",
    "sources/constitutional/00_PULSE_DNA.md",
    "sources/constitutional/00A_PULSE_Documentation_Map.md",
    "sources/constitutional/00_PULSE_Identity.md",
]
for path in required_paths:
    check((ROOT / path).exists(), f"Missing required path: {path}")

governance_text = (ROOT / required_paths[2]).read_text(encoding="utf-8")
frontmatter = yaml.safe_load(governance_text.split("---", 2)[1])
check(frontmatter["id"] == "CDI-GOV-001", "Wrong root governance id")
check(frontmatter["version"] == "0.2.0", "Root governance is not v0.2.0")
check(frontmatter["status"] == "approved", "Root governance is not approved")
check(frontmatter["normative"] is True, "Root governance is not normative")
check(frontmatter["approved_by"] == "Javier Forero", "Ratifier is not recorded")

concept_registry = load_yaml("governance/registries/concepts.yml")
areas = concept_registry["knowledge_areas"]
domains = concept_registry["domains"]
check(len(areas) == 8 and len(set(areas)) == 8, "Expected 8 unique knowledge areas")
check(len(domains) == 29 and len(set(domains)) == 29, "Expected 29 unique domains")
concept_ids = [item["concept_id"] for item in concept_registry["concepts"]]
check(len(concept_ids) == len(set(concept_ids)), "Duplicate concept_id")

claims = load_yaml("governance/registries/claims.yml")["claims"]
claim_ids = [item["claim_id"] for item in claims]
check(len(claim_ids) == len(set(claim_ids)), "Duplicate claim_id")
for claim in claims:
    check(bool(claim.get("claim_class")), f"Missing claim_class: {claim['claim_id']}")
    check(bool(claim.get("evidence_status")), f"Missing evidence_status: {claim['claim_id']}")

sources = load_yaml("governance/registries/sources.yml")["records"]
source_ids = [item["source_id"] for item in sources]
check(len(source_ids) == len(set(source_ids)), "Duplicate source_id")
active_materialized = [item for item in sources if item.get("canonical_repo_path")]
for source in active_materialized:
    path = source["canonical_repo_path"]
    check((ROOT / path).exists(), f"Missing materialized source: {source['source_id']}")
    check(sha256(path) == source["sha256"], f"Checksum mismatch: {source['source_id']}")
identity = next(item for item in sources if item["source_id"] == "SRC-PULSE-IDENTITY-002")
check(identity["declared_version"] == "2.0.0", "PULSE Identity v2.0.0 is not canonical")
check(identity["supersedes"] == "SRC-PULSE-IDENTITY-001", "Identity supersession is missing")

adr_index = load_yaml("governance/adr/index.yml")["decisions"]
check(len(adr_index) >= 11, "Expected at least ADR-001 through ADR-011")
check({f"ADR-{n:03d}" for n in range(1, 12)}.issubset({item["id"] for item in adr_index}), "Sprint 0 ADR range is incomplete")
for decision in adr_index:
    check(decision["status"] == "accepted", f"ADR not accepted: {decision['id']}")
    adr_path = ROOT / "governance" / "adr" / decision["file"]
    check(adr_path.exists(), f"ADR file missing: {decision['file']}")
    if adr_path.exists():
        adr_frontmatter = yaml.safe_load(adr_path.read_text(encoding="utf-8").split("---", 2)[1])
        check(adr_frontmatter["id"] == decision["id"], f"ADR id mismatch: {decision['file']}")
        check(adr_frontmatter["status"] == "accepted", f"ADR front matter not accepted: {decision['id']}")

brand_source = load_yaml("brand/brand-source.yml")
check(brand_source["snapshot"]["source_id"] == "SRC-BRAND-001", "Brand source id mismatch")
check(brand_source["snapshot"]["library_file_id"] == "libfile_380da03d59c8819197a664d746860db7", "Brand provenance mismatch")

with (ROOT / "brand/tokens.json").open(encoding="utf-8") as stream:
    tokens = json.load(stream)
expected_colors = {
    "purple": "#4e00ff",
    "purpleLight": "#7c4dff",
    "deepBlue": "#041c59",
    "vibrantBlue": "#0048ff",
    "background": "#f5f7fb",
    "white": "#ffffff",
    "border": "#e3e8f5",
    "softLilac": "#f6f3ff",
    "text": "#1f2937",
    "muted": "#5f6b7a",
}
for key, value in expected_colors.items():
    check(tokens["color"][key]["value"] == value, f"Wrong brand color: {key}")
check(tokens["typography"]["familyWeb"]["value"] == "'IgraSans', Aptos, Helvetica, Arial, sans-serif", "Wrong font stack")
check(tokens["modes"]["dark"]["status"] in {"pending-derived-token-contrast-audit", "implemented-pending-release-audit"}, "Dark token status is invalid")

assets = load_yaml("brand/asset-manifest.yml")["assets"]
asset_ids = [item["asset_id"] for item in assets]
check(len(asset_ids) == len(set(asset_ids)), "Duplicate asset_id")
for asset in assets:
    check("license_status" in asset, f"Missing license_status: {asset['asset_id']}")
font = next(item for item in assets if item["asset_id"] == "FONT-IGRASANS-WOFF2")
check(font["repository_distribution"] == "prohibited-until-license-evidence", "Font redistribution gate is absent")
repository_files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
).decode().split("\0")
font_binaries = [
    ROOT / name
    for name in repository_files
    if name and (ROOT / name).suffix.lower() in {".woff", ".woff2", ".ttf", ".otf"}
]
check(not font_binaries, "Font binary exists before license verification")

demo_registry = load_yaml("governance/registries/external-demos.yml")
demo = demo_registry.get("root") or demo_registry["demos"][0]
check(demo["url"] == "https://dashboards.javierforero.co", "Practice Lab URL mismatch")
check(demo["content_authority"] == "practice-evidence-only", "Practice Lab authority is too broad")

sprint = load_yaml("governance/sprint-0-manifest.yml")
check(sprint["release"] == "0.2.0", "Sprint manifest release mismatch")
check(sprint["gates"]["governance_ratified"] == "passed", "Ratification gate is not passed")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} error(s) across {CHECKS} checks", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: Sprint 0 integrity validated ({CHECKS} checks)")
