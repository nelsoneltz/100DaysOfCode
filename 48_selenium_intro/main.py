from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

url = 'https://www.amazon.com.br/dp/B09KMKD84X/?coliid=I2IDKEIYG91XYS&colid=1C5C8YG9P9SBP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it'

driver.get(url)

elem = driver.find_element(By.CLASS_NAME,'a-price-whole').text

print(elem)

# driver.close() # close tab
driver.quit() # quit browser

