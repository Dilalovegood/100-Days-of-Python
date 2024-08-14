# Logic
# Menghitung Badan Ideal Menggunakan Rumusa Broca


tb = float(input("Your height: "))
bb = float(input("Your weight: "))

gender = str(input("""Your gender :
1. female
2. male"""))

if gender == "female" or "1":
    female_weight = (tb - 100) - ((tb - 100) * 10/100)
    print(f"Your ideal weight is : {female_weight}")
elif gender == "male" or "2":
    male_weight = (tb - 100) - ((tb - 100)*15/100)
    print(f"Your ideal weight is : {male_weight}")
else:
    print("Write ur real gender")
