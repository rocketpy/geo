# Get location by IP address
import requests

response = requests.get("https://geolocation-db.com/json/29.100.135.73&position=true").json()
