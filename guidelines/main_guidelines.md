## 🧭 Plan d’apprentissage SQL

Une base de données relationnelle est un système qui organise les informations en tables reliées entre elles, où chaque table contient des lignes (ou rows) représentant les enregistrements et des colonnes (ou fields) décrivant les attributs. L’ensemble des tables et de leurs relations forme le schéma de la base. Pour interagir avec ces données, on utilise le langage SQL (Structured Query Language), qui permet de créer, interroger et manipuler les tables. Les SGBD (Systèmes de Gestion de Bases de Données) comme MySQL, PostgreSQL, SQLite, SQL Server ou Oracle sont les logiciels qui implémentent SQL et assurent le stockage, la sécurité et la performance des bases. Ainsi, SQL est le langage, tandis que le SGBD est l’outil qui l’exécute.


### 1. Bases fondamentales

* Les requêtes simples :
  * `SELECT ... FROM`
  * Clauses `WHERE`, `ORDER BY`, `LIMIT`
  * Les alias (`AS`).

### 2. Filtrage et conditions

* Opérateurs logiques : `=`, `!=`, `<`, `>`, `BETWEEN`, `IN`, `LIKE`.
* Combinaisons avec `AND`, `OR`, `NOT`.
* Expressions conditionnelles (`CASE WHEN`).

### 3. Fonctions d’agrégation

* `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.
* `GROUP BY` et `HAVING`.
* Différences entre `WHERE` et `HAVING`.

### 4. Relations entre tables

* Clés primaires et étrangères.
* Les **JOINS** :

  * `INNER JOIN`
  * `LEFT JOIN`
  * `RIGHT JOIN`
  * `FULL OUTER JOIN`
  * `CROSS JOIN`
* Cas d’usage des différents types de jointure.

### 5. Sous-requêtes

* `SELECT` dans un `WHERE`.
* Sous-requêtes corrélées.
* Expressions communes (`WITH` / CTE).

### 6. Modélisation & normalisation

* Règles de normalisation (1NF, 2NF, 3NF, BCNF).
* Index, clés uniques, contraintes (`CHECK`, `DEFAULT`, `NOT NULL`).
* Vues (`CREATE VIEW`).

### 7. SQL avancé

* Fenêtres analytiques (`OVER`, `PARTITION BY`, `ROW_NUMBER()`, `RANK()`).
* Fonctions de texte (`CONCAT`, `SUBSTRING`, regex).
* Fonctions de date/temps.
* Transactions : `BEGIN`, `COMMIT`, `ROLLBACK`.
* Verrous, isolation (`READ COMMITTED`, `SERIALIZABLE`).
* Optimisation de requêtes (index, EXPLAIN).

### 8. Pratique en entreprise

* Rédiger des requêtes pour l’analyse de données.
* Nettoyer des données avec SQL.
* Construire des **reportings**.
* Connexion avec Python (via `sqlalchemy`, `pandas`).
* Sécurité : injection SQL et bonnes pratiques.
