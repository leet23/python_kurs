'''Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.'''

def circle_field(radius):
    pi = 3.14
    return pi * radius ** 2



r = float(input("Podaj promien kola: "))

print(circle_field(r))