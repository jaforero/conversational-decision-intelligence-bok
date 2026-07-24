#!/usr/bin/env python3
"""Validate Sprint 7 evidence governance and the bilingual research candidate."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RELEASE = "0.9.0-rc.1"
ERRORS: list[str] = []
CHECKS = 0

ADDITIONAL_SOURCE_IDS = {
    "SRC-JF-001",
    "SRC-JF-002",
    "SRC-JF-003",
    "SRC-JF-004",
    "SRC-JF-005",
    "SRC-JF-006",
    "SRC-DR-001",
    "SRC-DR-002",
    "SRC-ARCH-001",
    "SRC-GARTNER-VALUE-001",
    "SRC-GARTNER-PREDICTIONS-001",
    "SRC-PRACTICE-B2B-001",
}
INCOMPLETE_IDS = {"SRC-JF-001", "SRC-JF-003"}
AI_SYNTHESIS_IDS = {"SRC-DR-001", "SRC-DR-002"}
FORECAST_IDS = {"SRC-GARTNER-PREDICTIONS-001"}
DIMENSIONS = {
    "authority",
    "independence",
    "method",
    "directness",
    "currency",
    "applicability",
    "conflicts_of_interest",
    "verification",
}
MATERIAL_CLAIMS = {
    "CLAIM-DI-MATURITY-001",
    "CLAIM-DI-LAYERS-001",
    "CLAIM-PULSE-SYNTHESIS-001",
    "CLAIM-PULSE-BIOLOGICAL-LENSES-001",
    "CLAIM-DMN-VERSION-001",
    "CLAIM-NIST-REVISION-001",
    "CLAIM-HUMAN-AI-EVIDENCE-001",
    "CLAIM-FUTURE-SIGNALS-001",
}
RESEARCH_PAGES = [
    "docs/research/index.md",
    "docs/research/decision-intelligence-state-of-the-art.md",
    "docs/research/pulse-evidence-map.md",
    "docs/research/future-signals.md",
    "docs/research/research-agenda.md",
    "docs/versions/v0.9.0-rc.1.md",
]


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def load_yaml(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def frontmatter(relative: str) -> dict:
    raw = text(relative)
    match = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    return yaml.safe_load(match.group(1)) if match else {}


manifest = load_yaml("governance/sprint-7-manifest.yml")
profiles_registry = load_yaml("governance/registries/evidence-profiles.yml")
sources_registry = load_yaml("governance/registries/sources.yml")
claims_registry = load_yaml("governance/registries/claims.yml")
translations = load_yaml("governance/registries/translations.yml")
content_map = load_yaml("governance/content-map.yml")
release_registry = load_yaml("governance/releases/index.yml")

check(manifest["release"] == RELEASE, "Sprint 7 manifest release differs")
check(manifest["status"] == "implementation-authorized", "Sprint 7 overstates its pre-review status")
check(manifest["decisions"] == ["ADR-028"], "Sprint 7 is not governed only by ADR-028")
check("Scientific validation" in " ".join(manifest["out_of_scope"]), "Scientific validation is not explicitly out of scope")
check("Redistribution" in " ".join(manifest["out_of_scope"]), "Analyst-report redistribution is not explicitly out of scope")
check(RELEASE in text("package.json"), "Package does not declare the active release candidate")
check(content_map["release"] == RELEASE, "Content map release differs")
check(content_map["public_portal"]["release"] == RELEASE, "Public portal release differs")
check(translations["release"] == RELEASE, "Translation registry release differs")
check("Candidato de evidencia v0.9.0-rc.1" in text("overrides/main.html"), "Spanish candidate banner is absent")
check("Evidence candidate v0.9.0-rc.1" in text("overrides/main.html"), "English candidate banner is absent")

source_records = {item["source_id"]: item for item in sources_registry["records"]}
profiles = {item["source_id"]: item for item in profiles_registry["profiles"]}
claims = {item["claim_id"]: item for item in claims_registry["claims"]}
release_records = {item["version"]: item for item in release_registry["releases"]}

check(set(profiles) == ADDITIONAL_SOURCE_IDS, "Evidence profile inventory is not exactly the 12 authorized sources")
check(ADDITIONAL_SOURCE_IDS <= set(source_records), "One or more audited sources are absent from the source registry")
check(MATERIAL_CLAIMS <= set(claims), "One or more Sprint 7 material claims are absent")
candidate = release_records.get(RELEASE, {})
check(candidate.get("release_class") == "release-candidate", "Sprint 7 is not registered as a release candidate")
check(candidate.get("tag") is None, "Sprint 7 invents a candidate tag")
check(candidate.get("reference_commit") == "pending-merge", "Sprint 7 pre-merge lineage differs")

for source_id, profile in profiles.items():
    check(bool(re.fullmatch(r"[0-9a-f]{64}", profile.get("sha256", ""))), f"Invalid source hash: {source_id}")
    check(profile["sha256"] == source_records[source_id].get("sha256"), f"Profile/source hash mismatch: {source_id}")
    check(set(profile.get("profile", {})) == DIMENSIONS, f"Evidence dimensions differ: {source_id}")
    check(bool(profile.get("provenance")), f"Provenance missing: {source_id}")
    check(bool(profile.get("completeness")), f"Completeness missing: {source_id}")
    check(bool(profile.get("rights")), f"Rights record missing: {source_id}")
    check(bool(profile.get("allowed_use")), f"Allowed use missing: {source_id}")
    check(bool(profile.get("prohibited_use")), f"Prohibited use missing: {source_id}")
    check(
        not any(key in profile for key in {"score", "total_score", "weighted_score", "rank"}),
        f"Aggregate evidence score is prohibited: {source_id}",
    )

for source_id in INCOMPLETE_IDS:
    profile = profiles[source_id]
    check(profile["completeness"].startswith("incomplete"), f"Incomplete source status lost: {source_id}")
    check(profile["prohibited_use"] == "claim-support", f"Incomplete source can support claims: {source_id}")
for source_id in AI_SYNTHESIS_IDS:
    profile = profiles[source_id]
    check(profile["source_class"] == "ai-assisted-research-map", f"AI synthesis class differs: {source_id}")
    check(profile["prohibited_use"] == "direct-or-sole-claim-support", f"AI synthesis claim block differs: {source_id}")
for source_id in FORECAST_IDS:
    profile = profiles[source_id]
    check(profile["source_class"] == "analyst-forecast", f"Forecast source class differs: {source_id}")
    for forbidden in ["fact", "causal", "readiness"]:
        check(forbidden in profile["prohibited_use"], f"Forecast block lacks {forbidden}: {source_id}")

for claim_id, claim in claims.items():
    claim_sources = set(claim.get("source_ids", []))
    check(claim_sources <= set(source_records), f"Unknown source in claim: {claim_id}")
    check(not claim_sources & INCOMPLETE_IDS, f"Incomplete source supports claim: {claim_id}")
    check(not claim_sources & AI_SYNTHESIS_IDS, f"AI-assisted map directly supports claim: {claim_id}")
    if claim_sources & FORECAST_IDS:
        check(claim["claim_class"] == "forecast-governance-rule", f"Forecast source supports non-forecast claim: {claim_id}")

for claim_id in MATERIAL_CLAIMS:
    claim = claims[claim_id]
    check(claim.get("governed_by") == "ADR-028", f"Sprint 7 claim lacks ADR-028: {claim_id}")
    for field in ["claim_class", "evidence_status", "maturity", "scope", "limits", "counterevidence", "review_status"]:
        check(bool(claim.get(field)), f"Sprint 7 claim lacks {field}: {claim_id}")
    check(bool(claim.get("source_ids")), f"Sprint 7 claim lacks sources: {claim_id}")

for path in sorted((ROOT / "docs").rglob("*.md")):
    relative = path.relative_to(ROOT).as_posix()
    metadata = frontmatter(relative)
    check(
        set(metadata.get("source_ids", [])) <= set(source_records),
        f"Page references an unknown source ID: {relative}",
    )
    check(
        set(metadata.get("claim_ids", [])) <= set(claims),
        f"Page references an unknown claim ID: {relative}",
    )

for filename in [
    "turn-data-analytics-and-ai-into-strategic-growth-drivers.pdf",
    "over-100-data-analytics-ia-predictions-through-2031.pdf",
]:
    check(not any(ROOT.rglob(filename)), f"Rights-reserved PDF was redistributed: {filename}")

translation_by_source = {item["source"]: item for item in translations["pairs"]}
for spanish in RESEARCH_PAGES:
    english = spanish.removesuffix(".md") + ".en.md"
    check((ROOT / spanish).exists(), f"Spanish research page missing: {spanish}")
    check((ROOT / english).exists(), f"English research page missing: {english}")
    if not (ROOT / spanish).exists() or not (ROOT / english).exists():
        continue
    es_meta = frontmatter(spanish)
    en_meta = frontmatter(english)
    check(es_meta.get("version") == en_meta.get("version") == RELEASE, f"Research page version parity failed: {spanish}")
    check(es_meta.get("claim_ids") == en_meta.get("claim_ids"), f"Claim ID parity failed: {spanish}")
    check(es_meta.get("source_ids") == en_meta.get("source_ids"), f"Source ID parity failed: {spanish}")
    entry = translation_by_source.get(spanish, {})
    check(entry.get("translation") == english, f"Translation pair missing: {spanish}")
    check(
        entry.get("source_sha256") == hashlib.sha256((ROOT / spanish).read_bytes()).hexdigest(),
        f"Research translation hash is stale: {spanish}",
    )

state_of_art = " ".join(text("docs/research/decision-intelligence-state-of-the-art.md").split())
for marker in [
    "campo de práctica integrador y emergente",
    "no revisión sistemática",
    "¿Qué no está validado?",
    "¿Qué evidencia cambiaría esta conclusión?",
]:
    check(marker.lower() in state_of_art.lower(), f"State-of-the-art boundary missing: {marker}")

future_signals = text("docs/research/future-signals.md")
for marker in ["no como hechos", "Horizonte", "Incertidumbre", "Stop condition"]:
    check(marker.lower() in future_signals.lower(), f"Future-signal boundary missing: {marker}")

check("DMN 1.5" in future_signals and "DMN 1.7 Beta 1" in future_signals, "DMN formal/beta distinction is absent")
check("está en revisión" in future_signals, "NIST AI RMF revision status is absent")
check("no se redistribuyen" in future_signals, "Analyst PDF redistribution boundary is absent")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"FAILED: {len(ERRORS)} Sprint 7 error(s) across {CHECKS} checks", file=sys.stderr)
    raise SystemExit(1)

print(f"PASS: Sprint 7 evidence backbone validated ({CHECKS} checks)")
