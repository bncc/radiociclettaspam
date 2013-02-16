import pycore

import file_handler
import json_handler
import logger

# TODO Json handler is now an object.
def read_by_day( day_of_week ):
    
    logger.log("searching for day " + day_of_week)

    # TODO recuperare dati da config...
    palim_path = "../conf/palinsesto.json"
    json_han = json_handler.json_handler(palim_path)
    
    # palim_obj = json_handler.from_file(palim_path)

    
    if(palim_obj == None):
        logger.log("Error in loading json from file " + file_name, -1)
        return None
        
    try:
        palim_week = palim_obj["Palinsesto"]
        
    except TypeError:
        logger.err("Error in retrieving day " + day_of_week + " from " + str(json_han.to_string(palim_week)), result.NOT_FOUND )
        return None

    day_data = json_han.array_search(palim_week, day_of_week)
    
    if day_data == None :
        logger.log("Day "  + str(day_of_week) + " not found", -1)
    else:
        logger.log("Day " + str(day_of_week) + " found", 0)

    return day_data


def read_by_hour( day_of_week, hour ):
    
    palim_day = read_by_day(day_of_week)
    
    if(palim_day == None):
        logger.log("Error in loading day "+ day_of_week + " from json")
        return None
    
    hour_data = json_hand.array_search(palim_day, hour)
    
    if hour_data == None :
        logger.log( "Hour " + str(hour) + " not found on " + str(day_of_week), -1)
    else:
        logger.log( "Hour " + str(hour) + " found on " + str(day_of_week), 0)

    return hour_data


def read( day_of_week, hour, minute ):

    palim_hour = read_by_hour( day_of_week, hour )

    if(palim_hour == None):
        logger.log("Error in loading day "+ day_of_week + " from json")
        return None

    program_data = json_han.array_search(palim_hour, minute)
    
    if program_data == None :
        logger.log("Program not found on "  + str(day_of_week) + " at " + str(hour) + ":" + str(minute), -1)
    else:
        logger.log("Found data for program on " + str(day_of_week) + " at " + str(hour) + ":" + str(minute) + "\n" + str(program_data), 0)

    return program_data

