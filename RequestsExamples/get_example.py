# get_example.py

import requests

res = requests.get('https://w3schools.com/python/demopage.htm')
print(f'Status: {res.status_code}')
print(f'Coontent:\n{res.text}')
