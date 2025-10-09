SELECT df_customers.customer_id,
customer_name,
order_id,
product_id,
quantity
FROM df_customers
INNER JOIN order_details
on df_customers.customer_id = order_details.customer_id