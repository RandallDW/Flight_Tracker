import requests
import json

"""
__author__ = "Sheng Wei, Xuanyu Duan, Dong Wang, Sheila Zhu"
__copyright__ = "Copyright 2016, find 3 nearest airport"
__credits__ = ["Sheng Wei", "Xuanyu Duan", "Dong Wang",
					"Sheila Zhu"]
__version__ = "1.0.0"
"""


class NearestAirport(object):
	
	"""
	Attributes:
        latitude: location latitude
        longitude: location longitude
    """
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	"""
		- airport_one
			airport one information  
		- airport_two 
			airport two information
		- airport_three
			airport three information
	"""
	def findAirport(self):
		request_front = 'https://airport.api.aero/airport/nearest/'
		request_tail  = '?maxAirports=3&user_key=c64311a5a1ec2577df9bf80e65815324'
		request = request_front + str(self.latitude) + '/' + str(self.longitude) + request_tail
		self.data = requests.get(request)

		#convert received data to dict
		response_text = self.data.text
		text_str = response_text[9 : len(response_text)-1]
		text_dict = json.loads(text_str)
		# airports_info (list)
		self.airport_info = text_dict.get('airports')
		
		#airport_# (dict)
		self.airport_one = self.airport_info[0]
		self.airport_two = self.airport_info[1]
		self.airport_three = self.airport_info[2]
		

