import time

import pycore

import logger

import spammer

while(True):

    logger.log("try to spam something now... ", 0, False)

    spammer.spam_now()

    time.sleep(60)
