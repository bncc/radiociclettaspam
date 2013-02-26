import sys
import util
import logging

from social_spammer import social_spammer

import tweepy

class twitter_spammer (social_spammer):
        
        __logger_handler = None

        def __init__(self, url = None):
                social_spammer.__init__(self, url)
                self.__logger_handler = util.log_handler(debug_level = logging.DEBUG)

        def social_spam(self, tweet, url):
                return self.__tweet(tweet, url)
        
        def __tweet( self, tweet, url = None ):
                
                if not url : url = self._url

                logh = self.__logger_handler

                tweet = self.__handle_tweet(tweet, url)
                logh.logger.debug( util.create_msg("tweet will be: " + tweet) )

                conf_obj = util.conf_handler("../conf/twitter.conf")
                
                consumer_key = conf_obj.get_conf_value("consumer_key" )
                if ( consumer_key == None ): 
                        logh.logger.error( util.create_message("Unable to retrieve consumer_key") )
                        return None
                consumer_secret = conf_obj.get_conf_value("consumer_secret" )
                if ( consumer_secret == None ): 
                        logh.logger.error( util.create_message("Unable to retrieve consumer_secret") )
                        return None
                
                access_token = conf_obj.get_conf_value("access_token" )
                if ( access_token == None ):
                        logh.logger.error( util.create_message("Unable to retrieve access_secret") )
                        return None
                access_secret = conf_obj.get_conf_value("access_secret" )
                if ( access_secret == None ): 
                        logh.logger.error( util.create_message("Unable to retrieve access_secret") )
                        return None
                
                # Errors must be handled here and then
                
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_secret)
                
                api = tweepy.API(auth)
                
                # api.update_status(tweet)
                
                return tweet

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
