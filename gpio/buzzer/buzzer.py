# ==========================================
# buzzer.py
#
# Make a buzzer make a sound
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 7-MAy-2015
# ==========================================

import RPi.GPIO as GPIO
import time

#
# This is the buzz function 
# that turns the buzzer on and off very fast
# which causes the sound and pitch
#

def buzz(pin, pitch, duration):

	#calculate the cycles and the delay
	period = 1.0 / pitch
	delay = period / 2
	cycles = int(duration * pitch)

	# repeat for number of cycles
	for i in range(cycles):

		#Set Pin High and pause
		GPIO.output(pin, True)
		time.sleep(delay)

		#Set Pin Low  and pause
		GPIO.output(pin, False)
		time.sleep(delay)

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

Buzzer = 23

#
# Initialise the GPIO Port to OUTPUT
#

GPIO.setup(Buzzer , GPIO.OUT)

#
# Buzz 10 times
#

count = 0
while(count < 10):

	#
	# Call buzz function to make the sound
	# Pin number, Pitch, duration
	#
		
	buzz(Buzzer , 600, 0.3)

	#
	# pause for a short while with no sound
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

