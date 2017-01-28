from run import app
from app.model import Users, Bucket, BucketListItems
from app.config_bucket import app_config
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
import sys
import json
import nose


sys.path.append('../')
db = SQLAlchemy()


app.config.from_object(app_config["testing"])


class TestBase(TestCase):
    """ Base configurations for the tests """

    def create_app(self):
        """ Returns app """
        return app

    def setUp(self):
        """ Create test database and set up test client """
        self.app = app.test_client()
        
    def test_index(self):
        """ Test response to the index route """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data.decode('utf-8'))
        self.assertEqual(output, {"message": "Welcome to the Bucket List API."
                                  " You can get started by :"
                                  "1. Login "
                                  "2. Register a new user "})

    def tearDown(self):
        """ Destroy test database """
        db.session.remove()
        db.drop_all()



if __name__ == "__main__":
    nose.run()
