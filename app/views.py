from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and data
    '''
    title = 'welcome'
    return render_template('index.html', title = title)

@app.route('/articles/<int:articles_id>')
def articles(articles_id):
    '''
    view articles page function that return  articles detail page
    '''
    return render_template('articles.html',id = articles_id)  