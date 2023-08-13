from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com.br")

driver.close()
driver.quit()