import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")


def generate_returns(output_dir="datasets", num_returns=8000):

    reasons = [
        "Damaged Product",
        "Wrong Item Delivered",
        "Customer Changed Mind",
        "Defective Product",
        "Late Delivery"
    ]

    returns = []

    for return_id in range(1, num_returns + 1):

        returns.append({
            "return_id": return_id,
            "order_id": random.randint(1, 100000),
            "product_id": random.randint(1, 2500),
            "return_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "return_reason": random.choice(reasons),
            "refund_amount": round(random.uniform(100, 10000), 2)
        })

    df = pd.DataFrame(returns)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_file = Path(output_dir) / "returns.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} returns")
    print(f"📁 Saved to: {output_file}")


if __name__ == "__main__":
    generate_returns()