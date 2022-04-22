# Get location by IP address
import requests

response = requests.get("https://geolocation-db.com/json/29.100.135.73&position=true").json()


import json
import urllib.request

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    result = json.loads(url.read().decode())
    print(result)
