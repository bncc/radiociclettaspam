import sys
import logger
import conf_handler

def publish( status ):

        status += " www.radiocicletta.it"

	logger.log("facebook will publish: " + status, 0)

        conf_path = "facebook.conf"

#	consumer_key = conf_handler.read_conf("consumer_key", conf_path )
#	if ( consumer_key == None ): 
#		logger.log("Unable to retrieve consumer_key", -1)
#		return None

	# Errors must be handled here and then
