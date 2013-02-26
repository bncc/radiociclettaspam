import time
import util
import logging

import spammer


log_handler = util.log_handler(debug_level = logging.DEBUG)

while(True):

    log_handler.logger.debug( util.create_msg("Time to log!") )

    spam = spammer.spammer()

    spam.spam_now()

    time.sleep(60)
