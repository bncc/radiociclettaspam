import os
import stat
import shutil
import inspect

import logging
import logging.handlers

import json

"""extends the message by adding filename and line no of the invocation. useful for logging purposes"""
def create_msg( message ):
    
    # retreive the outer frame that calls the actual function
    info = inspect.currentframe().f_back
    
    line = info.f_lineno
    filename = info.f_code.co_filename
    
    return str(filename)+","+str(line)+" "+str(message)


class log_handler:
    
    logger = None
    __handler = None
    
    """Initializes the logger by retrieving as much data as possible from parameters or config files"""
    def __init__( self, module_name = None, log_path = None, debug_level = logging.ERROR, set_formatter = True ):
            
        if not module_name :
            module_name = "spammer"

        self.logger = logging.getLogger( module_name )
        
        # Retrieve data from cfg in order to establish log data
        conf = conf_handler("../conf/logger.conf")
        if not conf : 
            raise ConfNotFound("Unable to find ../conf/logger.conf")

        if not log_path :
            log_path = conf.get_conf_value("log_file_path")
            if not log_path :
                log_path = "/tmp/spammer.log"
        
        max_bytes = conf.get_conf_value("max_log_file_size")
        if not max_bytes :
            max_bytes = "1000000"

        rotating_files = conf.get_conf_value("max_rotating_files")
        if not rotating_files :
            rotating_files = "1"

        self.__handler = logging.handlers.RotatingFileHandler( log_path, maxBytes = max_bytes, backupCount = rotating_files)
        
        if set_formatter :
            log_style = conf.get_conf_value("log_style")
            if not log_style :
                log_style = "%(asctime)s:%(levelname)s %(message)s"
                
            formatter = logging.Formatter( log_style )
            self.__handler.setFormatter( formatter )

        self.logger.addHandler(  self.__handler )
    
        self.logger.setLevel(debug_level)

        if not self.logger : 
            raise LogException('No log created') 
    
""" 
Handles configuration files. 

Searches for configurations in the path passed in creation phase (a good way to create custom configurations is to give the conf file the name of the module).
If is no file is passed it assumes configurations are in ../conf/configurations.conf

It's raccomended NOT to put too many data in the common conf file, since configurations have very basic and simple json structure so it's going to get a mess soon.

TODO: Wouldn't it be nice if it could read some sort of json's xpath?
"""
class conf_handler:

    __conf = None
    __path = "../conf/configurations.conf"
    
    def __init__(self, conf_path = None):
        if conf_path:
            self.__path = conf_path

        file_han = fs_handler(self.__path)
        if file_han == None :
            return
 
        conf_str = file_han.to_string()
        
        try:
            self.__conf = json.loads(conf_str)
        except:
            raise NameError("Unable to parse json")

    def get_conf_value(self, key):
        try:
            return self.__conf[key]
        except:
            return None


class fs_handler:

    __file = None

    def __init__( self, file_path, open_mode = 'r' ): 
                
        try:
            self.__file = open( file_path, open_mode )
        except:
            print create_msg( "error in opening file" )
            return
    
    def __del__( self ):
       try:
           self.__file.close()
       except:
            print create_msg( "error in closing file" )


    def to_string( self ):

        if not self.__file :
            print create_msg( "This object's member file is not initialized" )
            return

        try:
            file_str = self.__file.read()
        except IOError:
            print create_msg( "error in reading file due to IOException" )
            return
        except:
            print create_msg( "error in reading file" )
            return

        return file_str

        
    """Creates a folder in the given path if it does not exists"""
    def create_folder( self, folder_name ):
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except OSError:
                print create_msg( "error in creating dir due to OSException" )


    def get_file_size( file_name ):
	if not os.path.exists(file_name):
            print create_msg( "File does not exists" )
            return -1
	
        file_info = os.stat(file_name)
	return file_info[stat.ST_SIZE]


    def copy_file( file_src, file_dest ):
	print file_src + " " + file_dest
	shcopyfile(file_src, file_dest)
