#assertEqual
#assertNotEquel
import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_name(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        title=self.driver.title
        self.assertEqual("Google",title,"webpage titleis not the same")
        self.assertNotEqual("Google123",title,"this is not the same")
if __name__ == "__main__":
    unittest.main()