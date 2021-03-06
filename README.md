# Flight Tracker
## Concept of Operations

Air travel has become the long-distance transportation method of choice in the modern era. Travelers around the world elect to use air transportation for its convenience, speed, capability to reach remote destinations, and (often) smooth ride. However, there are often many obstacles barring air travel from reaching its optimal convenience, reliability, and customer satisfaction, including flight delays, airport location and accessibility, and flight traffic control. For example, a traveler unfamiliar with the area would have difficulty finding the best method to the nearest airport in a time-efficient manner if he or she needed to board an airplane as soon as possible.
Our proposed final project is an implementation of a Flight Informer system that conveniently provides the addresses and accessibility of the nearest airports, their flight information, and the weather forecasts of the flight destination based on the arrival times of the flights. It combines the latest in airport and flight information to serve as a flight management assistant for all travelers, whether casual or business. Users can plan an array of flights as needed in the application, including last-minute reservations based on the user’s current locational data. The user will be notified of any delays, cancellations, or changes to the flight information, and allow the user to plan accordingly, whether to reschedule the flight, or simply plan around it. Our application hopes to integrate locational, airport, and flight seeking into a go-to tool for unplanned flights.

## Setup Environment

This project is running under python 3. 

* Server <br />
Raspeberry Pi with a 7-Segement LED is used to monitor how many clients connect to the server simultaneously. 
I provided 2 version of server here, and made server is able to run without Pi.
	- with Raspberry Pi
		* need to install GPIO package 
	- without Raspberry Pi
* Client
	- need install PyQt5 package
* NOTE:
	- Project default socket port: 8080 
	- Project server IP address: need to manually change to your current server machine's IP address
	

## System Diagram & GUI Screen Shot

### System Diagram (Using two PI as examples)
![alt text](https://github.com/RandallDW/Flight_Tracker/blob/master/diagram.png "system diagram")
### Screen Shot
![alt text](https://github.com/RandallDW/Flight_Tracker/blob/master/Screen_Shot.png "screen shot")

## APIs

	- OpenWeatherMap
	- QPX
	- SITA FlightInfo




