import streamlit as st
import pandas as pd
import duckdb

st.write("""SQL SRS 
Spaced Repetition System SQL practice""")

options = st.selectbox(
    "What would you like to review?",
    ["joins", "GroupBy", "Window Functions"],
    index = None,
    placeholder = "Select a theme ...",
)

st.write('you selected:', options)

df = pd.read_csv("data/raw/EdStatsCountry.csv")
st.dataframe(df)

sql_query = st.text_area(label="Entrez votre query:")
result = duckdb.query(sql_query).df()
st.write(f"Vous avez entré la query suivante: {sql_query}")
st.dataframe(result)