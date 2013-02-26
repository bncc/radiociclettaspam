import os
import stat
import shutil
import inspect

import logging
import logging.handlers

import json

def create_msg( message ):
    
    # retreive the outer frame that calls the actual function
    info = inspect.currentframe().f_back
    
    line = info.f_lineno
    filename = info.f_code.co_filename
    
    return str(filename)+","+str(line)+" "+str(message)

class log_handler:
    
    logger = None
    __handler = None
    
    def __init__( self, module_name = None, log_path = None, debug_level = logging.ERROR, set_formatter = True ):
            
        if not module_name :
            module_name = "spammer"

        self.logger = logging.getLogger( module_name )
        
        # Retrieve data from cfg in order to establish log data
        conf = conf_handler("../conf/logger.cfg")

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
            # TODO log
            return

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
           return
       
    def __del__( self ):
       try:
           self.__file.close()
       except:
           return 

    def to_string( self ):

        if not self.__file : 
            return

        try:
            file_str = self.__file.read()
        except IOError:
            return None

        return file_str
        
    """Creates a folder in the given path if it does not exists"""
    def create_folder( self, folder_name ):
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except OSError:
                return None

    def get_file_size( file_name ):
	if not os.path.exists(file_name):
		return 0
	
        file_info = os.stat(file_name)
	return file_info[stat.ST_SIZE]

    def copy_file( file_src, file_dest ):
	print file_src + " " + file_dest
	shutil.copyfile(file_src, file_dest)
