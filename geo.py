# https://pypi.org/project/geocoder/1.0.6/  check a new version !!! 
# pip install geocoder

#  https://pypi.org/project/googlemaps/  - Python Client for Google Maps Services
# https://pypi.org/project/geo-py/  - GeoPy
# http://geopandas.org/install.html  - GeoPandas 
# https://docs.djangoproject.com/en/2.2/ref/contrib/gis/install/  - GeoDjango

# https://pypi.org/project/Orange3-Geo/  -  Orange add-on for dealing with geography and geo-location.
# https://automating-gis-processes.github.io/2017/index.html  -   Automating GIS-processes 

import geocoder


g = geocoder.ip('me')

print('Latitude, Longtitude =', g.latlng)  # input to google , see result at map
print('ip Addres =', g.ip)
print('Geolocation information\n', g.geojson)

#  OR GEOCODER with Pandas and GEOPY

# geocoding addresses with pandas and geopy
# pip install geopy

import geopy
from geopy.geocoders import ArcGIS
import pandas as pd

nom=ArcGIS()

# check some address
n=nom.geocode("# input some address ")

df=pd.read_csv("file_name.csv")
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]

df["Coordinates"]=df["Address"].apply(nom.geocode)

df.Coordinates[0].latitude

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longtitude"]=df["Coordinates"].apply(lambda x: x.longtitude if x != None else None)



#  get the geolocation of an IP address , using  https://www.geody.com

import re
import sys
import urllib2
import BeautifulSoup


usage = "Run the script: ./geolocate.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup.BeautifulSoup(html_page)

# filter paragraph containing geolocation info
paragraph = soup('p')[3]

# remove html tags using regex
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print(geo_txt[32:].strip())


# some example for googlemaps module
"""
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='Add here  your key')

geocode_result = gmaps.geocode('address, city, country')

reverse_geocode_result = gmaps.reverse_geocode((25.123456, 95.123456))

now = datetime.now()
result = gmaps.directions("place","district, state", mode="transit", departure_time=now)
"""
