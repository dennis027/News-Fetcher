from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = "News for a great update"
    return render_template('index.html' , news=news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
