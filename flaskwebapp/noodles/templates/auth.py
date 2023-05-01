from flask import Blueprint, render_template, request, flash 

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
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Your email appears to be invalid.", category="error")
        elif len(firstName) <= 2:
            flash("Your first name looks incorrect.", category="error")
        elif password1 != password2:
            flash("Your passwords do not seem to match.", category="error")
        elif len(password1) < 6:
            flash("Your password needs to be longer.", category="error")
        else:
            flash("Account created", category="success")
            # add user to db

    return render_template("sign_up.html")