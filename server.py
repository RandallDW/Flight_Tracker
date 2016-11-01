#!/usr/bin/env python3
import requests
import json

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
		print(self.weather_text)
"""
main function
"""
if __name__ == "__main__":
	weather = Weather('ROA')
	#airport_code = 'ROA'
	#data = requests.get( + airport_code)
	
	#print(type(data))
	
	#print (location)

#	weather = requests.get(Blacksburg)

#	print (weather.text)