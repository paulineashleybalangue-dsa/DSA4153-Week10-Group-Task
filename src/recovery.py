"""Recovery orchestration, duplicate removal, conflicts, and agreement checks."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
import numpy as np
from .readers import read_records, FileSchemaError
from .validator import validate_records, CANONICAL