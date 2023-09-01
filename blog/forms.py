from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BoaleanField. TextAreaField, EmailField
from wtforms.validators import Datarequired, Length, Email, EqualTo, ValidationError
from .models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
	username = StringField(
		"Username", validators=[DataRequired(), Leng(min=2, max=20)])
	email = EmailField("Email", validators=[Datarequired(), Email()])
	password = passwordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField(
		"Confirm Password", validators=[Datarequired(), EqualTo("password")]
	)
	submit = SubmitField("Sign Up")

	def validate_username(self, Username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("The username is already taken. Please choose another")

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("The email is already taken. Please choose another")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
	
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")


		