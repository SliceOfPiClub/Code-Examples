# ==========================================
#
# Control GPIO LED from Web using Bottle
# 
# sudo apt-get install python-bottle
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 8-May-2015
#
# http://10.0.0.173/toggle
# ==========================================

from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

#
# Set the IP of the raspberry Pi
# to find out IP type 'sudo ifconfig' and look for inet addr
#

IP_ADDRESS = '10.0.0.173'

#
# Use BCM e.g. by name noT BOARD by pin number
#

GPIO.setmode(GPIO.BCM)

#
# Set warnings off to suppress re-initialisation messages
#

GPIO.setwarnings(False)

#
# Set variable to the Pin that will control on or off
#

GPIO_LED = 23

#
# Set variable to keep status of LED
#

led = False

#
# Setup pins for output
#

GPIO.setup(GPIO_LED, GPIO.OUT)

#
# Function to loggle LED on or OFF
#

def toggle():
	global led
	if led == True:
		GPIO.output(GPIO_LED, False)
		led = False	
	else:
		GPIO.output(GPIO_LED, True)
		led = True	
#
# Define what we want when some visits web page
#

@route('/')
def home():
	#show the gome page from template
	return template('home')

#
# Define what we want when some visits TOGGLE web page
#

@route('/toggle')
def index():
	#call the toggle LED Function
	toggle()
	#show the gome page from template
	return template('home')
	
#
# Setup and run Web Server Host
#

try:
	# run bottle host on address and port
	run(host=IP_ADDRESS, port=8000)
finally:
	# Clean up
	print('cleaning')
	GPIO.cleanup() 
