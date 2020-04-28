from flask import render_template
from app import app
from .requests import get_sources,get_article,get_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and data
    '''
    General_news = get_sources()
    title = "Home - New highlight"
    return render_template('index.html', title = title,news = General_news)

@app.route('/articles/<id>')
def articles(id):
    '''
    view articles page function that return  articles detail page
    '''
    articles = get_article(id)
    title = f'(articles.title)'
    cnn_news = get_articles('cnn') 
    # BBC_News =get_articles('bbc_news')
    return render_template('articles.html',title = title, articles = articles,cnn = cnn_news)  