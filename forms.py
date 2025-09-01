from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional

class RegisterForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('student','Student'),('teacher','Teacher'),('parent','Parent'),('admin','Admin')], default='student')
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class MoodForm(FlaskForm):
    mood = SelectField('How are you feeling today?', choices=[('happy','Happy'),('okay','Okay'),('stressed','Stressed'),('sad','Sad')], validators=[DataRequired()])
    note = TextAreaField('Anything you want to note?', validators=[Optional(), Length(max=1000)])
    submit = SubmitField('Save Check-in')

class StudyPlanForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(max=120)])
    topic = StringField('Topic', validators=[DataRequired(), Length(max=255)])
    due_date = DateField('Due Date', validators=[Optional()])
    is_done = BooleanField('Mark as done')
    submit = SubmitField('Save')