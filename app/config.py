import os

class Config:
    """
    General configuration parent class
    """
    # pass
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    SECRET_KEY =  os.environ.get("SECRET_KEY")
    '''
    production configuration child class
    '''
    pass


class DevConfig:
    '''
    Development configuration child class
    '''
    pass


    DEBUG = True