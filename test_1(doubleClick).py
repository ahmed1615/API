from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
#using javascript power
driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
field1=driver.find_element_by_id("field1")
action.double_click(field1)

