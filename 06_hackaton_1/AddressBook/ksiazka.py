'''### Książka adresowa:
Program przechowujący danę kontaktowe znajomych/klientów.
- Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
    - Wyświetlenie wszystkich wpisów
    - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
    - Usunięcie wpisu
    - Zakończenie pracy programu
- Program powinien na starcie mieć już wprowadzone kilka wpisów.'''

def main_menu():
    return ('***** 1 - Show all records  *****'
            '\n***** 2 - Add new record  *****'
            '\n***** 3 - Delete record  *****'
            '\n***** 4 - Exit  *****')

def go_to_selection():
    print()
    print(main_menu())
    print()
    go_to = input('Insert menu number positon (1-4): ')
    if go_to == '1':
        show_all()
    elif go_to == '2':
        add_record()
    elif go_to == '3':
        remove_rec()
    elif go_to == '4':
        exit()
    else:
        print('xXx')


def show_all():
    counter = 1
    for rec in address_book:
        print(counter, rec)
        counter += 1
    go_to_selection()


def add_record():
    counter = input('How many records do you want to add?')
    if not counter.isdigit():
        print('Give me number.')
        againer = input('Do you want to try again? y/n')
        if againer == 'y':
            add_record()
        else:
            go_to_selection()
    else:
        add_ = 1
        while add_ <= int(counter):
            address_book.append({'Surname' : input('Surname: '), 'Name' : input('Name: '), 'Phone' : input('Phone number: '), 'City' : input('City: ')})
            add_ += 1
        show_all()


def remove_rec():
    to_remove = int(input('Which record do you want to remove? '))
    if to_remove > len(address_book):
        print('Record not found!')
        go_back = input('Do you want to try again? y/n: ')
        if go_back == 'y':
            remove_rec()
        else:
            go_to_selection()
    else:
        del address_book[to_remove-1]
        show_all()




def exit():
    print('See you next time!')


address_book = [{'Surname' : 'Kowalski', 'Name' : 'Jan', 'Phone' : '123456789', 'City' : 'Poznań'},
                {'Surname' : 'Mickiewicz', 'Name' : 'Adam', 'Phone' : '231274215', 'City' : 'Wielkopolska'},
                {'Surname' : 'Stefanowicz', 'Name' : 'Stefan', 'Phone' : '702342123', 'City' : 'Warszawa'},
                {'Surname' : 'Adamski', 'Name' : 'Adam', 'Phone' : '666222111', 'City' : 'Szczecin'},
                {'Surname' : 'Józefowicz', 'Name' : 'Józef', 'Phone' : '600555222', 'City' : 'Kraków'}]

go_to_selection()