import random


def deal_card():
    '''return a random from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
             10]  # 11 is ace card, 10 is king, queen and jack card
    card = random.choice(cards)
    return card


def calculate_score(cards):
    '''Take a list of cards and return score calculated from the cards
    check all the cards on computer/yours, is the total 21 or not?'''
    if sum(cards) and len(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose!, Opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blacjack"
    elif u_score > 21:
        return "You lose"
    elif c_score > 21:
        return "You win!!"
    elif u_score > c_score:
        return "You win!!"
    else:
        return "You Lose"


def play_game():
    computer_card = []
    your_card = []
    computer_score = -1
    your_score = -1
    is_game_over = False

    for _ in range(2):
        computer_card.append(deal_card())
        your_card.append(deal_card())

    while not is_game_over:
        your_score = calculate_score(your_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {your_card}, Your current score: {your_score}")
        print(f"Computer's first cards: {computer_card[0]}")

        if your_card == 0 or computer_card == 0 or your_score > 21:
            is_game_over = True
        else:
            add_card = input("\nget another card? y/n: ").lower()
            if add_card == "y":
                your_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {your_card}, final score: {your_score}")
    print(f"Computer's final hand: {
          computer_card}, final score: {computer_score}")
    print(compare(your_score, computer_score))


while input("Wanna play Blackjack game, y/n: ").lower() == "y":
    play_game()
