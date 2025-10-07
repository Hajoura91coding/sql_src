SELECT df_customers.customer_id,
customer_name,
order_id,
product_id,
quantity
FROM df_customers
INNER JOIN df_order_details
on df_customers.customer_id = df_order_details.customer_id