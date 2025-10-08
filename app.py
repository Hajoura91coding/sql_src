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


def parse_exercise_from_md(filepath: str) -> list:
    """
    Parse un fichier markdown et extrait tous les exercices

    Args:
        filepath: Chemin vers le fichier .md (ex: "guidelines/cross_joins.md")

    Returns:
        Liste de dicts: [{'name': 'ex1', 'consigne': '...'}, {...}]
    """
    exercises = []  # Liste pour stocker TOUS les exercices

    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # Utilise filepath
            content = f.read()

        # Split par le marker "### EXERCICE:"
        sections = content.split("### EXERCICE:")

        # Parcourir toutes les sections (sauf la première qui est vide ou contient l'intro)
        for section in sections[1:]:
            # Split la section en lignes
            lines = section.strip().split('\n')

            # Première ligne = nom de l'exercice
            exercise_name = lines[0].strip()

            # Chercher la consigne
            consigne = ""
            in_consigne = False
            consigne_lines = []

            for line in lines[1:]:  # Commencer après le nom
                # Détecter le début de la consigne
                if line.startswith("#### Consigne") :
                    in_consigne = True
                    continue  # Sauter la ligne "#### Consigne:"

                # Si on est dans la consigne et qu'on rencontre un nouveau ### EXERCICE
                if in_consigne and line.startswith("###"):
                    break  # Fin de la consigne

                # Collecter les lignes de consigne
                if in_consigne:
                    consigne_lines.append(line)

            # oindre toutes les lignes de consigne
            consigne = '\n'.join(consigne_lines).strip()

            # Ajouter l'exercice à la liste
            exercises.append({
                'name': exercise_name,
                'consigne': consigne
            })

    except FileNotFoundError:
        st.warning(f"Fichier {filepath} introuvable")
        return []
    except Exception as e:
        st.error(f"Erreur lors du parsing: {e}")
        return []

    return exercises  # Retourner la liste complète
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
if 'selected_exercise_name' not in st.session_state:
    st.session_state.selected_exercise_name = None
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
def on_exercise_change():
    st.session_state.selected_exercise_name = st.session_state.exercise_selector


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

        #  Parser une fois et stocker dans session_state
        if 'available_exercises' not in st.session_state or st.session_state.get('current_theme') != current_theme:
            st.session_state.available_exercises = parse_exercise_from_md(f"guidelines/{current_theme}.md")
            st.session_state.current_theme = current_theme

        available_exercises = st.session_state.available_exercises

        if available_exercises:
            exercises_name = [ex['name'] for ex in available_exercises]

            # Initialisation
            if 'selected_exercise_name' not in st.session_state:
                st.session_state.selected_exercise_name = exercises_name[0]

            # Selectbox
            selected_exercise_name = st.selectbox(
                "📝 Choisir un exercice:",
                exercises_name,
                key='exercise_selector',
                index=exercises_name.index(st.session_state.selected_exercise_name)
                if st.session_state.selected_exercise_name in exercises_name
                else 0
            )

            st.session_state.selected_exercise_name = selected_exercise_name

            # Charger la solution
            try:
                with open(f"answers/{selected_exercise_name}.sql", "r") as f:
                    answer = f.read()
                st.session_state.solution_df = con.execute(answer).df()
            except FileNotFoundError:
                st.error(f"Fichier answers/{selected_exercise_name}.sql introuvable")
            select_exercise_info = f"""
                SELECT tables
                FROM memory_state
                WHERE theme = '{current_theme}'
                AND exercise_name = '{selected_exercise_name}'
            """
            exercise_info = con.execute(select_exercise_info).df()

            if not exercise_info.empty:
                exercise_tables = exercise_info.loc[0, "tables"]

                # Tabs pour Tables et Solution
                tab2, tab3 = st.tabs(["Tables", "Solution"])

                with tab2:
                    st.write(f"**Tables pour {selected_exercise_name}:**")
                    for table in exercise_tables:
                        st.write(f"Table: {table}")
                        df_table = con.execute(f"SELECT * FROM {table}").df()
                        st.dataframe(df_table)

                with tab3:
                    if st.checkbox('Afficher la solution', key=f"solution_of_exercise:{selected_exercise_name}"):
                        st.code(answer, "sql")
                        solution_df = con.execute(answer).df()
                        st.dataframe(solution_df)
                        st.session_state.solution_df = con.execute(answer).df()
            else:
                st.warning(f"Exercice {selected_exercise_name} non trouvé dans la DB")
        else:
            st.warning("Aucun exercice trouvé dans le fichier markdown")
    else:
        st.info("Sélectionnez un thème pour commencer")


# ========== ZONE PRINCIPALE ==========
if current_theme and 'selected_exercise_name' in st.session_state:
    exercise_name = st.session_state.selected_exercise_name

    # Réutiliser les exercices déjà parsés (pas de re-parsing !)
    available_exercises = st.session_state.available_exercises

    # Utiliser next() au lieu de [0]
    current_exercise = next(
        (ex for ex in available_exercises if ex['name'] == exercise_name),
        None
    )

    if current_exercise:
        st.header(f"Exercice: {exercise_name}")
        st.info(current_exercise['consigne'])
    else:
        st.error(f"Exercice '{exercise_name}' non trouvé")

    # Formulaire pour la requête SQL
    st.header("Entrez votre code pour résoudre l'exercice:")

    with st.form("sql_query_form"):
        query = st.text_area(label="Votre code SQL ici", key="user_input", height=150)
        submitted = st.form_submit_button("Vérifier")
        if submitted and query:
            st.write(f"Valeur de query: {query}")
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


