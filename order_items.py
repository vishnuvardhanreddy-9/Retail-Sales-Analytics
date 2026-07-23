import pandas as pd
import random
from pathlib import Path


def generate_order_items(output_dir="datasets", num_orders=100000):

    order_items = []

    order_item_id = 1

    for order_id in range(1, num_orders + 1):

        # Each order contains between 1 and 5 products
        number_of_products = random.randint(1, 5)

        for _ in range(number_of_products):

            quantity = random.randint(1, 4)

            unit_price = round(random.uniform(100, 5000), 2)

            total_price = round(quantity * unit_price, 2)

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": random.randint(1, 2500),
                "quantity": quantity,
                "unit_price": unit_price,
                "total_price": total_price
            })

            order_item_id += 1

    df = pd.DataFrame(order_items)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(
        Path(output_dir) / "order_items.csv",
        index=False
    )

    print(f"✅ Generated {len(df)} order items")


if __name__ == "__main__":
    generate_order_items()