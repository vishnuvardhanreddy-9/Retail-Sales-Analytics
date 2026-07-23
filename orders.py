from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_IN")


def generate_orders(output_dir="datasets", num_orders=100000):

    order_status = [
        "Completed",
        "Cancelled",
        "Pending",
        "Returned"
    ]

    orders = []

    for order_id in range(1, num_orders + 1):

        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1, 50000),
            "store_id": random.randint(1, 50),
            "employee_id": random.randint(1, 500),
            "order_date": fake.date_between(start_date="-2y", end_date="today"),
            "order_status": random.choice(order_status)
        })

    df = pd.DataFrame(orders)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(Path(output_dir) / "orders.csv", index=False)

    print(f"✅ Generated {len(df)} orders")


if __name__ == "__main__":
    generate_orders()