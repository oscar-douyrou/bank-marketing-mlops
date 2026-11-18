from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "bank-full.csv"


def load_bank_data(path=DATA_PATH):
    return pd.read_csv(path, sep=";")