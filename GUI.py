import sys
import socket
import time
import json
import _thread
import requests
import datetime
from ctypes import*
from struct import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainWidget import*
from nearestAirport import NearestAirport
from geopy.geocoders import Nominatim


class GUI(QMainWindow):
	def __init__(self, host):
		super(GUI, self).__init__()
		# set up main widget
		self.widget = MainWidget()
		self.statusBar = QStatusBar()
		self.setStatusBar(self.statusBar)
		self.statusBar.showMessage("test")

		#Connecting to server
		self.host = host
		self.port = 2000
		self.size = 8192	
		self.server = None
		
		self.widget.submit_button.clicked.connect(self.create_flight_search_payload)
		self.widget.flight_submit_button.clicked.connect(self.create_flight_status_payload)

	'''
		connect to server
	'''
	def connectToServer(self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.connect((self.host, self.port))
		print ('Connect to server..')

	'''
		senf quest payload to server
	'''
	def sendMsgToServer(self, payload_dict):
		payload_str = json.dumps(payload_dict)
		self.server.send(payload_str.encode('utf-8'))
		print('Sent message to server..')

	'''
		Args:
			location_add(str): location address
		Returns:
			(location.latitude, location.longitude)(tuple): 
				inserted location's coordinate
	'''
	def getLocationCoord(self, location_add):
		geolocator = Nominatim()
		location = geolocator.geocode(location_add)
		return (location.latitude, location.longitude)
	

	'''
		check if date is valid
		Return:
			true is valid, otherwise is invalid
	'''
	def isValidDate(self, date):
		try:
			valid_date = time.strptime(date, '%Y-%m-%d')
			today_date=str(datetime.date.today())
			if date < today_date:
				return False
			else:
				return True 
		except ValueError:
			return False

	'''
		check if airport code is valid
		Return:
			true is valid, otherwise is invalid
	'''
	def isValidAirport(self, airport_code):
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

	'''
		recv answer payload from server, deserialize it
	'''
	def recvAnsFromServerFlightInfo(self):
		print('Waiting answer from server..')
		self.data_byte = self.server.recv(self.size)
		self.data_str  = self.data_byte.decode("utf-8")
		self.data_dict = json.loads(self.data_str)
		self.weather   = self.data_dict.get("weather")
		self.flightInfo = self.data_dict.get("flight")

		if self.flightInfo == None:
			self.widget.enter_no_flight()
			print('No flight available..')
		else:
			# print out weather information
			

			weather_info_name = self.weather.get("name")

			weather_info_weather = self.weather.get("weather")
			weather_info_weather_main = weather_info_weather[0].get('main')
			weather_info_weather_desc = weather_info_weather[0].get('description')

			weather_info_main_dict = self.weather.get("main")
			weather_info_main_temp_kelvin = weather_info_main_dict.get("temp")
			weather_info_main_temp_fahrenheit = (weather_info_main_temp_kelvin - 273) * 9/5 + 32

			weather_info_main_temp_humidity = weather_info_main_dict.get("humidity")

			weather_str = ("\t Name: \t\t\t" + weather_info_name + '\n') + \
							("\t Main:	\t\t" + weather_info_weather_main + '\n') + \
							 ("\t Description: \t\t" + weather_info_weather_desc + '\n') + \
							  ("\t Temperature: \t\t" + str(weather_info_main_temp_fahrenheit) + \
							  	" (Fahrenheit)\n") + ("\t Humidity: \t\t\t" + str(weather_info_main_temp_humidity) + '\n')

			self.widget.set_weather_info(weather_str)
			self.widget.set_flight_info(self.flightInfo[0], self.flightInfo[1])

	
	def recvAnsFromServer_flight_status(self):
		print('Waiting answer from server..')
		self.data_byte = self.server.recv(self.size)
		self.data_str  = self.data_byte.decode("utf-8")
		self.data_dict = json.loads(self.data_str)
	'''
		create flight searching payload, and send it to server
	'''
	@pyqtSlot()
	def create_flight_search_payload(self):
		name = self.widget.name_line_edit.text()
		destination = self.widget.dest_line_edit.text()
		year = self.widget.year_line_edit.text()
		month = self.widget.month_line_edit.text()
		day = self.widget.day_line_edit.text()
		date = year + '-' + month + '-' + day
		if name == '':
			self.widget.enter_address()
		elif destination == '':
			self.widget.enter_airport_code()
		elif year == '' or month == '' or day == '':
			self.widget.enter_date()
		else:
			
			check_airport = self.isValidAirport(destination)
			check_date = self.isValidDate(date)

			if check_airport == False:
				self.widget.show_invalid_airport_msg()
			elif check_date == False:
				self.widget.show_invalid_date_msg()
			else:
				self.widget.reset_error_msg_label()
				self.connectToServer()
				location = self.getLocationCoord(name)
				nearest = NearestAirport(location[0], location[1])
				nearest.findAirport()

				payload = {
					'first':  nearest.airport_one_code, \
					'second': nearest.airport_two_code, \
					'third':  nearest.airport_three_code, \
					'destination' : destination, \
					'date':	  date, \
					'Flight Status': False
				}
				print(payload)
				#send question payload to server
				self.sendMsgToServer(payload)
				self.recvAnsFromServerFlightInfo()
	'''
	create flight status quest payload, and send it to server
	'''			
	@pyqtSlot()
	def create_flight_status_payload(self):
		carrier = self.widget.carrier_line_edit.text()
		flight_num = self.widget.flight_line_edit.text()
		year = self.widget.flight_year_line_edit.text()
		month = self.widget.flight_month_line_edit.text()
		day = self.widget.flight_day_line_edit.text()
		date = year + '-' + month + '-' + day
		
		if carrier == '':
			self.widget.enter_carrier()
		elif flight_num == '':
			self.widget.enter_flight_num()
		elif year == '' or month == '' or day == '':
			self.widget.enter_date_flight_status()
		else:
			
			check_date = self.isValidDate(date)
			if check_date == False:
				self.widget.show_invalid_flight_date_msg()
			else:
				self.widget.reset_flight_error_msg_label()
				self.connectToServer()
				payload = {
					'carrier':	carrier, 	\
					'flight': flight_num, 	\
					'date':	date
				}
				self.sendMsgToServer(payload)



		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = GUI('localhost')
	sys.exit(app.exec_())
