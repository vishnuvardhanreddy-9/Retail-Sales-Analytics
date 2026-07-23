import pandas as pd
from pathlib import Path


# ---------------------------------------------------
# Dataset Folder
# ---------------------------------------------------

DATASET_PATH = Path(__file__).resolve().parent.parent / "datasets"


# ---------------------------------------------------
# Load All CSV Files
# ---------------------------------------------------

def load_data():
    """
    Load all CSV files from the datasets folder.

    Returns:
        dict: Dictionary containing all DataFrames.
    """

    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset folder not found:\n{DATASET_PATH}"
        )

    data = {}

    csv_files = sorted(DATASET_PATH.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            "No CSV files were found inside the datasets folder."
        )

    for file in csv_files:
        try:
            table_name = file.stem
            data[table_name] = pd.read_csv(
                file,
                encoding="utf-8"
            )

        except Exception as e:
            raise Exception(
                f"Error loading {file.name}: {e}"
            )

    return data