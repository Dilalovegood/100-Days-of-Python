alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# todo 1 : create a function called cryptograph() that takes 'original_text' and 'shift_amount' as 2 inputs
# todo 2: inside the cryptograpg() function, shift each letter of the origial_text forwards in the alphabet


def cryptograph(original_text, shift_amount, direction):
    final_text = ""
    for i in original_text:
        if direction == 'encode':
            shift_position = (alphabet.index(i.lower()) +
                              shift_amount) % 26
            final_text += alphabet[shift_position]
        elif direction == 'decode':
            shift_position = (alphabet.index(i.lower()) -
                              # use module%26 or len(alphabet) to anticipate if the shift exceeds the length of the alphabet
                              shift_amount) % 26
            final_text += alphabet[shift_position]

    print(f"The result is: {final_text}")


# todo 3: call the cryptograph() function and pass in the user inputs, also create a program that can repeat the direction again
repeat = "Y"
while repeat.upper() == "Y":
    direction = input(
        "choose one between 'encode' and 'decode' to decrypt: ").lower()
    message = input("Write your message: ")
    shift = int(input("Shift number: "))
    cryptograph(original_text=message, shift_amount=shift, direction=direction)

    repeat = input("Want to try again? Y/N: ")

print("See you in the next project")
