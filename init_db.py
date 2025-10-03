import io

import pandas as pd
import duckdb

"""
On déclare 
On lit avec pd_read.csv
On fait con.execute pour requeter le dataFrame pandas avec duckdb 
"""
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)
# ----------------------------------
# EXERCISES LIST
# ---------------------------------
data = {
    "theme": [
        "cross_joins",
        "cross_joins",
        "case_when",
        "case_when",
        "group_by",
        "group_by",
        "group_by",
        "group_by",
        "inner_joins",
        "inner_joins",
        "inner_joins"
    ],
    "exercise_name": [
        "beverages_and_food",
        "sizes_and_trademarks",
        "wages",
        "hours_quarters",
        "sales",
        "salaries_seniorities",
        "weights_turnover_retail",
        "weights_turnover_retail",
        "product_client_order1",
        "product_client_order2",
        "product_client_order3"
    ],
    "tables": [
        ["beverages", "food_items"],
        ["sizes", "trademarks"],
        ["wages"],
        ["hours", "quarters"],
        ["sales"],
        ["salaries", "seniorities"],
        ["weights", "turnover", "retail"],
        ["weights_turnover_retail"],
        ["products", "clients", "orders"],
        ["products", "clients", "orders"],
        ["products", "clients", "orders"]
    ],
    "last_reviews": [
        "01/09/2025",
        "02/09/2025",
        "03/09/2025",
        "04/09/2025",
        "22/09/2025",
        "23/09/2025",
        "24/09/2025",
        "25/09/2025",
        "26/09/2025",
        "27/09/2025",
        "28/09/2025"
    ],
}
memory_state_df = pd.DataFrame(data)

con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")
# CROSS JOIN EXERCICES
# ---------------------------------
CSV1 = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV1))
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")


CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
con.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""

trademarks = pd.read_csv(io.StringIO(trademarks))
con.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")

data = {
    "name": [
        "Toufik",
        "Jean-Nicolas",
        "Daniel",
        "Kaouter",
        "Sylvie",
        "Sebastien",
        "Diane",
        "Romain",
        "François",
        "Anna",
        "Zeinaba",
        "Gregory",
        "Karima",
        "Arthur",
        "Benjamin",
    ],
    "wage": [
        60000,
        75000,
        55000,
        80000,
        70000,
        90000,
        65000,
        72000,
        68000,
        85000,
        100000,
        120000,
        95000,
        83000,
        110000,
    ],
    "department": [
        "IT",
        "HR",
        "SALES",
        "IT",
        "IT",
        "HR",
        "SALES",
        "IT",
        "HR",
        "SALES",
        "IT",
        "IT",
        "HR",
        "SALES",
        "CEO",
    ],
}

wages = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS wages AS SELECT * FROM wages")


clients = ["Oussama", "Julie", "Chris", "Tom"]
ventes = [120, 49, 35, 23, 19, 5.99, 20, 18.77, 39, 10, 17, 12]

sales = pd.DataFrame(ventes)
sales.columns = ["montant"]
sales["client"] = clients * 3

con.execute("CREATE TABLE IF NOT EXISTS sales AS SELECT * FROM sales")

hours ='''
hour
08
09
10
11
12
'''
quarters ='''
00
15
30
45
'''
hours = pd.read_csv(io.StringIO(hours))
quarters = pd.read_csv(io.StringIO(quarters))

con.execute("CREATE TABLE IF NOT EXISTS hours AS SELECT * FROM hours")
con.execute("CREATE TABLE IF NOT EXISTS quarters AS SELECT * FROM quarters")

csv = '''
salary,employee_id
2000,1
2500,2
2200,3
'''

csv2 = '''
employee_id,seniority
1,2ans
2,4ans
'''


salaries = pd.read_csv(io.StringIO(csv))
seniorities = pd.read_csv(io.StringIO(csv2))

con.execute("CREATE TABLE IF NOT EXISTS salaries AS SELECT * FROM salaries")
con.execute("CREATE TABLE IF NOT EXISTS seniorities AS SELECT * FROM seniorities")

# Table des commandes:
orders_data = {
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 103, 104, 105]
}

df_orders = pd.DataFrame(orders_data)
con.execute("CREATE TABLE IF NOT EXISTS df_orders AS SELECT * FROM df_orders")


# Table des clients
customers_data = {
    'customer_id': [101, 102, 103, 104, 105, 106],
    'customer_name': ["Toufik", "Daniel", "Tancrède", "Kaouter", "Jean-Nicolas", "David"]
}
df_customers = pd.DataFrame(customers_data)
con.execute("CREATE TABLE IF NOT EXISTS df_customers AS SELECT * FROM df_customers")

# Table des produits
p_names = ["Laptop", "Ipad", "Livre", "Petitos"]
products_data = {
    'product_id': [101, 103, 104, 105],
    'product_name': p_names,
    'product_price': [800, 400, 30, 2]
}

df_products = pd.DataFrame(products_data)
con.execute("CREATE TABLE IF NOT EXISTS df_products AS SELECT * FROM df_products")

# Détail des commandes
order_details_data = {
    'order_id': [1, 2, 3, 4, 5],
    'product_id': [102, 104, 101, 103, 105],
    'quantity': [2, 1, 3, 2, 1]
}

df_order_details = pd.DataFrame(order_details_data)
con.execute("CREATE TABLE IF NOT EXISTS df_order_details AS SELECT * FROM df_order_details")


