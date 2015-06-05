# ==========================================
# graph_LogMulti.py
#
# Read the log file of temperatures and draw
# a graph of the results, uses google charts
# to display the graph results.
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 3-June-2015
# ==========================================
#

from GChartWrapper import *
from bottle import route, run, template, request, get, post
import time
import json


#
# Set the IP of the raspberry Pi
# to find out IP type 'sudo ifconfig' and look for inet addr
#

IP_ADDRESS = '192.168.1.86'

# create an entry point for web page
@route('/')     
def home():
        # initialise the readings
        Readings = [[],[],[]]

        #read the temp readings from the log file
        with open('tempreadingsmulti.dat','r') as infile:
                Readings = json.load(infile)
         
        #
        # Set up the Chart
        #
        G = Line([Readings[0],Readings[1], Readings[2]], encoding='text')
        G.color('Blue','Black','Red')
        G.size(500,300)
        G.axes('xy')
        G.axes.label(1, 15, 40)
        G.axes.label(0, 0, len(Readings) )
        G.legend('Temp 1','Temp 2','temp 3')
        G.scale(15,40)

        graphURL=str(G)

        if G:     
                # display the web page from template
                # injecting the graph url
                return template('graph',graphURL=str(G))

try:
    run(host=IP_ADDRESS, port=8000)
finally:
    print('end')
