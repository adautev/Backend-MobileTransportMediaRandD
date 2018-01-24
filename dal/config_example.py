import os


class ConfigExample(object):
    """
    Rename to config.py and Config(object): (:
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'MerryChristmasHackersHoHoHo'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']