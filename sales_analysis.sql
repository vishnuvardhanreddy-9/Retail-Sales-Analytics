-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Sales Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Orders
--------------------------------------------------------------
SELECT COUNT(*) AS total_orders
FROM orders;

--------------------------------------------------------------
-- 2. Total Revenue
--------------------------------------------------------------
SELECT
    ROUND(SUM(amount),2) AS total_revenue
FROM payments
WHERE payment_status = 'Paid';

--------------------------------------------------------------
-- 3. Average Order Value
--------------------------------------------------------------
SELECT
    ROUND(AVG(amount),2) AS average_order_value
FROM payments
WHERE payment_status = 'Paid';

--------------------------------------------------------------
-- 4. Highest Order Value
--------------------------------------------------------------
SELECT
    MAX(amount) AS highest_order
FROM payments
WHERE payment_status = 'Paid';

--------------------------------------------------------------
-- 5. Lowest Order Value
--------------------------------------------------------------
SELECT
    MIN(amount) AS lowest_order
FROM payments
WHERE payment_status = 'Paid';

--------------------------------------------------------------
-- 6. Revenue by Payment Method
--------------------------------------------------------------
SELECT
    payment_method,
    COUNT(*) AS transactions,
    ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status = 'Paid'
GROUP BY payment_method
ORDER BY revenue DESC;

--------------------------------------------------------------
-- 7. Orders by Status
--------------------------------------------------------------
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

--------------------------------------------------------------
-- 8. Payments by Status
--------------------------------------------------------------
SELECT
    payment_status,
    COUNT(*) AS total_payments
FROM payments
GROUP BY payment_status
ORDER BY total_payments DESC;

--------------------------------------------------------------
-- 9. Daily Sales
--------------------------------------------------------------
SELECT
    payment_date,
    ROUND(SUM(amount),2) AS daily_sales
FROM payments
WHERE payment_status = 'Paid'
GROUP BY payment_date
ORDER BY payment_date;

--------------------------------------------------------------
-- 10. Monthly Revenue
--------------------------------------------------------------
SELECT
    DATE_TRUNC('month', payment_date) AS month,
    ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status = 'Paid'
GROUP BY month
ORDER BY month;

--------------------------------------------------------------
-- 11. Yearly Revenue
--------------------------------------------------------------
SELECT
    EXTRACT(YEAR FROM payment_date) AS year,
    ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status = 'Paid'
GROUP BY year
ORDER BY year;

--------------------------------------------------------------
-- 12. Top 10 Highest Value Payments
--------------------------------------------------------------
SELECT
    payment_id,
    order_id,
    amount
FROM payments
WHERE payment_status = 'Paid'
ORDER BY amount DESC
LIMIT 10;

--------------------------------------------------------------
-- 13. Lowest 10 Payments
--------------------------------------------------------------
SELECT
    payment_id,
    order_id,
    amount
FROM payments
WHERE payment_status = 'Paid'
ORDER BY amount ASC
LIMIT 10;

--------------------------------------------------------------
-- 14. Revenue Distribution by Payment Method
--------------------------------------------------------------
SELECT
    payment_method,
    COUNT(*) AS transactions,
    ROUND(SUM(amount),2) AS revenue,
    ROUND(AVG(amount),2) AS average_payment
FROM payments
WHERE payment_status = 'Paid'
GROUP BY payment_method
ORDER BY revenue DESC;

--------------------------------------------------------------
-- 15. Revenue Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS paid_transactions,
    ROUND(SUM(amount),2) AS total_revenue,
    ROUND(AVG(amount),2) AS average_order_value,
    ROUND(MAX(amount),2) AS highest_order,
    ROUND(MIN(amount),2) AS lowest_order
FROM payments
WHERE payment_status = 'Paid';