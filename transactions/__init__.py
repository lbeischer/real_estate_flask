from flask import Flask, jsonify
from flask_restx import Resource, Api


# Instantiate the app
app = Flask(__name__)

api = Api(app)

# Set configuration
app.config.from_object('transactions.config.DevelopmentConfig')


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')