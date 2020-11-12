import unittest
class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("this is login by email")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("this is login by facebook")
        self.assertTrue(True)

    def test_loginBytwitter(self):
        print("this is login by twitter")
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()