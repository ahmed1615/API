from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://ask.fm/signup")
driver.find_element_by_class_name("inputForm").send_keys("hamoza010@yahoo.com")
driver.find_element_by_class_name("inputForm").clear()
driver.find_element_by_id("user_email").send_keys("lololololo")
driver.find_element_by_xpath("//input[@type='email']").clear()
driver.find_element_by_name("user[email]").send_keys("abcd123")
obj=Select(driver.find_element_by_id("date_day"))
obj.select_by_visible_text("15")
mes=Select(driver.find_element_by_id("date_month"))
mes.select_by_visible_text("May")
year=Select(driver.find_element_by_id("date_year"))
year.select_by_value("1999")
driver.find_element_by_xpath("//input[@type='submit']").click()
obj.deselect_by_value()

time.sleep(5)
driver.close()