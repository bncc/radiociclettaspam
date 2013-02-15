import pycore
import time

import logger

import palim_reader
import json_handler
import twitter_spammer as twits
# import facebook_spammer as fcbk

# Todo: add a methon to simply spam stuff around

def spam( spam_line = None, spam_url = None, day = None, hour = None, minute = None ):
    
    if( spam_line == None ): 
        spam_line = create_spam_line(day, hour, minute)
        if( not spam_line ):
            logger.err("no spam to do now!", -1)
            return None

    twit_spam = twits.twitter_spammer( spam_url )
    twit_spam.social_spam( spam_line )
    
#    fcbk_spam = twits.twitter_spammer( spam_url )
#    fcbk_spam.social_spam( spam_line )


''' If you pass a line or a line and a url it spams that. if you don't pass anything it checks for possible spam on palim '''
def spam_now( spam_line = None, spam_url = None ):
    
    day = time.strftime("%a")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    
    if( spam_url = None ): spam_url = "http://www.radiocicletta.it"
    
    spam( spam_line, spam_url, day, hour, minute )

def create_spam_line(day, hour, minute):

    logger.log("checking for programs on "+ day +" "+str(hour)+":"+str(minute))

    program = palim_reader.read(day, hour, minute)

    if(program == None): 
        logger.err("No program found", -1)
        return None

    title = str(json_handler.array_search(program, "title"))
    if( title == None):
        logger.err("No title found for program on "+ day +" "+hour+":"+minute+". Spam won't move on", -1)
        return
    
    author = str(json_handler.array_search(program, "author"))
    if( author == None): logger.err("No author found", -1)
    
    theme = str(json_handler.array_search(program, "theme"))
    if( theme == None): logger.err("No theme found", -1)
    
    spam_line = "Ora in onda " + title + ": " + theme + " con " + author + " su "

    logger.log("Spam Line created: " + spam_line)

    return spam_line
    
