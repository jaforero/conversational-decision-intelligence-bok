#!/usr/bin/env python3
"""Run static semantic checks against the generated MkDocs HTML."""

from __future__ import annotations

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

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
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
    if not parser.html_lang.startswith("es"):
        ERRORS.append(f"Missing Spanish lang attribute: {relative}")
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

if not (SITE / "CNAME").exists():
    ERRORS.append("CNAME was not copied into the site artifact")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} built-site audit error(s)", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: generated-site semantic audit ({len(html_files)} HTML files)")
