import random

stages = ['''
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

kpop_list = ["enhypen", "txt", "bonedo", "nct", "straykids",
             "seventeen", "ateez", "riize", "newjeans", "ive", "twice", "tws", "aespa", "itzy"]
placeholder = ""
game_over = False
correct_letters = []
lives = 6

chosen_word = random.choice(kpop_list)
for position in range(len(chosen_word)):
    placeholder += "_"
print(f"Name of the K-pop group to guess: {placeholder}")
print("*********************************")


while game_over != True:
    guess = input("Guess the letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("=====================you lose=====================")

    if "_" not in display:
        game_over = True
        print("=====================you win=====================")

    print(stages[lives])
