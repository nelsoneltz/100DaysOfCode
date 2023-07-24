import requests
from creds import api_key,news_api_key
from datetime import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

daily_params = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':api_key

}

response = requests.get(STOCK_ENDPOINT,params=daily_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
last_data = data_list[0]
last_closing_price = last_data['4. close']

day_before = data_list[1]
day_before_closing_price = day_before['4. close']

diff = abs(float(last_closing_price) - float(day_before_closing_price))

diff_percent = (diff / float(last_closing_price)) * 100

if diff_percent > 1:
    news_params = {
        "apiKey":news_api_key,
        "qInTitle":COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()['articles']
    first_three = articles[:3]

    formatted_headlines = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in first_three]

    for headline in formatted_headlines:
        print(headline)

