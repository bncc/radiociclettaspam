# import pycore
import time

import logger
import conf_handler
import json_handler

import twitter_spammer as twits
# import facebook_spammer as fcbk

class notifier:

    __m_module_name = str(__name__)
    __m_notifications_json = None

    def __init__( self ):
        conf = conf_handler.conf_handler(conf_name = __m_module_name + ".conf")
        if (conf == None):
            logger.log("Unable to load config file "+ __m_module_name + ".conf" )
            return
        
        notifications_path = conf.read_conf("notifications_path")
        if (notifications_path == None):
            logger.log("Unable to find notifications path in config." )
            return

        __m_notification_json = json_handler.json_handler(notifications_path)
        if ( __m_notification_json == None):
            logger.log("Unable to load json file " + __m_notification_json )
            return


    def check_notifications():
        
