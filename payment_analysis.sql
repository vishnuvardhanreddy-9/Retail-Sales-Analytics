-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Payment Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Payments
--------------------------------------------------------------
SELECT COUNT(*) AS total_payments
FROM payments;

--------------------------------------------------------------
-- 2. Payment Status Distribution
--------------------------------------------------------------
SELECT
    payment_status,
    COUNT(*) AS total_transactions
FROM payments
GROUP BY payment_status
ORDER BY total_transactions DESC;

--------------------------------------------------------------
-- 3. Payment Method Distribution
--------------------------------------------------------------
SELECT
    payment_method,
    COUNT(*) AS total_transactions
FROM payments
GROUP BY payment_method
ORDER BY total_transactions DESC;

--------------------------------------------------------------
-- 4. Revenue by Payment Method
--------------------------------------------------------------
SELECT
    payment_method,
    ROUND(SUM(amount),2) AS total_revenue
FROM payments
WHERE payment_status='Paid'
GROUP BY payment_method
ORDER BY total_revenue DESC;

--------------------------------------------------------------
-- 5. Average Payment by Method
--------------------------------------------------------------
SELECT
    payment_method,
    ROUND(AVG(amount),2) AS average_payment
FROM payments
WHERE payment_status='Paid'
GROUP BY payment_method
ORDER BY average_payment DESC;

--------------------------------------------------------------
-- 6. Highest Payment
--------------------------------------------------------------
SELECT
    payment_id,
    order_id,
    payment_method,
    amount
FROM payments
WHERE payment_status='Paid'
ORDER BY amount DESC
LIMIT 10;

--------------------------------------------------------------
-- 7. Lowest Payment
--------------------------------------------------------------
SELECT
    payment_id,
    order_id,
    payment_method,
    amount
FROM payments
WHERE payment_status='Paid'
ORDER BY amount ASC
LIMIT 10;

--------------------------------------------------------------
-- 8. Daily Revenue
--------------------------------------------------------------
SELECT
    payment_date,
    ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status='Paid'
GROUP BY payment_date
ORDER BY payment_date;

--------------------------------------------------------------
-- 9. Monthly Revenue
--------------------------------------------------------------
SELECT
    DATE_TRUNC('month', payment_date) AS month,
    ROUND(SUM(amount),2) AS revenue
FROM payments
WHERE payment_status='Paid'
GROUP BY month
ORDER BY month;

--------------------------------------------------------------
-- 10. Payment Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS paid_transactions,
    ROUND(SUM(amount),2) AS total_revenue,
    ROUND(AVG(amount),2) AS average_payment,
    ROUND(MAX(amount),2) AS highest_payment,
    ROUND(MIN(amount),2) AS lowest_payment
FROM payments
WHERE payment_status='Paid';