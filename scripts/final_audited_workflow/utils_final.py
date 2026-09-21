#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path
from typing import Dict
import numpy as np
import pandas as pd

CATEGORIES = ["Cancer", "Infectious diseases", "Inflammatory diseases", "Autoimmune diseases"]
ALIAS_TO_CANONICAL = {
    "miR-548ac-3p": "miR-548ac",
    "miR-548l-5p": "miR-548l",
    "miR-548s-3p": "miR-548s",
}

def clean_name(name: str) -> str:
    name = str(name).strip().replace("hsa-", "")
    name = name.replace("(3p)", "-3p").replace("(5p)", "-5p")
    return ALIAS_TO_CANONICAL.get(name, name)

def load_sequence_csv(path: Path) -> Dict[str, str]:
    df = pd.read_csv(path)
    mcol = next(c for c in df.columns if "mir" in c.lower() or "name" in c.lower())
    scol = next(c for c in df.columns if "seq" in c.lower())
    out = {}
    for _, r in df.iterrows():
        name = clean_name(r[mcol])
        seq = str(r[scol]).strip().upper().replace("T", "U")
        if re.fullmatch(r"[ACGU-]+", seq):
            out[name] = seq
    return out

def normalized_levenshtein(a: str, b: str) -> float:
    a, b = str(a), str(b)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            cur[j] = min(cur[j-1] + 1, prev[j] + 1, prev[j-1] + (ca != cb))
        prev = cur
    return prev[-1] / max(len(a), len(b))

def padded_mismatch(a: str, b: str) -> float:
    L = max(len(a), len(b))
    aa, bb = a.ljust(L, "-"), b.ljust(L, "-")
    return sum(x != y for x, y in zip(aa, bb)) / L

def jaccard_binary(a, b) -> float:
    a, b = np.asarray(a, int), np.asarray(b, int)
    union = np.logical_or(a, b).sum()
    if union == 0:
        return 0.0
    return 1.0 - np.logical_and(a, b).sum() / union
