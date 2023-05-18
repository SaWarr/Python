# need db model for users and for notes

from . import db # . = importing from current package (website folder)
from flask_login import UserMixin # custom class to make User class easier to do
from sqlalchemy.sql import func # gets current date and time for note object

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # list storing all notes


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Notes must belong to user, association with user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # must pass valid user id, one to many, user to notes
    
# class Reminder / Video etc (db.Model)  - - could add all sorts of other stuff