import shutil
from pathlib import Path
import pprint

import kagglehub
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"


def get_dataset() -> Path:
    if DATA_DIR.exists() and any(DATA_DIR.glob("*.csv")):
        return DATA_DIR
    print("Local data not found, downloading from Kaggle...")
    cache_path = kagglehub.dataset_download("robikscube/hourly-energy-consumption")
    shutil.copytree(cache_path, DATA_DIR, dirs_exist_ok=True)
    return DATA_DIR


path = get_dataset()

dfs = {
    f.stem: pd.read_csv(f, parse_dates=["Datetime"], index_col="Datetime")
    for f in sorted(path.glob("*.csv"))
}

missing = {
    name: {
        'missing': df.isna().sum().to_dict(),
        'rows': df.shape[0]
    }
    for name, df in dfs.items()
}

pprint.pprint(missing)