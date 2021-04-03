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
         'synopsis': '''Among the seminal texts of the 20th century, Nineteen Eighty-Four is a rare work
                        that grows more haunting as its futuristic purgatory becomes more real. Published in 1949,
                        the book offers political satirist George Orwell's nightmarish vision of a totalitarian,
                        bureaucratic world and one poor stiff's attempt to find individuality.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False},

        {'title': 'The Giver',
         'author': 'Lois Lowry',
         'synopsis': '''The Giver, the 1994 Newbery Medal winner, has become one of the most influential novels of
                        our time. The haunting story centers on twelve-year-old Jonas, who lives in a seemingly
                        ideal, if colorless, world of conformity and contentment.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Brave New World',
         'author': 'Aldous Huxley',
         'synopsis': '''Brave New World is a dystopian novel by English author Aldous Huxley, written in 1931 and
                        published in 1932. Largely set in a futuristic World State, inhabited by genetically
                        modified citizens and an intelligence-based social hierarchy.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False},

        {'title': 'Fahrenheit 451',
         'author': 'Ray Bradbury',
         'synopsis': '''Guy Montag is a fireman. In his world, where television rules and literature is on the
                        brink of extinction, firemen start fires rather than put them out. His job is to destroy
                        the most illegal of commodities, the printed book, along with the houses in which they
                        are hidden.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Animal Farm',
         'author': 'George Orwell',
         'synopsis': '''A farm is taken over by its overworked, mistreated animals. With flaming idealism and
                        stirring slogans, they set out to create a paradise of progress, justice, and equality.
                        Thus the stage is set for one of the most telling satiric fables ever penned –a razor-edged
                        fairy tale for grown-ups that records the evolution from revolution against tyranny to a
                        totalitarianism just as terrible.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Road',
         'author': 'Cormac McCarthy',
         'synopsis': '''A father and his son walk alone through burned America. Nothing moves in the ravaged landscape
                        save the ash on the wind. It is cold enough to crack stones, and when the snow falls it
                        is gray. The sky is dark. Their destination is the coast, although they don’t know what,
                        if anything, awaits them there.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_romance = [
        {'title': 'Pride and Prejudice',
         'author': 'Jane Austen',
         'synopsis': '''The romantic clash between the opinionated Elizabeth and her proud beau, Mr. Darcy, is a
                        splendid performance of civilized sparring. And Jane Austen's radiant wit sparkles as her
                        characters dance a delicate quadrille of flirtation and intrigue''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Beautiful Disaster',
         'author': 'Jamie McGuire',
         'synopsis': '''The new Abby Abernathy is a good girl. She doesn’t drink or swear, and she has the
                        appropriate number of cardigans in her wardrobe. Abby believes she has enough distance
                        from the darkness of her past, but when she arrives at college with her best friend,
                        her path to a new beginning is quickly challenged''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Twilight',
         'author': 'Stephenie Meyer',
         'synopsis': '''First, Edward was a vampire. Second, there was a part of him—and I didn't know how
                        dominant that part might be—that thirsted for my blood. And third, I was unconditionally
                        and irrevocably in love with him. Deeply seductive and extraordinarily suspenseful,
                        Twilight is a love story with bite.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Outlander',
         'author': 'Diana Gabaldon',
         'synopsis': '''The year is 1945. Claire Randall, a former combat nurse, is just back from the war and
                        reunited with her husband on a second honeymoon when she walks through a standing stone
                        in one of the ancient circles that dot the British Isles.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Bared to You',
         'author': 'Sylvia Day',
         'synopsis': '''Gideon Cross came into my life like lightning in the darkness. He was beautiful and
                        brilliant, jagged and white-hot. I was drawn to him as I'd never been to anything or
                        anyone in my life. I craved his touch like a drug, even knowing it would weaken me.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Gone with the Wind',
         'author': 'Margaret Mitchell',
         'synopsis': '''Scarlett O'Hara, the beautiful, spoiled daughter of a well-to-do Georgia plantation owner,
                        must use every means at her disposal to claw her way out of the poverty she finds herself
                        in after Sherman's March to the Sea.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'A Walk to Remember',
         'author': 'Nicholas Sparks',
         'synopsis': '''There was a time when the world was sweeter...when the women in Beaufort, North Carolina,
                        wore dresses, and the men donned hats...when something happened to a seventeen-year-old
                        boy that would change his life forever.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_humor = [
        {'title': 'The Princess Bride',
         'author': 'William Goldman',
         'synopsis': '''What happens when the most beautiful girl in the world marries the
                        handsomest prince of all time and he turns out to be...well...a lot less than the
                        man of her dreams?''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Catch-22',
         'author': 'Joseph Heller',
         'synopsis': '''Set in Italy during World War II, this is the story of the incomparable, malingering
                        bombardier, Yossarian, a hero who is furious because thousands of people he has never met
                        are trying to kill him. But his real problem is not the enemy—it is his own army, which
                        keeps increasing the number of missions the men must fly to complete their service.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'A Confederacy of Dunces',
         'author': 'John Kennedy Toole',
         'synopsis': '''Meet Ignatius J. Reilly, the hero of John Kennedy Toole's tragicomic tale, A Confederacy
                        of Dunces. This 30-year-old medievalist lives at home with his mother in New Orleans,
                        pens his magnum opus on Big Chief writing pads he keeps hidden under his bed, and relays
                        to anyone who will listen the traumatic experience he once had on a Greyhound Scenicruiser
                        bound for Baton Rouge.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Three Men in a Boat',
         'author': 'Jerome K.Jerome',
         'synopsis': '''Martyrs to hypochondria and general seediness, J. and his friends George and Harris decide
                        that a jaunt up the Thames would suit them to a 'T'. But when they set off, they can hardly
                        predict the troubles that lie ahead with tow-ropes, unreliable weather forecasts and tins
                        of pineapple chunks.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Breakfast of Champions',
         'author': 'Kurt Vonnegut Jr.',
         'synopsis': '''In Breakfast of Champions, one of Kurt Vonnegut’s most beloved characters, the aging
                        writer Kilgore Trout, finds to his horror that a Midwest car dealer is taking his fiction
                        as truth.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Green Eggs and Ham',
         'author': 'Dr. Seuss',
         'synopsis': '''With unmistakable characters and signature rhymes, Dr. Seuss’s beloved favorite has
                        cemented its place as a children’s classic. In this most famous of cumulative tales,
                        the list of places to enjoy green eggs and ham, and friends to enjoy them with, gets
                        longer and longer.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'I am America',
         'author': 'Stephen Colbert',
         'synopsis': '''I Am America (And So Can You!) showcases Stephen Colbert at his most eloquent and
                        impassioned. He is an unrelenting fighter for the soul of America, and in this book he
                        fights the good fight for the traditional values that have served this country so well
                        for so long.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_scifict = [
        {'title': 'The Echo Wife',
         'author': 'Sarah Gailey',
         'synopsis': '''I’m embarrassed, still, by how long it took me to notice. Everything was right there in
                        the open, right there in front of me, but it still took me so long to see the person I
                        had married. It took me so long to hate him.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Winters Orbit',
         'author': 'Everina Maxwell',
         'synopsis': '''While the Iskat Empire has long dominated the system through treaties and political
                        alliances, several planets, including Thea, have begun to chafe under Iskat's rule.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'This Golden Flame',
         'author': 'Emily Victoria',
         'synopsis': '''Orphaned and forced to serve her country’s ruling group of scribes, Karis wants nothing
                        more than to find her brother, long ago shipped away. But family bonds don’t matter to
                        the Scriptorium, whose sole focus is unlocking the magic of an ancient automaton army.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Yesterday is History',
         'author': 'Kosoko Jackson',
         'synopsis': '''A romantic, heart-felt, and whimsical novel about letting go of the past, figuring out
                        what you want in your future, and staying in the moment before it passes you by.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Never Have I Ever',
         'author': 'Isabel Yap',
         'synopsis': '''Amy Whey is proud of her ordinary life and the simple pleasures that come with it—teaching
                        diving lessons, baking cookies for new neighbors, helping her best friend, Charlotte, run
                        their local book club. Her greatest joy is her family: her devoted professor husband,
                        her spirited fifteen-year-old stepdaughter, her adorable infant son.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Glow',
         'author': 'Tim Jordan',
         'synopsis': '''A man battles his addiction to a devastating nanotech drug that steals identities and
                        threatens the survival and succession of mankind as a galactic species.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False},

        {'title': 'The Effort',
         'author': 'Claire Holroyde',
         'synopsis': '''When dark comet UD3 was spotted near Jupiter’s orbit, its existence was largely ignored.
                        But to individuals who knew better — scientists like Benjamin Schwartz, manager of NASA’s
                        Center for Near-Earth Object Studies — the threat this eight-kilometer comet posed to the
                        survival of the human race was unthinkable.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False}]

    books_history = [
        {'title': 'The Princess Spy',
         'author': 'Larry Loftis',
         'synopsis': '''When Aline Griffith was born in a quiet suburban New York hamlet, no one had any idea that
                        she would go on to live “a life of glamour and danger that Ingrid Bergman only played at
                        in Notorious” (Time).''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Icebound',
         'author': 'Andrea Pitzer',
         'synopsis': '''Long before Bering or Amundsen, long before Franklin or Shackleton, there was William
                        Barents, in many ways the greatest polar explorer of them all. In this engrossing narrative
                        of the Far North, enriched by her own adventurous sojourns in the Arctic, Andrea Pitzer
                        brings Barents' three harrowing expeditions to vivid life.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Land',
         'author': 'Simon Winchester',
         'synopsis': '''Land: How the Hunger for Ownership Shaped the Modern World examines in depth how we acquire
                        land, how we steward it, how and why we fight over it, and finally, how we can, and on
                        occasion do, come to share it.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Craft - An American History',
         'author': 'Glenn Adamson',
         'synopsis': '''At the center of the United States' economic and social development, according to
                        conventional wisdom, are industry, commodities, and technology-while craftspeople and
                        handmade objects are relegated to a bygone past.''' ,
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Innocent Witnesses',
         'author': 'Marilyn Yalom',
         'synopsis': '''The violence of war leaves indelible marks, and memories last a lifetime for those who
                        experienced this trauma as children. Marilyn Yalom experienced World War II from afar,
                        safely protected in her home in Washington, DC.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Thin Places',
         'author': 'Kerri Ni Dochartaigh',
         'synopsis': '''Kerri ní Dochartaigh was born in Derry, Northern Ireland, at the very height of the
                        Troubles. She was brought up on a grey and impoverished council estate on the wrong
                        side of town. But for her family, and many others, there was no right side.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Blood and Iron',
         'author': 'Katja Hoyer',
         'synopsis': '''Before 1871, Germany was not a nation but an idea. Its founder, Otto von Bismarck,
                        had a formidable task at hand. How would he bring thirty-nine individual states under
                        the yoke of a single Kaiser.''',
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
         'synopsis': '''Lo Denham is used to being on her own. After her parents died in a tragic car accident,
                        her sister Bea joined the elusive community called The Unity Project, leaving Lo to fend
                        for herself. Desperate not to lose the only family she has left, Lo has spent the last six
                        years trying to reconnect with Bea, only to be met with radio silence.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'What Big Teeth',
         'author': 'Rose Szabo',
         'synopsis': '''Eleanor Zarrin has been estranged from her wild family for years. When she flees boarding
                        school after a horrifying incident, she goes to the only place she thinks is safe: the
                        home she left behind.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Whisper Island',
         'author': 'Carissa Ann Lynch',
         'synopsis': '''For friends Riley, Sam, Mia and Scarlett, their trip to Whisper Island was meant to be a
                        once in a lifetime adventure – just four young women, with everything to live for… But as
                        soon as they arrive things start to go wrong. First there is the unexpected arrival of
                        Sammy’s drug addict brother and his girlfriend Opal – why are they here? And then the
                        deaths begin.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'These Lifeless Things',
         'author': 'Premee Mohamed',
         'synopsis': '''Eva is a survivor. She's not sure what she survived, exactly, only that They invaded
                        without warning, killed nearly all of humanity, and relentlessly attack everyone who's
                        left. All she can do to stay sane, in the blockaded city that's no longer home, is keep a
                        journal about her struggle.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Ash House',
         'author': 'Angharad Walker',
         'synopsis': '''When Eleven-year-old Sol arrives at the Ash House, desperate for a cure for his
                        complex pain syndrome, he finds a community of strange children long abandoned by their
                        mysterious Headmaster.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Spec Ops Z',
         'author': 'Gavin G.Smith',
         'synopsis': '''When Vadim Scorlenski and his elite Spetznaz squad are sent to New York at the height of
                        the Cold War, they’re told it’s a ‘training exercise.’ They discover, too late, that the
                        ‘practice’ chemical weapon they’re carrying is all too real. They go to their deaths...''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Deacon of Wounds',
         'author': 'David Annandale',
         'synopsis': '''The planet of Theotokos is dying. Drought has wiped out all but the capital city of
                        Magerit. Worse, an outbreak of a terrible plague, known as the Grey Tears, ravages its
                        populace. Only the charismatic Arch-Deacon Ambrose stands in the way of desperation and
                        anarchy.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False}]

    books_fantasy = [
        {'title': 'The Witchs Heart',
         'author': 'Genevieve Gornichec',
         'synopsis': '''Angrboda's story begins where most witches' tales end: with a burning. A punishment from
                        Odin for refusing to provide him with knowledge of the future, the fire leaves Angrboda
                        injured and powerless, and she flees into the farthest reaches of a remote forest.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'What Big Teeth',
         'author': 'Rose Szabo',
         'synopsis': '''Eleanor Zarrin has been estranged from her wild family for years. When she flees boarding
                        school after a horrifying incident, she goes to the only place she thinks is safe: the
                        home she left behind.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Game Changer',
         'author': 'Neal Shusterman',
         'synopsis': '''The changes start small, but they quickly spiral out of control as Ash slides into
                        universes where he has everything he’s ever wanted, universes where society is stuck in
                        the past…universes where he finds himself looking at life through entirely different eyes.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Fireheart Tiger',
         'author': 'Aliette de Bodard',
         'synopsis': '''Quiet, thoughtful princess Thanh was sent away as a hostage to the powerful faraway
                        country of Ephteria as a child. Now she’s returned to her mother’s imperial court,
                        haunted not only by memories of her first romance, but by worrying magical echoes of a
                        fire that devastated Ephteria’s royal palace.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Absolute Book',
         'author': 'Elizabeth Knox',
         'synopsis': '''Taryn Cornick believes that the past--her sister's violent death, and her own ill-conceived
                        revenge--is behind her, and she can get on with her life. She has written a successful
                        book about the things that threaten libraries: insects, damp, light, fire, carelessness
                        and uncaring . . . but not all of the attention it brings her is good.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'We are Fire',
         'author': 'Sam Taylor',
         'synopsis': '''In the cold, treacherous land of Vesimaa, children are stolen from their families by a
                        cruel emperor, forced to undergo a horrific transformative procedure, and serve in the
                        army as magical fire-wielding soldiers.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Wide Starlight',
         'author': 'Nicole Lesperance',
         'synopsis': '''According to Arctic legend, if you whistle at the Northern Lights, they'll swoop down and
                        carry you off forever. Sixteen-year-old Eline Davis knows it's true because it happened to
                        her mother. Eli was there that night on the remote glacier in Svalbard, when her mother
                        whistled, then vanished.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_adventure = [
        {'title': 'The Three Musketeers',
         'author': 'Alexandre Dumas',
         'synopsis': '''This swashbuckling epic of chivalry, honor, and derring-do, set in France during the 1620s,
                        is richly populated with romantic heroes, unattainable heroines, kings, queens, cavaliers,
                        and criminals in a whirl of adventure, espionage, conspiracy, murder, vengeance, love,
                        scandal, and suspense.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Ivanhoe',
         'author': 'Walter Scott',
         'synopsis': '''For this novel, Scott moved far away from the setting of his own turbulent time. He went
                        back to the late 12th century, and to England rather than the Scottish settings of all
                        his previous novels. He connected his writing Ivanhoe with his concerns about contemporary
                        events.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Treasure Island',
         'author': 'Robert Louis Stevenson',
         'synopsis': '''Treasure Island has never been surpassed. From the moment young Jim Hawkins first
                        encounters the sinister Blind Pew at the Admiral Benbow Inn until the climactic battle
                        for treasure on a tropic isle, the novel creates scenes and characters that have fired
                        the imaginations of generations of readers.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Kim',
         'author': 'Rudyard Kipling',
         'synopsis': '''Kim is a novel by Nobel Prize-winning English author Rudyard Kipling. It was first
                        published serially in McClure's Magazine from December 1900 to October 1901 as well as
                        in Cassell's Magazine from January to November 1901, and first published in book form
                        by Macmillan & Co. Ltd in October 1901.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Mark of Zorro',
         'author': 'Johnston McCulley',
         'synopsis': '''Old California, in a bygone era of sprawling haciendas and haughty caballeros, suffers
                        beneath the whip-lash of oppression. Missions are pillaged, native peasants are abused,
                        and innocent men and women are persecuted by the corrupt governor and his army.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Lost Horizon',
         'author': 'James Hilton',
         'synopsis': '''Hugh Conway saw humanity at its worst while fighting in the trenches of the First World
                        War. Now, more than a decade later, Conway is a British diplomat serving in Afghanistan
                        and facing war yet again—this time, a civil conflict forces him to flee the country by
                        plane.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True}]

    books_mystery = [
        {'title': 'The Burning Girls',
         'author': 'C.J. Tudor',
         'synopsis': '''Welcome to Chapel Croft. Five hundred years ago, eight protestant martyrs were burned at
                        the stake here. Thirty years ago, two teenage girls disappeared without a trace. And two
                        months ago, the vicar of the local parish killed himself.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Upstairs House',
         'author': 'Julia Fine',
         'synopsis': '''Ravaged and sore from giving birth to her first child, Megan is mostly raising her
                        newborn alone while her husband travels for work. Physically exhausted and mentally
                        drained, she’s also wracked with guilt over her unfinished dissertation—a thesis on
                        mid-century children’s literature.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Lola on Fire',
         'author': 'Rio Youers',
         'synopsis': '''Brody Ellis is short on luck and even shorter on cash to buy the medication his sister
                        Molly needs. Desperate, he robs a convenience store, but on the way out, he bumps into
                        a young woman and loses his wallet. Just when he expects the cops to arrive, the phone
                        rings.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Downstairs Neighbor',
         'author': 'Helen Cooper',
         'synopsis': '''From her downstairs apartment in suburban London, Emma has often overheard the everyday
                        life of the seemingly perfect family upstairs–Steph, Paul and teenage daughter Freya–but
                        has never got to know them.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'Her Every Move',
         'author': 'Kelly Irvin',
         'synopsis': '''When a deadly bomb goes off during a climate change debate, librarian and event coordinator
                        Jackie Santoro becomes the prime suspect. Her motive, according to Detective Avery Wick:
                        to avenge the suicide of her prominent father, who was accused of crimes by a city
                        councilman attending the event.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False},

        {'title': 'The Lady in Residence',
         'author': 'Allison Pittman',
         'synopsis': '''Visit historic American landmarks through the Doors to the Past series. History and today
                        collide in stories full of mystery, intrigue, faith, and romance.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': True},

        {'title': 'The Silent Speak',
         'author': 'Val Collins',
         'synopsis': '''Aoife Walsh has plenty keeping her busy—finalising her divorce from her manipulative
                    husband, settling into her still-new relationship with Detective Conor Moloney, and trying
                    to win the trust of his teenage son.''',
         'personal_rating': 5,
         'global_rating': 4,
         'in_read_list': False}]
    
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
