import requests
import json
from nearestAirport import NearestAirport
from geopy.geocoders import Nominatim

"""
__author__ = "Sheng Wei, Xuanyu Duan, Dong Wang, Sheila Zhu"
__copyright__ = "Copyright 2016, client"
__credits__ = ["Sheng Wei", "Xuanyu Duan", "Dong Wang",
					"Sheila Zhu"]
__version__ = "1.0.0"
"""



"""
	Args:
		location_add(str): location address
	Returns:
		(location.latitude, location.longitude)(tuple):
				insert location's latitude and longitude
"""
def getLocation(location_add):
	geolocator = Nominatim()
	location = geolocator.geocode(location_add)
	return (location.latitude, location.longitude)




if __name__ == "__main__":
	location = getLocation('Blacksburg, VA')
	nearest = NearestAirport(location[0], location[1])
	nearest.findAirport()
	#print (nearest.airport_one)
	#print ((nearest.airports_info[2]))

	#print (nearest.data.json())
	#print (nearest.data.headers['content-type'])
	
	#print(type(nearest.airports_info[0]))
	#print(type(json_type))
	#print (json_type)
	#print (str(location[0]))

	#data = requests.get('https://airport.api.aero/airport/nearest/30/-80?maxAirports=3&user_key=c64311a5a1ec2577df9bf80e65815324')
	#print (data.text)
		

