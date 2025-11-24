import pandas as pd
from src.config import DATA_PATH

def load_interactions():
    return pd.read_csv(f"{DATA_PATH}/interactions_train.csv")

def load_items():
    return pd.read_csv(f"{DATA_PATH}/items.csv")

def load_samples():
    return pd.read_csv(f"{DATA_PATH}/sample_submission.csv")