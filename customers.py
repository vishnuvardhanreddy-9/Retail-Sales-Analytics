from faker import Faker
import pandas as pd
from pathlib import Path
import random

fake = Faker("en_IN")


def generate_customers(output_dir="datasets", num_customers=50000):

    customers = []

    for customer_id in range(1, num_customers + 1):
        customers.append({
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(["Male", "Female"]),
            "email": fake.unique.email(),
            "phone": fake.msisdn()[:10],
            "city": fake.city(),
            "state": fake.state(),
            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })

    df = pd.DataFrame(customers)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    output_file = Path(output_dir) / "customers.csv"

    df.to_csv(output_file, index=False)

    print(f"Generated {len(df)} customers")
if __name__ == "__main__":
    generate_customers()