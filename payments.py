import pandas as pd
import random
from faker import Faker
from pathlib import Path

fake = Faker("en_IN")


def generate_payments(output_dir="datasets", num_orders=100000):

    payment_methods = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Cash"
    ]

    payment_status = [
        "Paid",
        "Pending",
        "Failed",
        "Refunded"
    ]

    payments = []

    for payment_id in range(1, num_orders + 1):

        payments.append({
            "payment_id": payment_id,
            "order_id": payment_id,
            "payment_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "payment_method": random.choice(payment_methods),
            "payment_status": random.choice(payment_status),
            "amount": round(random.uniform(200, 50000), 2)
        })

    df = pd.DataFrame(payments)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_file = Path(output_dir) / "payments.csv"

    df.to_csv(output_file, index=False)

    print(f"✅ Generated {len(df)} payments")
    print(f"📁 Saved to: {output_file}")


if __name__ == "__main__":
    generate_payments()