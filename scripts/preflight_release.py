#!/usr/bin/env python3
"""Execute the canonical release gate for the current CDI-BoK release."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    [sys.executable, "scripts/validate_bilingual_portal.py"],
    [sys.executable, "scripts/validate_sprint2.py"],
    [sys.executable, "scripts/validate_sprint3.py"],
    [sys.executable, "scripts/validate_sprint4.py"],
    [sys.executable, "scripts/validate_sprint5.py"],
    [sys.executable, "scripts/validate_sprint6.py"],
    [sys.executable, "scripts/validate_version_governance.py"],
    [sys.executable, "scripts/validate_release_v080.py"],
    [sys.executable, "scripts/validate_release_v081.py"],
    [sys.executable, "scripts/validate_release_v082.py"],
    [sys.executable, "scripts/preflight_sprint1.py"],
]


for command in COMMANDS:
    print(f"\n$ {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)

print("\nPASS: current portal preflight completed")
