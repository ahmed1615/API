from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://ask.fm/")
driver.find_element_by_class_name("btn-primary-wide").click()
driver.find_element_by_xpath("//input[@type='email']").send_keys("hamoza2010@yahoo.com")
driver.find_element_by_id("user_email").clear()


