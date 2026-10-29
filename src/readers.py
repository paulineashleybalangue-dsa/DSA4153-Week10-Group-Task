from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import pandas as pd

CANONICAL = ["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]

class FileSchemaError(ValueError):
    """Raised when an input file cannot be parsed or lacks required fields."""

def _flatten_path(record: dict[str, Any], dotted: str) -> Any:
    value: Any = record
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value

def read_records(path: str | Path, manifest: dict[str, Any]) -> pd.DataFrame:
    """Read one input file using the layout recorded in the manifest."""
    path = Path(path)
    spec = next((item for item in manifest["files"] if item["file"] == path.name), None)
    if spec is None:
        # Failure-test fixtures use canonical CSV fields and default CSV parsing.
        if path.suffix.lower() == ".csv":
            df = pd.read_csv(path)
            missing = set(CANONICAL) - set(df.columns)
            if missing:
                raise FileSchemaError(f"Missing required columns: {sorted(missing)}")
            return df[CANONICAL].copy()
        raise FileSchemaError(f"Unsupported format or unconfigured input: {path.name}")
    fmt = spec["format"]