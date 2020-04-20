from user import db
from datetime import datetime


# User models
class User(db.Model):
    """ Contains the user data for site users"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    properties = db.relationship('Property', backref='manager', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Property(db.Model):
    """ Contains the users owned or managed properties """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(124))
    description = db.Column(db.String(1024))
    date_added = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Property {}>'.format(self.id)