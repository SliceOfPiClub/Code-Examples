from twython import Twython 
import time 
from datetime import datetime 
import RPi.GPIO as GPIO

from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

twitter = Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret


)

led = False

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

def timestr_to_datetime(timestr):
	timestr = "{0} {1}".format(timestr[:19],datetime.now().year)
	return datetime.strptime(timestr,'%a %b %d %H:%M:%S %Y')

def toggle():
	global led
	if led == True:
		GPIO.output(18, False)
		led = False	
	else:
		GPIO.output(18, True)
		led = True	

def main():
	last_date = datetime.now()
	message = "Hello world!"
	toggle()
	#twitter.update_status(status=message)
	print('looking for tweets')
	try:
		while(True):
			#tweets = twitter.cursor(t.search, q='SliceOfPiClubIO LED',result_type='popular')	
			#print(tweets)		
			tweets = twitter.get_home_timeline(screen_name = 'SliceOfPiClubIO', count=1)
			#print(tweets)
			
			for t in tweets:
				tweet_time = timestr_to_datetime(t['created_at'])
				if tweet_time > last_date:
					#print(tweet_time)
					if 'LED' in t['text']:
						print(t['text'])
						toggle()
						last_date = tweet_time
						break
			#be careful you are only allowed 100 requests per hour
			time.sleep(30)

	except KeyboardInterrupt:
		
		print( 'end' )
	finally:
		print('cleaning')
		GPIO.cleanup() 
if __name__ == '__main__':
	main()
