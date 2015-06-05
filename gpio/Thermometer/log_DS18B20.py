# ==========================================
# Log_DS18B20.py
#
# Take the temprature from a DS18B20's using
# 1-wire digital temperature sensor and store 
# the results in a log file
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 29-May-2015
# ==========================================
#
# Enable in sudo nano /boot/config.txt
# dtoverlay=w1-gpio,gpiopin=4
# ensure reboot after change
#
# Wire 
#
# D + -------------------+---- +5V (Pin 2)
# S                      |
# 1                     470 K
# 8                      |  
# B signal --------------+---- GPIO 4 (Pin 7)
# 2                     
# 0                       
#   - ------------------------ GROUND ( Pin 6)

import time
import datetime
import json

#
# All the GPIO stuff is handled by the kernal
# so no need to interact directly with GPIO
# we need to read the data from files store 
# in the w1_slave file

#
# create array of the device Id's
# get the ids from 
# cd /sys/bus/w1/devices
# ls
# cat w1_slave

deviceID= '28-0000062f3b6c'
#
# Create list to store readings in called Readings
#
Readings = []
MAX_READINGS = 30

#
# Create a function to read the tempreature from the 
# w1_slave file for a specified device
#
# the file will contain the following format of data:
#
# HH HH HH HH HH HH HH HH HH : crc=56 YES
# HH HH HH HH HH HH HH HH HH t=21023    
# 
# where HH is a hexidecimal number e.g. 0A hex = 10 decimal
#
def getTemperature(id):
        try:
                filename = '/sys/bus/w1/devices/' + id + '/w1_slave'
                

                # open the file for the specified device
                f = open(filename, 'r')
              
                #read the first line from the file
                line = f.readline()

                #get the last 3 characters from the line read
                crc = line.strip()[-3:]
                
                                
                #check crc is YES
                if crc == 'YES':
                        #read next line in the file
                        line = f.readline()

                        # get the characters after the t=
                        tempPos = line.index('=')
                        
                        # get the temp using the position
                        tempString = line[tempPos+1:]
                
                        # convert the temp into real temps
                        tempC = float(tempString) / 1000.0
                        tempF = tempC * 9.0 / 5.0 + 32.0
                
                        return tempC, tempF
        except:
                return -999


while True:
	# get the temperature
        tempC,tempF = getTemperature(deviceID)
        print tempC
        
	# add the new tempC to the Readings list
        Readings.append(tempC)

	# if we have more than the MAX_READINGS remove the first
        if len(Readings) > MAX_READINGS:
             # delete first reading
             del Readings[0]

	#save the Readings  to a file called 'tempreadings.dat'
        with open('tempreadings.dat','w') as outfile:
                json.dump(Readings,outfile)

        # sleep for 1 minute before reading and storing the next value
        time.sleep(60)

