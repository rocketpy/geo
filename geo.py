# https://pypi.org/project/geocoder/1.0.6/  check a new version !!! 
# pip install geocoder
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
