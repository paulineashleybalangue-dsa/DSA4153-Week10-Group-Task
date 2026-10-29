"""Pandas and NumPy analyses for the recovered canonical table."""
from __future__ import annotations
import numpy as np
import pandas as pd

def create_analyses(canonical: pd.DataFrame, reporting_year: int) -> dict[str, pd.DataFrame]:
    """Build the three required analytical CSV tables."""
    asia = canonical.loc[(canonical["continent"] == "Asia") & (canonical["year"] == reporting_year)].copy()
    asia["population_millions"] = asia["pop"] / 1_000_000
    asia["lifeExp_rank"] = asia["lifeExp"].rank(method="min", ascending=False).astype("int64")
    asia = asia.sort_values(["lifeExp_rank","country"]).reset_index(drop=True)