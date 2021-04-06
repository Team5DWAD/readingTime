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
        self.views_module = importlib.import_module('readingTime.views')
        self.views_module_listing = dir(self.views_module)
        
        self.project_urls_module = importlib.import_module('readingTime.urls')
    
    def test_home_exists(self):
        """
        Does the home() view exist in readingTime views.py module?
        """
        name_exists = 'home' in self.views_module_listing
        is_callable = callable(self.views_module.home)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}Home() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Home() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_category_exists(self):
        """
        Does the category() view exist in readingTime views.py module?
        """
        name_exists = 'category' in self.views_module_listing
        is_callable = callable(self.views_module.category)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}category() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}category() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_book_exists(self):
        """
        Does the book() view exist in readingTime views.py module?
        """
        name_exists = 'book' in self.views_module_listing
        is_callable = callable(self.views_module.book)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}book() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}book() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_myBooks_exists(self):
        """
        Does the myBooks() view exist in readingTime views.py module?
        """
        name_exists = 'myBooks' in self.views_module_listing
        is_callable = callable(self.views_module.myBooks)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}myBooks() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}myBooks() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_signIn_exists(self):
        """
        Does the signIn() view exist in readingTime views.py module?
        """
        name_exists = 'signIn' in self.views_module_listing
        is_callable = callable(self.views_module.signIn)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}signIn() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}signIn() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_logOut_exists(self):
        """
        Does the logOut() view exist in readingTime views.py module?
        """
        name_exists = 'logOut' in self.views_module_listing
        is_callable = callable(self.views_module.logOut)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}logOut() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}logOut() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_register_exists(self):
        """
        Does the register() view exist in readingTime views.py module?
        """
        name_exists = 'register' in self.views_module_listing
        is_callable = callable(self.views_module.register)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}register() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}register() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_myAccount_exists(self):
        """
        Does the myAccount() view exist in readingTime views.py module?
        """
        name_exists = 'myAccount' in self.views_module_listing
        is_callable = callable(self.views_module.myAccount)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}myAccount() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}myAccount() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_editProfile_exists(self):
        """
        Does the editProfile() view exist in readingTime views.py module?
        """
        name_exists = 'editProfile' in self.views_module_listing
        is_callable = callable(self.views_module.editProfile)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}editProfile() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}editProfile() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_changePassword_exists(self):
        """
        Does the changePassword() view exist in readingTime views.py module?
        """
        name_exists = 'changePassword' in self.views_module_listing
        is_callable = callable(self.views_module.changePassword)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}changePassword() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}changePassword() function does not exist or will not execute{FAILURE_FOOTER}")

    def test_ContactUs_exists(self):
        """
        Does the ContactUs() view exist in readingTime views.py module?
        """
        name_exists = 'ContactUs' in self.views_module_listing
        is_callable = callable(self.views_module.ContactUs)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}ContactUs() view does not exist{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}ContactUs() function does not exist or will not execute{FAILURE_FOOTER}")
    
    
    
    
    
   
