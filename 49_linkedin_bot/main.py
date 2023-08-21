from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime



driver = webdriver.Chrome(executable_path='./chromedriver.exe')

url = "https://www.linkedin.com/jobs/search/?currentJobId=3684447197&f_LF=f_AL&geoId=102199904&keywords=python%20developer&location=Calgary%2C%20Alberta%2C%20Canada&refresh=true"

driver.get(url)
