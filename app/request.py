from app import app
import urllib.request,json
from .models import news

News = news.News
#getting API key 
api_key = app.config['NEWS_API_KEY']
#getting thr news base url
base_url = app.config['NEWS_API_BASE_URL']

# def get_news(category):
#     '''
#     function getting json reply to our url request
#     '''
#     get_news_url = base_url.format(category,api_key)
#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data=  url.read
#         get_news_response = json.loads(get_news_data)
#         news_result = None
#         if get_news_response['result']:
#             news_results_list= get_news_response['result']
#             news_results = process_results(news_results_list)
#     return news_results 


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):   
    '''
    function that process news results and transforms them into news objects
    '''    
    news_results = []
    for news_item in news_list: 
        source = news_item('source') 
        author = news_item('author') 
        title = news_item('title') 
        description = news_item('description') 
        poster = news_item('poster')

        if poster:
            news_objects = News (source, author, title, description)
            news_results.append(news_objects)

    return news_results        

