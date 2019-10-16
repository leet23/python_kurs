secret_num = 23
loteria = int(input("Zgadnij liczbę ukrytą w programie: "))

while secret_num != loteria:
    print("Liczba", loteria, "nie jest liczbą ukrytą w programie!")
    loteria = int(input("Zgadnij liczbę ukrytą w programie: "))

print('Tak! To ta liczba!')
