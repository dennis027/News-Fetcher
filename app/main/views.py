from flask import render_template,request, redirect, url_for
from . import main
from ..requests import get_news_sources

@main.route('/')
def index():
    '''
    view root function that returns the idex page and its data
    '''
    title="Welcome to your favorite news app"
    message='Read your favorite news here'
    # getting the sources
    news_sources=get_news_sources('sources')
    return render_template('index.html', title=title, message=message, sources=news_sources)
