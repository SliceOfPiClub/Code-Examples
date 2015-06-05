# ==========================================
# usList.py
#
# interface to a ultrasonic range sensor
# HC-SR04 1.99 Ebay
# Keep a list of the last 30 readings
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 19-May-2015
# ==========================================
# HC-SR04, 1k ohm Resistor, 2kOhm Resistor
#
# GND -------------+------------- GPIO GND [6]
#                  |
#                  2K
#                  |
# ECHO ----1K------+------------- GPIO 24 [18]
#
# TRIG -------------------------- GPIO 23 [16]  
#
# Vcc --------------------------- GPIO 5V [2]

import RPi.GPIO as GPIO
import time


#
# Create list to store readings in
#
Readings = []
TimeTaken = []
MAX_READINGS = 30


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
# one for trigger output and one for echo input
#

TRIG = 23
ECHO = 24

#
# Initialise the GPIO Ports to OUTPUT
#

print "Measuring Distance"
GPIO.setup(TRIG , GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ECHO , GPIO.IN, initial=GPIO.HIGH,  pull_up_down=GPIO.PUD_UP)


#
# Reset Sensor
#
print "Wait for Sensor Reset"
time.sleep(2)


def Read_Distance():
    global TRIG, ECHO
    #print "check High Already"
    if not GPIO.input(ECHO):
        #print "Ping Reset 10 micro seconds"
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        distance = 0
        #print "waiting low"
        pulse_start = time.time()
        pulse_end = time.time()

        while not GPIO.input(ECHO):
            pulse_start = time.time()
            if pulse_start - pulse_end > 0.02:
                distance = 100
                break
        if distance != 100:
            #print "waiting high"
            pulse_end = time.time()
            while GPIO.input(ECHO):
                pulse_end = time.time()
                if pulse_end - pulse_start > 0.02:
                    distance = 100
                    break
        if distance != 100:
            pulse_duration= pulse_end - pulse_start
            distance = pulse_duration / 0.00000295 / 2 / 10
            distance = round(distance, 2)
        #print "Distance:",distance,"cm"
        return (distance)


try:
    while True:
        d = Read_Distance()
        print d
        Readings.Add(d)
        TimeTaken.Add(time.time())
        if Len(Readings) > MAX_READINGS:
             # delete first reading
             del Readings[0]
             del TimeTaken[0]

        time.sleep(0.05)


except KeyboardInterrupt:
    #
    # clean up on finish
    #
    print "clean Up"
    GPIO.cleanup()

    # print all readings
    print Readings, TimeTaken

