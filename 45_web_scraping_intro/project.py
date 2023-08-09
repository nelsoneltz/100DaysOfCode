import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

webpage =response.text

soup = BeautifulSoup(webpage,'lxml')

titles = soup.find_all(name='h3',class_='jsx-1913936986')

for title in titles:
    print(title.getText())



