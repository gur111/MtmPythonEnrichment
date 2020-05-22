# post_example.py
import json
import requests
from pprint import pprint

# Create user
response = requests.post('https://reqres.in/api/users',
                         data={'name': 'Monty',
                               'Job': 'The Knight Who Say "NI"'})
# Extract result
result = json.loads(response.text)
# Print in pretty format
print('Result:')
pprint(result)
pass
