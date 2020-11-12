from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
#using javascript power
driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,1000)","") #pix scroll down
#how can u find element by scroll
#driver.execute_script("arguments[0].scrollIntoView();", element)
egypt=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[57]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView()",egypt)
#scroll down till end
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")





