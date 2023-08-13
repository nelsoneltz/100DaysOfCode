import requests
from bs4 import BeautifulSoup

TARGET_VALUE = 2300.00

url = 'https://www.amazon.com.br/dp/B09KMKD84X/?coliid=I2IDKEIYG91XYS&colid=1C5C8YG9P9SBP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url, headers=header)

webpage_text = response.text

soup = BeautifulSoup(webpage_text,'html.parser')

price = float(soup.find(class_="a-offscreen").getText().replace('R$','').replace('.','').replace(',','.'))

if price < TARGET_VALUE:
    print("Price below target. You sould buy it.")
else:
    print("Not yet. More luck next time.")