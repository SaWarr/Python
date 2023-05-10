# need db model for users and for notes

from . import db # . = importing from current package (website folder)
from flask_login import UserMixin # custom class to make User class easier to do
from sqlalchemy.sql import func # gets current date and time for note object

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    