def add(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")
    return n1+n2


def subtract(n1, n2):
    print(f"{n1} - {n2} = {n1 - n2}")
    return n1-n2


def multiply(n1, n2):
    print(f"{n1} * {n2} = {n1 * n2}")
    return n1*n2


def divide(n1, n2):
    # if n2 == 0:
    #     print("tidak bisa dibagi dengan 0")
    #     return n1
    try:
        print(f"{n1} / {n2} = {n1 / n2}")
        return n1/n2
    except Exception as e:  # untuk memperlihatkan errornya
        print(e)
        return n1


operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide}


def input_user(number1, number2, operation):
    if operation == "1":
        result = (operations_dict["+"](number1, number2))
    elif operation == "2":
        result = (operations_dict["-"](number1, number2))
    elif operation == "3":
        result = (operations_dict["*"](number1, number2))
    elif operation == "4":
        result = (operations_dict["/"](number1, number2))
    else:
        print("please pick the right number")
    return result


should_accumulate = True
number1 = int(input("what is the first number: "))

while should_accumulate:
    number2 = int(input("what is the next number: "))
    operation = str(input(
        "\npick an operator \n1. Add (+)\n2. Subtrack (-)\n3. Multiply (*)\n4. Divide (/)\nwhich one 1/2/3/4: "))
    result = input_user(number1, number2, operation)
    is_lanjut = True
    while is_lanjut:
        is_continue = input(
            f"Type y to continue calculating with {result} or type n to restart: ")
        if is_continue == "y":
            print(f"your currently number {result}")
            number1 = result
            is_lanjut = False

        elif is_continue == "n":
            print(
                "Thanks for using calculator by dilalovegood, see you in the next project\n")
            should_accumulate = False
            break
        else:
            print("Please type the right answer")
