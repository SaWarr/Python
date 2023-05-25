from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() # database object, name below
DB_NAME = "database.db"


def create_app(__name__):
    app = Flask(__name__, template_folder='noodles/templates') # initialising flask
    # had to define template_folder as was getting jinja2.exceptions.TemplateNotFound exception
    app.config['SECRET_KEY'] = 'randomstringgoeshereshouldneverbeshared' # encrypts session data
    # after setting up the views bit
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # sql alchemy located within website folder

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    create_database(app)

    return app

def create_database(app):
    if not path.exists('noodles/' + DB_NAME): #did I call it website or noodles? Come back to
        db.create_all(app=app)
        print('Created Database')
