# The purpose of this file is to create realistic and credible data
# to test the database

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'reading_time.settings')

import django
django.setup()
from readingTime.models import Category, Book

def populate():

    books_dystopian = [
        {'title': 'The Hunger Games',
         'author': 'Suzanne Collins'},
        {'title': '1984',
         'author': 'George Orwell'},
        {'title': 'The Giver',
         'author': 'Lois Lowry'},
        {'title': 'Brave New World',
         'author': 'Aldous Huxley'},
        {'title': 'Fahrenheit 451',
         'author': 'Ray Bradbury'},
        {'title': 'Animal Farm',
         'author': 'George Orwell'},
        {'title': 'The Road',
         'author': 'Cormac McCarthy'}]

    books_romance = [
        {'title': 'Pride and Prejudice',
         'author': 'Jane Austen'},
        {'title': 'Beautiful Disaster',
         'author': 'Jamie McGuire'},
        {'title': 'Twilight',
         'author': 'Stephenie Meyer'},
        {'title': 'Outlander',
         'author': 'Diana Gabaldon'},
        {'title': 'Bared to You',
         'author': 'Sylvia Day'},
        {'title': 'Gone with the Wind',
         'author': 'Margaret Mitchell'},
        {'title': 'A Walk to Remember',
         'author': 'Nicholas Sparks'}]

    books_humor = [
        {'title': 'The Princess Bride',
         'author': 'William Goldman'},
        {'title': 'Catch-22',
         'author': 'Joseph Heller'},
        {'title': 'A Confederacy of Dunces',
         'author': 'John Kennedy Toole'},
        {'title': 'Three Men in a Boat',
         'author': 'Jerome K.Jerome'},
        {'title': 'Breakfast of Champions',
         'author': 'Kurt Vonnegut Jr.'},
        {'title': 'Green Eggs and Ham',
         'author': 'Dr. Seuss'},
        {'title': 'I am America',
         'author': 'Stephen Colbert'}]

    books_scifict = [
        {'title': 'The Echo Wife',
         'author': 'Sarah Gailey'},
        {'title': 'Winters Orbit',
         'author': 'Everina Maxwell'},
        {'title': 'This Golden Flame',
         'author': 'Emily Victoria'},
        {'title': 'Yesterday is History',
         'author': 'Kosoko Jackson'},
        {'title': 'Never Have I Ever',
         'author': 'Isabel Yap'},
        {'title': 'Glow',
         'author': 'Tim Jordan'},
        {'title': 'The Effort',
         'author': 'Claire Holroyde'}]

    books_history = [
        {'title': 'The Princess Spy',
         'author': 'Larry Loftis'},
        {'title': 'Icebound',
         'author': 'Andrea Pitzer'},
        {'title': 'Land',
         'author': 'Simon Winchester'},
        {'title': 'Craft: An American History',
         'author': 'Glenn Adamson'},
        {'title': 'Innocent Witnesses',
         'author': 'Marilyn Yalom'},
        {'title': 'Thin Places',
         'author': 'Kerri Ni Dochartaigh'},
        {'title': 'Blood and Iron',
         'author': 'Katja Hoyer'}]

    books_nonfict = [
        {'title': 'Four Lost Cities',
         'author': 'Annalee Newitz'},
        {'title': 'The Good Girls',
         'author': 'Sonia Faleiro'},
        {'title': 'The Rope',
         'author': 'Alex Tresniowski'},
        {'title': 'Mike Nichols: A Life',
         'author': 'Mark Harris'},
        {'title': 'Chatter',
         'author': 'Ethan Kross'},
        {'title': 'White Feminism',
         'author': 'Koa Beck'},
        {'title': 'American Baby',
         'author': 'Gabrielle Glaser'}]

    books_horror = [
        {'title': 'The Project',
         'author': 'Courtney Summers'},
        {'title': 'What Big Teeth',
         'author': 'Rose Szabo'},
        {'title': 'Whisper Island',
         'author': 'Carissa Ann Lynch'},
        {'title': 'These Lifeless Things',
         'author': 'Premee Mohamed'},
        {'title': 'The Ash House',
         'author': 'Angharad Walker'},
        {'title': 'Spec Ops Z',
         'author': 'Gavin G.Smith'},
        {'title': 'Deacon of Wounds',
         'author': 'David Annandale'}]

    books_fantasy = [
        {'title': 'The Witchs Heart',
         'author': 'Genevieve Gornichec'},
        {'title': 'What Big Teeth',
         'author': 'Rose Szabo'},
        {'title': 'Game Changer',
         'author': 'Neal Shusterman'},
        {'title': 'Fireheart Tiger',
         'author': 'Aliette de Bodard'},
        {'title': 'The Absolute Book',
         'author': 'Elizabeth Knox'},
        {'title': 'We are Fire',
         'author': 'Sam Taylor'},
        {'title': 'The Wide Starlight',
         'author': 'Nicole Lesperance'}]

    books_adventure = [
        {'title': 'The Three Musketeers',
         'author': 'Alexandre Dumas'},
        {'title': 'Ivanhoe',
         'author': 'Walter Scott'},
        {'title': 'Treasure Island',
         'author': 'Robert Louis Stevenson'},
        {'title': 'Kim',
         'author': 'Rudyard Kipling'},
        {'title': 'The Call of the Wind',
         'author': 'Jack London'},
        {'title': 'The Mark of Zorro',
         'author': 'Johnston McCulley'},
        {'title': 'Lost Horizon',
         'author': 'James Hilton'}]

    books_mystery = [
        {'title': 'The Burning Girls',
         'author': 'C.J. Tudor'},
        {'title': 'The Upstairs House',
         'author': 'Julia Fine'},
        {'title': 'Lola on Fire',
         'author': 'Rio Youers'},
        {'title': 'The Downstairs Neighbor',
         'author': 'Helen Cooper'},
        {'title': 'Her Every Move',
         'author': 'Kelly Irvin'},
        {'title': 'The Lady in Residence',
         'author': 'Allison Pittman'},
        {'title': 'The Silent Speak',
         'author': 'Val Collins'}]
    
    categories = {'Non-Fiction': {'books': books_nonfict},
                  'Science-Fiction': {'books': books_scifict},
                  'Horror': {'books': books_horror},
                  'Fantasy': {'books': books_fantasy},
                  'Adventure': {'books': books_adventure},
                  'Romance': {'books': books_romance},
                  'Dystopian': {'books': books_dystopian},
                  'Mystery': {'books': books_mystery},
                  'History': {'books': books_history},
                  'Humor': {'books': books_humor}}
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
