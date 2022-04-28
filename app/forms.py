from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField

from wtforms.validators import InputRequired,Length,Email


class SignInForm(FlaskForm):
    email = StringField("Email",validators=[Email("Enter a valid email address"),InputRequired("Email is required")])
    password = PasswordField("Password",validators=[InputRequired("Password is required"),Length(min=6,message="Password must be 6 or more characters long")])
    remember = BooleanField("Remember Me")


class SignUpForm(FlaskForm):
    name = StringField("Name",validators=[Length(min = 4,message="Name must be 4 or more letters long")])
    email = StringField("Email",validators=[Email("Enter a valid email address"),InputRequired("Email is required")])
    password1 = PasswordField("Password",validators=[InputRequired("Password is required"),Length(min=6)])
    password2 = PasswordField("Confirm Password",validators=[InputRequired(),Length(min=6,message="Password must be 6 or more characters long")])