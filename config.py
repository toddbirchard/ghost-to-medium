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

    TOKEN = os.environ['TOKEN']
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    PUBLICATION = os.environ['PUBLICATION']

    REDIS_URL = os.environ['REDIS_URL']

    ME_ENDPOINT = os.environ['ME_ENDPOINT']
