#from twython import Twython
from twython import TwythonStreamer
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

'''
twitter = Twython(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret


)
'''

class MyStreamer(TwythonStreamer):
	def on_sucess(self, data):
		print(' Tweet Arrived ')
		if 'text' in data:
			print( data['text'].encode('utf-8') )

	def on_error(self, status_code, data):
		print( status_code )

def main():
	message = "Hello world!"
	#twitter.update_status(status=message)
	print('looking for tweets')
	try:
		stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
		stream.statuses.filter(track='twitter')
	except KeyboardInterrupt:
		print( 'end' )
 
if __name__ == '__main__':
	main()
