# ==========================================
#
# Control GPIO from Web using Bottle
# 
# sudo apt-get install python-bottle
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 8-May-2015
#
# http://192.168.1.70/on 
# http://192.168.1.70/off 
# ==========================================


from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

#
# Set the IP of the raspberry Pi
# to find out IP type 'sudo ifconfig' and look for inet addr
#

IP_ADDRESS = '10.12.66.170'

#
# Use BCM e.g. by name noT BOARD by pin number
#

GPIO.setmode(GPIO.BCM)

#
# Set warnings off to suppress re-initialisation messages
#

GPIO.setwarnings(False)


#
# Set 2 variables to the Pin numbers we what to use
# one is used to turn on the other to turn off
#

button_1_ON = 18
button_1_OFF = 23

#
# Setup pins for output
#

GPIO.setup(button_1_ON , GPIO.OUT)
GPIO.setup(button_1_OFF , GPIO.OUT)


#
# Function to simulate button pressed
# set the pin high - to simulate someone pressing
# pause, then set low - simulating someone releasing the button
#

def clickButton(button):
	GPIO.output(button, True)
	time.sleep(0.2)
	GPIO.output(button, False)


#
# Define what we want when some visits web page
#

@route('/')	
def home():
	# display a HTML template
	return template('remote')
	
#
# Define what we want when some visits ON web page
#

@route('/on')
def turnON():
	# Call the click on button
	clickButton(button_1_ON)
	# display a HTML template
	return template('remote')

#
# Define what we want when some visits OFF web page
#
	
@route('/off')
def turnOFF():
	# Call the click off button
	clickButton(button_1_OFF)
	# display a HTML template
	return template('remote')
	

try:
	# run bottle host on address and port
	run(host=IP_ADDRESS, port=8000)
finally:
	# clean up 
	print('cleaning')
	GPIO.cleanup() 
