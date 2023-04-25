from flask import Flask

def create_app(__name__):
    app = Flask(__name__) # initialising flask
    app.config['SECRET_KEY'] = 'randomstringgoeshereshouldneverbeshared' # encrypts session data
    
    return app