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

			# airline information
			flight_airlines = appendix_dict.get('airlines')
			airlines = [None] * len(flight_airlines)
			for i in range (0, len(flight_airlines)):
				name = flight_airlines[i].get('name')
				fs = flight_airlines[i].get('fs')
				phone_number = flight_airlines[i].get('phoneNumber')
				airlines[i] = [name, fs, phone_number]

			#flight equipment
			flight_equipment = appendix_dict.get('equipments')

			#flight status
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
			# flight id and number
			flight_id = flightStatuses_list[0].get('flightId')
			flight_num = self.carrier + ' ' + str(self.flight)
			
			# flight time	
			operational_time = flightStatuses_list[0].get('operationalTimes')

			# depart time
			published_departure_dict = operational_time.get('publishedDeparture')
			published_departure_local = published_departure_dict.get('dateLocal')
			published_departure_utc = published_departure_dict.get('dateUtc')

			# arrival time
			published_arrival_dict = operational_time.get('publishedArrival')
			published_arrival_local = published_arrival_dict.get('dateLocal')

			# flight duration
			flight_durations_dict = flightStatuses_list[0].get('flightDurations')
			scheduled_block_time = flight_durations_dict.get('scheduledBlockMinutes')

			# arrival terminal
			airport_resources_dict = flightStatuses_list[0].get('airportResources')
			arrival_terminal = airport_resources_dict.get('arrivalTerminal')

			new_flight_status_dict = {'flightId' : flight_id, \
									  'localDepartTime': published_departure_local, \
									  'UtcDepartTime':   published_departure_utc, \
									  'localArrivalTime': published_arrival_local, \
									  'flightDurations': scheduled_block_time, \
									  'arrivalTerminal': arrival_terminal, \
									  'flightStatus': flight_status \
									  }

			return [airlines, flight_equipment, new_flight_status_dict]