import time

import palim_reader
import util
import json
# import twitter_spammer as twits
# import facebook_spammer as fcbk

class spammer:

    __palimpsest = None
    __conf       = None

    def __init__(self):
        
        self.__conf = util.conf_handler("../conf/spammer.conf");
        
        pal_file = util.fs_handler( self.__conf.get_conf_value("palimpsest_path") )
        
        self.__palimpsest = json.loads( pal_file.to_string() )


    def spam(self, spam_line = None, spam_url = None, day = None, hour = None, minute = None ):
    
        if( spam_line == None ): 
            program_obj = self.get_on_air_program(day, hour, minute)
            if not program_obj :
                # logger.err("no spam to do now!", -1)
                return None

            spam_line = self.create_on_air_line(program_obj.author, program_obj.title, program_obj.theme)

            # TODO log here

            # twit_spam = twits.twitter_spammer( program_obj.url )
            # twit_spam.social_spam( spam_line )
    
            #    fcbk_spam = twits.twitter_spammer( spam_url )
            #    fcbk_spam.social_spam( spam_line )

    
    def get_on_air_program(self, day, hour, minute):

        pal_reader = palim_reader.palim_reader(self.__palimpsest)
        if pal_reader == None:
            #TODO log errore
            return

        palim_obj = pal_reader.read(day, hour, minute)
        if palim_obj == None:
            # TODO log che non c'e' niente da spammare
            return
        
        return palim_obj
        

    def create_on_air_line(self, author, title, theme):
            
        return "Ora in onda " + str(title) + " con " + str(author) + ": " + str(theme)

    
    # Le notifiche vanno ancora implementate... eccheccazzo
    def cerate_notification_line(self, notif_line, notif_author = None, notif_title = None, notif_theme = None, notif_url = None):
        pass
        
    def get_actual_notification(self, day, hour, minute):
        pass

    ''' If you pass a line or a line and a url it spams that. if you don't pass anything it checks for possible spam on palim '''
    def spam_now( self, spam_line = None, spam_url = None ):
    
        day = time.strftime("%a")
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        
        self.spam( spam_line, spam_url, day, hour, minute )
