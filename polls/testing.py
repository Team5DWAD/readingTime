import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}ReadingTime TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

    
class view_test(TestCase):
    """
    Testing for views and ensuring they are executable.
    """
    def setUp(self):
        self.views_module = importlib.import_module('polls.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('polls.urls')
    
    def test_index_exists(self):
        """
        Does the home() view exist in readingTime views.py module?
        """
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.index)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}index() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}index() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_detail_exists(self):
        """
        Does the detail() view exist in readingTime views.py module?
        """
        name_exists = 'detail' in self.views_module_listing
        is_callable = callable(self.views_module.detail)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}detail() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}detail() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_results_exists(self):
        """
        Does the results() view exist in readingTime views.py module?
        """
        name_exists = 'results' in self.views_module_listing
        is_callable = callable(self.views_module.results)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}results() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}results() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_vote_exists(self):
        """
        Does the vote() view exist in readingTime views.py module?
        """
        name_exists = 'vote' in self.views_module_listing
        is_callable = callable(self.views_module.vote)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}vote() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}vote() function does not exist or will not execute{FAILURE_FOOTER}")

    
    
