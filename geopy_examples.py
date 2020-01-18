#  calculate the distance between 2 city's
from geopy import distance


first_city = ("51.5074° N, 0.1278° W")
second_city = ("40.7128° N, 74.0060° W")
print("Distance between first and second city's (in km):")
print(distance.distance(first_city, second_city).km, " kms")


