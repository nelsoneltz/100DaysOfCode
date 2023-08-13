from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

url = 'https://www.python.org/'

driver.get(url)

dates_ = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu time')
events_ = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu a')

dates = [date.get_attribute('datetime').split('T')[0] for date in dates_]
events = [event.text for event in events_]

# combined = [{event,dates[i]} for i,event in enumerate(events)]

event_dict = {}
for index in range(len(dates)):
    event_dict[index] = {
        "time":dates[index],
        "name":events[index],
    }

print(event_dict)

    
driver.quit()