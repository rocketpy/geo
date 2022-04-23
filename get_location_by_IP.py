# Get location by IP address
import requests

response = requests.get("https://geolocation-db.com/json/29.100.135.73&position=true").json()


#  Use the service of https://geolocation-db.com, supported: IPv4 and IPv6
import json
import urllib.request

with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    result = json.loads(url.read().decode())
    print(result)


# Using JSON
import json
import urllib.request


with urllib.request.urlopen("https://geolocation-db.com/jsonp/8.8.8.8") as url:
    data = url.read().decode()
    result = data.split("(")[1].strip(")")
    print(result)

