import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_name(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        title=self.driver.title
        self.assertTrue(title=="Google","this not the same")
        self.assertFalse(title=="google123")

if __name__ == "__main":
    unittest.main()