import unittest

from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'KiatuLonzo', pasword = '1234')

    def test_pasword_setter(self):
        self.assertTrue(self.new_user.pasword is not None)

    def test_no_access_pasword(self):
        with self.assertTrue(AttributeError):
            self.new_user.pasword

    def test_pasword_verification(self):
        self.assertTrue(self.new_user.verify_pasword('1234'))        

