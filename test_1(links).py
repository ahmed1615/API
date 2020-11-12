from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://demo.guru99.com/test/newtours/")
links=driver.find_elements(By.TAG_NAME,"a")
print("number of liks: ",len(links))
for link in links:
    print(link.text)
driver.find_element_by_link_text("REGISTER").click()
