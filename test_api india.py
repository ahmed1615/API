from selenium import webdriver
driver=webdriver.Chrome()
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
act=ActionChains(driver)
driver.get("http://www.facebook.com")
driver.find_element_by_name("email").send_keys("testing is love")
#act.send_keys(Keys.CONTROL).send_keys("a").perform()
act.send_keys(Keys.CONTROL).send_key("b").perform()
act.send_keys(Keys.TAB).perform()

#act.send_keys(Keys.CONTROL).send_keys("x").perform()
#screenshoot
