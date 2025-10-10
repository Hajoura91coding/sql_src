# 🎓 SQL Learning Platform

**Master SQL through interactive exercises and spaced repetition**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit-brightgreen?style=for-the-badge)](https://votre-app.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Stars](https://img.shields.io/github/stars/VotreUsername/sql-learning-platform?style=for-the-badge)](https://github.com/VotreUsername/sql-learning-platform/stargazers)

---

### Why this project?

As a developer learning SQL, I needed a **better way to practice and retain knowledge**. This platform uses **spaced repetition** (proven learning technique) to help you master SQL concepts efficiently.

 **Perfect for:**
- Developers preparing for interviews
- Students learning SQL
- Anyone wanting to level up their database skills

---

## Features

✅ **Smart Review System** - Exercises come back at optimal intervals  
✅ **Real-time Validation** - Instant feedback on your queries  
✅ **Multiple Themes** - JOINS, GROUP BY, CASE WHEN, Window Functions...  
✅ **Progress Tracking** - See your improvement over time  
✅ **Admin Panel** - Easily add new exercises  

---

## Screenshots

### Main Interface
![Main App](screenshots/![img.png](img.png))

### Exercise View
![Exercise](screenshots/exercise.png)

---

## Try it now!

**[Launch Live Demo](https://votre-app.streamlit.app/)**

No installation needed - just click and start learning!

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Streamlit (Python) |
| **Database** | DuckDB |
| **Data Processing** | Pandas |
| **Deployment** | Streamlit Cloud |
| **AI** | Groq API (planned) |

---

## Quick Start (Local)
```bash
# Clone the repo
git clone https://github.com/VotreUsername/sql-learning-platform.git
cd sql-learning-platform

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run the app
streamlit run app.py