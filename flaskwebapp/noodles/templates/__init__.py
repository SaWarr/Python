from flask import Flask

def create_app():
    app = Flask(__name__) # initialising flask
    app.config['SECRET_KEY'] = 'randomstringgoeshereshouldneverbeshared' # encrypts session data
    
    return app