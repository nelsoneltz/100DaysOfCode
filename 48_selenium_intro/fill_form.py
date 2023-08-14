from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

# url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'

url = 'http://secure-retreat-92358.herokuapp.com/'

driver.get(url)

# article_count = driver.find_element(By.CSS_SELECTOR,".hp-statistieken p b")
# print(article_count.text.replace(' ',''))

# portais = driver.find_element(By.LINK_TEXT,'Portais')
# portais.click()

# search = driver.find_element(By.NAME,'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME,'fName')
fname.send_keys('Testing')

lname = driver.find_element(By.NAME,'lName')
lname.send_keys('Testing')

email = driver.find_element(By.NAME,'email')
email.send_keys('email@email.com')

sign_up_button = driver.find_element(By.CSS_SELECTOR,'button')
sign_up_button.click()


while True:
    pass

driver.quit()