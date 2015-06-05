# ==========================================
# remote.py
#
# turn a device on and off using a remote control
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 7-May-2015
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
# Set 2 variables to the Pin numbers we what to use
# one is used to turn on the other to turn off
#

GPIOPinON = 18
GPIOPinOFF = 23

#
# Setup pins for output
#

GPIO.setup(GPIOPinON , GPIO.OUT)
GPIO.setup(GPIOPinOFF , GPIO.OUT)

#
# Print message to say we are turning on device
# the red light on the remote should flash
#

print 'TURN ON'

#
# To turn on set the pin high - to simulate someone pressing
# pause then set low - simulating someone releasing the button
#

GPIO.output(GPIOPinON , GPIO.HIGH)
time.sleep(0.2)
GPIO.output(GPIOPinON , GPIO.LOW)

#
# Pause for 5 seconds
#
print 'PAUSE'
time.sleep(5.0)

#
# Print message to say we are turning off device
# the red light on the remote should flash
#

print 'TURN OFF'

#
# To turn off set the pin high - to simulate 
# someone pressing the off button
# pause then set low - simulating someone releasing the button
#

GPIO.output(GPIOPinOFF, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(GPIOPinOFF, GPIO.LOW)

#
# clean up
#

GPIO.cleanup()
