"""Recovery orchestration, duplicate removal, conflicts, and agreement checks."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import numpy as np
from .readers import read_records, FileSchemaError
from .validator import validate_records, CANONICAL

class ConflictingKeyError(ValueError):
    """Raised when a country-year key has multiple valid payloads."""

@dataclass
class RecoveryBundle:
    """Results from recovering one source format."""
    source_file: str
    raw_count: int
    canonical: pd.DataFrame
    quarantine: pd.DataFrame
    duplicates: pd.DataFrame
    audit: list[dict]

def recover_one(path: Path, manifest: dict) -> RecoveryBundle:
    """Parse, validate, quarantine, deduplicate and sort one source file."""
    raw = read_records(path, manifest)
    result = validate_records(raw, path.name, manifest["allowed_years"], manifest["allowed_continents"])
    valid = result.valid.copy()
    key = manifest.get("key", ["country", "year"])