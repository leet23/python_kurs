wyraz = input("Podaj dowolny ciąg znaków: ")
dlugosc = len(wyraz)
ilosc = wyraz.count("a")
print(ilosc)

#Sprawdzam czy ciąg jest dłuższy niż 5
if dlugosc > 5:
    print("Ten ciąg znaków ma więcej niż 5 znaków")
elif dlugosc == 5:
    print("Ten ciąg znaków ma dokładnie 5 znaków")
else:
    print("Ten ciąg znaków ma mniej niż 5 znaków")

if ilosc >0:
    print("Zamieniam 'a' na 'z'!" , wyraz.replace("a","z"))
else:
    print("Twój ciąg nie zawiera 'a'")