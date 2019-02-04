import os
from flask import Flask
from flask_restful import Api
from .config_bucket import app_config
from .db import db


def create_app(configuration):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(app_config[configuration])
    return app


app = create_app("development")
api = Api(app=app)
