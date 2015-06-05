# ==========================================
# fadeled.py
#
# Fade a led from off to on then
# on to off - like a pulse
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
# Set up Pulse Width Mod
#

p = GPIO.PWM(LED, 50)

p.start(50)
p.ChangeFrequency(100)

try:
	#
	# Loop from 0 to 101 increasing by 1
	#

	for d in range(0,101):
		p.ChangeDutyCycle(d)
		time.sleep(0.02)

	#
	# Loop from 100 to 1 decrease by 1
	#

	for d in range(100,1,-1):
		p.ChangeDutyCycle(d)
		time.sleep(0.02)



except KeyboardInterrupt:
	print "end"

p.stop()

GPIO.cleanup()
