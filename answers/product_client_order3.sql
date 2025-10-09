SELECT * FROM df_customers
INNER JOIN order_details
USING (customer_id)