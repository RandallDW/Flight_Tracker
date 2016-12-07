import sys, os
import socket
import time
import _thread
import json
from ctypes import*
from struct import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWidget(QTabWidget):
	submit = pyqtSignal()
	def __init__(self, parent = None):
		super(MainWidget, self).__init__(parent) 
		self.setGeometry(100,100,1200,800)
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()

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


		# add layout
		layout.addRow(box_line_1)
		layout.addRow(box_line_2)
		layout.addRow(self.flight_err_msg)
		
		
	
		self.setTabText(0,"Flight searching")
		self.tab4.setLayout(layout)


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
		self.flight_err_msg.setText('')

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
		self.solution_text_edit.setText("Flight Info:")
		for i in range (0, len(flight)):
			if flight[i] != None:
				self.solution_text_edit.append("\t Solution# %d: Sale Price: %s" % (i + 1, price[i]) )
				self.solution_text_edit.append("\t\tOrigin\tDestination\tDepartureTime\tArrivalTime\t\tAvailable Seat\t\tMeal")
				for j in range (0, len(flight[i])):
					self.solution_text_edit.append("\t\t" + (flight[i])[j])