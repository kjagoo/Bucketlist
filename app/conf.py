from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config_bucket import app_config

db = SQLAlchemy()


def create_app(configuration):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://joshuakagenyi:#@joshua2016@localhost:5432/bucketlist'
    app.config.from_object(app_config[configuration])
    db.init_app(app)

    return app

app = create_app("development")
api = Api(app=app, prefix="/")
