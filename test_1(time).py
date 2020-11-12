#implicit wait
#explicit wait
#sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
#driver.get("http://demo.guru99.com/test/newtours/reservation.php") #opinig url takes some time
#driver.implicitly_wait(10) #for all the elements in the page
#assert"Find a Flight: Mercury Tours: " in driver.title
driver.get("https://www.espanol.skyscanner.com/")
driver.implicitly_wait(5)
driver.minimize_window()
time.sleep(5)
fromm=driver.find_element_by_id("fsc-origin-search")
fromm.clear()
time.sleep(2)
fromm.send_keys('New york')
to=driver.find_element_by_xpath("//(input[@id='fsc-origin-search'][2])")
to.clear()
to.send_keys("egypt")
driver.find_element_by_xpath("//button[@type='submit']").click()


