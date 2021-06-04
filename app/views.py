from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news = "they are comming to update us"
    return render_template('index.html' , news=news)