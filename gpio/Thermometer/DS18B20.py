# ==========================================
# DS18B20.py
#
# Take the temprature from a DS18B20 using
# 1-wire digital temperature sensor
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

deviceList = []
deviceList.append('28-0000062f3b6c')

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
		#this is the CRC and should be YES
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

# keep reading the Temperature forever
while True:
        # loop around all the devices connected
        for device in deviceList:
                print device ,getTemperature(device) 

	# pause before getting next reading
        time.sleep(1)

