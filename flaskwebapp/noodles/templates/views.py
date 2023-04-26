from flask import Blueprint # module - bunch of urls inside it

views = Blueprint('views', __name__)

@views.route('/') #define decorator
def home(): #define function
    return "<h1>Test</h1>"
