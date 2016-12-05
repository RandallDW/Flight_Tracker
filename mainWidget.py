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

class MainWidget(QTabWidget):
	def __init__(self, parent = None):
		super(MainWidget, self).__init__(parent) 
		self.setGeometry(400,100,800,800)
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()
		self.tab4 = QWidget()

		self.addTab(self.tab1, "Search")
		self.addTab(self.tab2, "Destination Weather")
		self.addTab(self.tab3, "Solutions")
		self.tab1UI()
		self.tab2UI()		
		self.tab3UI()

		self.setWindowTitle("Network Application Design")
		self.show()

	def tab1UI(self):
		layout = QFormLayout()
		box_line_1 = QGridLayout()
		box_line_2 = QGridLayout()
		



		# first layout box
		name = QLabel("Name:")
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
		
		# add layout
		layout.addRow(box_line_1)
		layout.addRow(box_line_2)
		
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
		layout = QGridLayout()
		
		label_1 = QLabel("Rover 1 Sent")
		label_2 = QLabel("Rover 2 Received")
		
		self.rover_1_sent  = QTextEdit()
		self.rover_1_received  = QTextEdit()
		self.rover_1_received.setReadOnly(True)
		self.rover_1_sent.setReadOnly(True)

		layout.addWidget(label_1, 0, 0)
		layout.addWidget(label_2, 0, 1)
		layout.addWidget(self.rover_1_sent, 1, 0)
		layout.addWidget(self.rover_1_received, 1, 1)

		self.setTabText(3, "milestone 4")
		self.tab4.setLayout(layout)

