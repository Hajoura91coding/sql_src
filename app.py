# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st

if "data" not in os.listdir():
    logging.debug(os.listdir())
    logging.debug("creating folder data")
    os.mkdir("data")
if "exercises_sql_tables_duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess, run(["python",'init_db.py"])

def check_users_solution(query_users: str) -> None:
    """
    Checks that user SQL is correct by:
    1)checking the columns
    2) checking the values
    :param query_users:a string containing the query inserted by the user
    """
    result = con.execute(query_users).df()
    st.dataframe(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        (st.write("Some columns are missing"))
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(f"{n_lines_difference} lines difference with the solution_df")


def selects_exercises():
    available_theme_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review?",
        available_theme_df["theme"].unique(),
        index=None,
        placeholder="Select a theme ...",
    )
    if theme:
        st.write("you selected:", theme)
        select_exercises = f"SELECT * FROM memory_state WHERE theme = '{theme}'"
    else:
        select_exercises = f"SELECT * FROM memory_state"

    exercise = (
        con.execute(select_exercises)
        .df()
        .sort_values(by=["last_reviews"])
        .reset_index(drop=True)
    )
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    solution_df = con.execute(answer).df()

st.header("Entrez votre code:")
query = st.text_input(label="Votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        (st.write("Some columns are missing"))
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(f"{n_lines_difference} lines difference with the solution_df")


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab3:
    st.write(answer)
