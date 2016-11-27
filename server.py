#!/usr/bin/env python3
import json
import socket
import time
import requests
import _thread
import threading



"""
	airport_code (str)
"""
class Weather(object):
	def __init__(self, airport_code):
		self.airport_code = airport_code
		self.getAirportLoc()
		self.getWeather()
	def getAirportLoc(self):
		url = 'http://www.airport-data.com/api/ap_info.json?iata='
		request = url + self.airport_code
		data = requests.get(request)
		data_dict = json.loads(data.text)
		self.location = data_dict.get('location')
	def getWeather(self):
		url = 'http://api.openweathermap.org/data/2.5/weather?q='
		api_key = '&APPID=2463e27646249ffba883b72a3a592b36'
		request = url + self.location + api_key
		weather = requests.get(request)
		self.weather_text = weather.text
"""

"""
class flightInfo(object):
	def __init__(self, origin, destination, date):
		self.origin = origin
		self.destination = destination
		self.date = date
		self.getInfo()
	def getInfo(self):
		api_key = "AIzaSyCXUADGIAa5BkzzRUh8CbIWFFAzKYoTCd4"
		url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
		params = {
		  "request": {
		    "slice": [
		      {
		        "origin": self.origin,
		        "destination": self.destination,
		        "date": self.date
		      }
		    ],
		    "passengers": {
		      "adultCount": 1
		    },
		    "solutions": 1,
		    "refundable": False
		  }
		}
		response = requests.post(url, data=json.dumps(params), headers=headers)
		data = response.json()
		trips_text = data.get('trips')
		self.trips_data = trips_text.get('data')

		if self.trips_data.get('airport') == None:
			self.info = None
		else:
			self.info = self.trips_data 

"""
client thread, 
"""
class ClientThread(threading.Thread) :

	def __init__(self,clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		self.size = 1024
		#self.id = id
		print ("[+] New thread started ")

	def run(self): 
		question_byte = self.csocket.recv(self.size)
		question_str  = decode(question_byte, 'utf-8')
		print(question_str)
		"""
		count = 0
		while True:
			time.sleep(1)
			#print("Id is " + str(self.id))
			
			print(data)
			count += 1
			if (count == 5):
				self.csocket.close()
				self.csocket = None
				break
		"""
"""
LED thread, control 7 segement LED show coresponding client number
"""
class LEDThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.num = 0;
	def run(self):
		while 1:
			time.sleep(1)
			self.num = threading.active_count() - 2
			print(self.num)
		
			#print(Server.backlog)
			#if (Server.client[0] == None):
			#	print("NONE")
	#def count_1(self):

"""
server 
"""
class Server(object):
	def __init__(self, hostAdd):
		self.host = hostAdd
		self.backlog = 5
		self.client = None
		self.address = None
		self.openServer()
		self.startListen()

	def openServer(self):
		port = 2000
		size = 1024		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((self.host, port))

	def startListen(self):
		# LED thread
		led = LEDThread()
		led.start()

		error_msg = '<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>'
		while True:
			self.server.listen(self.backlog)
			print ('server started and listening..')
			self.client, self.address = self.server.accept()

			#pass client socket 
			newthread = ClientThread(self.client)
			newthread.start()
			



"""
	main function
"""
if __name__ == "__main__":

	a_lock = _thread.allocate_lock()
	host = ''
	server = Server(host)

	
	

	weather = Weather('ROA')
	print(weather.weather_text)