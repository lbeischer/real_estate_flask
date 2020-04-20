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


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')

from user import models