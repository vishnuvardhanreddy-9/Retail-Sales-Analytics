from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_IN")


def generate_employees(output_dir="datasets", num_employees=500):

    designations = [
        "Store Manager",
        "Sales Executive",
        "Cashier",
        "Inventory Executive",
        "Customer Support"
    ]

    employees = []

    for employee_id in range(1, num_employees + 1):

        gender = random.choice(["Male", "Female"])

        employees.append({
            "employee_id": employee_id,
            "first_name": fake.first_name_male() if gender == "Male" else fake.first_name_female(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "phone": fake.msisdn()[:10],
            "gender": gender,
            "hire_date": fake.date_between(start_date="-8y", end_date="today"),
            "salary": random.randint(18000, 80000),
            "designation": random.choice(designations),
            "store_id": random.randint(1, 50)
        })

    df = pd.DataFrame(employees)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(Path(output_dir) / "employees.csv", index=False)

    print(f"✅ Generated {len(df)} employees")


if __name__ == "__main__":
    generate_employees()