# Created by Aditya Govil
# github username : adityag3
# website : https://adityagovil.co

from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy

ckey = "Rgo8vXnDEOvctSWnTWFwMLii9j" #Dummy key
csecret = "MadEaCClFHM0m8WHCmzvAL55ZtMBOayXU6MfrCHQxiGfr0U8w96" #Dummy consumer secret
atoken = "546688389-xrYORiZdYqp8BNs2venEOmUt48d5Ya5CBAcOATJ9r" #Dummy access token
asecret = "Jlq4gjOGJv2r1stGmxdUEqAwYHzjTWzmV2edisGf7hcV9e" #Dummy access secret

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
twitterStream = Stream( auth, listener() )
twitterStream.filter( track= ['Modi'] )

'''
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
'''
