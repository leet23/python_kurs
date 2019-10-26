print('|------Welcome to Address Book---------|')
print('|--------------------------------------|')
print('|Please choice from the following:-----|')
print('|----------1: Find   Contacts----------|')
print('|----------2: Add    Contacts----------|')
print('|----------3: Delete Contacts----------|')
print('|----------4: View   Contacts----------|')
print('|----------5: Quit Address Book--------|')


address = {'ray':123456789,'simon':222222222,'alen':88888888}

while 1:
    i = int(input('Can I help you?'))
    if i == 1:
        x=input('What\'s his/her name?')
        if x in address:
            print(address[x])
        else:
            print('Contact does not exist!')

    if i == 2:
        x = (input('New Contact name?'))
        if x in address:
            z = str(input('Contact'+x+' with phone number: '+str(address[x])+ ' address already existed, do you want to override?(Yes/No)'))
            if z == 'yes':
                address[x] = input('New number?')
            elif z == 'no':
                continue
            else:
                print('Please choose yes or no')
        else:
            address[x] = input('New number?')

    if i == 3:
        z = input('Who you want to delete:')
        if z  in address:
            del address[z]
        else:
            print('Contact does not exist!')

    if i == 4:
        print(address)

    if i == 5:
        break
