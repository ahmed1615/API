#setup ,teardown
import unittest
from selenium import webdriver
def setUpmodule():
    print("setupmodule")
def tearDownModule():
    print("teardown")

class Apptesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("this is setupclass")

    @classmethod
    def tearDownClass(cls):   #it will hapen for once
        print("this is tearclass")
    @classmethod
    def setUp(self):      #it will happen in all the test
        print("this is login test")



    @classmethod
    def tearDown(self):     #it will happen in all the test after donig setup
        print("this is logout")


    def test_search(self):
        print("this is for searching test")


    def test_advanced(self):
        print("this is advanced search test")

    def test_prepidrecharge(self):
        print("this is prepaid recharge test")


    def test_postpaidrecharge(self):
        print("this is post rpaidrecharge test")



if __name__ == "__main__":
    unittest.main()
