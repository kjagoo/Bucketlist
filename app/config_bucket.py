import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Default configurations """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joshuakagenyi:#@joshua2016@localhost:5432/bucketlist'
    SECRET_KEY = "p9Bv<3Eid9%$i01"

class DevelopmentConfig(Config):
    """ Development configurations """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joshuakagenyi:#@joshua2016@localhost:5432/bucketlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "p9Bv<3Eid9%$i01"


class TestingConfig(Config):
    """ Test configurations """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joshuakagenyi:#@joshua2016@localhost:5432/bucketlist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "p9Bv<3Eid9%$i01"


class ProductionConfig(Config):
    """ Production configurations """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://joshuakagenyi:#@joshua2016@localhost:5432/bucketlist'

app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
