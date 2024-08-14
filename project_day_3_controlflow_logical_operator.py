height = int(input("Please input your height: "))
bill = 0

if height > 120:
    print("Congrats, you can ride")
    age = int(input("How old r you: "))
    if age < 12:
        bill += 5
        print("You should pay $5")
    elif age > 12 and age < 18:
        bill += 7
        print("You should pay $7")
    else:
        bill += 12
        print("You r an adult so you should pay $12")
    photo = str(input("Do you want take a picture? Y/N: "))
    if photo == "Y" or photo == "y":
        bill += 3
        print(f"Add $3, So you should pay: {bill}")
    else:
        print("Ok")

else:
    print("Sorry, you can't ride")
