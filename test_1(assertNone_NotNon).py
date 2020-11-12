import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_name(self):
        driver=webdriver.Chrome()
        #self.driver.get("https://www.google.com/")
        self.assertIsNone(driver)

if __name__ == "__main":
    unittest.main()
#not important
