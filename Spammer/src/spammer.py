import time

import palim_reader
import util

import logging
import json

import twitter_spammer as twits
# import facebook_spammer as fcbk

class spammer:

    __logger_handler = None
    __palimpsest     = None
    __conf           = None

    def __init__(self):
        
        self.__conf = util.conf_handler("../conf/spammer.conf");
        
        pal_file = util.fs_handler( self.__conf.get_conf_value("palimpsest_path") )
        
        self.__palimpsest = json.loads( pal_file.to_string() )

        self.__logger_handler = util.log_handler(debug_level = logging.DEBUG)

    ''' If you pass a line or a line and a url it spams that. if you don't pass anything it checks for possible spam on palim '''
    def spam_now( self, spam_line = None, spam_url = None ):
    
        day = time.strftime("%a")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        
        self.__logger_handler.logger.error( util.create_msg("try to spam "+day+" "+hour+":"+minute) )

        self.spam( spam_line, spam_url, day, hour, minute )


    def spam(self, spam_line = None, spam_url = None, day = None, hour = None, minute = None ):
    
        if( spam_line == None ): 
            program_obj = self.get_on_air_program(day, hour, minute)
            if not program_obj :
                self.__logger_handler.logger.warning( util.create_msg("No on air program found") )
                return None

            spam_line = self.create_on_air_line(program_obj.author, program_obj.title, program_obj.theme)
            
            self.__logger_handler.logger.debug( util.create_msg("Spam Line created correctly: " + spam_line) )
            
            # twit_spam = twits.twitter_spammer( program_obj.url )
            # twit_spam.social_spam( spam_line )
    
            # fcbk_spam = twits.twitter_spammer( spam_url )
            # fcbk_spam.social_spam( spam_line )

    
    def get_on_air_program(self, day, hour, minute):
        
        pal_reader = palim_reader.palim_reader(self.__palimpsest)
        if pal_reader == None:
            self.__logger_handler.logger.error( util.create_msg("Unable to get palimpsest reader") )
            return

        palim_obj = pal_reader.read(day, hour, minute)
        if palim_obj == None:
            self.__logger_handler.logger.warning( util.create_msg("Unable to read "+day+", "+hour+":"+minute+" on palimpsest") )
            return
        
        return palim_obj
        

    def create_on_air_line(self, author, title, theme):
            
        return "Ora in onda " + str(title) + " con " + str(author) + ": " + str(theme)

    
    # Le notifiche vanno ancora implementate... eccheccazzo
    def cerate_notification_line(self, notif_line, notif_author = None, notif_title = None, notif_theme = None, notif_url = None):
        pass
        
    def get_actual_notification(self, day, hour, minute):
        pass
