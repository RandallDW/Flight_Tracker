import sys
import socket
import time
import _thread
import json
from ctypes import*
from struct import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWidget import*

class GUI(QObject):
	def __init__(self, host):
		super(GUI, self).__init__()
		# set up main widget
		self.widget = MainWidget()

		#Connecting to server
		self.host = host
		self.port = 2000
		self.size = 8192	
		self.server = None
		#self.connectToServer()
		self.widget.submit_button.clicked.connect(self.create_payload)
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
			print('No flight available..')
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
			self.flight = self.flightInfo[0]
			self.price = self.flightInfo[1]
			for i in range (0, len(self.flight)):
				if self.flight[i] != None:
					print("\t Solution# %d: Sale Price: %s" % (i + 1, self.price[i]) )
					print ("\t\tOrigin\tDestination\tDepartureTime\tArrivalTime")
					for j in range (0, len(self.flight[i])):
						print ("\t\t" + (self.flight[i])[j])

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
							
	def flight_searching(self):
		self.widget.submit_button.clicked(self.create_payload)

	@pyqtSlot()
	def create_payload(self):
		name = self.widget.name_line_edit.text()
		dest = self.widget.dest_line_edit.text()
		year = self.widget.year_line_edit.text()
		month = self.widget.month_line_edit.text()
		day = self.widget.day_line_edit.text()
		date = year + '-' + month + '-' + day
		print(name)
		print(dest)
		print(date)
		print(type(name))
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUI('localhost')
	sys.exit(app.exec_())
