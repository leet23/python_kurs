'''Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.'''

names = input('podaj imiona podzielone spacja')
names = names.split()
print(names)

for name in names:
    print('hello ', name, '!')

id = 0
while id < len(names):
    print("Hi", names[id])
    id = id +1


