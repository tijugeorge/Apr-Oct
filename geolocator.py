import geopy

from geopy.geocoders import Nominatim
nom = Nominatim()
entry = input("Enter your address: ")
x, y = nom.geocode(entry)

print('Longitude =', y[0])
print('Latitude =', y[1])
