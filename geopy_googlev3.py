from geopy import GoogleV3
# Docs:  https://geopy.readthedocs.io/en/stable/
# Get API Key: https://geopy.readthedocs.io/en/stable/#googlev3


place = "Some place name or city"
location = GoogleV3(api_key="HERE YOUR API KEY", domain="maps.google.ua").geocode(place)

print(location.address)
print(location.latitude, location.longitude)

# or 
from geopy import GoogleV3


new_place = "157 Baker Street, London"
location = GoogleV3().geocode(new_place)

print(location.address)
print(location.location)
