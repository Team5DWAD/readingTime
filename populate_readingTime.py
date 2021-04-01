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
         'author': 'Suzanne Collins',
         'synopsis': '''The hunger games is a novel that unfolds in Panem, an apocalyptic world.
                        The story is centered on a 16-year-old girl, Katniss Everdeen and her struggle
                        for survival in dystopia. Each year, as a punishment for the failed rebellion by District 13,
                        the 12 Panem Districts are forced to pay tribute to the ruthless Capitol regime.''',
        'personal_rating': 5,
        'global_rating': 4,
        'in_read_list': True},

        {'title': '1984',
         'author': 'George Orwell',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Giver',
         'author': 'Lois Lowry',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Brave New World',
         'author': 'Aldous Huxley',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Fahrenheit 451',
         'author': 'Ray Bradbury',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Animal Farm',
         'author': 'George Orwell',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Road',
         'author': 'Cormac McCarthy',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_romance = [
        {'title': 'Pride and Prejudice',
         'author': 'Jane Austen',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Beautiful Disaster',
         'author': 'Jamie McGuire',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Twilight',
         'author': 'Stephenie Meyer',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Outlander',
         'author': 'Diana Gabaldon',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Bared to You',
         'author': 'Sylvia Day',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Gone with the Wind',
         'author': 'Margaret Mitchell',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'A Walk to Remember',
         'author': 'Nicholas Sparks',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_humor = [
        {'title': 'The Princess Bride',
         'author': 'William Goldman',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Catch-22',
         'author': 'Joseph Heller',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'A Confederacy of Dunces',
         'author': 'John Kennedy Toole',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Three Men in a Boat',
         'author': 'Jerome K.Jerome',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Breakfast of Champions',
         'author': 'Kurt Vonnegut Jr.',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Green Eggs and Ham',
         'author': 'Dr. Seuss',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'I am America',
         'author': 'Stephen Colbert',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_scifict = [
        {'title': 'The Echo Wife',
         'author': 'Sarah Gailey',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Winters Orbit',
         'author': 'Everina Maxwell',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'This Golden Flame',
         'author': 'Emily Victoria',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Yesterday is History',
         'author': 'Kosoko Jackson',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Never Have I Ever',
         'author': 'Isabel Yap',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Glow',
         'author': 'Tim Jordan',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Effort',
         'author': 'Claire Holroyde',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_history = [
        {'title': 'The Princess Spy',
         'author': 'Larry Loftis',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Icebound',
         'author': 'Andrea Pitzer',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Land',
         'author': 'Simon Winchester',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Craft: An American History',
         'author': 'Glenn Adamson',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Innocent Witnesses',
         'author': 'Marilyn Yalom',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Thin Places',
         'author': 'Kerri Ni Dochartaigh',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Blood and Iron',
         'author': 'Katja Hoyer',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_nonfict = [
        {'title': 'Four Lost Cities',
         'author': 'Annalee Newitz',
         'synopsis': '''In Four Lost Cities, acclaimed science journalist Annalee Newitz takes readers
                    on an entertaining and mind-bending adventure into the deep history of urban life. ''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Good Girls',
         'author': 'Sonia Faleiro',
         'synopsis': '''The girls' names were Padma and Lalli, but they were so inseparable that people in
                    the village called them Padma Lalli. Sixteen-year-old Padma sparked and burned. Fourteen-year-old
                    Lalli was an incorrigible romantic. They grew up in Katra Sadatganj, an eye-blink of a village in
                    western Uttar Pradesh crammed into less than one square mile of land. It was out in the fields,
                    in the middle of mango season, that the rumors started.''',
,
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Rope',
         'author': 'Alex Tresniowski',
         'synopsis': '''In the tranquil seaside town of Asbury Park, New Jersey, ten-year-old schoolgirl Marie Smith is brutally murdered.
                    Small town officials, unable to find the culprit, call upon the young manager of a New York detective agency for help.
                    It is the detective’s first murder case, and now, the specifics of the investigation and daring sting operation that
                    caught the killer is captured in all its rich detail for the first time.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Mike Nichols - A Life',
         'author': 'Mark Harris',
         'synopsis': '''Mike Nichols burst onto the scene as a wunderkind: while still in his twenties, he was half of a hit improv duo with
                    Elaine May that was the talk of the country. Next he directed four consecutive hit plays, won back-to-back Tonys, ushered in
                    a new era of Hollywood moviemaking with Who's Afraid of Virginia Woolf?, and followed it with The Graduate, which won him an
                    Oscar and became the third-highest-grossing movie ever. At thirty-five, he lived in a three-story Central Park West penthouse,
                    drove a Rolls-Royce, collected Arabian horses, and counted Jacqueline Kennedy, Elizabeth Taylor, Leonard Bernstein, and Richard
                    Avedon as friends.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Chatter',
         'author': 'Ethan Kross',
         'synopsis': '''Tell a stranger that you talk to yourself, and you're likely to get written off as eccentric. But the truth is that we all
                    have a voice in our head. When we talk to ourselves, we often hope to tap into our inner coach but find our inner critic instead.
                    When we're facing a tough task, our inner coach can buoy us up: Focus--you can do this. But, just as often, our inner critic sinks
                    us entirely: I'm going to fail. They'll all laugh at me. What's the use?''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'White Feminism',
         'author': 'Koa Beck',
         'synopsis': '''Join the important conversation about race, empowerment, and inclusion in the United States with this powerful new feminist classic
                    and rousing call for change. Koa Beck, writer and former editor-in-chief of Jezebel, boldly examines the history of feminism,
                    from the true mission of the suffragettes to the rise of corporate feminism with clear-eyed scrutiny and meticulous detail.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'American Baby',
         'author': 'Gabrielle Glaser',
         'synopsis': '''In 1960s America, at the height of the Baby Boom, women were encouraged to stay home and raise large families, but sex and childbirth
                    were taboo subjects. Premarital sex was not uncommon, but birth control was hard to get and abortion was illegal. In 1961, sixteen-year-old
                    Margaret Erle fell in love and became pregnant. Her unsympathetic family sent her to a maternity home.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_horror = [
        {'title': 'The Project',
         'author': 'Courtney Summers',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'What Big Teeth',
         'author': 'Rose Szabo',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Whisper Island',
         'author': 'Carissa Ann Lynch',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'These Lifeless Things',
         'author': 'Premee Mohamed',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Ash House',
         'author': 'Angharad Walker',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Spec Ops Z',
         'author': 'Gavin G.Smith',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Deacon of Wounds',
         'author': 'David Annandale',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_fantasy = [
        {'title': 'The Witchs Heart',
         'author': 'Genevieve Gornichec',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'What Big Teeth',
         'author': 'Rose Szabo',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Game Changer',
         'author': 'Neal Shusterman',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Fireheart Tiger',
         'author': 'Aliette de Bodard',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Absolute Book',
         'author': 'Elizabeth Knox',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'We are Fire',
         'author': 'Sam Taylor',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Wide Starlight',
         'author': 'Nicole Lesperance',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_adventure = [
        {'title': 'The Three Musketeers',
         'author': 'Alexandre Dumas',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Ivanhoe',
         'author': 'Walter Scott',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Treasure Island',
         'author': 'Robert Louis Stevenson',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Kim',
         'author': 'Rudyard Kipling',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Call of the Wind',
         'author': 'Jack London',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Mark of Zorro',
         'author': 'Johnston McCulley',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Lost Horizon',
         'author': 'James Hilton',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_mystery = [
        {'title': 'The Burning Girls',
         'author': 'C.J. Tudor',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Upstairs House',
         'author': 'Julia Fine',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Lola on Fire',
         'author': 'Rio Youers',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Downstairs Neighbor',
         'author': 'Helen Cooper',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Her Every Move',
         'author': 'Kelly Irvin',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Lady in Residence',
         'author': 'Allison Pittman',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Silent Speak',
         'author': 'Val Collins',
         'synopsis': 'temp',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]
    
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
            add_book(c,i['title'],i['author'],i['synopsis'],i['personal_rating'],i['global_rating'],i['in_read_list'])


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_book(cat, title, author, synopsis, personal_rating, global_rating, in_read_list):
    b = Book.objects.get_or_create(category=cat, title=title, author=author, synopsis=synopsis,
                                   personal_rating=personal_rating, global_rating=global_rating,
                                   in_read_list=in_read_list)[0]
    b.save()
    return b


# Start execution here!
if __name__ == '__main__':
    print('Starting ReadingTime population script...')
    populate()
