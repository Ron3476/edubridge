# EduBridge (Starter MVP)

A minimal Flask app for a student success system: mood check-ins, study plans, and a simple dashboard.

## Quick Start

1) Create a virtual environment

Windows PowerShell:
```bash
py -m venv .venv
.\.venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Create .env from example
```bash
copy .env.example .env   # Windows
cp .env.example .env     # macOS/Linux
```

4) Initialize the database
```bash
flask --app app.py init-db
```

5) Run the app
```bash
flask --app app.py run
```
Then open (https://edubridge-z9vy.onrender.com)

## Switching to MySQL (optional)
- Install `pymysql`: `pip install pymysql`
- Set `DATABASE_URL` in `.env`, e.g. `mysql+pymysql://user:pass@localhost/edubridge`
- Re-run `flask --app app.py init-db`

## Next Steps
- Add mentorship matching, parent/teacher dashboards, and AI study helper.
- Protect against CSRF on toggle forms if needed (Flask-WTF already included).
