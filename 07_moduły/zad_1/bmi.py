def calc_bmi(w, h):
    return round(w / (h **2), 3)

def bmi_stat(bmi):
    if bmi < 19:
        return 'Niedowaga'
    elif bmi < 25:
        return 'WagaNormalna'
    elif bmi < 30:
        return 'Nadwaga'
    else:
        return "Otylosc"

def main():
    result = calc_bmi(56,1.75)
    print(bmi_stat(result))

if __name__ == "__main__":
    main()