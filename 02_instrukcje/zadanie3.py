a = int(input("Podaj pierwsza  opinie od 0-10"))
b = int(input("Podaj druga opinie od 0-10"))
c = int(input("Podaj trzecia opinie od 0-10"))

srednia = (a + b + c) /3
if srednia >= 7:
    print('Bardzo Dobra')
elif srednia >= 4:
    print("Przeciętna")
else:
    print("Nie warta uwagi")


