from pathlib import Path
import json
import pandas as pd
import pytest
from src.recovery import recover_one, ConflictingKeyError
from src.readers import FileSchemaError

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "data/raw/manifest.json").read_text(encoding="utf-8"))