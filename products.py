from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker()

NUM_PRODUCTS = 2500

categories = {
    1: "Electronics",
    2: "Clothing",
    3: "Groceries",
    4: "Furniture",
    5: "Sports"
}

brands = {
    1: ["Samsung", "Apple", "HP", "Dell", "Sony"],
    2: ["Nike", "Adidas", "Puma", "Levis"],
    3: ["Fortune", "Aashirvaad", "India Gate"],
    4: ["Nilkamal", "Home Centre", "IKEA"],
    5: ["Nivia", "Cosco", "Yonex"]
}


def generate_products(output_dir="datasets", num_products=NUM_PRODUCTS):

    products = []

    for product_id in range(1, num_products + 1):

        category_id = random.randint(1, 5)

        brand = random.choice(brands[category_id])

        products.append({
            "product_id": product_id,
            "product_name": fake.word().title() + " " + categories[category_id],
            "brand": brand,
            "category_id": category_id,
            "supplier_id": random.randint(1, 10),
            "cost_price": round(random.uniform(100, 5000), 2),
            "selling_price": round(random.uniform(500, 7000), 2),
            "stock_unit": random.choice(
                ["Piece", "Box", "Packet", "Kg", "Litre"]
            )
        })

    df = pd.DataFrame(products)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(Path(output_dir) / "products.csv", index=False)

    print(f"Generated {len(df)} products")


if __name__ == "__main__":
    generate_products()