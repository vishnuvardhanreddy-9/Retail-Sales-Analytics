-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- KPI ANALYSIS
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Revenue
--------------------------------------------------------------
SELECT
    ROUND(SUM(amount),2) AS total_revenue
FROM payments
WHERE payment_status='Paid';

--------------------------------------------------------------
-- 2. Total Orders
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_orders
FROM orders;

--------------------------------------------------------------
-- 3. Total Customers
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_customers
FROM customers;

--------------------------------------------------------------
-- 4. Total Products
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_products
FROM products;

--------------------------------------------------------------
-- 5. Average Order Value
--------------------------------------------------------------
SELECT
    ROUND(AVG(amount),2) AS average_order_value
FROM payments
WHERE payment_status='Paid';

--------------------------------------------------------------
-- 6. Total Refund Amount
--------------------------------------------------------------
SELECT
    ROUND(SUM(refund_amount),2) AS total_refund
FROM returns;

--------------------------------------------------------------
-- 7. Return Rate
--------------------------------------------------------------
SELECT
ROUND(
(
SELECT COUNT(*) FROM returns
)::numeric/
(
SELECT COUNT(*) FROM orders
)*100,2
) AS return_rate;

--------------------------------------------------------------
-- 8. Paid Transactions
--------------------------------------------------------------
SELECT
COUNT(*) AS paid_transactions
FROM payments
WHERE payment_status='Paid';

--------------------------------------------------------------
-- 9. Pending Transactions
--------------------------------------------------------------
SELECT
COUNT(*) AS pending_transactions
FROM payments
WHERE payment_status='Pending';

--------------------------------------------------------------
-- 10. Failed Transactions
--------------------------------------------------------------
SELECT
COUNT(*) AS failed_transactions
FROM payments
WHERE payment_status='Failed';

--------------------------------------------------------------
-- 11. Inventory Value
--------------------------------------------------------------
SELECT
ROUND(SUM(i.stock_quantity*p.cost_price),2)
AS inventory_value
FROM inventory i
JOIN products p
ON i.product_id=p.product_id;

--------------------------------------------------------------
-- 12. Average Product Price
--------------------------------------------------------------
SELECT
ROUND(AVG(selling_price),2)
AS average_product_price
FROM products;

--------------------------------------------------------------
-- 13. Highest Product Price
--------------------------------------------------------------
SELECT
MAX(selling_price)
AS highest_product_price
FROM products;

--------------------------------------------------------------
-- 14. Lowest Product Price
--------------------------------------------------------------
SELECT
MIN(selling_price)
AS lowest_product_price
FROM products;

--------------------------------------------------------------
-- 15. Executive KPI Summary
--------------------------------------------------------------
SELECT
(SELECT COUNT(*) FROM customers) AS customers,
(SELECT COUNT(*) FROM orders) AS orders,
(SELECT COUNT(*) FROM products) AS products,
(SELECT COUNT(*) FROM stores) AS stores,
(SELECT COUNT(*) FROM employees) AS employees,
(SELECT ROUND(SUM(amount),2)
 FROM payments
 WHERE payment_status='Paid') AS revenue,
(SELECT ROUND(SUM(refund_amount),2)
 FROM returns) AS refunds;