# Data Dictionary

## Project Name

Retail Sales Analytics

---

# Table 1 : Categories

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| category_id | INT | Primary Key | Unique category ID |
| category_name | VARCHAR(100) | NOT NULL | Category Name |

---

# Table 2 : Suppliers

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| supplier_id | INT | Primary Key | Unique Supplier ID |
| supplier_name | VARCHAR(150) | NOT NULL | Supplier Name |
| contact_person | VARCHAR(100) | | Contact Person |
| phone | VARCHAR(20) | | Phone Number |
| email | VARCHAR(100) | UNIQUE | Supplier Email |
| city | VARCHAR(100) | | City |
| state | VARCHAR(100) | | State |

---

# Table 3 : Stores

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| store_id | INT | Primary Key | Store ID |
| store_name | VARCHAR(100) | NOT NULL | Store Name |
| city | VARCHAR(100) | | Store City |
| state | VARCHAR(100) | | Store State |
| opening_year | INT | | Opening Year |

---

# Table 4 : Employees

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| employee_id | INT | PRIMARY KEY | Unique Employee ID |
| first_name | VARCHAR(50) | NOT NULL | Employee First Name |
| last_name | VARCHAR(50) | NOT NULL | Employee Last Name |
| email | VARCHAR(100) | UNIQUE | Employee Email |
| phone | VARCHAR(20) | NOT NULL | Phone Number |
| gender | VARCHAR(10) | NOT NULL | Gender |
| hire_date | DATE | NOT NULL | Joining Date |
| salary | DECIMAL(10,2) | NOT NULL | Monthly Salary |
| designation | VARCHAR(100) | NOT NULL | Job Role |
| store_id | INT | FOREIGN KEY | Store Assignment |

---

# Table 5 : Customers

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| customer_id | INT | PRIMARY KEY | Unique Customer ID |
| first_name | VARCHAR(50) | NOT NULL | First Name |
| last_name | VARCHAR(50) | NOT NULL | Last Name |
| gender | VARCHAR(10) | NOT NULL | Gender |
| email | VARCHAR(100) | UNIQUE | Email Address |
| phone | VARCHAR(20) | NOT NULL | Phone Number |
| city | VARCHAR(100) | NOT NULL | City |
| state | VARCHAR(100) | NOT NULL | State |
| registration_date | DATE | NOT NULL | Registration Date |

---

# Table 6 : Products

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| product_id | INT | PRIMARY KEY | Unique Product ID |
| product_name | VARCHAR(150) | NOT NULL | Product Name |
| brand | VARCHAR(100) | NOT NULL | Brand Name |
| category_id | INT | FOREIGN KEY | Product Category |
| supplier_id | INT | FOREIGN KEY | Supplier |
| cost_price | DECIMAL(10,2) | NOT NULL | Purchase Price |
| selling_price | DECIMAL(10,2) | NOT NULL | Selling Price |
| stock_unit | VARCHAR(20) | NOT NULL | Unit |

---

# Table 7 : Orders

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| order_id | INT | PRIMARY KEY | Unique Order ID |
| customer_id | INT | FOREIGN KEY | Customer who placed the order |
| employee_id | INT | FOREIGN KEY | Employee handling the order |
| store_id | INT | FOREIGN KEY | Store where the order was placed |
| order_date | DATE | NOT NULL | Order Date |
| order_status | VARCHAR(20) | NOT NULL | Pending, Completed, Cancelled, Returned |
| total_amount | DECIMAL(10,2) | NOT NULL | Total Order Amount |

---

## Table 8 : Order_Items

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| order_item_id | INT | PRIMARY KEY | Unique Order Item ID |
| order_id | INT | FOREIGN KEY | Order ID |
| product_id | INT | FOREIGN KEY | Product Purchased |
| quantity | INT | NOT NULL | Quantity Purchased |
| unit_price | DECIMAL(10,2) | NOT NULL | Price Per Unit |
| discount | DECIMAL(5,2) | DEFAULT 0 | Discount Percentage |
| subtotal | DECIMAL(10,2) | NOT NULL | Total Amount After Discount |

---

# Table 9 : Payments

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| payment_id | INT | PRIMARY KEY | Unique Payment ID |
| order_id | INT | FOREIGN KEY | Order ID |
| payment_method | VARCHAR(30) | NOT NULL | UPI, Credit Card, Debit Card, Cash, Net Banking |
| payment_status | VARCHAR(20) | NOT NULL | Paid, Pending, Failed, Refunded |
| payment_date | DATE | NOT NULL | Payment Date |
| amount | DECIMAL(10,2) | NOT NULL | Paid Amount |

---

# Table 10 : Inventory

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| inventory_id | INT | PRIMARY KEY | Unique Inventory ID |
| product_id | INT | FOREIGN KEY | Product ID |
| store_id | INT | FOREIGN KEY | Store ID |
| stock_quantity | INT | NOT NULL | Available Stock |
| reorder_level | INT | NOT NULL | Minimum Stock Level |
| last_restock_date | DATE | NOT NULL | Last Restock Date |

---

## Table 11 : Returns

| Column Name | Data Type | Constraints | Description |
|--------------|-----------|-------------|-------------|
| return_id | INT | PRIMARY KEY | Unique Return ID |
| order_id | INT | FOREIGN KEY | Order ID |
| product_id | INT | FOREIGN KEY | Returned Product |
| return_date | DATE | NOT NULL | Return Date |
| return_reason | VARCHAR(150) | NOT NULL | Reason for Return |
| refund_amount | DECIMAL(10,2) | NOT NULL | Refund Amount |