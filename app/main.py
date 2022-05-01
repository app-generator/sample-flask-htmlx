# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint, redirect,render_template,url_for,request,flash
from flask_login import current_user,login_required
from app import db
from app.models import Contact
from app.forms import ContactForm
from datetime import datetime

main = Blueprint('main', __name__)

# Aka HOMEPage
@main.route('/',methods=['GET','POST'])
def dashboard():
    form = ContactForm()
    if request.method =='POST':
    
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data

            new_message  = Contact(name=name,email = email,subject=subject,message=message )
            db.session.add(new_message)
            db.session.commit()

            flash(message="Your feedback has been submitted", category="success")

            # Aka HOMEPage
            return redirect(url_for('main.dashboard'))

    return  render_template("dashboard.html",form = form)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',user=current_user)
