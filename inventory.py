import pandas as pd
import random
from pathlib import Path


def generate_inventory(output_dir="datasets", num_products=2500, num_stores=50):

    inventory = []

    inventory_id = 1

    for store_id in range(1, num_stores + 1):

        for product_id in range(1, num_products + 1):

            inventory.append({
                "inventory_id": inventory_id,
                "product_id": product_id,
                "store_id": store_id,
                "stock_quantity": random.randint(10, 500),
                "last_updated": "2026-07-07"
            })

            inventory_id += 1

    df = pd.DataFrame(inventory)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_file = Path(output_dir) / "inventory.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} inventory records")
    print(f"📁 Saved to: {output_file}")


if __name__ == "__main__":
    generate_inventory()