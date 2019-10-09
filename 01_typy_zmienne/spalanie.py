litry = float(input('Podaj spalanie na litry/100km'))
dystans = 120
cenalitr = 5.04

spalanie = round(cenalitr * dystans / 100 * litry, 2)
print(spalanie)