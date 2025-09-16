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
    "theme": ["cross_joins", "cross_joins", "case when"],
    "exercise_name": ["beverages_and_food", "sizes_and_trademarks", "wages"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"], ["wages"]],
    "last_reviews": ["01/09/2025", "02/09/2025", "03/09/2025"],
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
