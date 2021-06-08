import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    """
    Test class to tes the behavior of the category class
    """
    def setUp(self):
        """
        Setup method that will run before every test
        """
        self.new_category = Category
        ("Biden Summons Russia for meddling with US election which he won",
        "In a press interview with Journalist at Whitehouse",
        "https://www.nbc.com/live?brand=nbc-news",
        "https://www.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2018/01/26/Foreign/Images/Trump_32516-08392.jpg?t=20170517",
        "2021-01-2T05:28:21Z")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    
