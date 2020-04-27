from flask import render_template
from app import app
from .requests import get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and data
    '''

    #Getting new news
    cnn_news = get_articles('cnn')
    bbc_news = get_articles('bbc-news')
    fox_news = get_articles('fox-news')
    # aljazeera_news = get_sources('AlJazeera')
    title = "Home - New highlight"
    return render_template('index.html', title = title,cnn = cnn_news,bbc_news = bbc_news,fox_news = fox_news)

@app.route('/articles/<int:articles_id>')
def articles(articles_id):
    '''
    view articles page function that return  articles detail page
    '''
    return render_template('articles.html',id = articles_id)  