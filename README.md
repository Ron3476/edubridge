# EduBridge

EduBridge is a sleek, futuristic school support system built with **Flask**, **SQLAlchemy**, and **Flask-WTF**. It helps students track moods, manage study plans, and provides role-based dashboards for **students, teachers, parents, and admins**.

---

## Features

- **Role-based dashboards**: Student, Teacher, Parent, Admin
- **Mood tracking**: Log daily moods with optional notes
- **Study plans**: Create and track study tasks, mark as done
- **User management**: Admins can view all users
- **Responsive design**: Sleek, light-themed, futuristic UI
- **Secure authentication**: Registration and login system with hashed passwords

---

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS (Futuristic UI), JavaScript
- **Forms**: Flask-WTF, WTForms
- **Database**: SQLite (development), can be swapped with PostgreSQL/MySQL
- **Deployment Ready**: Compatible with **Railway** and **Render**

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/edubridge.git
   cd edubridge
# EduBridge (Starter MVP)

A minimal Flask app for a student success system: mood check-ins, study plans, and a simple dashboard.

## Quick Start

1) Create a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Create .env from example
FLASK_SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///edubridge.db
FLASK_DEBUG=1


4) Initialize the database
bash
>>> from app import db
>>> db.create_all()
>>> exit()


5) Run the app
```bash
python -m waitress --listen=0.0.0.0:5000 app:app

```
Then open Open http://127.0.0.1:5000 in your browser.

## Switching to MySQL (optional)
- Install `pymysql`: `pip install pymysql`
- Set `DATABASE_URL` in `.env`, e.g. `mysql+pymysql://user:pass@localhost/edubridge`
- Re-run `flask --app app.py init-db`

## Next Steps
- Add mentorship matching, parent/teacher dashboards, and AI study helper.
- Protect against CSRF on toggle forms if needed (Flask-WTF already included).
