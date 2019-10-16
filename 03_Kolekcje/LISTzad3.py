test = []
counter = int(input('ile liczb chcesz dodac'))
for _ in range(counter):
    tmp = input('podaj dowolny ciag znakow: ')
    #zapytaj o kolejna liczbe
    test.append(tmp)


print ("The original list is : " +  str(test))
rez = [ test[0], test[-1] ]

#lub

if test[0] == test[-1]:
    print('pierwszy i ostatni element sa takie same')
else:
    print('elementy nie sa takie same')

