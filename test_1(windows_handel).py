from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@class='btn btn-info']").click()
print(driver.current_window_handle) #parent window
handels=driver.window_handles #returns all the handel vaslues of opened browser widows
for handel in handels:
    driver.switch_to_window(handel)
    print(driver.title)
driver.find_element_by_link_text("Projects").click()





