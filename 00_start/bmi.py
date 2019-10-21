def calc_bmi(w, h):
    return w / h **2

def bmi_stat(bmi):
    if bmi < 19:
        print('Niedowaga')
    elif bmi < 25:
        print('Waga Normalna')
    elif bmi < 30:
        print('Nadwaga')
    else:
        print("Otyłość")

h = float(input("Twój wzrost w metrach:"))
w = int(input("Twoja waga:"))
bmi = round(calc_bmi(w, h))
print('Twoje BMI to:', bmi)
bmi_stat(bmi)
