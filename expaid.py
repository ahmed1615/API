from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.expedia.com/")
driver.maximize_window()
act=ActionChains(driver)
driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
time.sleep(3)
driver.find_element_by_id("flight-origin-hp-flight").send_keys(" San Francisco")
driver.find_element_by_id("flight-destination-hp-flight").clear()
driver.find_element_by_id("flight-destination-hp-flight").send_keys("CAI")
time.sleep(3)
driver.find_element_by_id("flight-destination-hp-flight").send_keys(" cairo")
#driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("10/12/2020")
act.send_keys(Keys.ESCAPE).send_keys(Keys.TAB).send_keys("12/12/2020").perform()
#driver.find_element_by_id("flight-returning-hp-flight").send_keys("12/12/2020")

#act.send_keys(Keys.ENTER).perform()
