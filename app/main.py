from crypt import methods
from flask import Blueprint,render_template,url_for,request
from flask_login import current_user,login_required
from app import db
from app.forms import ContactForm

main = Blueprint('main', __name__)

@main.route('/',methods=['GET','POST'])
def dashboard():
    form = ContactForm()
    if request.method =='POST':
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data
    return  render_template("dashboard.html",form = form)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',user=current_user)
