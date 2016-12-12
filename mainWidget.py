import sys, os
import socket
import time
import _thread
import threading
import json
from ctypes import*
from struct import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta

class MainWidget(QTabWidget):
	submit = pyqtSignal()
	def __init__(self, parent = None):
		super(MainWidget, self).__init__(parent) 
		self.setGeometry(100,100,1200,1100)
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()
		self.thread = None

		self.addTab(self.tab1, "Search")
		self.addTab(self.tab2, "Destination Weather")
		self.addTab(self.tab3, "Solutions")
		self.addTab(self.tab4, "Flight Status")
		self.tab1UI()
		self.tab2UI()		
		self.tab3UI()
		self.tab4UI()
		self.setWindowTitle("Network Application Design")
		self.show()


	def tab1UI(self):
		layout = QFormLayout()
		box_line_1 = QGridLayout()
		box_line_2 = QGridLayout()


		# first layout box
		name = QLabel("Current Address:")
		dest_code = QLabel("Destination Airport Code:")
		self.name_line_edit = QLineEdit()
		self.dest_line_edit = QLineEdit()
		
		box_line_1.addWidget(name, 0, 0)
		box_line_1.addWidget(dest_code, 1, 0)
		box_line_1.addWidget(self.name_line_edit, 0, 1)
		box_line_1.addWidget(self.dest_line_edit, 1, 1)
		box_line_1.addWidget(QLabel("\t\t\t\t\t\t\t\t"), 0, 2)
		
		# seconde layout box
		date = QLabel("Date:")
		self.year_line_edit = QLineEdit()
		self.year_line_edit.setPlaceholderText("YYYY")

		self.month_line_edit = QLineEdit()
		self.month_line_edit.setPlaceholderText("MM")

		self.day_line_edit = QLineEdit()
		self.day_line_edit.setPlaceholderText("DD")

		box_line_2.addWidget(date, 0, 0)
		box_line_2.addWidget(QLabel("\t\t"), 0, 1)
		box_line_2.addWidget(self.year_line_edit, 0, 2)
		box_line_2.addWidget(QLabel("-"), 0, 3)
		box_line_2.addWidget(self.month_line_edit, 0, 4)
		box_line_2.addWidget(QLabel("-"), 0, 5)
		box_line_2.addWidget(self.day_line_edit, 0, 6)
		
		self.submit_button = QPushButton()
		self.submit_button.setText("Submit")
		box_line_2.addWidget(self.submit_button, 1, 6)
		

		# self.invalid label
		font = QFont()
		font.setPointSize(20)
		self.err_msg = QLabel('')
		self.err_msg.setFont(font)


		# add layout
		layout.addRow(box_line_1)
		layout.addRow(box_line_2)
		layout.addRow(self.err_msg)
		
		pic = QLabel(self.tab1)
		pic.setGeometry(0, 0, 1200, 900)
		#use full ABSOLUTE path to the image, not relative
		pic.setPixmap(QPixmap(os.getcwd() + "/flight.jpg"))
	
		self.setTabText(0,"Flight searching")
		self.tab1.setLayout(layout)

	def tab2UI(self):
		layout = QGridLayout()
		
		weather_label = QLabel("Destination Weather")
		weather_font = QFont()
		weather_font.setBold(True)
		weather_label.setFont(weather_font)
		
		self.weather_text_edit  = QTextEdit()
		self.weather_text_edit.setReadOnly(True)
		
		layout.addWidget(weather_label, 0, 0)
		layout.addWidget(self.weather_text_edit, 1, 0)
		
		self.setTabText(1,"Destination Weather")
		self.tab2.setLayout(layout)
		
	def tab3UI(self):
		layout = QGridLayout()
		
		solution_label = QLabel("Solutions")
		solution_font = QFont()
		solution_font.setBold(True)
		solution_label.setFont(solution_font)
		
		self.solution_text_edit  = QTextEdit()
		self.solution_text_edit.setReadOnly(True)

		layout.addWidget(solution_label, 0, 0)
		layout.addWidget(self.solution_text_edit, 1, 0)
		
		self.setTabText(2, "Flight Information")
		self.tab3.setLayout(layout)

	def tab4UI(self):

		layout = QFormLayout()
		box_line_1 = QGridLayout()
		box_line_2 = QGridLayout()
		box_line_3 = QGridLayout()
		box_line_4 = QGridLayout()

		# first layout box
		carrier = QLabel("Carrier:")
		flight_num = QLabel("Flight:")
		self.carrier_line_edit = QLineEdit()
		self.flight_line_edit = QLineEdit()
		
		box_line_1.addWidget(carrier, 0, 0)
		box_line_1.addWidget(flight_num, 1, 0)
		box_line_1.addWidget(self.carrier_line_edit, 0, 1)
		box_line_1.addWidget(self.flight_line_edit, 1, 1)
		box_line_1.addWidget(QLabel("\t\t\t\t\t\t\t\t"), 0, 2)
		
		# seconde layout box
		date = QLabel("Date:")
		self.flight_year_line_edit = QLineEdit()
		self.flight_year_line_edit.setPlaceholderText("YYYY")

		self.flight_month_line_edit = QLineEdit()
		self.flight_month_line_edit.setPlaceholderText("MM")

		self.flight_day_line_edit = QLineEdit()
		self.flight_day_line_edit.setPlaceholderText("DD")

		box_line_2.addWidget(date, 0, 0)
		box_line_2.addWidget(QLabel("\t\t"), 0, 1)
		box_line_2.addWidget(self.flight_year_line_edit, 0, 2)
		box_line_2.addWidget(QLabel("-"), 0, 3)
		box_line_2.addWidget(self.flight_month_line_edit, 0, 4)
		box_line_2.addWidget(QLabel("-"), 0, 5)
		box_line_2.addWidget(self.flight_day_line_edit, 0, 6)
		
		self.flight_submit_button = QPushButton()
		self.flight_submit_button.setText("Submit")
		box_line_2.addWidget(self.flight_submit_button, 1, 6)

		# self.invalid label
		font = QFont()
		font.setPointSize(20)
		self.flight_err_msg = QLabel('')
		self.flight_err_msg.setFont(font)

		#
		self.flight_status_text_edit  = QTextEdit()
		self.flight_status_text_edit.setReadOnly(True)
		


		# add layout
		layout.addRow(box_line_1)
		layout.addRow(box_line_2)
		layout.addRow(self.flight_err_msg)

		font = QFont()
		font.setPointSize(20)
		font.setBold(True)
		self.remaining_time_label = QLabel('Time remaining to departure:')
		self.remaining_time_label.setFont(font)

		self.remaining_time = QLabel(' ')
		self.remaining_time.setFont(font)
		box_line_4.addWidget(self.remaining_time_label, 0, 0)
		box_line_4.addWidget(self.remaining_time, 0, 1)

		box_line_3.addLayout(layout,0, 0)
		box_line_3.addWidget(self.flight_status_text_edit, 1, 0)
		box_line_3.addLayout(box_line_4,2, 0)

		
		
		
	
		self.setTabText(0,"Flight searching")
		self.tab4.setLayout(box_line_3)


	'''
	flight searching error msg
	'''
	def show_invalid_airport_msg(self):	
		self.err_msg.setText('Error: Invalid airport code..')
		self.err_msg.setStyleSheet('color: red')


	def show_invalid_date_msg(self):
		self.err_msg.setText('Error: Invalid date..')
		self.err_msg.setStyleSheet('color: red')

	def reset_error_msg_label(self):
		self.err_msg.setText('')

	def enter_address(self):
		self.err_msg.setText('Error: Please enter current address')
		self.err_msg.setStyleSheet('color: red')

	def enter_airport_code(self):
		self.err_msg.setText('Error: Please enter destination airport code')
		self.err_msg.setStyleSheet('color: red')
	def enter_date(self):
		self.err_msg.setText('Error: Please enter date')
		self.err_msg.setStyleSheet('color: red')
	def enter_no_flight(self):
		self.err_msg.setText('Error: No flight available..')
		self.err_msg.setStyleSheet('color: red')

	'''
	flight status error msg
	'''
	def show_invalid_flight_date_msg(self):
		self.flight_err_msg.setText('Error: Invalid date..')
		self.flight_err_msg.setStyleSheet('color: red')

	def reset_flight_error_msg_label(self):
		self.flight_err_msg.setText(None) 

	def enter_carrier(self):
		self.flight_err_msg.setText('Error: Please enter flight carrier')
		self.flight_err_msg.setStyleSheet('color: red')

	def enter_flight_num(self):
		self.flight_err_msg.setText('Error: Please enter flight number')
		self.flight_err_msg.setStyleSheet('color: red')
	def enter_date_flight_status(self):
		self.flight_err_msg.setText('Error: Please enter date')
		self.flight_err_msg.setStyleSheet('color: red')
	
	'''
	set weather info
	'''
	def set_weather_info(self, msg):
		self.weather_text_edit.setText(msg)

	'''
	set soluitons
	'''
	def set_flight_info(self, flight, price):
		self.solution_text_edit.setText(" ")
		for i in range (0, len(flight)):
			if flight[i] != None:
				self.solution_text_edit.append("Solution# %d: Sale Price: %s" % (i + 1, price[i]) )
				self.solution_text_edit.append("\tFlight\tOrigin\tDestination\tDepartureTime\tArrivalTime\t\t\tAvailable Seat\tMeal")
				for j in range (0, len(flight[i])):
					self.solution_text_edit.append("\t" + (flight[i])[j])

	'''
	set flight status info
	'''
	def set_flight_status_info(self, flight_info):
		self.flight_status_text_edit.setStyleSheet("QTextEdit {color:black}")
		self.flight_status_text_edit.setText('Flight Status:')

		flight_status = flight_info[2]
		flight_id = flight_status.get('flightId')
		departure_airport_code = flight_status.get('departure_airport_code')
		arrival_airport_code = flight_status.get('arrival_airport_code')
		localDepartTime = flight_status.get('localDepartTime')
		localArrivalTime = flight_status.get('localArrivalTime')
		flightDurations = flight_status.get('flightDurations')
		arrivalTerminal = flight_status.get('arrivalTerminal')
		flightStatus = flight_status.get('flightStatus')

		self.flight_status_text_edit.append('\tFlight ID:\t\t' + str(flight_id))
		self.flight_status_text_edit.append('\tDesparture Airport Code:\t' + departure_airport_code)
		self.flight_status_text_edit.append('\tArrival Airport Code:\t' + arrival_airport_code)
		self.flight_status_text_edit.append('\tFlight Status:\t' + flightStatus)
		self.flight_status_text_edit.append('\tArrival Terminal:\t' + arrivalTerminal)
		self.flight_status_text_edit.append('\tLocal Departure Time:\t' + localDepartTime)
		self.flight_status_text_edit.append('\tLocal Arrival Time:\t' + localArrivalTime)
		self.flight_status_text_edit.append('\tFlight Durations:\t' + str(flightDurations) + " mintues")

		lines = flight_info[0]
		self.flight_status_text_edit.append('Airline:')
		for i in range (0, len(lines)):
			airline = lines[i]
			self.flight_status_text_edit.append('\tAirline #' + str(i + 1))
			self.flight_status_text_edit.append('\t\tName:\t\t' + airline[0])
			self.flight_status_text_edit.append('\t\tFS: \t\t' + airline[1])
			if airline[2] != None:
				self.flight_status_text_edit.append('\t\tPhone Number:\t' + airline[2])
			else:
				self.flight_status_text_edit.append('\t\tPhone Number:\t-')

		self.flight_status_text_edit.append('Flight Equipments:')
		equipment = flight_info[1]
		for i in range (0, len(equipment)):
			equip = equipment[i]
			name = equip.get('name')
			turboProp = equip.get('turboProp')
			jet = equip.get('jet')
			widebody = equip.get('widebody')
			regional = equip.get('regional')

			self.flight_status_text_edit.append('\tEquipment #' + str(i + 1))
			self.flight_status_text_edit.append('\t\tName: \t\t' + name)
			self.flight_status_text_edit.append('\t\tRurboProp: \t\t' + str(turboProp))
			self.flight_status_text_edit.append('\t\tJet:\t\t' + str(jet))
			self.flight_status_text_edit.append('\t\tWidebody\t\t' + str(widebody))
			self.flight_status_text_edit.append('\t\tRegional\t\t' + str(regional))



	def set_flight_status_error(self, error):
		self.flight_status_text_edit.setStyleSheet("QTextEdit {color:red}")
		self.flight_status_text_edit.setText('Error:')

		err_msg = error.get('errorMessage')
		err_code = error.get('errorCode')

		self.flight_status_text_edit.append('\tError Code')
		self.flight_status_text_edit.append('\t\t\t' + err_code)
		self.flight_status_text_edit.append('\tError Message')
		self.flight_status_text_edit.append('\t\t\t' + err_msg)


	def departure_time(self, departure_time_list):
		depart_date_time = datetime(departure_time_list[0], departure_time_list[1], departure_time_list[2], \
			departure_time_list[3], departure_time_list[4], departure_time_list[5])
		self.duration_hour = int((depart_date_time - datetime.utcnow()).total_seconds() / 3600)
		self.duration_minute =  int((depart_date_time - datetime.utcnow()).total_seconds() % 3600 / 60)
		self.duration_second = int((depart_date_time - datetime.utcnow()).total_seconds() % 3600 % 60)

		print(depart_date_time - datetime.utcnow())
		print(str(self.duration_hour) + ':' + str(self.duration_minute) + ':' + str(self.duration_second))
		if self.thread == None:
			self.thread = Timer(self.duration_hour, self.duration_minute, self.duration_second, self.remaining_time)
			self.thread.daemon = True
			self.thread.start()
		else:
			self.thread.stop()

			self.thread = Timer(self.duration_hour, self.duration_minute, self.duration_second, self.remaining_time)
			self.thread.daemon = True
			self.thread.start()

		#self.remaining_time.setText(str(duration_hour) + ':' + str(duration_minute) + ':' + str(duration_second))



class Timer(threading.Thread):
	def __init__(self, hour, minute, second, remaining_time):
		threading.Thread.__init__(self)
		self.hour = hour
		self.minute = minute
		self.second = second
		self.remaining_time = remaining_time
	def run(self):
		print(str(self.hour) + ' ' + str(self.minute) +  ' ' + str(self.second))
		while self.hour != 0 or self.minute != 0 or self.second != 0:
			self.remaining_time.setText(str(self.hour) + ':' + str(self.minute) + ':' + str(self.second))
			self.second -= 1
			if self.second < 0:
				self.minute -= 1
				self.second = 59
				if self.minute < 0:
					self.hour -= 1
					self.minute = 59
					if self.hour < 0:
						break
			time.sleep(1)
	def stop(self):
		self.hour = 0
		self.minute = 0
		self.second = 0
