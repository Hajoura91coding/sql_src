# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st
from datetime import date, timedelta
from groq import Groq
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialisation des dossiers et DB
if "data" not in os.listdir():
    logging.debug(os.listdir())
    logging.debug("creating folder data")
    os.mkdir("data")
if "exercises_sql_tables_duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())


def check_users_solution(query_users: str) -> None:
    """
    Checks that user SQL is correct by:
    1) checking the columns
    2) checking the values
    :param query_users: a string containing the query inserted by the user
    """
    result = con.execute(query_users).df()
    st.dataframe(result)
    solution_df = st.session_state.solution_df

    if solution_df is None:
        st.error("Solution non disponible")
        return

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(f"{n_lines_difference} lines difference with the solution_df")


# Connexion à la base de données
con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

# Initialisation du session_state
if 'solution_df' not in st.session_state:
    st.session_state.solution_df = None
if 'exercise_name' not in st.session_state:
    st.session_state.exercise_name = None
if 'selected_theme' not in st.session_state:
    st.session_state.selected_theme = ""


# Fonction callback pour le selectbox
def on_theme_change():
    """Callback appelé quand le thème change"""
    st.session_state.selected_theme = st.session_state.theme_selector


# ========== SIDEBAR ==========
with st.sidebar:
    available_theme_df = con.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme_options = [""] + list(available_theme_df["theme"].unique())

    # Selectbox avec callback
    theme = st.selectbox(
        "What would you like to review?",
        theme_options,
        key='theme_selector',
        on_change=on_theme_change,
        format_func=lambda x: "Sélectionnez un thème..." if x == "" else x
    )

    # Récupérer le thème actuel
    current_theme = st.session_state.selected_theme if st.session_state.selected_theme != "" else None

    if current_theme:
        st.write("You selected:", current_theme)

        # Charger les exercices du thème
        select_exercises = f"SELECT * FROM memory_state WHERE theme = '{current_theme}'"
        exercise = (
            con.execute(select_exercises)
            .df()
            .sort_values(by=["last_reviews"])
            .reset_index(drop=True)
        )
        st.write(exercise)

        # Sauvegarder l'exercice et la solution dans session_state
        st.session_state.exercise_name = exercise.loc[0, "exercise_name"]
        exercise_name = st.session_state.exercise_name

        with open(f"answers/{exercise_name}.sql", "r") as f:
            answer = f.read()
        st.session_state.solution_df = con.execute(answer).df()

        # Tabs pour Tables et Solution
        tab2, tab3 = st.tabs(["Tables", "Solution"])

        with tab2:
            exercise_tables = exercise.loc[0, "tables"]
            for table in exercise_tables:
                st.write(f"Table: {table}")
                df_table = con.execute(f"SELECT * FROM {table}").df()
                st.dataframe(df_table)

        with tab3:
            if st.checkbox('Afficher la solution'):
                st.code(answer, "sql")
    else:
        st.info("👈 Sélectionnez un thème pour commencer")

# ========== ZONE PRINCIPALE ==========
if current_theme:
    exercise_name = st.session_state.exercise_name

    # Afficher les guidelines
    with open(f"guidelines/{current_theme}.md", 'r') as f:
        guidelines = f.read()
        marker = f"EXERCICE: {exercise_name}"

        if marker in guidelines:
            sections = guidelines.split(marker)
            for section in sections:
                if section.startswith("Consigne"):
                    end_idx = section.find("EXERCICE: ")
                    st.write(section[:end_idx])
                else:
                    st.write(section)

    # Formulaire pour la requête SQL
    st.header("Entrez votre code pour résoudre l'exercice:")
    with st.form("sql_query_form"):
        query = st.text_area(label="Votre code SQL ici", key="user_input", height=150)
        submitted = st.form_submit_button("Vérifier")

        if submitted and query:
            check_users_solution(query)

    # Boutons de révision
    st.subheader("Programmer la prochaine révision:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Revoir dans 2 jours"):
            next_review = date.today() + timedelta(days=2)
            con.execute(
                f"UPDATE memory_state SET last_reviews = '{next_review}' WHERE exercise_name = '{exercise_name}'"
            )
            st.rerun()

    with col2:
        if st.button("Revoir dans 7 jours"):
            next_review = date.today() + timedelta(days=7)
            con.execute(
                f"UPDATE memory_state SET last_reviews = '{next_review}' WHERE exercise_name = '{exercise_name}'"
            )
            st.rerun()

    with col3:
        if st.button("Revoir dans 21 jours"):
            next_review = date.today() + timedelta(days=21)
            con.execute(
                f"UPDATE memory_state SET last_reviews = '{next_review}' WHERE exercise_name = '{exercise_name}'"
            )
            st.rerun()

    with col4:
        if st.button("Reset"):
            con.execute(f"UPDATE memory_state SET last_reviews = '1970-01-01'")
            st.rerun()

else:
    # Page d'accueil
    st.title("Bienvenue sur la plateforme d'apprentissage de SQL")
    with open(f"guidelines/main_guidelines.md", "r") as f:
        main_pages = f.read()
    st.write(main_pages)