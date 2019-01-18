from configparse import ConfigParser
import os

configParser = ConfigParser()
dir_path = os.path.dirname(os.path.realpath(__file__))
configFilePath = (os.path.join(dir_path, 'config.ini'))
configParser.read(configFilePath)

DEBUG = True
TESTING = True
