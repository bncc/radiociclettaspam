import json
import util

class palim_reader:

    __pal_json = None

    def __init__(self, pal_json):
        self.__pal_json = pal_json
        

    def read( self, day_of_week, hour, minute ):

        palim_hour = self.read_by_hour( day_of_week, hour )
        if(palim_hour == None):
            # logger.log("Error in loading day "+ day_of_week + " from json")
            return None

        minute_data = palim_hour[minute]
        
        if minute_data == None :
            return
            # logger.log("Program not found on "  + str(day_of_week) + " at " + str(hour) + ":" + str(minute), -1)

        pal_obj = palimpsest_obj(day_of_week, hour, minute)

        pal_obj.from_json(minute_data)

        return pal_obj

    def read_by_hour( self, day_of_week, hour ):
    
        palim_day = self.read_by_day(day_of_week)
        if(palim_day == None):
            # TODO log here
            return None
        
        hour_data = palim_day[hour]
        
        if hour_data == None :
            # logger.log( "Hour " + str(hour) + " not found on " + str(day_of_week), -1)
            return
        
        return hour_data

    def read_by_day( self, day_of_week ):
        
        try:
            palim_week = self.__pal_json["Palinsesto"]
        except:
            # TODO Log Here
            return None
        
        day_data = palim_week[day_of_week]
        if day_data == None :
            # TODO log here
            return

        return day_data


class palimpsest_obj:

    day     = None
    hour    = None
    minute  = None
    title   = None
    author  = None
    url     = None
    theme   = None

    def __init__( self, day, hour, minute ):
        
        self.day    = day
        self.hour   = hour
        self.minute = minute
        
        
    def from_string( self, program_data_str ):
        
        try:
            program_data = json.loads(program_data_str)
        except:
            return

        self.from_json( program_data )
        
        
    def from_json( self, program_data ):

        try: self.title = program_data["title"]
        except KeyError: return
        
        try: self.author = program_data["author"]
        except KeyError: return

        try: self.url = program_data["url"]
        except KeyError: self.url = "www.radiocicletta.it"

        try: self.theme = program_data["theme"]
        except KeyError: return


    def to_string(self):
        # TODO logger
        
        result  = self.day     + " - "
        result += self.hour    + ":" 
        result += self.minute  + " "
        result += self.title   + " with "
        result += self.author  + ": "
        result += self.theme   + " on "
        result += self.url
        
        print result

        return result

    # TODO someday
    def to_json(self):
        pass
