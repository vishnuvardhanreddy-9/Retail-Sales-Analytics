-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Return Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Returns
--------------------------------------------------------------
SELECT COUNT(*) AS total_returns
FROM returns;

--------------------------------------------------------------
-- 2. Total Refund Amount
--------------------------------------------------------------
SELECT
    ROUND(SUM(refund_amount),2) AS total_refund
FROM returns;

--------------------------------------------------------------
-- 3. Average Refund Amount
--------------------------------------------------------------
SELECT
    ROUND(AVG(refund_amount),2) AS average_refund
FROM returns;

--------------------------------------------------------------
-- 4. Top Return Reasons
--------------------------------------------------------------
SELECT
    return_reason,
    COUNT(*) AS total_returns
FROM returns
GROUP BY return_reason
ORDER BY total_returns DESC;

--------------------------------------------------------------
-- 5. Top Returned Products
--------------------------------------------------------------
SELECT
    p.product_name,
    COUNT(r.return_id) AS total_returns
FROM returns r
JOIN products p
ON r.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_returns DESC
LIMIT 10;

--------------------------------------------------------------
-- 6. Refund Amount by Product
--------------------------------------------------------------
SELECT
    p.product_name,
    ROUND(SUM(r.refund_amount),2) AS refund_amount
FROM returns r
JOIN products p
ON r.product_id = p.product_id
GROUP BY p.product_name
ORDER BY refund_amount DESC
LIMIT 10;

--------------------------------------------------------------
-- 7. Returns by Month
--------------------------------------------------------------
SELECT
    DATE_TRUNC('month', return_date) AS month,
    COUNT(*) AS total_returns
FROM returns
GROUP BY month
ORDER BY month;

--------------------------------------------------------------
-- 8. Return Percentage
--------------------------------------------------------------
SELECT
    ROUND(
        (COUNT(r.return_id)::numeric /
        (SELECT COUNT(*) FROM orders))*100,
        2
    ) AS return_percentage
FROM returns r;

--------------------------------------------------------------
-- 9. Highest Refunds
--------------------------------------------------------------
SELECT
    return_id,
    refund_amount
FROM returns
ORDER BY refund_amount DESC
LIMIT 10;

--------------------------------------------------------------
-- 10. Return Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_returns,
    ROUND(SUM(refund_amount),2) AS total_refund,
    ROUND(AVG(refund_amount),2) AS average_refund,
    ROUND(MAX(refund_amount),2) AS highest_refund,
    ROUND(MIN(refund_amount),2) AS lowest_refund
FROM returns;