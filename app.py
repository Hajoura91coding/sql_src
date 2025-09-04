import streamlit as st
import pandas as pd
import duckdb

st.write("hello world!")
df = pd.read_csv("data/raw/EdStatsCountry.csv")
st.dataframe(df)

sql_query = st.text_area(label="Entrez votre query:")
result = duckdb.query(sql_query).df()
st.write(f"vous avez entré la query suivante: {sql_query}")
st.dataframe(result)