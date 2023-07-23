import requests
import os
from creds import api_key
from datetime import datetime

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

daily_params = {
    'function':'SYMBOL_SEARCH',
    'keywords':'Petrobras',
    'apikey':api_key

}

response = requests.get(STOCK_ENDPOINT,params=daily_params)
print(response.json())