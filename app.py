from datetime import datetime, date
from flask import Flask, render_template, redirect, url_for, request, flash, abort
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from config import Config
from models import db, User, MoodEntry, StudyPlan
from forms import RegisterForm, LoginForm, MoodForm, StudyPlanForm

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Role-based access decorator
def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return wrapped
    return decorator

# Admin-only route example
@app.route("/admin-only")
@role_required("admin")
def admin_panel():
    return "Welcome to the admin panel!"

# CLI command to initialize DB
@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized.")

# Index route
@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template("index.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data.lower()).first():
            flash("Email already registered.", "danger")
            return redirect(url_for('register'))
        user = User(
            name=form.name.data.strip(),
            email=form.email.data.lower(),
            password_hash=generate_password_hash(form.password.data),
            role=form.role.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in.", "success")
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Welcome back!", "success")
            return redirect(url_for('dashboard'))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)

# Logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "info")
    return redirect(url_for('index'))

# Dashboard (all roles use a unified template approach)
@app.route("/dashboard")
@login_required
def dashboard():
    role = current_user.role.lower()  # ensure lowercase for template checks

    # For students
    recent_moods = []
    plans = []
    students = []
    children = []
    users = []

    if role == "student":
        recent_moods = MoodEntry.query.filter_by(user_id=current_user.id).order_by(MoodEntry.created_at.desc()).limit(7).all()
        plans = StudyPlan.query.filter_by(user_id=current_user.id).order_by(StudyPlan.created_at.desc()).limit(10).all()

    elif role == "teacher":
        students = User.query.filter_by(role="student").all()

    elif role == "parent":
        children = User.query.filter_by(role="student").all()  # adjust as needed

    elif role == "admin":
        users = User.query.all()

    else:
        flash("Role not recognized.", "danger")
        return redirect(url_for("logout"))

    return render_template(
        "dashboard.html",
        role=role,
        recent_moods=recent_moods,
        plans=plans,
        students=students,
        children=children,
        users=users
    )




# Mood check-in
@app.route("/mood", methods=["GET", "POST"])
@login_required
def mood():
    form = MoodForm()
    if form.validate_on_submit():
        entry = MoodEntry(user_id=current_user.id, mood=form.mood.data, note=form.note.data)
        db.session.add(entry)
        db.session.commit()
        flash("Mood check-in saved.", "success")
        return redirect(url_for('dashboard'))
    entries = MoodEntry.query.filter_by(user_id=current_user.id).order_by(MoodEntry.created_at.desc()).all()
    return render_template("mood.html", form=form, entries=entries)

# Study Plan
@app.route("/study-plan", methods=["GET", "POST"])
@login_required
def study_plan():
    form = StudyPlanForm()
    if form.validate_on_submit():
        plan = StudyPlan(
            user_id=current_user.id,
            subject=form.subject.data.strip(),
            topic=form.topic.data.strip(),
            due_date=form.due_date.data if form.due_date.data else None,
            is_done=form.is_done.data
        )
        db.session.add(plan)
        db.session.commit()
        flash("Study plan saved.", "success")
        return redirect(url_for('study_plan'))
    plans = StudyPlan.query.filter_by(user_id=current_user.id).order_by(StudyPlan.created_at.desc()).all()
    return render_template("study_plan.html", form=form, plans=plans)

# Toggle plan completion
@app.route("/study-plan/<int:plan_id>/toggle", methods=["POST"])
@login_required
def toggle_plan(plan_id):
    plan = StudyPlan.query.filter_by(id=plan_id, user_id=current_user.id).first_or_404()
    plan.is_done = not plan.is_done
    db.session.commit()
    return redirect(url_for('study_plan'))

# Run app
if __name__ == "__main__":
    app.run(debug=True)
