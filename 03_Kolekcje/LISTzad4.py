#Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

elements = int(input("Sprawdzę czy 2 środkowe elementy są takie same. Podaj parzystą liczbę elementów: "))

while elements%2 == 1:
    print("Liczba elementów musi być parzysta")
    elements = int(input("Podaj PARZYSTĄ liczbę elementów "))

print("Teraz podaj po kolei elementy. ")

tabela = []

for i in range(elements):
    wartosc = input("Podaj element: ")
    tabela.append(wartosc)

print("Sprawdźmy czy środkowe elementy twojej tabeli są takie same")

center = int(len(tabela)/2)
cent1 = tabela[center-1]
cent2 = tabela[center]

if cent1 == cent2:
    print("Twoje środkowe elementy są takie same!")
else:
    print("Twoje środkowe elementy są różne.")