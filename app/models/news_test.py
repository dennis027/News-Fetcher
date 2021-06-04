import unittest
from . import News
News = news.News
class NewsTest(unittest.TestCase):
    '''
    testing the behaviour of News class
    '''
    def setUp(self):
        '''
        Setup class that will run before every test
        '''
        self.new_news = News('Slash.org','feedfeeder','dow jones','hello world')

    def test_instance(self):
        self.asserTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()        
