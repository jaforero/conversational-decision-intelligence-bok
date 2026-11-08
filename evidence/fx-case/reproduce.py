#!/usr/bin/env python3
"""Reproduce the Practice Lab FX reference results from a pinned data revision."""

import json
from decimal import Decimal
from urllib.request import urlopen


REVISION = "dd7a205e147ccb7c00171bbd319e4b0b5fed5e52"
BASE_URL = f"https://raw.githubusercontent.com/jaforero/fx-bancos-centrales/{REVISION}/data/series/"
START = "2026-11-03"
END = "2026-11-06"
WEEKEND = "2026-11-07"
REVIEW_THRESHOLD = Decimal("1")
COP_EFFECTIVE = "usd_cop_trm"
COP_MARKET = "usd_cop_trm_mkt"
MXN_FIX = "usd_mxn_fix"
CROSS = "mxn_cop_cross"


def load_series(series_id):
    with urlopen(f"{BASE_URL}{series_id}.json", timeout=20) as response:
        return json.load(response, parse_float=Decimal)


def observation(series, day):
    return next(row for row in series["observations"] if row["date"] == day)


def main():
    series = {key: load_series(key) for key in (COP_EFFECTIVE, COP_MARKET, MXN_FIX, CROSS)}
    changes = {}
    print(f"Revision {REVISION} | {START} to {END}")
    for key in (COP_EFFECTIVE, COP_MARKET, MXN_FIX):
        start = observation(series[key], START)
        end = observation(series[key], END)
        if start["filled"] or end["filled"]:
            raise ValueError(f"Expected source observations at both endpoints for {key}")
        index = Decimal(100) * end["value"] / start["value"]
        changes[key] = index - 100
        print(f"{key}: {start['value']} → {end['value']} | index {index:.2f} | change {changes[key]:+.2f}%")

    last_fix = observation(series[MXN_FIX], END)
    carried = observation(series[MXN_FIX], WEEKEND)
    if not carried["filled"] or carried["value"] != last_fix["value"]:
        raise ValueError("The Saturday FIX row must carry forward the Friday value")
    print(f"{WEEKEND} FIX: carried forward {carried['value']} MXN/USD from {END}")

    cross_series = series[CROSS]
    if cross_series["inputs"] != [COP_MARKET, MXN_FIX]:
        raise ValueError("The cross must use the two market-date series")
    cop = observation(series[COP_MARKET], END)["value"]
    computed = (cop / last_fix["value"]).quantize(Decimal("0.0001"))
    cross = observation(cross_series, END)
    if cross["filled"] or cross["value"] != computed:
        raise ValueError("The computed cross differs from the published derived series")
    print(f"{END} MXN-COP: {cop} / {last_fix['value']} = {computed} COP/MXN (derived)")

    for name, cop_key in (("market-date", COP_MARKET), ("effective-date", COP_EFFECTIVE)):
        flagged = [key for key in (cop_key, MXN_FIX) if changes[key] >= REVIEW_THRESHOLD]
        print(f"{name} review flags at +{REVIEW_THRESHOLD}%: {', '.join(flagged) or 'none'}")


if __name__ == "__main__":
    main()
