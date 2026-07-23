-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Product Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Products
--------------------------------------------------------------
SELECT COUNT(*) AS total_products
FROM products;

--------------------------------------------------------------
-- 2. Products by Category
--------------------------------------------------------------
SELECT
    c.category_name,
    COUNT(*) AS total_products
FROM products p
JOIN categories c
ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_products DESC;

--------------------------------------------------------------
-- 3. Products by Brand
--------------------------------------------------------------
SELECT
    brand,
    COUNT(*) AS total_products
FROM products
GROUP BY brand
ORDER BY total_products DESC;

--------------------------------------------------------------
-- 4. Average Selling Price by Category
--------------------------------------------------------------
SELECT
    c.category_name,
    ROUND(AVG(p.selling_price),2) AS avg_price
FROM products p
JOIN categories c
ON p.category_id=c.category_id
GROUP BY c.category_name
ORDER BY avg_price DESC;

--------------------------------------------------------------
-- 5. Most Expensive Products
--------------------------------------------------------------
SELECT
    product_id,
    product_name,
    brand,
    selling_price
FROM products
ORDER BY selling_price DESC
LIMIT 10;

--------------------------------------------------------------
-- 6. Cheapest Products
--------------------------------------------------------------
SELECT
    product_id,
    product_name,
    brand,
    selling_price
FROM products
ORDER BY selling_price ASC
LIMIT 10;

--------------------------------------------------------------
-- 7. Profit Per Product
--------------------------------------------------------------
SELECT
    product_id,
    product_name,
    selling_price,
    cost_price,
    ROUND(selling_price-cost_price,2) AS profit
FROM products
ORDER BY profit DESC
LIMIT 20;

--------------------------------------------------------------
-- 8. Highest Margin Products
--------------------------------------------------------------
SELECT
    product_name,
    ROUND(((selling_price-cost_price)/cost_price)*100,2) AS margin_percent
FROM products
ORDER BY margin_percent DESC
LIMIT 20;

--------------------------------------------------------------
-- 9. Products by Supplier
--------------------------------------------------------------
SELECT
    s.supplier_name,
    COUNT(*) AS total_products
FROM products p
JOIN suppliers s
ON p.supplier_id=s.supplier_id
GROUP BY s.supplier_name
ORDER BY total_products DESC;

--------------------------------------------------------------
-- 10. Products Costing Above ₹5000
--------------------------------------------------------------
SELECT
    product_name,
    selling_price
FROM products
WHERE selling_price>5000
ORDER BY selling_price DESC;

--------------------------------------------------------------
-- 11. Products Between ₹1000 and ₹5000
--------------------------------------------------------------
SELECT
    product_name,
    selling_price
FROM products
WHERE selling_price BETWEEN 1000 AND 5000
ORDER BY selling_price DESC;

--------------------------------------------------------------
-- 12. Product Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_products,
    COUNT(DISTINCT brand) AS total_brands,
    ROUND(AVG(selling_price),2) AS average_price,
    ROUND(MAX(selling_price),2) AS highest_price,
    ROUND(MIN(selling_price),2) AS lowest_price
FROM products;