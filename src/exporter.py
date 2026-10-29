"""Safe export staging and round-trip verification."""
from __future__ import annotations
import json, shutil
from pathlib import Path
import pandas as pd
import numpy as np
from .validator import CANONICAL

def write_canonical_formats(canonical: pd.DataFrame, folder: Path) -> None:
    """Write all four canonical formats into a staging folder."""
    folder.mkdir(parents=True, exist_ok=True)
    canonical[CANONICAL].to_csv(folder / "canonical.csv", index=False)
    with pd.ExcelWriter(folder / "canonical.xlsx", engine="openpyxl") as writer:
        canonical[CANONICAL].to_excel(writer, sheet_name="observations", index=False)
    canonical[CANONICAL].to_json(folder / "canonical.json", orient="records", indent=2)
    canonical[CANONICAL].to_parquet(folder / "canonical.parquet", index=False, engine="pyarrow")
