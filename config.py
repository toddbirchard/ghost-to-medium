from configparser import ConfigParser
import os


class Config:
    """Flask Config."""
    configParser = ConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFilePath = (os.path.join(dir_path, 'config.ini'))
    configParser.read(configFilePath)

    DEBUG = True
    TESTING = True

    TOKEN = os.environ.get('TOKEN')
    PUBLICATION = os.environ.get('PUBLICATION')
    REDIS_URL = os.environ.get('REDIS_URL')
