SELECT * FROM df_customers
INNER JOIN df_order_details
USING (customer_id)