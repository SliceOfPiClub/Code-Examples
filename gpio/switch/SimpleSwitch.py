# ==========================================
# SimpleSwitch.py
#
# Print a message when a switch is pressed
# 
# Use GND  -  (3rd Down on right)
# & GPIO 23   (8th Down on right)
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 7-MAy-2015
# ==========================================

import RPi.GPIO as GPIO
import time

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
#

Button = 23

#
# Initialise the GPIO Port to INPUT and pulled down to Ground
#

GPIO.setup(Button , GPIO.IN, pull_up_down=GPIO.PUD_UP)


#
# keep going forever
#

while True:

	#
	# Check if the button has been pressed
	#

	if GPIO.input(Button) == False:
		
		print "The Button has been pressed"

	time.sleep(0.5)				

# if we get to here clean up GPIO
GPIO.cleanup()

