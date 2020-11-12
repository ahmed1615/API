from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
#using javascript power
driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
user1=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user2=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
action.move_to_element(admin).perform() #1
action.move_to_element(user1).perform()   #2
action.move_to_element(user2).click().perform() #3
#1,2,3 togther
#action.move_to_element(admin).move_to_element(user1).move_to_element(user2).click().perform()

