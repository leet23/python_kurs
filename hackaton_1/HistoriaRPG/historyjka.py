'''### Historyjka a'la RPG:
- Konieczność użycia modułu `random`.
- Program wypisuje kolejne "przygody" bohatera.
- Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami, np: "(bohater) poszedł do (miejsce) aby (czasownik)." może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
- Historyjka ma mieć zadaną długość i ma być możliwie losowa.'''

import random
names = ['Matylda', 'Johnatan', 'Stefaniusz', 'Santa', 'Euzebiusz']
places = ['Hogward', 'Poznań', 'Santaville', 'New York', 'New Mexico', 'Sim City']
adventures = ['Beat the beast', 'Seek for holy cup', 'Surfing', 'Destroy the village', 'Killing infidels']
roles = ['witch', 'wizard', 'Fighter', 'Mage', 'Thief', 'Ranger']

rand_n = random.choice(names)
rand_p = random.choice(places)
rand_a = random.choice(adventures)
rand_r = random.choice(roles)

story = "Once upon a time there was a " + rand_r + " whose name was " + rand_n + \
        ". He followed the path that led to the " + rand_p + ". An "+ rand_a +" awaits him here."
print(story)