# ==========================================
# led.py
#
# Turn a led on and off
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

LED = 23

#
# Initialise the GPIO Port to OUTPUT
#

GPIO.setup(LED , GPIO.OUT)

#
# set the Pin High - turning on the LED
#

GPIO.output(LED, GPIO.HIGH)

#
# Flash the LED 10 times 
# turn on and off within a loop
#

count = 0
while(count < 10):


	#
	# Set Pin HIGH to light LED
	#

	GPIO.output(LED, GPIO.HIGH)

	#
	# Pause for a short while 
	#

	time.sleep(0.1)

	#
	# Set Pin LOW to light LED
	#

	GPIO.output(LED, GPIO.LOW)

	#
	# Pause for a short while 
	#

	time.sleep(0.1)

	#
	# Add 1 to the count
	#

	count = count + 1

#
# clean up on finish
#
GPIO.cleanup()

