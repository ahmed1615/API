from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

action= ActionChains(driver)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window() #for maximize the screen
title=driver.title #to get the title of the page
assert "Register" in driver.title  #for assertion some wordes in the title
print(title)
url=driver.current_url #to get the current url of the page
print(url)
source=driver.page_source #to get all the codes of the page in HTML
print(source)

driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("ahmed")
driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("mohamed")
driver.find_element_by_xpath("//textarea[@rows='3']").send_keys("it is for testing")
driver.find_element_by_xpath("//input[@type='email']").send_keys("ahmedmohamed@gmail.com")
driver.find_element_by_xpath("//input[@type='tel']").send_keys("1170268675")
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_id("checkbox1").click()
driver.find_element_by_id("checkbox3").click()
driver.find_element_by_id("msdd").click()
driver.find_element_by_xpath("//a[contains(text(),'Catalan')]").click()
driver.find_element_by_xpath("//input[@placeholder='First Name']").click()
#driver.find_element_by_id("Skills").click()
skill=Select(driver.find_element_by_id("Skills"))
skill.select_by_value("Analytics")
pais=Select(driver.find_element_by_id("countries"))
pais.select_by_value("Afghanistan")
driver.find_element_by_css_selector("#basicBootstrapForm > div:nth-child(10) > div > span > span.selection > span").click()
country=driver.find_element_by_class_name("select2-search__field")
country.click()
country.send_keys("ind")
action.send_keys(Keys.ENTER).perform()
year=Select(driver.find_element_by_id("yearbox"))
year.select_by_value("1917")
month=Select(driver.find_element_by_xpath("//select[@placeholder='Month']"))
month.select_by_value("May")
day=Select(driver.find_element_by_id("daybox"))
day.select_by_value("2")
driver.find_element_by_id("firstpassword").send_keys("ahmed16")
driver.find_element_by_id("secondpassword").send_keys("khfjhdjgf")



time.sleep(5)
driver.close()











