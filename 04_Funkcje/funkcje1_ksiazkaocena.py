''' Napisz funkcje ktora pyta uzytkownika o pary ksiazka + ocena i zapisuje w programie'''

def add_book(dict_books):
    counter = int(input("ile ksiazek chcesz dodac: "))
    for _ in range(counter):
        title = input("Podaj tytul: ")
        grade = input("Podaj ocene: ")
        dict_books[title] = grade
    return dict_books
print("*" *10)
def read_book_by_grade(libr):
    g = input("Podaj ocene ksiazki jaka chcesz przeczytac: ")
    if g in libr.values():
        for title, grade in libr.items():
            if grade == g:
                print(title, " - ocena: ", grade)
    else:
        print("Nie ma ksiazki o takiej ocenie")

books= {}
books= add_book(books)
print(books)
read_book_by_grade(books)




print("*" *10)
