from .request import get_news
from flask import render_template
from app import app
# from .request import get_news

# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     # getting popular news
#     # source_news = get_news('source')
#     # print(source_news)


#     title = 'Welcome Home the website of the best News Highlights'
#     return render_template('index.html' , title=title)#)


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,popular = popular_news)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
