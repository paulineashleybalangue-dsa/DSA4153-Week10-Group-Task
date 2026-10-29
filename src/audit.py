"""Helpers for machine-readable validation and audit reports."""
from __future__ import annotations
import pandas as pd

def write_validation(rows: list[dict], path) -> None:
    """Write validation checks using the required columns."""
    pd.DataFrame(rows, columns=["check","expected","actual","tolerance","pass"]).to_csv(path, index=False)
