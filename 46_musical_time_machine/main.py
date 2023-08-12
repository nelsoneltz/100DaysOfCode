import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from creds import client_id,client_secret



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri='https://open.spotify.com/collection/playlists',
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='neelister', 
    )
)
user_id = sp.current_user()["id"]

print(user_id)

# data = input('Enter the date(yyyy-mm-dd): ')

# response = requests.get(f'https://www.billboard.com/charts/hot-100/{data}')

# soup = BeautifulSoup(response.text,'html.parser')

# titles = soup.select(selector="li ul li h3")
# for index, title in enumerate(titles):
#     print(index+1,title.getText().strip())

