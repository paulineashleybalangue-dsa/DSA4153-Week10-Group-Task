from pathlib import Path
import json
import pandas as pd
import pytest
from src.readers import read_records, FileSchemaError
from src.validator import validate_records
from src.recovery import recover_one, ConflictingKeyError
from src.exporter import write_canonical_formats, reload_and_verify

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "data/raw/manifest.json").read_text(encoding="utf-8"))

def test_missing_file_fails():
    with pytest.raises((FileNotFoundError, FileSchemaError)):
        read_records(ROOT / "data/raw/not_here.csv", MANIFEST)
