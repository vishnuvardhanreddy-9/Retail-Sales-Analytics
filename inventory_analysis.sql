-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Inventory Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Inventory Records
--------------------------------------------------------------
SELECT COUNT(*) AS total_inventory_records
FROM inventory;

--------------------------------------------------------------
-- 2. Total Stock Available
--------------------------------------------------------------
SELECT
    SUM(stock_quantity) AS total_stock
FROM inventory;

--------------------------------------------------------------
-- 3. Inventory Value
--------------------------------------------------------------
SELECT
    ROUND(SUM(i.stock_quantity * p.cost_price),2) AS inventory_value
FROM inventory i
JOIN products p
ON i.product_id = p.product_id;

--------------------------------------------------------------
-- 4. Top 10 Products with Highest Stock
--------------------------------------------------------------
SELECT
    p.product_name,
    SUM(i.stock_quantity) AS stock
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
GROUP BY p.product_name
ORDER BY stock DESC
LIMIT 10;

--------------------------------------------------------------
-- 5. Top 10 Products with Lowest Stock
--------------------------------------------------------------
SELECT
    p.product_name,
    SUM(i.stock_quantity) AS stock
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
GROUP BY p.product_name
ORDER BY stock ASC
LIMIT 10;

--------------------------------------------------------------
-- 6. Inventory by Category
--------------------------------------------------------------
SELECT
    c.category_name,
    SUM(i.stock_quantity) AS total_stock
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
JOIN categories c
ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_stock DESC;

--------------------------------------------------------------
-- 7. Inventory by Store
--------------------------------------------------------------
SELECT
    s.store_name,
    SUM(i.stock_quantity) AS total_stock
FROM inventory i
JOIN stores s
ON i.store_id = s.store_id
GROUP BY s.store_name
ORDER BY total_stock DESC;

--------------------------------------------------------------
-- 8. Average Stock Per Product
--------------------------------------------------------------
SELECT
    ROUND(AVG(stock_quantity),2) AS average_stock
FROM inventory;

--------------------------------------------------------------
-- 9. Highest Inventory Value Products
--------------------------------------------------------------
SELECT
    p.product_name,
    ROUND(SUM(i.stock_quantity * p.cost_price),2) AS inventory_value
FROM inventory i
JOIN products p
ON i.product_id = p.product_id
GROUP BY p.product_name
ORDER BY inventory_value DESC
LIMIT 10;

--------------------------------------------------------------
-- 10. Inventory Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS inventory_records,
    SUM(stock_quantity) AS total_stock,
    ROUND(AVG(stock_quantity),2) AS average_stock,
    MAX(stock_quantity) AS highest_stock,
    MIN(stock_quantity) AS lowest_stock
FROM inventory;