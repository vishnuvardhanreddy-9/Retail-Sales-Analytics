import pandas as pd
from pathlib import Path

def generate_stores(output_dir="datasets", num_stores=50):
    cities = [
        ("Chennai", "Tamil Nadu"),
        ("Bangalore", "Karnataka"),
        ("Hyderabad", "Telangana"),
        ("Mumbai", "Maharashtra"),
        ("Delhi", "Delhi"),
        ("Pune", "Maharashtra"),
        ("Kolkata", "West Bengal"),
        ("Ahmedabad", "Gujarat"),
        ("Jaipur", "Rajasthan"),
        ("Lucknow", "Uttar Pradesh")
    ]

    stores = []

    for i in range(1, num_stores + 1):
        city, state = cities[(i - 1) % len(cities)]

        stores.append({
            "store_id": i,
            "store_name": f"Retail Hub {city} Branch {((i-1)//10)+1}",
            "city": city,
            "state": state,
            "opening_year": 2015 + (i % 10)
        })

    df = pd.DataFrame(stores)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(f"{output_dir}/stores.csv", index=False)

    print(f"✅ Generated {len(df)} stores")


if __name__ == "__main__":
    generate_stores()