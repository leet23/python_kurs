'''subject = input('Przedmiot szkolny: ')
grade = input('Ocena w skali 1-6: ')
subject2 = input('Przedmiot szkolny: ')
grade2 = input('Ocena w skali 1-6: ')
subject3 = input('Przedmiot szkolny: ')
grade3 = input('Ocena w skali 1-6: ')
print(subject + ": " + grade)
print(subject2 + ": " + grade2)
print(subject3 + ": " + grade3)'''

p=1
while(p<=3):
    subject = input('Przedmiot szkolny: ')
    grade = input('Ocena w skali 1-6: ')
    print(subject, "-", grade)
    p=p+1