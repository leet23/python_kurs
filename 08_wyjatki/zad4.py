numbers = input("Podaj liczby całkowite, które dodasz do listy oddzielając je przecinkiem:")
numbers = numbers.split(",")

list_ex = []
for index, elem in enumerate(numbers):
    try:
        numbers[index] = float(elem)
    except (ValueError, TypeError) as ex:
        list_ex.append(ex)
        numbers[index] = "-"
print(numbers)

while "-" in numbers:
    numbers.remove("-")
print(numbers)

avg = sum(numbers)/len(numbers)
print(avg)
print(list_ex)

with open("error.txt", "w") as f:
    f.write("błąd!")
    for i in list_ex:
        f.write(str(i)+"\n")