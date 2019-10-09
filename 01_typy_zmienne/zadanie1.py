# zadanie 1
txt = 'ciastko'
print(txt)
middle = len(txt)//2
txt[middle -1] + txt[middle] + txt[middle +2]
print(txt[2:5])
print()
# zadanie 3
quote = "Honesty is the first chapter in the book of wisdom."
print(quote)
print(len(quote)) #1
print(quote[-7:-1]) #2
print(quote[0:25]) #3
print(quote[0:len(quote)//2]) #3
print(quote[-1]) #4
print(quote[len(quote)//2 : : 3]) #5
print(quote[ : : 2]) #6
print(quote[ : : -1]) #7
print(quote.replace("wisdom", "friendship")) #8
print()
# zadanie 5
p='kajak'
print(p)
print(str(p) == str(p)[::-1])