from app import app
import urllib.request,json
from .models import source,article

Articles = article.Articles
Source = source.Source

# Getting api key
apiKey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_ARTICLES_BASE_URL']

# Getting the articles url
articles_url = app.config['NEWS_SOURCE_BASE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results        


def process_articles(articles_list):
    '''
    Function that processes the articles result and transform them to a list of objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns:
       articles_results: A list of articles objects   
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        if content:
            articles_object = Articles(id,name,title,description,url,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results        


def get_sources(id):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(id,apikey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            sources_results = process_sources(sources_results_list)


    return sources_results   


def process_sources(sources_list):
    '''
      Function that processes the sources result and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns:
       sources_results: A list of sources objects  
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        country = sources_item.get('country')

        if image:
            sources_results = Source(id,name,description,url,category,country)

    return sources_results        
