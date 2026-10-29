#Row-level validation with a result object for accepted and quarantined records.
from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Any
import numpy as np
import pandas as pd

CANONICAL = ["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]
STRING_COLUMNS = ["country", "continent"]
NUMERIC_COLUMNS = ["year", "lifeExp", "pop", "gdpPercap"]

@dataclass
class ValidationResult:
    """Accepted canonical rows and rejected source rows with reasons."""
    valid: pd.DataFrame
    quarantine: pd.DataFrame

def validate_records(df: pd.DataFrame, source_file: str, allowed_years: list[int],
                     allowed_continents: list[str]) -> ValidationResult:
    """Validate raw field values before casting integer columns."""
    accepted, rejected = [], []
    for record_no, (_, row) in enumerate(df.iterrows(), start=1):
        original = {col: row.get(col) for col in CANONICAL}
        reasons = []
        country = "" if pd.isna(original["country"]) else str(original["country"]).strip()
        continent = "" if pd.isna(original["continent"]) else str(original["continent"]).strip()
        if not country: reasons.append("empty_country")
        if not continent: reasons.append("empty_continent")
        elif continent not in allowed_continents: reasons.append("invalid_continent")

        parsed: dict[str, Any] = {}
        for col in NUMERIC_COLUMNS:
            raw = original[col]
            try:
                val = float(raw)
                if not math.isfinite(val):
                    reasons.append(f"non_finite_{col}")
                else:
                    parsed[col] = val
            except (TypeError, ValueError):
                reasons.append(f"missing_or_unparseable_{col}") 
                