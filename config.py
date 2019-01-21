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

    TOKEN = configParser.get('MEDIUM', 'TOKEN')
    CLIENT_ID = configParser.get('MEDIUM', 'CLIENT_ID')
    CLIENT_SECRET = configParser.get('MEDIUM', 'CLIENT_SECRET')
    PUBLICATION = configParser.get('MEDIUM', 'PUBLICATION')

    REDIS_URL = configParser.get('DATABASE', 'REDIS_URL')

    ME_ENDPOINT = configParser.get('ENDPOINTS', 'ME_ENDPOINT')
