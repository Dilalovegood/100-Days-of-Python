import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '&', '(', ')', '*',
           '+', '@', ';', '[', ']', '\\', '/', '<', '>']

print("Let's Make a Password")
pw_letters = int(input("How many letters would you like in your password?\n"))
pw_numbers = int(input("How many numbers would you like?\n"))
pw_symbols = int(input("How many symbols would you like?\n"))

password_components = []


for i in range(0, pw_letters):
    password_components.append(random.choice(letters))

for i in range(0, pw_numbers):
    password_components.append(random.choice(numbers))

for i in range(0, pw_symbols):
    password_components.append(random.choice(symbols))

random.shuffle(password_components)

password = ""
for char in password_components:
    password += str(char)

print(f"Your password is: {password}")
