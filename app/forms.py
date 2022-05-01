# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import datetime
from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateTimeField

from wtforms.validators import InputRequired, Length, Email


class SignInForm(FlaskForm):
    email = StringField("Email", validators=[Email(
        "Enter a valid email address"), InputRequired("Email is required")])
    password = PasswordField("Password", validators=[InputRequired("Password is required"), Length(
        min=4, message="Password must be 4 or more characters long")])
    remember = BooleanField("Remember Me")


class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[Length(
        min=4, message="Name must be 4 or more letters long")])
    email = StringField("Email", validators=[Email(
        "Enter a valid email address"), InputRequired("Email is required")])
    password1 = PasswordField("Password", validators=[
                              InputRequired("Password is required"), Length(min=4)])
    password2 = PasswordField("Confirm Password", validators=[InputRequired(
    ), Length(min=6, message="Password must be 4 or more characters long")])


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[Length(
        min=4, message="Name must be 4 or more letters long"),InputRequired("Name is required")])
    email = StringField("Email", validators=[Email(
        "Enter a valid email address"), InputRequired("Email is required")])
    subject = StringField("Subject", validators=[
                          InputRequired("Subject is required")])
    message = TextAreaField("Message", validators=[
                            InputRequired("Write a Message")])
    createdAt = DateTimeField("CreatedAt", default=datetime.now)
