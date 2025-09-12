# pylint: disable=missing-module-docstring
import ast

import duckdb
import streamlit as st

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ["cross_joins", "GroupBy", "window_functions"],
        index=None,
        placeholder="Select a theme ...",
    )
    st.write("you selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)


st.header("Entrez votre code:")
query = st.text_input(label="Votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.write(answer)

