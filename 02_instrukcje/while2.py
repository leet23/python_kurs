przedmioty = input('podaj przedmioty podzielone myslnikiem')
oceny = input('podaj oceny poddzielone myslnikiem')

przedmioty = przedmioty.split('-')
oceny = oceny.split ('-')

licznik = 0

while licznik <3:
    print(przedmioty[licznik], ' - ', oceny[licznik])
    licznik = licznik + 1