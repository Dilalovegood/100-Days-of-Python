import random

number = random.randint(1, 101)


def easy():
    attempts = 10
    print("You have 10 attemps to guess the right number")
    while attempts > 0:
        guess_num = int(input("make a guess: "))
        if guess_num == number:
            print(f"You got it, the answer is {number}")
            break
        elif guess_num > number:
            print("Too high")
        elif guess_num < number:
            print("Too low")

        attempts -= 1
        if attempts > 0:
            print(f"You have {
                attempts} attempts remaining to guess the number")
        else:
            print(
                f"Sorry, you have reached the trial limit. The number was {number}")


def hard():
    attempts = 5
    print("You have 5 attemps to guess the right number")
    while attempts > 0:
        guess_num = int(input("make a guess: "))
        if guess_num == number:
            print(f"You got it, the answer is {number}")
            break
        elif guess_num > number:
            print("Too high")
        elif guess_num < number:
            print("Too low")

        attempts -= 1
        if attempts > 0:
            print(f"You have {
                attempts} attempts remaining to guess the number")
        else:
            print(
                f"Sorry, you have reached the trial limit. The number was {number}")


print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if level == "easy":
    easy()
elif level == "hard":
    hard()
else:
    print("invalid choice")
