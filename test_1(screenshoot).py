from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import openpyxl
import time
driver=webdriver.Chrome()
driver.get("http://demo.guru99.com/test/newtours/")
driver.save_screenshot("C:\screenshoot\homepage.png") #jpg or png
driver.get_screenshot_as_file("C:\screenshoot\homepage2.png") # the location then the name of the photo
