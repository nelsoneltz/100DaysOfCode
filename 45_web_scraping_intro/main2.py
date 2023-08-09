import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage,'html.parser')

articles_texts = []
articles_links = []
articles = soup.find_all(name='a',rel='noreferrer')
for article in articles:
    text = article.getText()
    link = article.get('href')
    articles_texts.append(text)
    articles_links.append(link)

artices_scores = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

index = artices_scores.index(max(artices_scores))

print(articles_texts[index])
print(articles_links[index])
print(artices_scores[index])