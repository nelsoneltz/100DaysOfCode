from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

url = 'https://orteil.dashnet.org/experiments/cookie/'

driver.get(url)

cookie = driver.find_element(By.ID,'cookie')
timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    cookie.click()
    if time.time() > timeout:
        items = driver.find_elements(By.CSS_SELECTOR,'#store div')
        items_ids = [item.get_attribute("id") for item in items]



        prices = driver.find_elements(By.CSS_SELECTOR,'#store b')
        item_prices = []
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split('-')[1].strip().replace(',',''))
                item_prices.append(cost)

        cookie_upgrades = {}
        for i in range(len(item_prices)):
            cookie_upgrades[item_prices[i]] = items_ids[i]

        money = driver.find_element(By.ID,'money').text
        if "," in money:
            money = money.replace(",","")
        cookie_count = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID,to_purchase_id).click()

        timeout = time.time() + 5           
    # if time.time() > five_min:
    #         cookie_per_s = driver.find_element_by_id("cps").text
    #         print(cookie_per_s)
    #         break
driver.quit()