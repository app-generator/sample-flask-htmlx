from flask import Blueprint,render_template,url_for
from flask_login import current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return  render_template("dashboard.html")

@main.route('/profile')
def profile():
    return render_template('profile.html',user=current_user)
