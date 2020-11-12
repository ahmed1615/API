from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import openpyxl
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
cookies=driver.get_cookies()
print(len(cookies))  #number of cookies
print(cookies)   #print all cookies pairs
#how u can add a new cookie in the browser
cookie={"name":"mycookie","value":"125263654"}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))  #number of cookies after adding a new cookie
print(cookies)
#how u can delete the cookie
driver.delete_cookie("mycookie")
cookies=driver.get_cookies()
print(len(cookies))  #number of cookies after deleting one of them
print(cookies)
#for deleting all the cookies
driver.delete_all_cookies()  #its for deleting all of them
cookies=driver.get_cookies()
print(len(cookies))  #number of cookies
print(cookies)
