from flask_restful import Resource
from flask_restful import reqparse
from .inputfields import user_inputs
from .model import Users
from .smain import unauthorized, add_item


class UserRegister(Resource):
    """Register a new user.  URL: /auth/register/   Request method: POST"""

    def post(self):
        """ Add a user """
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True,
                            help="Please enter a username.")
        parser.add_argument("password", required=True,
                            help="Please enter a password.")
        parser.add_argument("email", required=True,
                            help="Please enter an Email.")
        args = parser.parse_args()
        username, password, email = args["username"], args["password"], args["email"]
        user = Users(username=username, password=password, email=email)
        return add_item(name="username",
                        item=user,
                        serializer=user_inputs,
                        is_user=True,
                        is_bucket=False,
                        is_item=False)


class Login(Resource):
    """  URL: /auth/login/ Request method: POST"""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True,
                            help="Please enter a username.")
        parser.add_argument("password", required=True,
                            help="Please enter a password.")
        args = parser.parse_args()
        username, password = args["username"], args["password"]

        if username and password:
            user = Users.query.filter_by(username=username).first()
        else:
            return {"message": "Error: Please enter a username and password."}
        if user and user.verify_password(password):
            token = user.generate_auth_token()
            return {"message": "Successfully logged in. Use the "
                    "token below to make requests.",
                    "token": token.decode("ascii")}
        else:
            return unauthorized("Error: Invalid username and/or password.")
