'''5▹ W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

"""Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""
Zadbaj o sposób wyświetlania np.:

szybko : 5

zbudź : 1'''

''' stworzenie pustego slownika 
slownik = {}
txt = tekst wiersza
txt split podzielenie tekstu na pojedyncze wyrazy
for -> list txt
 czy slowo jest w slowniku
 jestli jest = tak - slownik od slowo = +1 / jak nie ma to dodaj do slownika slowo = 1
 
 ladne wyswietlanie, 
 szybko : 5
 zbudz : 1 itd.'''

dict = {}

text = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

text_list = text.replace(',', '').split()

for word in text_list:
    if word.lower() in dict:
        dict[word.lower()] += 1
    else:
        dict[word.lower()] = 1
print(dict)

for keys, values in dict.items():
    print(keys+':', values)