#Row-level validation with a result object for accepted and quarantined records.
from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Any
import numpy as np
import pandas as pd

CANONICAL = ["country", "continent", "year", "lifeExp", "pop", "gdpPercap"]
STRING_COLUMNS = ["country", "continent"]
NUMERIC_COLUMNS = ["year", "lifeExp", "pop", "gdpPercap"]
