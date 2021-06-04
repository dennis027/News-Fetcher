class Config:
    '''
    general configuration class paren
    '''
    NEWS_API_BASE_URL ='https://newsapi.org//3/news/{}?api_key={}'

class ProdConfig:
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