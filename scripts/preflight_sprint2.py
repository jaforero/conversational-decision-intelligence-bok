#!/usr/bin/env python3
"""Execute the reproducible Sprint 2 release gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = [
    [sys.executable, "scripts/validate_sprint2.py"],
    [sys.executable, "scripts/preflight_sprint1.py"],
]


for command in COMMANDS:
    print(f"\n$ {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)

print("\nPASS: Sprint 2 preflight completed")

