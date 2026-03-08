-- Revenue by Product Line
SELECT
    productline,
    SUM(sales) AS total_revenue
FROM cleaned_sales
GROUP BY productline;


-- Products with revenue greater than 50000
SELECT
    productline,
    SUM(sales) AS revenue
FROM cleaned_sales
GROUP BY productline
HAVING revenue > 50000;


-- Subquery example: products above average sales
SELECT productline, sales
FROM cleaned_sales
WHERE sales >
(
    SELECT AVG(sales)
    FROM cleaned_sales
);


-- Join example (self-join style analysis)
SELECT
    c1.productline,
    SUM(c1.sales) AS revenue
FROM cleaned_sales c1
JOIN cleaned_sales c2
ON c1.ordernumber = c2.ordernumber
GROUP BY c1.productline;