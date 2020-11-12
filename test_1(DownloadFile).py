from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
driver=webdriver.Chrome()
chromoption=Options()
#chromoption.add_experimental_option("pref","the locatian which u want to download")
#how u can upload file
action= ActionChains(driver)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element_by_id("textbox").send_keys("testing")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()