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
class ClientThread(threading.Thread) :

	def __init__(self,clientsocket):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		#self.id = id
		print ("[+] New thread started ")

	def run(self): 
		count = 0
		while True:
			time.sleep(1)
			#print("Id is " + str(self.id))
			count += 1
			if (count == 5):
				self.csocket.close()
				self.csocket = None
				break
				
"""

"""
class LEDThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		while 1:
			time.sleep(1)
			print(threading.active_count() - 2)
		
			#print(Server.backlog)
			#if (Server.client[0] == None):
			#	print("NONE")
	#def count_1(self):

"""

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
	#airport_code = 'ROA'
	#data = requests.get( + airport_code)
	
	#print(type(data))
	
	#print (location)

#	weather = requests.get(Blacksburg)

#	print (weather.text)