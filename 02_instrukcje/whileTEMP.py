'''C = 5/9 * (F - 32)'''

tempF = 0
while tempF <= 200:
    tempC= 5 / 9 * tempF - 32
    tempC= round(tempC,2)
    print(tempF,'F =' , tempC, 'C')
    tempF = tempF + 20