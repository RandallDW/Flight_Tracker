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


class ClientThread(threading.Thread):

	def __init__(self,clientsocket,id):
		threading.Thread.__init__(self)
		self.csocket = clientsocket
		self.id = id
		print ("[+] New thread started ")

	def run(self): 
		count = 0
		while True:
			time.sleep(1)
			print("Id is " + str(self.id))
			count += 1
			if (count == 20):
				break


class LEDThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	def run(self):
		while 1:
			time.sleep(1)
			print(threading.active_count() - 2)
	def increment(self):
		self.num += 1
	def decrement(self):
		self.num -= 1



class Server(object):
	def __init__(self, hostAdd):
		self.host = hostAdd
		self.backlog = 5
		self.clientIndex = 0
		self.openServer()
		#self.startListen()
	def openServer(self):
		port = 2000
		size = 1024
		self.client = [None] * self.backlog
		self.address = [None] * self.backlog
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((self.host, port))

	def startListen(self):
		# LED thread
		led = LEDThread(self.clientIndex)
		led.start()

		while True:
			self.server.listen(self.backlog)
			print ('server started and listening ')
			self.client[self.clientIndex], self.address[self.clientIndex] = self.server.accept()

			#pass client socket 
			newthread = ClientThread(self.client[self.clientIndex], self.clientIndex)
			newthread.start()
			self.clientIndex += 1
			led.increment()


#class Flight(object):
#	def __init__(self, origin, destination, date):

"""
main function
"""
if __name__ == "__main__":

	a_lock = _thread.allocate_lock()
	host = ''
	server = Server(host)
	server.startListen()

	
	

	weather = Weather('ROA')
	print(weather.weather_text)
	#airport_code = 'ROA'
	#data = requests.get( + airport_code)
	
	#print(type(data))
	
	#print (location)

#	weather = requests.get(Blacksburg)

#	print (weather.text)