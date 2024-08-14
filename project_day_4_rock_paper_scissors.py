import random

rock = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choices = [rock, paper, scissors]
computer_choice = random.choice(choices)

print("""Hey man, Let's Play Rock Paper Scissors with me
      1. rock
      2. paper
      3. scissors""")
chose = input("What do you choose? 1/2/3: ")
if chose == "1":
    player_choice = rock
elif chose == "2":
    player_choice = paper
elif chose == "3":
    player_choice = scissors
else:
    ("sorry, invalid choice")

print(f"you chose: {player_choice}")
print(f"computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("draw!")
elif (player_choice == rock and computer_choice == scissors) or \
     (player_choice == paper and computer_choice == rock) or \
     (player_choice == scissors and computer_choice == paper):
    print("You win")
else:
    print("you lose!")
