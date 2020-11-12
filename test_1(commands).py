from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)
driver.get("http://demo.automationtesting.in/Register.html")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.refresh()

