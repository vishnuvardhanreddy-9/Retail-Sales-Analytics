-- ===========================
-- MASTER DATA
-- ===========================

COPY suppliers
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/suppliers.csv'
DELIMITER ','
CSV HEADER;

COPY stores
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/stores.csv'
DELIMITER ','
CSV HEADER;

-- ===========================
-- BUSINESS DATA
-- ===========================

COPY customers
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/customers.csv'
DELIMITER ','
CSV HEADER;

COPY employees
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/employees.csv'
DELIMITER ','
CSV HEADER;

COPY products
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/products.csv'
DELIMITER ','
CSV HEADER;

COPY orders
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/orders.csv'
DELIMITER ','
CSV HEADER;

COPY order_items
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/order_items.csv'
DELIMITER ','
CSV HEADER;

COPY inventory
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/inventory.csv'
DELIMITER ','
CSV HEADER;

COPY payments
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/payments.csv'
DELIMITER ','
CSV HEADER;

COPY returns
FROM '/Users/vishnuvardhanreddy/Desktop/Retail-Sales-Analytics/datasets/returns.csv'
DELIMITER ','
CSV HEADER;