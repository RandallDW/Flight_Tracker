import requests
import json
from geopy.geocoders import Nominatim

"""
__author__ = "Sheng Wei, Xuanyu Duan, Dong Wang, Sheila Zhu"
__copyright__ = "Copyright 2016, client"
__credits__ = ["Sheng Wei", "Xuanyu Duan", "Dong Wang",
					"Sheila Zhu"]
__version__ = "1.0.0"
"""
class NearestAirport(object):
		def __init__(self, latitude, longitude):
			self.latitude = latitude
			self.longitude = longitude
		def findAirport(self):
			print (str(self.latitude) + " " + str(self.longitude))
			request_front = 'https://airport.api.aero/airport/nearest/'
			request_tail  = '?maxAirports=3&user_key=c64311a5a1ec2577df9bf80e65815324'
			request = request_front + str(self.latitude) + '/' + str(self.longitude) + request_tail
			self.data = requests.get(request)

			#convert received data to dict
			response_text = nearest.data.text
			text_str = response_text[9 : len(response_text)-1]
			text_dict = json.loads(text_str)
			# airports_info (list)
			self.airports_info = text_dict.get('airports')

			#airport_# (dict)
			self.airport_one = self.airports_info[0]
			self.airport_two = self.airports_info[1]
			self.airport_three = self.airport_info[2]




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

	#print (nearest.data.json())
	#print (nearest.data.headers['content-type'])
	
	#print(type(nearest.airports_info[0]))
	#print(type(json_type))
	#print (json_type)
	#print (str(location[0]))

	#data = requests.get('https://airport.api.aero/airport/nearest/30/-80?maxAirports=3&user_key=c64311a5a1ec2577df9bf80e65815324')
	#print (data.text)
		

