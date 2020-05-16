# json_example.py

import json

with open("sample.json") as f:
    character = json.load(f)
    print(character['id'])
