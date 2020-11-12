from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)
drp.select_by_value("Radio-1")
print(drp.options)   # this is for caputring the options
all_options=drp.options  #this is varible tosave the texts which i have in the box
for option in all_options:
    print(option.text)
