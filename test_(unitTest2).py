import unittest
from selenium import webdriver

class Searching(unittest.TestCase):
    def test_google(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        print("this is the title of my page: "+self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://bing.com")
        print("'this is the title of my page: '" + self.driver.title)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()