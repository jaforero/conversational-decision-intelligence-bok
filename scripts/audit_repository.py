#!/usr/bin/env python3
"""Check workflows, dependency pinning and common secret signatures."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
EXPECTED_ACTIONS = {
    "actions/checkout": "v7",
    "actions/setup-python": "v7",
    "actions/setup-node": "v7",
    "actions/configure-pages": "v6",
    "actions/upload-pages-artifact": "v5",
    "actions/deploy-pages": "v4",
    "actions/upload-artifact": "v5",
}

workflow_files = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
for path in workflow_files:
    text = path.read_text(encoding="utf-8")
    try:
        yaml.load(text, Loader=yaml.BaseLoader)
    except yaml.YAMLError as error:
        ERRORS.append(f"Invalid workflow YAML {path.name}: {error}")
    for action, version in re.findall(r"uses:\s*([\w-]+/[\w-]+)@(v\d+)", text):
        expected = EXPECTED_ACTIONS.get(action)
        if expected and version != expected:
            ERRORS.append(f"Outdated action {action}@{version}; expected {expected} in {path.name}")

requirements = (ROOT / "requirements.lock").read_text(encoding="utf-8")
for line in requirements.splitlines():
    stripped = line.strip()
    if line and not line[0].isspace() and not stripped.startswith("#") and "==" not in stripped:
        ERRORS.append(f"Unpinned Python dependency: {stripped}")

tracked = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
).decode().split("\0")
secret_patterns = {
    "GitHub token": re.compile(r"(?:ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
for name in tracked:
    if not name:
        continue
    path = ROOT / name
    if not path.is_file():
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, pattern in secret_patterns.items():
        if pattern.search(text):
            ERRORS.append(f"Possible {label} in {name}")

if ERRORS:
    print(f"FAILED: {len(ERRORS)} repository audit error(s)", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"PASS: repository audit ({len(workflow_files)} workflows, pinned dependencies, secret scan)")
