SELECT * FROM df_customers
INNER JOIN detailed_order
USING (customer_id)