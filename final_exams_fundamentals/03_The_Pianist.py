def add(music, my_key, people, part):
    if my_key not in music:
        music[my_key] = [people, part]
        print(f"{my_key} by {people} in {part} added to the collection!")
    else:
        print(f"{my_key} is already in the collection!")
    return music


def remove(music, my_key):
    if my_key in music:
        del music[my_key]
        print(f"Successfully removed {my_key}!")
    else:
        print(f"Invalid operation! {my_key} does not exist in the collection.")
    return music


def change_key(music, my_key, part):
    if my_key in music:
        music[my_key][1] = part
        print(f"Changed the key of {my_key} to {part}!")
    else:
        print(f"Invalid operation! {my_key} does not exist in the collection.")
    return music


my_music = {}
number = int(input())

for _ in range(number):
    key, composer, peace = input().split("|")
    if key not in my_music.keys():
        my_music[key] = [composer, peace]

command = input()

while command != "Stop":
    command = command.split("|")
    action = command[0]

    if action == "Add":
        key = command[1]
        composer = command[2]
        piece = command[3]
        my_music = add(my_music, key, composer, piece)

    elif action == "Remove":
        key = command[1]
        my_music = remove(my_music, key)

    elif action == "ChangeKey":
        key = command[1]
        peace = command[2]
        music = change_key(my_music, key, peace)

    command = input()

for key, item in my_music.items():
    print(f"{key} -> Composer: {item[0]}, Key: {item[1]}")


# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have. On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:

# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"

# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."

# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"


# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.
