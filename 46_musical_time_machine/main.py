import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from creds import client_id,client_secret

data = input('Enter the date(yyyy-mm-dd): ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{data}')

soup = BeautifulSoup(response.text,'html.parser')

song_names_ = soup.select(selector="li ul li h3")

song_names = [song.getText().strip() for song in song_names_]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id,
                              client_secret=client_secret,
                              redirect_uri='http://example.com',
                              scope="playlist-modify-private",
                              show_dialog=True,
                              cache_path="token.txt",
                              username="neelister",))

user_id = sp.current_user()["id"]

print(user_id)



song_uris = []
year = data.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(song)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{data} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)