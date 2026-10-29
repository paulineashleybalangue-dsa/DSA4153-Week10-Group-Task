from pathlib import Path
import json
import pytest
from src.readers import read_records, FileSchemaError, CANONICAL

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "data/raw/manifest.json").read_text(encoding="utf-8"))