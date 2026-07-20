#!/usr/bin/env python3
"""Audit public Markdown, navigation, front matter, headings and internal links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml
from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ERRORS: list[str] = []
REQUIRED = {
    "title",
    "description",
    "status",
    "version",
    "artifact_type",
    "authority_level",
    "normative",
    "owner",
    "domains",
    "last_reviewed",
}


def flatten_nav(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from flatten_nav(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten_nav(item)


config = load_config(str(ROOT / "mkdocs.yml"))
nav_paths = list(flatten_nav(config["nav"]))
if len(nav_paths) != len(set(nav_paths)):
    ERRORS.append("Duplicate document in MkDocs navigation")
for path in nav_paths:
    if not (DOCS / path).exists():
        ERRORS.append(f"Navigation target does not exist: {path}")

content_map = yaml.safe_load((ROOT / "governance" / "content-map.yml").read_text(encoding="utf-8"))
registered = {item["path"] for item in content_map["public_portal"]["navigation"]}
for path in registered:
    if not (ROOT / path).exists():
        ERRORS.append(f"Registered portal document does not exist: {path}")
for path in nav_paths:
    registered_path = f"docs/{path}"
    if registered_path not in registered:
        ERRORS.append(f"Navigable document is absent from content-map.yml: {registered_path}")

markdown_files = sorted(DOCS.rglob("*.md"))
for path in markdown_files:
    relative = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        ERRORS.append(f"Missing front matter: {relative}")
        continue
    parts = text.split("---", 2)
    metadata = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    if relative != "docs/governance/architecture.md":
        missing = REQUIRED - metadata.keys()
        if missing:
            ERRORS.append(f"Missing front matter {sorted(missing)}: {relative}")
    headings = [(len(match.group(1)), match.group(2).strip()) for match in re.finditer(r"^(#{1,6})\s+(.+)$", body, re.MULTILINE)]
    h1_count = sum(level == 1 for level, _ in headings)
    if h1_count != 1:
        ERRORS.append(f"Expected one H1, found {h1_count}: {relative}")
    for previous, current in zip(headings, headings[1:]):
        if current[0] > previous[0] + 1:
            ERRORS.append(f"Heading level jump H{previous[0]} to H{current[0]}: {relative}")
    if re.search(r"\]\(\s*\)", body):
        ERRORS.append(f"Empty Markdown link: {relative}")
    if "http://" in body:
        ERRORS.append(f"Insecure HTTP link: {relative}")

    for raw_target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", body):
        target = raw_target.split()[0].strip("<>")
        parsed = urlparse(target)
        if parsed.scheme or target.startswith("#") or target.startswith("mailto:"):
            continue
        clean = unquote(parsed.path)
        if not clean:
            continue
        candidate = (path.parent / clean).resolve()
        options = [candidate]
        if candidate.suffix == "":
            options.extend([candidate / "index.md", candidate.with_suffix(".md")])
        if candidate.suffix == ".html":
            options.append(candidate.with_suffix(".md"))
        if not any(option.exists() for option in options):
            ERRORS.append(f"Broken internal link {target}: {relative}")

if (DOCS / "CNAME").read_text(encoding="utf-8").strip() != "decision.javierforero.co":
    ERRORS.append("docs/CNAME does not contain the canonical subdomain")

for phrase in ["CDI es el estándar internacional", "PULSE garantiza mejores decisiones"]:
    for path in markdown_files:
        if phrase.lower() in path.read_text(encoding="utf-8").lower():
            ERRORS.append(f"Premature absolute claim '{phrase}': {path.relative_to(ROOT)}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} content audit error(s)", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: content audit ({len(markdown_files)} Markdown files, {len(nav_paths)} navigation targets)")

