from pathlib import Path

import pandas as pd

from mlops_projet.data.schema import validate_bank_data

DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "bank-full.csv"


def load_bank_data(path=DATA_PATH, validate=True):
    """Charge le fichier Bank Marketing et vérifie son contrat."""
    df = pd.read_csv(path, sep=";")
    if validate:
        df = validate_bank_data(df)
    return df