from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
#using javascript power
driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
capital=driver.find_element_by_xpath("//*[@id='box7']")
contury=driver.find_element_by_xpath("//*[@id='box106']")
action.drag_and_drop(capital,contury).perform() #take 2 paramiter source,target


