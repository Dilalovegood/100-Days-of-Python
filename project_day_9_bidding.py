import random
bid_dictionary = {}  # key = name, value = bid prices
harry_potter_merch = ["Nimbus 2000", "Voldemort's Wand", "Golden Snitch",
                      "Bag of Gringotts", "Gryffyndor Sword", "Revenclaw's Diadem", "Dumbledore Cup"]

ask_for_bidding = input(f'''Hello Potter Heads \nWe have an authentic {random.choice(harry_potter_merch)} from Harry Potter Merch up for bidding.
Are you interested in placing a bid?  yes or no: ''').lower()

if ask_for_bidding == "no":
    print("Thank you! Maybe next time.")

# ask_for_bidding = input("Are there any other bidders? 'Yes' or 'No':")
# while yes asking again,  if condition == no do comparison and print the winner
while ask_for_bidding == "yes":
    name = input("What's your name?: ")
    bid_price = int(input("What's your bid?: $"))
    bid_dictionary[name] = bid_price
    ask_for_bidding = input(
        "Are there any other bidders? 'Yes' or 'No': ").lower()
    if ask_for_bidding == "no":
        winner_name = ""
        highest_bid = 0
        for name, price in bid_dictionary.items():
            if price > highest_bid:
                highest_bid = price
                winner_name = name

        print(f"The winner is {winner_name} achieving a bid of ${highest_bid}")

        print("Thank you to everyone who participated! See you in the next event")
print(f"\nAnnouncement Board\n{bid_dictionary}")
