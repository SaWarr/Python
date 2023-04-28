from flask import Blueprint, render_template # module - bunch of urls inside it

views = Blueprint('views', __name__)

@views.route('/') #define decorator
def home(): #define function
    return render_template("home.html")
