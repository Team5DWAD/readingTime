# The purpose of this file is to create realistic and credible data
# to test the database

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'reading_time.settings')

import django
django.setup()
from readingTime.models import Category, Book

def populate():

    books_fiction = [
        {'title': 'BLBL'},
        {'title': 'ASLD'},
        {'title': 'ads'},
        {'title': 'the'},
        {'title': 'frg'}]

    books_nonfiction = [
        {'title': 'NON-Fiction'},
        {'title': 'ASLD'},
        {'title': 'ads'},
        {'title': 'the'},
        {'title': 'frg'}]
    
    categories = {'Fiction': {'books': books_fiction},
                  'Non-Fiction': {'books': books_nonfiction},
                  'Horror': {'books': books_nonfiction},
                  'Medieval': {'books': books_nonfiction},
                  'A': {'books': books_nonfiction},
                  'B': {'books': books_nonfiction},
                  'C': {'books': books_nonfiction},
                  'D': {'books': books_nonfiction},
                  'E': {'books': books_nonfiction},
                  'F': {'books': books_nonfiction}}
    # iterate through the category dictionary and add each category
    for cat, book in categories.items():
        c = add_category(cat)
        for i in book['books']:
            add_book(c,i['title'])


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_book(cat, title):
    b = Book.objects.get_or_create(category=cat, title=title)[0]
    b.save()
    return b
    
   
# Start execution here!
if __name__ == '__main__':
    print('Starting ReadingTime population script...')
    populate()
