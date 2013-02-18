import os
import stat
import shutil
import json

class conf_handler:

    __conf = None
    __path = "../conf/configurations.conf"

    def __init__(self, conf_path = None):
        if conf_path:
            self.__path = conf_path

        file_han = fs_handler(self.__path)
        if file_han == None : return

        conf_str = file_han.to_string()
        try:
            self.__conf = json.loads(conf_str)
        except:
            return

    def get_conf_value(self, key):
        try:
            return self.__conf[key]
        except:
            return None


class fs_handler:

    __file = None

    def __init__( self, file_path ): 
       try:
           self.__file = open( file_path )
       except:
           return
       
    def to_string( self ):
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
