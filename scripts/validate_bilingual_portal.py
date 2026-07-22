#!/usr/bin/env python3
"""Validate the complete ES/EN portal and translation-maintenance contract."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = ROOT / "governance/registries/translations.yml"
ERRORS: list[str] = []
CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def markdown(path: Path) -> tuple[dict, str]:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not match:
        return {}, raw
    return yaml.safe_load(match.group(1)) or {}, match.group(2)


registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
check(registry["schema_version"] == "1.0.0", "Translation registry schema differs")
check(registry["canonical_language"] == "es", "Spanish is not canonical")
check(registry["translation_language"] == "en", "English translation language differs")
check(registry["release"] == "0.8.1", "Translation registry release differs")
check(registry["policy"]["fallback_to_default"] is False, "Fallback must be disabled")

spanish = sorted(p for p in DOCS.rglob("*.md") if not p.name.endswith(".en.md"))
english = sorted(DOCS.rglob("*.en.md"))
pairs = registry["pairs"]
by_source = {item["source"]: item for item in pairs}

check(len(spanish) == len(english) == len(pairs), "ES/EN page inventory is not one-to-one")
check(len(by_source) == len(pairs), "Duplicate canonical paths in translation registry")

for source_path in spanish:
    relative = source_path.relative_to(ROOT).as_posix()
    translated_path = source_path.with_name(f"{source_path.stem}.en.md")
    translated_relative = translated_path.relative_to(ROOT).as_posix()
    entry = by_source.get(relative, {})
    check(bool(entry), f"Unregistered Spanish page: {relative}")
    check(translated_path.exists(), f"Missing English page: {translated_relative}")
    if not entry or not translated_path.exists():
        continue

    source_meta, source_body = markdown(source_path)
    translated_meta, translated_body = markdown(translated_path)
    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()

    check(entry["translation"] == translated_relative, f"Wrong pair path: {relative}")
    check(entry["status"] == "complete", f"Translation is not complete: {relative}")
    check(entry["version"] == source_meta.get("version"), f"Registry/source version mismatch: {relative}")
    check(entry["source_sha256"] == digest, f"Stale English translation after Spanish change: {relative}")
    check(entry["owner"] == source_meta.get("owner"), f"Translation owner mismatch: {relative}")
    check(bool(entry.get("last_reviewed")), f"Missing translation review date: {relative}")

    for field in ["status", "version", "artifact_type", "authority_level", "normative", "owner"]:
        check(source_meta.get(field) == translated_meta.get(field), f"Frontmatter parity failed for {field}: {relative}")

    check(bool(translated_meta.get("title")) and bool(translated_meta.get("description")), f"English metadata incomplete: {translated_relative}")
    check(len(translated_body.split()) >= 35, f"English page is implausibly short: {translated_relative}")
    check("translation pending" not in translated_body.lower(), f"Pending marker published: {translated_relative}")
    check("lorem ipsum" not in translated_body.lower(), f"Placeholder published: {translated_relative}")

config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
override = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
requirements = (ROOT / "requirements.in").read_text(encoding="utf-8")
for marker in [
    "mkdocs-static-i18n==1.3.0",
    "fallback_to_default: false",
    "reconfigure_search: false",
    "scripts/localize_portal.py",
    "locale: es",
    "locale: en",
    "name: Español",
    "name: English",
    "site_name: CDI-BoK · Inteligencia de Decisiones Conversacional",
    "site_name: CDI-BoK · Conversational Decision Intelligence",
]:
    check(marker in requirements + config, f"Bilingual configuration marker missing: {marker}")
for marker in ['hreflang="x-default"', "og:locale", "i18n_page_locale"]:
    check(marker in override, f"Localized metadata marker missing: {marker}")
check(
    "i18n_current_language" not in override,
    "Page template uses the template-only locale variable instead of i18n_page_locale",
)

for spanish_label, english_label in {
    "1. Enfocar la decisión": "1. Frame the decision",
    "2. Evidencia y contexto": "2. Evidence and context",
    "4. Control humano–IA": "4. Human–AI control",
    "5. Acción y aprendizaje": "5. Action and learning",
    "Caso B2B · Propuesta": "B2B case · Proposal",
    "Calidad de la decisión": "Decision Quality",
    "Sistema de medición de decisiones": "Decision Measurement System",
    "Registro de medición de decisiones": "Decision Measurement Record",
}.items():
    check(
        f"{spanish_label}: {english_label}" in config,
        f"Exact English navigation translation missing: {spanish_label}",
    )
for marker in ["Switch to dark mode", "Switch to light mode"]:
    check(marker in config, f"English theme control label missing: {marker}")

hook = (ROOT / "scripts/localize_portal.py").read_text(encoding="utf-8")
site_script = (ROOT / "docs/assets/javascripts/site.js").read_text(encoding="utf-8")
template = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
for marker in ["Enlace permanente", "search_index.json", 'startswith("en/")']:
    check(marker in hook, f"Localized portal hook marker missing: {marker}")
for marker in ["Buscar en español", "Search in English"]:
    check(marker in site_script, f"Language-specific search label missing: {marker}")
for marker in ["XMLHttpRequest.prototype.open", "localizeSearchIndex", "/en/search/search_index.json"]:
    check(marker in template, f"English search request routing marker missing: {marker}")

if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"FAILED: {len(ERRORS)} bilingual error(s) across {CHECKS} checks", file=sys.stderr)
    raise SystemExit(1)

print(f"PASS: bilingual ES/EN portal validated ({CHECKS} checks, {len(pairs)} pairs)")
