from twython import Twython
import time
from datetime import datetime
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

def timestr_to_datetime(timestr):
	timestr = "{0} {1}".format(timestr[:19],datetime.now().year)
	return datetime.strptime(timestr,'%a %b %d %H:%M:%S %Y')


def main():
	last_date = datetime.now()
	message = "Hello world!"
	#twitter.update_status(status=message)
	print('looking for tweets')
	try:
		while(True):
			timeline = twitter.get_user_timeline(screen_name = 'SliceOfPiClubIO', count=1)
			for t in timeline:
				tweet_time = timestr_to_datetime(t['created_at'])
				print(last_date)
				if tweet_time > last_date:
					print(tweet_time)
					if 'LED' in t['text']:
						print(t['text'])
						last_date = tweet_time
						break
			time.sleep(10)

	except KeyboardInterrupt:
		print( 'end' )
 
if __name__ == '__main__':
	main()
