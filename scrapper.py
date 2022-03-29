from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://getbootstrap.com/docs/5.0/getting-started/download/')
driver.implicitly_wait(3)
element = driver.find_element_by_css_selector('btn-bd-primary')
element.click()