password  = input('podaj hasło')
alphanum = password.isalnum()
condition = alphanum and password.islower()

if len(password) < 8:
    print('Hasło jest za krótkie.')

if not alphanum:
    print("Your password should be alphanumeric.")

if password.isalpha():
    print("Should contain digits too")

if password.isdigit():
    print("Should contain letters too")

if condition:
    print('Should contain at least 1 upper')

print("End")