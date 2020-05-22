# spotify_example.py
from pprint import pprint
import requests
import json
import base64

AUTH_URL = 'https://accounts.spotify.com/api/token'

base_url = 'https://api.spotify.com/v1'

# Get Token from creds.json
with open('Spotify/creds.json') as f:
    spotify_token = json.load(f)['token']

headers = {
    "Cont6ent-Type": "application/json",
    "Authorization": f"Bearer {spotify_token}"
}

# Next
query = f"{base_url}/me/player/next"
response = requests.post(query, headers=headers)
pprint(json.loads(response.text))
pass

# Beginning
query = f"{base_url}/me/player/previous"
response = requests.post(query, headers=headers)
pprint(json.loads(response.text))
pass

# Previous Track
query = f"{base_url}/me/player/previous"
response = requests.post(query, headers=headers)
response = requests.post(query, headers=headers)
pprint(json.loads(response.text))
pass

query = f"{base_url}/me/player/pause"
response = requests.put(query, headers=headers)
pprint(json.loads(response.text))
pass

query = f"{base_url}/me/player/play"
response = requests.put(query, headers=headers)
pprint(json.loads(response.text))
pass


pprint(json.loads(response.text))
pass
