import os
import env_variables


class Config(object):
    """ Default configurations """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['PRODUCTIONDB']
    SECRET_KEY = "p9Bv<3Eid9%$i01"


class DevelopmentConfig(Config):
    """ Development configurations """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['DEVELOPMENTDB']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "p9Bv<3Eid9%$i01"


class TestingConfig(Config):
    """ Test configurations """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TESTDB']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "p9Bv<3Eid9%$i01"


class ProductionConfig(Config):
    """ Production configurations """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['PRODUCTIONDB']


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
