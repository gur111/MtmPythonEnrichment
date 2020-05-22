import requests
import json
import urllib


base_url = 'https://www.googleapis.com/customsearch/v1'
with open('GoogleSearch/creds.json') as f:
    api_key = json.load(f)['api_key']

search_term = urllib.parse.quote('Donald Trump')
search_engine = '014944568599467514515:kbz22k4qdru'
query = f'{base_url}?key={api_key}&q={search_term}&cx={search_engine}&count=100'

res = requests.get(query)

results = json.loads(res.text)
print(f'Total Results: {results["searchInformation"]["formattedTotalResults"]}',
      f'Search Time: {results["searchInformation"]["formattedSearchTime"]}', 
      f'First Results Title: {results["items"][0]["title"]}',
      f'First Results Link: {results["items"][0]["link"]}',
      f'First Results Snippet: {results["items"][0]["snippet"]}',
      sep='\n')

pass
