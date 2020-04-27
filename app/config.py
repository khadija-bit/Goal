class Config:
    '''
    General configuration parent class
    '''
    NEWS_ARTICLES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_SOURCE_BASE_URL = 'http://newsapi.org/v2/everything?sources={}&apiKey={}'
    
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
