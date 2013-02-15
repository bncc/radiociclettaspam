import sys
import logger
import conf_handler

from social_spammer import social_spammer

import tweepy

class twitter_spammer (social_spammer):
        
        __url = "http://www.radiocicletta.it"

        def __init__(self, url):
                if(url != None):
                        self.__url = url

        def social_spam(self, tweet):
                return self.__tweet(tweet, self.__url)
        
        def __tweet( self, tweet, url = None ):
                
                tweet = self.__handle_tweet(tweet, url)
                logger.log("tweet will be: " + tweet, 0)

                conf_path = "twitter.conf"

                conf_obj = conf_handler.conf_handler(conf_name="twitter.conf")
                
                consumer_key = conf_obj.read_conf("consumer_key" )
                if ( consumer_key == None ): 
                        logger.log("Unable to retrieve consumer_key", -1)
                        return None
                consumer_secret = conf_obj.read_conf("consumer_secret" )
                if ( consumer_secret == None ): 
                        logger.log("Unable to retrieve consumer_secret", -1)
                        return None
                
                access_token = conf_obj.read_conf("access_token" )
                if ( access_token == None ):
                        logger.log("Unable to retrieve access_secret", -1)
                        return None
                access_secret = conf_obj.read_conf("access_secret" )
                if ( access_secret == None ): 
                        logger.log("Unable to retrieve access_secret", -1)
                        return None
                
                # Errors must be handled here and then
                
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_secret)
                
                api = tweepy.API(auth)
                
                # api.update_status(tweet)
                

        def __handle_tweet( self, tweet, url):
                        
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
