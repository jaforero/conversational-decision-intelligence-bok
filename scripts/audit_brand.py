#!/usr/bin/env python3
"""Audit brand token integrity, approved colors, typeface policy and contrast pairs."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def relative_luminance(value: str) -> float:
    channels = [int(value[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4 for channel in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(first: str, second: str) -> float:
    high, low = sorted((relative_luminance(first), relative_luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


tokens = json.loads((ROOT / "brand" / "tokens.json").read_text(encoding="utf-8"))
colors = {name: token["value"].lower() for name, token in tokens["color"].items()}
approved = set(colors.values())

for path in [
    ROOT / "docs" / "assets" / "stylesheets" / "brand-tokens.css",
    ROOT / "docs" / "assets" / "stylesheets" / "brand.css",
    ROOT / "docs" / "assets" / "stylesheets" / "cdi-bok.css",
    ROOT / "docs" / "assets" / "javascripts" / "site.js",
    ROOT / "overrides" / "main.html",
]:
    text = path.read_text(encoding="utf-8")
    for value in re.findall(r"#[0-9a-fA-F]{6}", text):
        if value.lower() not in approved:
            ERRORS.append(f"Unauthorized color {value} in {path.relative_to(ROOT)}")

brand_css = (ROOT / "docs" / "assets" / "stylesheets" / "brand.css").read_text(encoding="utf-8")
if "https://javierforero.com/fonts/IgraSans.woff2" not in brand_css:
    ERRORS.append("Authorized IgraSans URL is missing")
if "Aptos, Helvetica, Arial, sans-serif" not in brand_css:
    ERRORS.append("Approved font fallback stack is missing")

checks = [
    ("light body", colors["text"], colors["background"], 4.5),
    ("light secondary", colors["muted"], colors["background"], 4.5),
    ("light link", colors["vibrantBlue"], colors["background"], 4.5),
    ("light primary", colors["purple"], colors["white"], 4.5),
    ("dark body", colors["white"], colors["deepBlue"], 4.5),
    ("dark secondary", colors["border"], colors["deepBlue"], 4.5),
    ("dark link", colors["softLilac"], colors["deepBlue"], 4.5),
    ("dark non-text accent", colors["purpleLight"], colors["deepBlue"], 3.0),
]
for name, foreground, background, minimum in checks:
    actual = contrast(foreground, background)
    if actual < minimum:
        ERRORS.append(f"Contrast {name}: {actual:.2f} < {minimum:.1f}")

if tokens["modes"]["dark"]["status"] != "implemented-pending-release-audit":
    ERRORS.append("Dark mode must remain marked as pending release audit")

repository_files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
).decode().split("\0")
font_binaries = [
    ROOT / name
    for name in repository_files
    if name and (ROOT / name).suffix.lower() in {".woff", ".woff2", ".ttf", ".otf"}
]
if font_binaries:
    ERRORS.append("Font binaries are present before redistribution rights are verified")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} brand audit error(s)", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: brand audit ({len(checks)} contrast pairs, approved palette and font policy)")
