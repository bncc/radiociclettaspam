import sys

import pycore

import logger

import conf_handler

import facebook

def publish( status ):

        status += " www.radiocicletta.it"

	logger.log("facebook will publish: " + status, 0)

        conf_path = "facebook.conf"

        api_key = conf_handler.read_conf("api_key", conf_path )
        if ( api_key == None ): 
		logger.log("Unable to retrieve consumer_key", -1)
		return None
        
        secret_key = conf_handler.read_conf("secret_key", conf_path )
        if ( api_key == None ): 
		logger.log("Unable to retrieve consumer_key", -1)
		return None

        fb = facebook.Facebook(api_key, secret_key)

        token = fb.auth.createToken()
        
        logger.log("Token created successfully: " + str(token), 0 )

        # fb.login()
        # fb.
        fb.auth.getSession()

        fb.status.set("Ascoltate tanta Radiocicletta!", fb.uid)
        
        
