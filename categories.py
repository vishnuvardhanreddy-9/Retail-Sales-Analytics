import pandas as pd
from pathlib import Path


def generate_categories(output_dir="datasets"):

    categories = [
        {"category_id": 1, "category_name": "Electronics"},
        {"category_id": 2, "category_name": "Clothing"},
        {"category_id": 3, "category_name": "Groceries"},
        {"category_id": 4, "category_name": "Furniture"},
        {"category_id": 5, "category_name": "Sports"},
    ]

    df = pd.DataFrame(categories)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(Path(output_dir) / "categories.csv", index=False)

    print("✅ Categories Generated")


if __name__ == "__main__":
    generate_categories()