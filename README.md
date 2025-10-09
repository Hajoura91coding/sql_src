
---

# 📘 SQL Learning Platform

Une application **Streamlit** pour pratiquer et réviser le SQL de manière interactive, avec correction automatique et gestion des révisions espacées.

Mais qu'est-ce que la répétition espacée ?

La répétition espacée est une technique d'apprentissage qui consiste à se faire interroger (ou s'auto-interroger) d'autant moins souvent qu'on maîtrise la question. 

## 🚀 Fonctionnalités

* Interface simple et intuitive avec **Streamlit**.
* Exercices organisés par **thèmes** (choix dans la sidebar).
* Affichage des tables nécessaires pour chaque exercice.
* Vérification automatique des solutions de l’utilisateur :

  * Comparaison des colonnes et des résultats avec la solution attendue.
  * Signalement des différences de lignes ou colonnes.
  * Possibilité de demander un indice
* Système de **révisions planifiées** (2, 7 ou 21 jours) pour renforcer la mémoire.
* Stockage et gestion des données via **DuckDB**.

## 📂 Structure du projet

```
├── app.py               # Application principale Streamlit
├── init_db.py           # Script d'initialisation de la base DuckDB
├── data/                # Base DuckDB et données générées
├── answers/             # Réponses SQL des exercices
├── guidelines/          # Consignes associées aux thèmes/exercices
├── requirements.txt     # Dépendances Python
```

## ⚙️ Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/ton-compte/sql-learning-platform.git
   cd sql-learning-platform
   ```

2. Créer et activer un environnement virtuel :

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Initialiser la base DuckDB (automatique au premier lancement).

## ▶️ Lancer l'application

**[→ Try the live demo](https://sql-learning-platform.streamlit.app/)**

ou bien localement :

```bash
streamlit run app.py
```

Accéder ensuite à [http://localhost:8501](http://localhost:8501).

## 🧑‍💻 Exemple d’utilisation

1. Choisir un **thème** dans la sidebar.
2. Lire les **consignes** affichées.
3. Écrire sa requête SQL dans le champ prévu.
4. Valider et comparer son résultat à la **solution officielle**.
5. Planifier la prochaine révision (2, 7 ou 21 jours).

