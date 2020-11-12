import unittest
class SignUpTest(unittest.TestCase):
    def test_signupByEmail(self):
        print("this is sing login by email")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("this is sing by facebook")
        self.assertTrue(True)

    def test_signupBytwitter(self):
        print("this is sing by twitter")
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()