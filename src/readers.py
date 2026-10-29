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