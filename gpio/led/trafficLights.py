# ==========================================
# trafficLights.py
#
# Turn 3 leds on and off to simulate traffic lights
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 19-May-2015
# ==========================================

import RPi.GPIO as GPIO
import time
import random

#
# Use BCM e.g. by name noT BOARD by pin number
#

GPIO.setmode(GPIO.BCM)

#
# Set warnings off to suppress re-initialisation messages
#

GPIO.setwarnings(False)

#
# Set a variable to the Pin number we what to use
# one for each of the 3 leds
#

RED = 18
AMBER = 23
GREEN = 24

#
# Initialise the GPIO Ports to OUTPUT
#

GPIO.setup(RED , GPIO.OUT)
GPIO.setup(AMBER , GPIO.OUT)
GPIO.setup(GREEN , GPIO.OUT)

#
# Stop Function - Red light only
#
def Stop():
	global RED, AMBER, GREEN
	print "STOP"
	GPIO.output(RED , GPIO.HIGH)
	GPIO.output(AMBER, GPIO.LOW)
	GPIO.output(GREEN, GPIO.LOW)
	
#
# Get Ready to go Function - Red and amber lit
#
def GetReadyToGo():
	global RED, AMBER, GREEN
	print "Get Ready"
	GPIO.output(RED , GPIO.HIGH)
	GPIO.output(AMBER, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)

#
# Go function - Green Only
#
def Go():
	global RED, AMBER, GREEN
	print "Go !"
	GPIO.output(RED , GPIO.LOW)
	GPIO.output(AMBER, GPIO.LOW)
	GPIO.output(GREEN, GPIO.HIGH)

#
# Get Ready To Stop function - Amber Only
#
def GetReadyToStop():
	global RED, AMBER, GREEN
	print "Warning lights changing"
	GPIO.output(RED , GPIO.LOW)
	GPIO.output(AMBER, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.LOW)


#
# Run through the traffic light secquence forever
#
# If ctrl-C is pressed then quit
#

try:

	while (True):

		# stop and pause between 3 and 5 seconds
		Stop();
		pauseTime = random.randint(3,5)
		time.sleep(pauseTime)	

		GetReadyToGo();
		time.sleep(1)	

		# go and pause between 3 and 5 seconds
		Go();
		pauseTime = random.randint(3,5)
		time.sleep(pauseTime)	

		GetReadyToStop();
		time.sleep(2.9)	

except KeyboardInterrupt:
	#
	# clean up on finish
	#
	print "clean Up"
	GPIO.cleanup()

