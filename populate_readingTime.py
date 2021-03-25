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
        {'title': 'Fiction1'},
        {'title': 'Fiction2'},
        {'title': 'Fiction3'},
        {'title': 'Fiction4'},
        {'title': 'Fiction5'}]

    books_nonfiction = [
        {'title': 'NON-Fiction'},
        {'title': 'ASLD'},
        {'title': 'ads'},
        {'title': 'the'},
        {'title': 'frg'}]
    
    categories = {'Fiction': {'books': books_fiction},
                  'Non-Fiction': {'books': books_nonfiction},
                  'Science-Fiction': {'books': books_fiction},
                  'Horror': {'books': books_nonfiction},
                  'Fantasy': {'books': books_nonfiction},
                  'Adventure': {'books': books_nonfiction},
                  'Romance': {'books': books_nonfiction},
                  'Dystopian': {'books': books_nonfiction},
                  'Mystery': {'books': books_nonfiction},
                  'History': {'books': books_nonfiction},
                  'Humor': {'books': books_nonfiction}}
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
