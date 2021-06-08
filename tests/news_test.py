import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_news = News
        ("NBC News", 
        "Biden critisized for useless border thef",
        "In an interview with the journal",
        "https://www.nbc.com/pride-is-universal",
        "https://www.nbc.com/the-blacklist/video/godwin-page/4370827",
        "2021-04-03T05:25:21Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

