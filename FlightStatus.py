import sys, os
import socket
import time
import _thread
import json
import requests
from ctypes import*
from struct import*


class FlightStatus(object):
	def __init__(self, carrier, flight, date):
		self.carrier = carrier
		self.flight = flight
		date_list = date.split("-")
		self.year  = date_list[0]
		self.month = date_list[1]
		self.day = date_list[2]
	def getInfo(self):
		url = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/'
		api_id = '?appId=053776e6&appKey=8658e5310713410e629f3268cc383238&utc=false'
		request = url + self.carrier + '/' + self.flight + \
					'/dep/' + self.year + '/' + self.month + '/'+ self.day + api_id

		data = requests.get(request)
		data_str = data.text
		data_dict = json.loads(data_str)
		error = data_dict.get('error')
		if error != None:
			error_code = error.get('errorCode')
			error_message = error.get('errorMessage')
			error_dict = {
				'errorCode': error_code, \
				'errorMessage': error_message	\
			}

			return error_dict
		else:
			appendix_dict = data_dict.get('appendix')
			flightStatuses_list = data_dict.get('flightStatuses')
			flight_status_abbr = flightStatuses_list[0].get('status')
			
			flight_status_dict = {'S': 'Scheduled',	\
								  'A': 'Active',	\
								  'C': 'Canceled',	\
								  'D': 'Diverted',	\
								  'DN': 'Data source needed',	\
								  'L': 'Landed',	\
								  'NO': 'Not Operational', \
								  'R': 'Redirected',	\
								  'U': 'Unknown'
								  }
			flight_status = flight_status_dict.get(flight_status_abbr)
			print(flight_status)
			return flightStatuses_list[0]
