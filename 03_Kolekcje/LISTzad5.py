'''Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

Dorota, Wellman, dziennikarka
Adam, Małysz, sportowiec
Robert, Lewandowski, piłkarz
Krystyna, Janda, aktorka

Wyświetl w sposób przyjazny dla użytkownika'''


tablica = [
    ["Dorota", "Wellmann", "dziennikarka"],
    ["Adam", "Małysz", "Sportowiec"],
    ['Krystyna', 'Janda', 'aktorka'],
    ['Robert', 'Lewandowski', 'piłkarz']
    ]
for row in tablica:
    print(row[0], row[1], "-", row[2])

'''print(tablica[0][0], tablica[0][1], '-', tablica[0][2])
print(tablica[1][0], tablica[1][1], '-', tablica[1][2])
print(tablica[2][0], tablica[2][1], '-', tablica[2][2])
print(tablica[3][0], tablica[3][1], '-', tablica[3][2])'''


