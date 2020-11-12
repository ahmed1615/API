from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
texts=driver.find_elements_by_class_name("text_field")
print(len(texts))  # for knowing how much??
driver.find_element_by_id("RESULT_TextField-1").send_keys("ahmed")
driver.find_element_by_id("RESULT_TextField-2").send_keys("mohamed")
