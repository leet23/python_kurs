# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#
# Co wiemy o tych numerach tych kart?
#
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
# American Express card numbers start with 34 or 37 and have 15 digits
#
# # 4035300539804083  visa
# # 5168441223630339  mastercard
# # 371642190784801   american


def is_visa(is_card, number):
    # All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
    if is_card and (len(number) == 16 or len(number) == 13):
        if number[0] == '4':
            return True

# Master Card
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
# All have 16 digits.
def is_mastercard(is_card, number):
    if is_card and len(number) == 16:
        if int(number[0:2]) in range(51, 56) or int(number[0:4]) in range(2221, 2721):
            return True
# American Express
# American Express card numbers start with 34 or 37 and have 15 digits

def is_american_express(is_card, number):
    if is_card and len(number) == 15:
        if number[0:2] in ("34", "37"):
            return True

#główna część programu

card_number = input("Put your card number here: ")

can_be_card_number = False

if len(card_number) < 13 or len(card_number) > 16:
    print("Wrong number")
else:
    if card_number.isdecimal():
        print("Can be card number")
        can_be_card_number = True
    else:
        print("Not a number")

if is_visa(can_be_card_number, card_number):
    print("I'm Visa")
elif is_mastercard(can_be_card_number, card_number):
    print("I'm mastercard")
elif is_american_express():
    print("I'm american express")
else:
    print("Not known card type")
