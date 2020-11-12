#is_display()
#is_enabled()
#is_selected()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://demo.guru99.com/test/newtours/")
name=driver.find_element_by_name("userName")
print(name.is_enabled()) #true or false
print(name.is_displayed()) #true or false
driver.find_element_by_link_text("Flights").click()
economy=driver.find_element_by_xpath("//input[@value='Coach']")
print(economy.is_selected())
first=driver.find_element_by_xpath("//input[@value='First']")
print(first.is_selected())

