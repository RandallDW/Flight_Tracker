import sys
import json
import time
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

"""
	main function
	client.py "current location" "destnation airport code" "date" 
"""
if __name__ == "__main__":
	if len(sys.argv) == 4:
		argvlist = [];
		for index in range(len(sys.argv)):
			argvlist.append(sys.argv[index])
		#print (argvlist)	
		destnation = argvlist[2]
		date = argvlist [3]
		
		# check airport code
		if isValidAirport(destnation) == False:
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

		#for i in range (0,2):


	else:
		print('Invalid command line arguements...');
		sys.exit(-1);


	

	#print (nearest.airport_one)
	#print ((nearest.airports_info[2]))

	#print (nearest.data.json())
	#print (nearest.data.headers['content-type'])
	
	#print(type(nearest.airports_info[0]))
	#print(type(json_type))
	#print (json_type)
	#print (str(location[0]))

	#data = requests.get('https://airport.api.aero/airport/nearest/30/-80?maxAirports=3&user_key=c64311a5a1ec2577df9bf80e65815324')
	#print (data.text)
		

