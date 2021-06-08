from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_news, get_category,search_news

@main.route('/')
def index():
    
    #view root page function that returns the index page and its data
    
    # Getting various news categories
    general_news = get_sources( 'general' )
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    health_news = get_sources('health')
    technology_news = get_sources('technology')
    sports_news = get_sources('sports')

    title = "Eagle NewsHub"
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name= search_news))
    return render_template('index.html', title=title, general = general_news,
    business = business_news, entertainment = entertainment_news, health = health_news, technology = technology_news, sports = sports_news)

@main.route('/news/<id>')
def news(id):
    
    #view root page function that returns the news page and its data
    
    news_articles = get_news(id)
       
    return render_template('news.html', news = news_articles)

    

@main.route('/categories/<category>')
def general(category):
    
    #view root page function that returns the categories page and its data
    
    news_categories_articles = get_category(category)

    return render_template('general.html', general = news_categories_articles)


@main.route('/categories/<category>')
def business(category):
    
    #view root page function that returns the categories page and its data
    
    news_categories_articles = get_category(category)

    return render_template('business.html', business = news_categories_articles)


@main.route('/categories/<category>')
def entertainment(category):
    
    #view root page function that returns the categories page and its data
    
    news_categories_articles = get_category(category)

    return render_template('entertainment.html', entertainment=news_categories_articles)


@main.route('/categories/<category>')
def health(category):
    
    #view root page function that returns the categories page and its data
    
    news_categories_articles = get_category(category)

    return render_template('health.html', health = news_categories_articles)

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_mnews = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',mnews = searched_mnews)    