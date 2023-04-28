from flask import Flask

def create_app(__name__):
    app = Flask(__name__, template_folder='noodles/templates') # initialising flask
    # had to define template_folder as was getting jinja2.exceptions.TemplateNotFound exception
    app.config['SECRET_KEY'] = 'randomstringgoeshereshouldneverbeshared' # encrypts session data
    # after setting up the views bit
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app