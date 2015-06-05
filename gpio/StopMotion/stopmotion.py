# ==========================================
# stopmotion.py
#
# click a GPIO button and take a picture
# store each as SMxxxxx.jpg where xxxxx with be a counter
# when esc is pressed the images will be joined together
# to produce a movie
#
# Author:  Martin Eyre (Slice of Pi Club)
# Created: 15-May-2015
# ==========================================


import RPi.GPIO as GPIO
import time
import picamera

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
# Set a variable to count the number of images taken
#

images_taken = 0

#
# Initialise the GPIO Port to INPUT and pulled down to Ground
#

GPIO.setup(Button , GPIO.IN, pull_up_down=GPIO.PUD_UP)

#
# initialise the camera, set the resolution
#
camera = picamera.PiCamera()


#
# start the preview
#
camera.start_preview()


#
# keep going forever
#

try:

	while True:

		#
		# Check if the button has been pressed
		#

		if GPIO.input(Button) == False:
			#
			# capture image from camera and store as image
			#
			camera.capture('/home/pi/stopmotion/SM' + str(images_taken) + '.jpg')
		
			print 'Picture ' + str(images_taken) 
	
			# increase the images taken count
			images_taken +=1

		time.sleep(0.2)				

except KeyboardInterrupt:

	# if we get to here clean up GPIO
	camera.stop_preview()

	GPIO.cleanup()

	camera.close()

	os.system('avconv -r 5 -i /home/pi/stopmotion/SM%d.jpg -vcodec libx264 stopmotion.mp4')

