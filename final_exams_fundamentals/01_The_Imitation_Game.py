def move(my_message, number):
    my_message = my_message[number:] + my_message[:number]
    return my_message


def insert(my_message, position, new_string):
    for i in range(len(my_message) + 1):
        if i == position:
            my_message = my_message[:position] + new_string + my_message[position:]
    return my_message


def change_all(my_message, old, new):
    if old in my_message:
        my_message = my_message.replace(old, new)
    return my_message


message = input()

command = input()

while command != "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = insert(message, index, value)

    elif action == "ChangeAll":
        old_message = command[1]
        new_message = command[2]
        message = change_all(message, old_message, new_message)

    command = input()

print(f"The decrypted message is: {message}")