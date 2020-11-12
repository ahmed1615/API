from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
#using javascript power
driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element_by_xpath("//*[@class='context-menu-one btn btn-neutral']")
action.context_click(button).perform()