from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Chrome()
#how u can upload file
action= ActionChains(driver)
driver.get("http://testautomationpractice.blogspot.com/")
driver.switch_to_frame("frame-one1434677811")
driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("Capture1.PNG")

