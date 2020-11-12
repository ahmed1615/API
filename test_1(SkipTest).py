import unittest
class AppTesting(unittest.TestCase):
    def test_search(self):
        print("this is search test")
    def test_advanced(self):
        print("this is advanced")
    @unittest.SkipTest
    def test_pre(self):
        print("pre")
    @unittest.skip("it  is skiped and will back")
    def test_post(self):
        print("this is post")

    def test_loginwithgmail(self):
        print("this is login with gmail")
    @unittest.skipIf(1==1,"numbers not it the same")
    def test_loginwithtwiter(self):
        print("this is login with twiter")
if __name__ == "__main__":
    unittest.main