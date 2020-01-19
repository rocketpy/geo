#  https://nominatim.org/release-docs/develop/api/Overview/    Nominatim API 

#  calculate the distance between 2 city's
from geopy import distance


first_city = ("51.5074° N, 0.1278° W")
second_city = ("40.7128° N, 74.0060° W")
print("Distance between first and second city's (in km):")
print(distance.distance(first_city, second_city).km, " kms")

#  search the street address, name from a given location information
from geopy.geocoders import Nominatim


geoloc = Nominatim(user_agent="geoapiExercises")
add_1 = "12345 Stanford Avenue, North Dakota"
print("Location address:", add_1)

loc = geolocator.geocode(add_1)
print("Street address, street name: ")
print(loc.address)

add_2 = "150 New York St, Redlands, CA 12345"
print("\nLocation address:", add_2)

loc = geolocator.geocode(add_2)
print("Street address, street name : ")
print(loc.address)

add_3 = "123 Pennsylvania Avenue NW"
print("\nLocation address:", add_3)

loc = geolocator.geocode(add_3)
print("Street address, street name: ")
print(loc.address)
