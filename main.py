import json

with open('dle012.json') as json_data:
    rooms = json.load(json_data)

# Player inventory and current place
inventory = []
current_room = "start"
lives = 3;

# Method to list all possible decisions
def look(dmg):
    room = rooms[current_room]
    global lives
    if dmg:
        print("\nLives: " + str(lives) + "\n" + room["description"])
    else:
        print("\nLives: " + str(lives) + "\n" + room["description"])

    # Exits:
    exits = room["exits"]
    print("You can go to the following directions: " + ", ".join(exits.keys()))

    # Items:
    if len(room["items"]) > 0:
        print(f"You see the following items: {', '.join(room['items'])}")

    # Commands:
    print("\nAvailable commands: 'go [direction]', 'look', 'get [item]', 'inventory', 'quit'")

# Challenge method when before the user can escape
def challenge():
    global current_room
    choice = input("\nEnter yes to escape.\nWhat will you do? ")

    while choice != "yes" and choice != "no":
        choice = input("Invalid input.  Enter yes to escape.")

    if choice == "yes":
        print("Congrats! You escaped the loop.")
    else:
        print("You failed and you find yourself back at the start...")
        current_room = "eerie start"
        look(False)

# Change the location of the player to a different element in the array
def go(direction):
    global current_room
    global lives
    room = rooms[current_room]
    if direction in room["exits"]:
        current_room = room["exits"][direction]

        # Checks if look is necessary
        if current_room == "escape":
            challenge()
        elif rooms[current_room]["damage"] == 1:
            lives -= 1
            if lives == 0:
                print("Game Over!")
            else:
                look(True)
        else:
            look(False)

    else:
        print("You can't go that way!")
        look(False)

# Function to add to the available item to the player inventory list
def get(item):
    room = rooms[current_room]
    if item in room["items"]:
        inventory.append(item)
        room["items"].remove(item)
        print(f"You picked up {item}.")
    else:
        print(f"There is no {item} here.")
    look(False)

# Player inventory getter
def show_inventory():
    if inventory:
        print(f"\nYou are carrying: {', '.join(inventory)}")
    else:
        print("\nYou are not carrying anything.")
    look(False)

# Keeps the game repeating while the player makes an invalid input or has not exited
def play_game():
    print("Welcome to the text adventure!")
    look(False)

    while lives > 0:
        # Prevent another room description if the user runs out of lives
        if lives == 0 or current_room == "escape":
            break
        else:
            command = input("\nWhat do you want to do? ").lower().split()
            if len(command) < 1:
                continue

        action = command[0]
        if action == "go" and len(command) > 1:
            go(command[1])
        elif action == "look":
            look(False)
        elif action == "get" and len(command) > 1:
            get(command[1])
        elif action == "inventory":
            show_inventory()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")
            look(False)

# Main
play_game()
