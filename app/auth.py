# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint,render_template,url_for,redirect,request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from app  import db
from app.models import User
from app.forms import SignInForm,SignUpForm 
from flask_login import login_user,logout_user,login_required


auth = Blueprint('auth', __name__)

@auth.route('/signin',methods=["GET","POST"])
def signin():
    form = SignInForm()
    if request.method =='POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            user = User.query.filter_by(email=email).first()
            if not user or not check_password_hash(user.password, password):
                flash('Please check your credentials and try again.',category="danger")
                return redirect(url_for('auth.signin'))
            
            login_user(user,remember=remember)
            flash("Signin success",category="success")
            return redirect(url_for('main.profile'))

    return render_template('signin.html',form=form)

@auth.route('/signup',methods=["GET","POST"])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            name = form.name.data
            password1 = form.password1.data
            password2 = form.password2.data

            if password1 != password2:
                form.password2.errors.append("Passwords do not match")
                return redirect(url_for('auth.signup'))

            user = User.query.filter_by(email=email).first()

            if user:
                flash(message="User with email already exists",category="danger")
                return redirect(url_for('auth.signup'))

            new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
            flash(message="Account created successfully",category="success")
            return redirect(url_for('auth.signin'))

    return render_template('signup.html',form=form)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    flash("Signout successful",category="success")
    return redirect(url_for('auth.signin'))
