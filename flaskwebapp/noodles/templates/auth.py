from flask import Blueprint, render_template, request, flash, redirect, url_for  
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"]) #define decorator
def login(): #define function, often same designation as route
    return render_template("login.html")

@auth.route('/logout') 
def logout(): 
    return "<p>Logout<p>"

@auth.route('/sign-up', methods=["GET", "POST"]) 
def signup(): 
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Your email appears to be invalid.", category="error")
        elif len(first_name) <= 2:
            flash("Your first name looks incorrect.", category="error")
        elif password1 != password2:
            flash("Your passwords do not seem to match.", category="error")
        elif len(password1) < 6:
            flash("Your password needs to be longer.", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256') )
            # sha256 just a hashing algorithm
            db.session.add(new_user)
            db.session.commit()

            flash("Account created", category="success")
            # add user to db
            return redirect(url_for('views.home'))


    return render_template("sign_up.html")