#!/usr/bin/env python3
"""Compatibility wrapper for the canonical stable release gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
command = [sys.executable, "scripts/preflight_release.py"]
completed = subprocess.run(command, cwd=ROOT, check=False)
raise SystemExit(completed.returncode)
