import geopy

from geopy.geocoders import Nominatim
nom = Nominatim()
entry = input("Enter your address: ")
x, y = nom.geocode(entry)

print('Longitude =', y[0])
print('Latitude =', y[1])


'''
import geopy

from geopy.geocoders import Nominatim
nom = Nominatim()
entry = input("Enter your address: ")
#x, y = nom.geocode(entry)
#y = nom.geocode(entry)[1]
if nom.geocode(entry) is None:
	print("Not available")
else:
	print('Longitude =', nom.geocode(entry)[1][0])
	print('Latitude =', nom.geocode(entry)[1][1])
  
  '''
