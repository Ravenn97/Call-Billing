import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_restful import Api

from configs import get_config


db = MongoEngine()


def create_app():
    flask_app = Flask(__name__)
    CORS(flask_app, resources={r"/api/*": {"origins": "*"}})
    flask_app.config.update(get_config())
    flask_app.config
    db = MongoEngine()
    db.init_app(flask_app)
    flask_api = Api(flask_app)

    import apps.routers  
    apps.routers.routes(flask_api)

    return flask_app



