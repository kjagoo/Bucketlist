import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DEVELOPMENTDB']

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


class Bucket(db.Model):
    """ Creates bucketlist  """

    __tablename__ = "bucket"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("Users", backref=db.backref("users",
                                                       lazy="dynamic"))

    items = db.relationship("BucketListItems",
                            backref=db.backref("items"), lazy="select")

    def __repr__(self):
        return "<Bucketlist: %r>" % self.title


class BucketListItems(db.Model):
    """ Creates bucketlist items """

    __tablename__ = "bucketlistitems"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2), unique=True)
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime,
                              onupdate=datetime.utcnow)

    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))

    bucket_id = db.Column(db.Integer, db.ForeignKey("bucket.id"))

    def __repr__(self):
        return "<Bucketlist Item: %r>" % self.title


class Users(db.Model):
    """   Users   """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128))


if __name__ == '__main__':
    manager.run()
