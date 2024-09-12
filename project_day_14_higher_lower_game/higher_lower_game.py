import random
from art import logo, vs
from dataset import data


# display art
print(logo)


def format_data(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_founder = account["founder"]
    account_country = account["country"]
    return f"{account_name}, founded by {
        account_founder}, from {account_country}."


def check_answer(ask_user, a_users_count, b_users_count):
    """"Take the account data and returns the printable format"""

    if a_users_count > b_users_count:
        return ask_user == "a"
    else:
        return ask_user == "b"


# generate a random account from the game dataset
account_b = random.choice(data)
# Initialize the score
score = 0
game_continue = True
while game_continue:
    account_a = account_b   # making account at position B become the next at position A
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    ask_user = input("Who has more users? Type 'A' or 'B': ").lower()

    # clear the screen
    print("\n"*20)
    print(logo)

    a_users_count = account_a["users"]
    b_users_count = account_b["users"]
    # check if user is correct
    is_correct = check_answer(ask_user, a_users_count, b_users_count)
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
