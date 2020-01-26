#  https://pypi.org/project/geocoder/

#  is a typical example of retrieving a Lat & Lng from Google using Python
import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
r = requests.get(url, params=params)
results = r.json()['results']
location = results[0]['geometry']['location']
location['lat'], location['lng']

#  same task but using geocoder :
import geocoder

result = geocoder.google('Mountain View, CA')
result.latlng

#  multiple queries ( batch )
import geocoder

result = geocoder.mapquest(['Mountain View, CA', 'Boulder, Co'], method='batch')
for res in result:
    print(result.address, result.latlng)
    
#  many methods 
import geocoder

result = geocoder.google('Mountain View, CA')
result.geojson
result.json
result.wkt
result.osm
