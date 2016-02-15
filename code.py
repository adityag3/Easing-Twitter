from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy

ckey = "JiMJeyvleEz4lQvuWywMFgMEU"
csecret = "B488MOxbEdcqXAaJZB3caTK5W2i8QxxWYZYI5wWiRcgiFPYkSN"
atoken = "546688389-xrYORiZdYqp8BNs2venEOmUt48d5Ya5CBAcOATJr"
asecret = "Jlq4gjOGJv2r1stGmxdUEqAwYHzjTWzmV2edisGf7hcVe"

class listener( StreamListener ):

	def on_data( self, data ):
		try:
			#print data

			tweet = data.split(',"text":"')[1].split('","source')[0]
			print tweet

			saveThis = str(time.time()) + '::'
			saveFile = open('TwitterDB2.csv','a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True

		except BaseException, e:
			print 'failed ondata', str(e)
			time.sleep(5)

	def on_error( self, status ):
		print status

auth = OAuthHandler( ckey, csecret )
auth.set_access_token( atoken, asecret )
#twitterStream = Stream( auth, listener() )
#twitterStream.filter( track= ['car'] )

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text