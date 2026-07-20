#!/usr/bin/env python3
"""Publish an exact, auditable copy of CDI-GOV-001 inside docs_dir."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "governance" / "00_CDI-BoK_Architecture_and_Editorial_Governance.md"
TARGET = ROOT / "docs" / "governance" / "architecture.md"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    source = SOURCE.read_bytes()
    if args.write:
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        TARGET.write_bytes(source)
        print(f"SYNCED: {TARGET.relative_to(ROOT)}")
        return 0

    if not TARGET.exists() or TARGET.read_bytes() != source:
        print("FAILED: public governance copy differs from CDI-GOV-001", file=sys.stderr)
        return 1
    print("PASS: public governance copy is synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

