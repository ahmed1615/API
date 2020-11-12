
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
time.sleep(5)
#driver.switch_to_alert().accept() #it will closes alert windows using button
driver.switch_to_alert().dismiss()  #it will cancel it
driver.switch_to_alert().send_keys() #it will send some words for the alert