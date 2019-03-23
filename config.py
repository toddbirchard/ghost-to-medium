import os


class Config:
    """Flask Config."""

    # General Configuration
    DEBUG = True
    TESTING = True
    REDIS_URL = os.environ['REDIS_URL']

    # Medium Account & API Vars
    MEDIUM_TOKEN = os.environ['MEDIUM_TOKEN']
    MEDIUM_CLIENT_ID = os.environ['MEDIUM_CLIENT_ID']
    MEDIUM_CLIENT_SECRET = os.environ['MEDIUM_CLIENT_SECRET']
    MEDIUM_PUBLICATION = os.environ['MEDIUM_PUBLICATION']
    MEDIUM_ME_ENDPOINT = os.environ['ME_ENDPOINT']




