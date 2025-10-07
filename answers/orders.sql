SELECT *,
       CASE
           WHEN order_amount < 200 THEN 'Small'
           WHEN order_amount >= 200 AND order_amount < 800 THEN 'Medium'
           ELSE 'Large'
       END AS order_category
FROM orders