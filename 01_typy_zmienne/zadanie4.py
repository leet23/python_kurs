title = input("Tytuł książki:")
name = input("Nazwisko autora:")
page = input("Liczba stron:")
print("sprawdzenie czy Tytuł książki składa się tylko z liter")
print(title.isalpha())
print("sprawdzenie czy nazwisko autora składa się tylko z liter")
print(name.isalpha())
print("sprawdzenie czy liczba stron składa się tylko z cyfer")
print(page.isdigit())
print("poprawienie tytułu ksiązki i nazwisko autora zaczyna sie od dużej litery")
name = name.capitalize()
title = title.capitalize()
print(title, name)
book = title + " " + name + " " + page
print(book)
print(len(book))