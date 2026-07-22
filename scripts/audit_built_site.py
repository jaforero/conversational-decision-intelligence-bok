#!/usr/bin/env python3
"""Run static semantic checks against the generated MkDocs HTML."""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ERRORS: list[str] = []


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_lang = ""
        self.title = 0
        self.h1 = 0
        self.main = 0
        self.skip = 0
        self.images_without_alt = 0
        self.insecure_references = 0
        self.open_lists = 0
        self.orphan_list_items = 0
        self.canonical = 0
        self.alternate_languages: set[str] = set()
        self.language_switch_links: set[str] = set()
        self.labels: list[str] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for attribute in ("aria-label", "title"):
            if values.get(attribute):
                self.labels.append(values[attribute])
        if tag == "html":
            self.html_lang = values.get("lang", "")
        elif tag == "title":
            self.title += 1
        elif tag == "h1":
            self.h1 += 1
        elif tag == "main":
            self.main += 1
        elif tag == "a" and "md-skip" in values.get("class", "").split():
            self.skip += 1
        elif tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical += 1
        elif tag == "link" and values.get("rel") == "alternate":
            hreflang = values.get("hreflang", "")
            if hreflang:
                self.alternate_languages.add(hreflang)
        if tag == "a" and "md-select__link" in values.get("class", "").split():
            hreflang = values.get("hreflang", "")
            if hreflang:
                self.language_switch_links.add(hreflang)
        if tag in {"ol", "ul"}:
            self.open_lists += 1
        elif tag == "li" and self.open_lists == 0:
            self.orphan_list_items += 1
        for attribute in ("href", "src", "action"):
            if values.get(attribute, "").startswith("http://"):
                self.insecure_references += 1

    def handle_endtag(self, tag):
        if tag in {"ol", "ul"} and self.open_lists:
            self.open_lists -= 1


html_files = sorted(SITE.rglob("*.html"))
if not html_files:
    ERRORS.append("No generated HTML files found")
for path in html_files:
    parser = PageAudit()
    text = path.read_text(encoding="utf-8")
    parser.feed(text)
    relative = path.relative_to(ROOT)
    is_error_page = path == SITE / "404.html"
    expected_language = "en" if path.is_relative_to(SITE / "en") else "es"
    if not is_error_page and not parser.html_lang.startswith(expected_language):
        ERRORS.append(f"Expected lang={expected_language}: {relative}")
    if parser.title != 1:
        ERRORS.append(f"Expected one title element: {relative}")
    if parser.h1 != 1:
        ERRORS.append(f"Expected one H1 in generated page: {relative}")
    if parser.main != 1:
        ERRORS.append(f"Expected one main landmark: {relative}")
    if parser.skip < 1:
        ERRORS.append(f"Missing skip link: {relative}")
    if parser.images_without_alt:
        ERRORS.append(f"Image without alt attribute: {relative}")
    if parser.insecure_references:
        ERRORS.append(f"Insecure HTTP reference: {relative}")
    if parser.orphan_list_items:
        ERRORS.append(f"List item outside ol/ul: {relative}")
    if not is_error_page and parser.canonical != 1:
        ERRORS.append(f"Expected one canonical link: {relative}")
    if not is_error_page and parser.alternate_languages != {"es", "en", "x-default"}:
        ERRORS.append(f"Incomplete hreflang set: {relative}")
    if not is_error_page and parser.language_switch_links != {"es", "en"}:
        ERRORS.append(f"Incomplete contextual language selector: {relative}")
    if expected_language == "en" and not is_error_page:
        forbidden_ui_fragments = {
            "1. Enfocar la decisión",
            "2. Evidencia y contexto",
            "4. Control humano–IA",
            "5. Acción y aprendizaje",
            "Cambiar a tema oscuro",
            "Cambiar a tema claro",
            "En esta página",
            "Portal bilingüe estable v0.8.1",
            "El español sigue siendo canónico",
            "Identidad y estado editorial",
            "Fuente y versiones",
            "Caso B2B · Propuesta",
        }
        normalized = " ".join(text.split())
        leaked = sorted(fragment for fragment in forbidden_ui_fragments if fragment in normalized)
        leaked.extend(
            label
            for label in parser.labels
            if label.startswith("Cambiar a tema") or label == "En esta página"
        )
        if leaked:
            ERRORS.append(
                f"Spanish interface text leaked into English page {relative}: "
                + ", ".join(sorted(set(leaked)))
            )
        if 'property="og:locale" content="en_US"' not in text:
            ERRORS.append(f"English Open Graph locale is not en_US: {relative}")
        if "Learn to turn data, analytics and AI into better business decisions" not in text:
            ERRORS.append(f"English Open Graph description is missing: {relative}")
        if 'title="Enlace permanente"' in text:
            ERRORS.append(f"Spanish permanent-link label leaked into English page: {relative}")
    if expected_language == "es" and not is_error_page:
        if 'title="Permanent link"' in text:
            ERRORS.append(f"English permanent-link label leaked into Spanish page: {relative}")
        if "CDI-BoK · Inteligencia de Decisiones Conversacional" not in text:
            ERRORS.append(f"Localized Spanish site name is missing: {relative}")

spanish_search_path = SITE / "search" / "search_index.json"
english_search_path = SITE / "en" / "search" / "search_index.json"
if not spanish_search_path.exists() or not english_search_path.exists():
    ERRORS.append("Language-specific search indexes were not generated")
else:
    spanish_search = json.loads(spanish_search_path.read_text(encoding="utf-8"))
    english_search = json.loads(english_search_path.read_text(encoding="utf-8"))
    spanish_documents = spanish_search.get("docs", [])
    english_documents = english_search.get("docs", [])
    if not spanish_documents or any(str(doc.get("location", "")).startswith("en/") for doc in spanish_documents):
        ERRORS.append("Spanish search index contains no documents or leaks English routes")
    if not english_documents or any(not str(doc.get("location", "")).startswith("en/") for doc in english_documents):
        ERRORS.append("English search index contains no documents or leaks Spanish routes")
    spanish_pages = [doc for doc in spanish_documents if "#" not in str(doc.get("location", ""))]
    english_pages = [doc for doc in english_documents if "#" not in str(doc.get("location", ""))]
    if len(spanish_pages) != 47 or len(english_pages) != 47:
        ERRORS.append(
            f"Expected 47 page roots in each search index; got ES={len(spanish_pages)}, EN={len(english_pages)}"
        )

if not (SITE / "CNAME").exists():
    ERRORS.append("CNAME was not copied into the site artifact")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} built-site audit error(s)", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: generated-site semantic audit ({len(html_files)} HTML files)")
