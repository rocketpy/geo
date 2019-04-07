# https://pypi.org/project/geocoder/1.0.6/  check a new version !!! 
# pip install geocoder
import geocoder


g = geocoder.ip('me')

print('Latitude, Longtitude =', g.latlng)  # input to google , see result at map
print('ip Addres =', g.ip)
print('Geolocation information\n', g.geojson)
