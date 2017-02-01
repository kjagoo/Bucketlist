from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from . import db, app

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# Create the Post Class
class Bucket(db.Model):
    """ Creates bucketlist  """

    __tablename__ = "bucket"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(
        "Users", backref=db.backref("users", lazy="dynamic"))

    items = db.relationship("BucketListItems",
                            backref=db.backref("items"), lazy="select")

    def __repr__(self):
        return "<Bucketlist: %r>" % self.title


class BucketListItems(db.Model):
    """ Creates bucketlist items """

    __tablename__ = "bucketlistitems"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
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
    email = db.Column(db.String(128), unique=True)

    @property
    def password(self):
        """Prevents access to password property"""
        raise AttributeError("password is not a readable attribute.")

    @password.setter
    def password(self, password):
        """Sets password to a hashed password"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Checks if password matches"""
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=20000):
        """Generating an authentication token that expires in 20 minutes"""
        serializer = Serializer(app.config["SECRET_KEY"],
                                expires_in=expiration)
        return serializer.dumps({"email": self.email,
                                 "username": self.username})

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(app.config["SECRET_KEY"])
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            """When token is valid but expired """
            return None
        except BadSignature:
            """When token is invalid """
            return None

        user = Users.query.filter_by(email=data["email"]).first()
        return user

    def __repr__(self):
        return "<User: %r>" % self.username


if __name__ == '__main__':
    manager.run()
