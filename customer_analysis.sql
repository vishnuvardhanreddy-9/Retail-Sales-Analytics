-- ==========================================================
-- RETAIL SALES ANALYTICS PROJECT
-- Customer Analysis
-- ==========================================================

--------------------------------------------------------------
-- 1. Total Customers
--------------------------------------------------------------
SELECT COUNT(*) AS total_customers
FROM customers;

--------------------------------------------------------------
-- 2. Customers by Gender
--------------------------------------------------------------
SELECT
    gender,
    COUNT(*) AS total_customers
FROM customers
GROUP BY gender
ORDER BY total_customers DESC;

--------------------------------------------------------------
-- 3. Top 10 Cities by Customer Count
--------------------------------------------------------------
SELECT
    city,
    COUNT(*) AS customers
FROM customers
GROUP BY city
ORDER BY customers DESC
LIMIT 10;

--------------------------------------------------------------
-- 4. Top 10 States by Customer Count
--------------------------------------------------------------
SELECT
    state,
    COUNT(*) AS customers
FROM customers
GROUP BY state
ORDER BY customers DESC
LIMIT 10;

--------------------------------------------------------------
-- 5. New Customers by Registration Year
--------------------------------------------------------------
SELECT
    EXTRACT(YEAR FROM registration_date) AS year,
    COUNT(*) AS new_customers
FROM customers
GROUP BY year
ORDER BY year;

--------------------------------------------------------------
-- 6. Customers Registered This Year
--------------------------------------------------------------
SELECT *
FROM customers
WHERE EXTRACT(YEAR FROM registration_date)=EXTRACT(YEAR FROM CURRENT_DATE);

--------------------------------------------------------------
-- 7. Customers Whose Name Starts With A
--------------------------------------------------------------
SELECT
    customer_id,
    first_name,
    last_name
FROM customers
WHERE first_name LIKE 'A%';

--------------------------------------------------------------
-- 8. Customers Having Gmail Accounts
--------------------------------------------------------------
SELECT
    customer_id,
    first_name,
    email
FROM customers
WHERE email LIKE '%gmail.com';

--------------------------------------------------------------
-- 9. Customers From Chennai
--------------------------------------------------------------
SELECT *
FROM customers
WHERE city='Chennai';

--------------------------------------------------------------
-- 10. Customers From Bangalore
--------------------------------------------------------------
SELECT *
FROM customers
WHERE city='Bangalore';

--------------------------------------------------------------
-- 11. Top 20 Recently Registered Customers
--------------------------------------------------------------
SELECT
    customer_id,
    first_name,
    registration_date
FROM customers
ORDER BY registration_date DESC
LIMIT 20;

--------------------------------------------------------------
-- 12. Oldest Registered Customers
--------------------------------------------------------------
SELECT
    customer_id,
    first_name,
    registration_date
FROM customers
ORDER BY registration_date ASC
LIMIT 20;

--------------------------------------------------------------
-- 13. Distinct Cities
--------------------------------------------------------------
SELECT DISTINCT city
FROM customers
ORDER BY city;

--------------------------------------------------------------
-- 14. Distinct States
--------------------------------------------------------------
SELECT DISTINCT state
FROM customers
ORDER BY state;

--------------------------------------------------------------
-- 15. Customer Summary
--------------------------------------------------------------
SELECT
    COUNT(*) AS total_customers,
    COUNT(DISTINCT city) AS total_cities,
    COUNT(DISTINCT state) AS total_states
FROM customers;