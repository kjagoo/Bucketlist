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
        db.create_all()
        user = Users(username="joshua", password="joshua")
        bucketlist1 = Bucket(title="Knowledge Goals",
                             description="Things to learn",
                             created_by=1)
        bucketlist2 = Bucket(title="Adventures",
                             description="Awesome adventures to go on",
                             created_by=1)
        item1 = BucketListItems(title="Learn to Cook",
                                description="Cook at least 10 different meals",
                                created_by=1,
                                bucket_id=1)
        item2 = BucketListItems(title="Swim with Dolphins",
                                description="Go swimming with dolphins in Watamu",
                                created_by=1,
                                bucket_id=1)

        db.session.add(user)
        db.session.add(bucketlist1)
        db.session.add(bucketlist2)
        db.session.add(item1)
        db.session.add(item2)
        db.session.commit()

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
