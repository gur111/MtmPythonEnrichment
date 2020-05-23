# spotify_example.py
from pprint import pprint
import requests
import json
import spotipy
import config

SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
# See authorization scopes descriptions in: https://developer.spotify.com/documentation/general/guides/scopes/
SCOPE = 'user-modify-playback-state user-read-email'

base_url = 'https://api.spotify.com/v1'

username = input("Username: ")

token = spotipy.util.prompt_for_user_token(username,
                                           SCOPE,
                                           client_id=config.SPOTIPY_CLIENT_ID,
                                           client_secret=config.SPOTIPY_CLIENT_SECRET,
                                           redirect_uri=SPOTIPY_REDIRECT_URI)

headers = {
    "Authorization": f"Bearer {token}"
}

# You can read about Spotify API in: https://developer.spotify.com/documentation/web-api/reference/

# Next
query = f"{base_url}/me/player/next"
response = requests.post(query, headers=headers)
print(response.reason)

# Previous Track
query = f"{base_url}/me/player/previous"
response = requests.post(query, headers=headers)
print(response.reason)

query = f"{base_url}/me/player/pause"
response = requests.put(query, headers=headers)
print(response.reason)

query = f"{base_url}/me/player/play"
response = requests.put(query, headers=headers)
print(response.reason)

position = '93000'
query = f"{base_url}/me/player/seek?position_ms={position}"
response = requests.put(query, headers=headers)
print(response.reason)

print('END')