-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- EXECUTIVE DASHBOARD
-- ==========================================================

--------------------------------------------------------------
-- Dashboard KPI Cards
--------------------------------------------------------------

SELECT COUNT(*) AS Total_Customers
FROM customers;

SELECT COUNT(*) AS Total_Orders
FROM orders;

SELECT COUNT(*) AS Total_Products
FROM products;

SELECT COUNT(*) AS Total_Stores
FROM stores;

SELECT COUNT(*) AS Total_Employees
FROM employees;

SELECT ROUND(SUM(amount),2) AS Total_Revenue
FROM payments
WHERE payment_status='Paid';

SELECT ROUND(AVG(amount),2) AS Average_Order_Value
FROM payments
WHERE payment_status='Paid';

SELECT ROUND(SUM(refund_amount),2) AS Total_Refund
FROM returns;

--------------------------------------------------------------
-- Dashboard Charts
--------------------------------------------------------------

-- Monthly Revenue

SELECT
DATE_TRUNC('month',payment_date) AS month,
ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status='Paid'
GROUP BY month
ORDER BY month;

--------------------------------------------------------------

-- Orders By Status

SELECT
order_status,
COUNT(*)
FROM orders
GROUP BY order_status;

--------------------------------------------------------------

-- Payments By Method

SELECT
payment_method,
COUNT(*)
FROM payments
GROUP BY payment_method;

--------------------------------------------------------------

-- Revenue By Store

SELECT
s.store_name,
ROUND(SUM(p.amount),2) AS revenue
FROM stores s
JOIN orders o
ON s.store_id=o.store_id
JOIN payments p
ON o.order_id=p.order_id
WHERE p.payment_status='Paid'
GROUP BY s.store_name
ORDER BY revenue DESC;

--------------------------------------------------------------

-- Revenue By Category

SELECT
c.category_name,
ROUND(SUM(pmt.amount),2) AS revenue
FROM categories c
JOIN products pr
ON c.category_id=pr.category_id
JOIN order_items oi
ON pr.product_id=oi.product_id
JOIN payments pmt
ON oi.order_id=pmt.order_id
WHERE pmt.payment_status='Paid'
GROUP BY c.category_name
ORDER BY revenue DESC;

--------------------------------------------------------------

-- Top Selling Products

SELECT
pr.product_name,
COUNT(*) AS total_sales
FROM order_items oi
JOIN products pr
ON oi.product_id=pr.product_id
GROUP BY pr.product_name
ORDER BY total_sales DESC
LIMIT 10;

--------------------------------------------------------------

-- Top Customers

SELECT
c.customer_id,
c.first_name,
c.last_name,
ROUND(SUM(p.amount),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id=o.customer_id
JOIN payments p
ON o.order_id=p.order_id
WHERE p.payment_status='Paid'
GROUP BY
c.customer_id,
c.first_name,
c.last_name
ORDER BY total_spent DESC
LIMIT 10;

--------------------------------------------------------------

-- Return Reasons

SELECT
return_reason,
COUNT(*)
FROM returns
GROUP BY return_reason
ORDER BY COUNT(*) DESC;