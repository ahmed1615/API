from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
act =ActionChains (driver)

driver.get("https://www.facebook.com")
driver.maximize_window()
act.move_to_element(driver.find_element_by_name("birthday_day")).perform()
driver.find_element_by_xpath("//input[@class='inputtext _58mg _5dba _2ph-']").send_keys("ahmed")
act.send_keys(Keys.TAB).send_keys("mohamed").perform()
driver.find_element_by_name("lastname").send_keys("mohamed")
driver.find_element_by_name("reg_email__").send_keys(123457859)
driver.find_element_by_xpath("//input[@id='password_step_input']").send_keys("holahema")
day=Select(driver.find_element_by_id("day"))
driver.implicitly_wait(10)
day.select_by_value("20")
month=Select(driver.find_element_by_name("birthday_month"))
month.select_by_value("5")
year=Select(driver.find_element_by_id("year"))
year.select_by_value("1990")
driver.find_element_by_xpath("//input[@id='u_0_7']").click()
#act.move_to_element(driver.find_element_by_class_name("fb_logo img sp_YcHQbMgDbjJ sx_125510")).double_click(). perform()
act.context_click().perform()



time.sleep(5)
driver.close()



