import streamlit as st
import pandas as pd
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

exercice_name = memory_state_df.loc[1, "exercise_name"]
exercice_table = memory_state_df.loc[0, "tables"]
print(exercice_name)
print(exercice_table)
