#!/usr/bin/env python3
"""Synchronize the approved brand token CSS into the MkDocs asset tree."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "brand" / "tokens.css"
TARGET = ROOT / "docs" / "assets" / "stylesheets" / "brand-tokens.css"


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
        print("FAILED: published brand tokens differ from brand/tokens.css", file=sys.stderr)
        return 1
    print("PASS: published brand tokens are synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

