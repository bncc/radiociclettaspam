import json
import util
import logging

class palim_reader:

    __pal_json = None
    __lgr = None

    def __init__(self, pal_json):
        self.__pal_json = pal_json
        self.__lgr = util.log_handler(debug_level = logging.DEBUG)

    def read( self, day_of_week, hour, minute ):

        palim_hour = self.read_by_hour( day_of_week, hour )
        if(palim_hour == None):
            self.__lgr.logger.error( util.create_msg( "Error in loading day "+ day_of_week + " from json" ) )
            return None

        minute_data = None

        try:
            minute_data = palim_hour[minute]
        except KeyError:
            pass
            
        if minute_data == None :
            self.__lgr.logger.warning( util.create_msg("Program not found on "  + str(day_of_week) + " at " + str(hour) + ":" + str(minute)) )
            return
            

        pal_obj = palimpsest_obj(day_of_week, hour, minute)

        pal_obj.from_json(minute_data)

        return pal_obj


    def read_by_hour( self, day_of_week, hour ):
    

        palim_day = self.read_by_day(day_of_week)
        if(palim_day == None):
            return None
        
        try:
            hour_data = palim_day[hour]
        except KeyError:
            pass
        
        if hour_data == None :
            self.__lgr.logger.warning( util.create_msg( "Hour " + str(hour) + " not found on " + str(day_of_week), -1) )
            return
        
        return hour_data

    def read_by_day( self, day_of_week ):
        
        try:
            palim_week = self.__pal_json["Palinsesto"]
        except:
            self.__lgr.logger.exception( util.create_msg( "Error in retrieving object from json" ) )
            return None
        
        try:
            day_data = palim_week[day_of_week]
        except KeyError:
            pass

        if day_data == None :
            self.__lgr.logger.warning( util.create_msg( "Unable to retrieve data" + day_of_week ) )
            return None

        self.__lgr.logger.warning( util.create_msg( "data found " + str(day_data) ) )
        return day_data


class palimpsest_obj:

    __lgr   = None

    day     = None
    hour    = None
    minute  = None
    title   = None
    author  = None
    url     = None
    theme   = None

    def __init__( self, day, hour, minute ):
        self.__logger_handler = util.log_handler(debug_level = logging.DEBUG)
        
        self.day    = day
        self.hour   = hour
        self.minute = minute
        
        
    def from_string( self, program_data_str ):
        
        try:
            program_data = json.loads(program_data_str)
        except:
            self.__lgr.logger.error( util.create_msg( "" ) )
            return

        self.from_json( program_data )
        
        
    def from_json( self, program_data ):

        logh = self.__lgr.logger

        try: self.title = program_data["title"]
        except KeyError:
            logh.exception( util.create_msg( "unable to find title for the program" ) )
            return
        
        try: self.author = program_data["author"]
        except KeyError: 
            logh.exception( util.create_msg( "unable to find author of the program" ) )
            return

        try: self.url = program_data["url"]
        except: 
            logh.warning( util.create_msg( "unable to find url for the program, default will be set" ) )
            # TODO put in config
            self.url = "www.radiocicletta.it"

        try: self.theme = program_data["theme"]
        except: 
            logh.warning( util.create_msg( "unable to find program theme, default will be set" ) )
            # TODO put in config
            self.theme = "ON AIR"

        logh.log( util.create_msg( "All data successfully retrieved" ) )

    def to_string(self):
        
        result  = self.day     + " - "
        result += self.hour    + ":" 
        result += self.minute  + " "
        result += self.title   + " with "
        result += self.author  + ": "
        result += self.theme   + " on "
        result += self.url
        
        self.__lgr.logger.log( util.create_msg( "string created: " + result ) )

        return result

    # TODO someday (some - FAR - day)
    def to_json(self):
        pass
