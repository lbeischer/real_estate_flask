import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate the app
app = Flask(__name__)

api = Api(app)

# Set configuration
app.config.from_object('user.config.DevelopmentConfig')

# Instantiate the database
db = SQLAlchemy(app)

# Instantiate the migration engine
migrate = Migrate(app, db)


# model
class Users(db.Model):
    """ Contains the user data for site users"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')