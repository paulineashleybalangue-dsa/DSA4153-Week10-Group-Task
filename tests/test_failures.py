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

def test_unparseable_nonfinite_and_fractional_values_are_rejected():
    base = {"country":"X","continent":"Asia","year":2007,"lifeExp":70,"pop":100,"gdpPercap":200}
    rows = [{**base,"year":"not-a-number"}, {**base,"lifeExp":float("nan")},
            {**base,"year":2007.25}, {**base,"pop":100.5}]
    result = validate_records(pd.DataFrame(rows), "edge.csv", MANIFEST["allowed_years"], MANIFEST["allowed_continents"])
    assert len(result.quarantine) == 4

def test_missing_required_column_fails():
    with pytest.raises(FileSchemaError):
        read_records(ROOT / "data/raw/missing_column.csv", MANIFEST)