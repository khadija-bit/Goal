import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_ARTICLES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    
    


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
