import streamlit as st
import pandas as pd
import duckdb
import io

csv1 = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv1))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
"""

solution = duckdb.sql(answer).df()
st.header("Entrez votre code:")
query = st.text_input(label="Votre code SQL ici", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)
with tab3:
    st.write(answer)

#options = st.selectbox(
#    "What would you like to review?",
#    ["joins", "GroupBy", "Window Functions"],
#    index = None,
#    placeholder = "Select a theme ...",
#)

#st.write('you selected:', options)

#df = pd.read_csv("data/raw/EdStatsCountry.csv")
#st.dataframe(df)

#sql_query = st.text_area(label="Entrez votre query:")
#result = duckdb.query(sql_query).df()
#st.write(f"Vous avez entré la query suivante: {sql_query}")
#st.dataframe(result)