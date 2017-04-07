import json
from tests import TestBase


class TestAuth(TestBase):
    """ Test user registration and login """

    def test_user_register(self):
        """ Test user registration """
        self.user = {"username": "testuser2", "password": "testpassword",
                     "email": "test@test.com"}
        response = self.app.post("/auth/register/", data=self.user)
        if response.status_code == 201:
            self.assertEqual(response.status_code, 201)
            output = json.loads(response.data.decode('utf-8'))
            self.assertIn("Successfully added user", output["message"])
            self.assertIn(self.user["username"], response.data.decode('utf-8'))
        elif response.status_code == 200:
            output = json.loads(response.data.decode('utf-8'))
            print (output)
            self.assertIn('The username already exists.', output["error"])

    def test_login(self):
        """ Test user login """
        self.user = {"username": "joshua", "password": "joshua"}
        response = self.app.post("/auth/login/", data=self.user)
        self.assertEqual(response.status_code, 200)

        output = json.loads(response.data.decode('utf-8'))
        self.assertIn("Successfully logged in", output["message"])

    def test_invalid_credentials(self):
        """ Test that users cannot login with invalid credentials """
        self.user = {"username": "testuserother", "password": "testpassword"}
        response = self.app.post("/auth/login/", data=self.user)
        self.assertEqual(response.status_code, 403)

        output = json.loads(response.data.decode('utf-8'))
        self.assertIn("Error: Invalid username and/or password.",
                      output["message"])

        self.user = {"username": "testuser", "password": "invalid"}
        response = self.app.post("/auth/login/", data=self.user)
        self.assertEqual(response.status_code, 403)

        output = json.loads(response.data.decode('utf-8'))
        self.assertIn("Error: Invalid username and/or password.",
                      output["message"])
