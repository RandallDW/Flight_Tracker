import sys
import json
import time
import socket
import requests
import datetime
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

"""
def isValidAirport(airport_code):
	url = 'https://airport.api.aero/airport/'
	user_key = 'c64311a5a1ec2577df9bf80e65815324'
	request = '%s%s?user_key=%s'%(url, airport_code, user_key)
	data = requests.get(request)
	response_text = data.text
	text_str = response_text[9 : len(response_text)-1]
	text_dict = json.loads(text_str)
	error_message = text_dict.get('errorMessage')
	if error_message == None:
		return True
	else:
		return False


"""
	check if date is valid
"""
def isValidDate(date):
	try:
		valid_date = time.strptime(date, '%Y-%m-%d')
		today_date=str(datetime.date.today())
		if date < today_date:
			return False
		else:
			return True
	except ValueError:
		return False
								
"""
	Args:
		location_add(str): location address
	Returns:
		(location.latitude, location.longitude)(tuple):
				inserted location's coordinate
"""
def getLocationCoord(location_add):
	geolocator = Nominatim()
	location = geolocator.geocode(location_add)
	return (location.latitude, location.longitude)


class Server():
	def __init__(self, host):
		self.host = host
		self.port = 2000
		self.size = 8192	
		self.server = None
		self.connectToServer()
	def connectToServer(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.connect((self.host, self.port))
		print ('Connect to server..')
	def sendMsgToServer(self, payload_dict):
		payload_str = json.dumps(payload_dict)
		self.server.send(payload_str.encode('utf-8'))
		print('Sent message to server..')
	def recvAnsFromServer(self):
		print('Waiting answer from server..')
		self.data_byte = self.server.recv(self.size)
		self.data_str  = self.data_byte.decode("utf-8")
		self.data_dict = json.loads(self.data_str)
		self.weather   = self.data_dict.get("weather")
		self.flightInfo = self.data_dict.get("flight")

		if self.flightInfo == None:
			print('No flight available on this date..')
		else:
			# print out weather information
			print("Weather: ")

			weather_info_name = self.weather.get("name")

			weather_info_weather = self.weather.get("weather")
			weather_info_weather_main = weather_info_weather[0].get('main')
			weather_info_weather_desc = weather_info_weather[0].get('description')

			weather_info_main_dict = self.weather.get("main")
			weather_info_main_temp_kelvin = weather_info_main_dict.get("temp")
			weather_info_main_temp_fahrenheit = (weather_info_main_temp_kelvin - 273) * 9/5 + 32

			weather_info_main_temp_humidity = weather_info_main_dict.get("humidity")

			print("\t Name: \t\t\t" + weather_info_name)
			print("\t Main:	\t\t" + weather_info_weather_main)
			print("\t Description: \t\t" + weather_info_weather_desc)
			print("\t Temperature: \t\t" + str(weather_info_main_temp_fahrenheit) + " (Fahrenheit)")
			print("\t Humidity: \t\t" + str(weather_info_main_temp_humidity)) 


			print("Flight Info:")
			for i in range (0, len(self.flightInfo)):
				if self.flightInfo[i] != None:
					print("\t Solution %d" % (i + 1))
					print('\t' + self.flightInfo[i] + '\n')

			# to do, print out flight information


"""
	main function
	client.py "current location" "destination airport code" "date" 
"""
if __name__ == "__main__":
	if len(sys.argv) == 4:
		argvlist = [];
		for index in range(len(sys.argv)):
			argvlist.append(sys.argv[index])
		#print (argvlist)	
		destination = argvlist[2]
		date = argvlist [3]
		
		# check airport code
		if isValidAirport(destination) == False:
			print ('Invalid airport code...')
			sys.exit(-1)

		# check if date is valid
		if isValidDate(date) == False:
			print ('Invalid date (YYYY-MM-DD) or Day already got over')
			sys.exit(-1)

		location = getLocationCoord(argvlist[1])
		nearest = NearestAirport(location[0], location[1])
		nearest.findAirport()
		#print(nearest.airport_one)

		host = ''
		server = Server(host)

		#create question payload 
		payload = {
			'first':  nearest.airport_one_code, \
			'second': nearest.airport_two_code, \
			'third':  nearest.airport_three_code, \
			'destination' : destination, \
			'date':	  date
		}

		#send question payload to server
		server.sendMsgToServer(payload)

		#receive answer payload from server
		server.recvAnsFromServer()


	


	else:
		print('Invalid command line arguements...');
		sys.exit(-1);
