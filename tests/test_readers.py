from pathlib import Path
import json
import pytest
from src.readers import read_records, FileSchemaError, CANONICAL