import sys
import logger
import conf_handler

import tweepy

def tweet( tweet, url = None ):

	tweet = handle_tweet(tweet, url)
	logger.log("tweet will be: " + tweet, 0)

        conf_path = "twitter.conf"

	consumer_key = conf_handler.read_conf("consumer_key", conf_path )
	if ( consumer_key == None ): 
		logger.log("Unable to retrieve consumer_key", -1)
		return None
	consumer_secret = conf_handler.read_conf("consumer_secret", conf_path )
	if ( consumer_secret == None ): 
                logger.log("Unable to retrieve consumer_secret", -1)
		return None

	access_token = ("access_token", conf_path )
	if ( access_token == None ):
                logger.log("Unable to retrieve access_secret", -1)
		return None
	access_secret =("access_secret", conf_path )
	if ( access_secret == None ): 
                logger.log("Unable to retrieve access_secret", -1)
		return None

	# Errors must be handled here and then

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)

	# api.update_status(tweet)


def handle_tweet(tweet, url):
	
	max_len = 140
	if( url != None ):
		max_len = 110
		url = "... " + url
        else:
                url = ""

	if ( len(tweet) < max_len ):
		return tweet + url
	else:
		return tweet[:max_len] + url
