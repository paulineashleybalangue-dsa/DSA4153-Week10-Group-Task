import pandas as pd
from src.validator import validate_records

YEARS = [1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007]
CONTINENTS = ["Africa", "Americas", "Asia", "Europe", "Oceania"]

def valid_row():
    return {"country":"Testland","continent":"Asia","year":2007,"lifeExp":70.0,"pop":1000,"gdpPercap":500.0}
