
from menu import MENU, resources
money = 0


def show_report(resources):
    stock_water = resources["water"]
    stock_milk = resources["milk"]
    stock_coffee = resources["coffee"]
    print(f"water: {stock_water}ml")
    print(f"milk: {stock_milk}ml")
    print(f"coffee: {stock_coffee}g")
    print(f"money: ${money}")


def price_list():
    print("Price List\nespresso: $1.5\nlatte: $2.5\ncappuccino: $3.0")


def is_resource_enough(order_ingredients):
    """Return True when order can be made, False if ingredients are not enough"""
    is_enough = True  # terjadi jika semua resources cukup untuk order
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_enough = False  # terjadi jika 1 bahan resources tidak cukup untuk order
    return is_enough


def transaction():
    """return the total coins inserted"""
    print("Please insert coins.")
    quarter = int(input("How many quarters? "))*0.25
    dime = int(input("How many dimes? ")) * 0.1
    nickle = int(input("How many nickles? ")) * 0.05
    penny = int(input("How many pennies? ")) * 0.01
    total = quarter + dime + nickle + penny
    return total


def is_transaction_succesful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's no enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy")


is_on = True
while is_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        show_report(resources)
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = transaction()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
