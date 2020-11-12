from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.grid.web").click()
driver.switch_to_default_content()  #it is for backing to the main page
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("EdgeDriver").click()
driver.switch_to_default_content()
driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("com.thoughtworks.selenium.condition").click()
driver.switch_to_default_content()