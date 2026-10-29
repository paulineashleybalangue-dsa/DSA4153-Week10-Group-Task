from pathlib import Path
import json
import pytest
from src.recovery import recover_one, assert_agreement
from src.analysis import create_analyses

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "data/raw/manifest.json").read_text(encoding="utf-8"))

def test_required_pandas_analyses_and_numpy_population_index():
    bundle = recover_one(ROOT / "data/raw/country_records.csv", MANIFEST)
    result = create_analyses(bundle.canonical, 2007)