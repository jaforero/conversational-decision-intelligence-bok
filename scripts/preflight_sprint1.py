#!/usr/bin/env python3
"""Execute the reproducible Sprint 1 release gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    [sys.executable, "scripts/validate_sprint0.py"],
    [sys.executable, "scripts/sync_brand_tokens.py", "--check"],
    [sys.executable, "scripts/sync_public_governance.py", "--check"],
    [sys.executable, "scripts/audit_brand.py"],
    [sys.executable, "scripts/audit_content.py"],
    [sys.executable, "scripts/audit_repository.py"],
    [sys.executable, "-m", "mkdocs", "build", "--strict", "--clean"],
    [sys.executable, "scripts/audit_built_site.py"],
]


for command in COMMANDS:
    print(f"\n$ {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)

print("\nPASS: Sprint 1 preflight completed")

