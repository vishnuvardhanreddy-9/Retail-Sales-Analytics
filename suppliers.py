import pandas as pd
from pathlib import Path

def generate_suppliers(output_dir="datasets"):

    suppliers = [
        {"supplier_id":1,"supplier_name":"Samsung India","contact_person":"Rahul Sharma","phone":"9876543210","email":"sales@samsung.com","city":"Noida","state":"Uttar Pradesh"},
        {"supplier_id":2,"supplier_name":"Apple India","contact_person":"Amit Verma","phone":"9876543211","email":"sales@apple.com","city":"Bangalore","state":"Karnataka"},
        {"supplier_id":3,"supplier_name":"HP India","contact_person":"Priya Reddy","phone":"9876543212","email":"sales@hp.com","city":"Chennai","state":"Tamil Nadu"},
        {"supplier_id":4,"supplier_name":"Nike India","contact_person":"Karan Singh","phone":"9876543213","email":"sales@nike.com","city":"Delhi","state":"Delhi"},
        {"supplier_id":5,"supplier_name":"Adidas India","contact_person":"Sneha Rao","phone":"9876543214","email":"sales@adidas.com","city":"Mumbai","state":"Maharashtra"},
        {"supplier_id":6,"supplier_name":"Puma India","contact_person":"Vikram Kumar","phone":"9876543215","email":"sales@puma.com","city":"Hyderabad","state":"Telangana"},
        {"supplier_id":7,"supplier_name":"Levi's India","contact_person":"Anjali Gupta","phone":"9876543216","email":"sales@levis.com","city":"Bangalore","state":"Karnataka"},
        {"supplier_id":8,"supplier_name":"Fortune Foods","contact_person":"Suresh Babu","phone":"9876543217","email":"sales@fortune.com","city":"Ahmedabad","state":"Gujarat"},
        {"supplier_id":9,"supplier_name":"India Gate Foods","contact_person":"Rohit Jain","phone":"9876543218","email":"sales@indiagate.com","city":"Delhi","state":"Delhi"},
        {"supplier_id":10,"supplier_name":"Nilkamal Ltd","contact_person":"Harish Patel","phone":"9876543219","email":"sales@nilkamal.com","city":"Mumbai","state":"Maharashtra"}
    ]

    df = pd.DataFrame(suppliers)

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df.to_csv(f"{output_dir}/suppliers.csv", index=False)

    print("✅ Generated suppliers.csv")


if __name__ == "__main__":
    generate_suppliers()