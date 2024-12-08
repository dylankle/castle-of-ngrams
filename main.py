import json

with open('dle012.json') as json_data:
    rooms = json.load(json_data)

# Player inventory and current place
inventory = []
current_room = "start"

# Method to list all possible decisions
def look():
    room = rooms[current_room]
    print("\n" + room["description"])

    # Exits:
    exits = room["exits"]
    print("You can go to the following directions: " + ", ".join(exits.keys()))

    # Items:
    if len(room["items"]) > 0:
        print(f"You see the following items: {', '.join(room['items'])}")

    # Commands:
    print("\nAvailable commands: 'go [direction]', 'look', 'get [item]', 'inventory', 'quit'")

# Change the location of the player to a different element in the array
def go(direction):
    global current_room
    room = rooms[current_room]
    if direction in room["exits"]:
        current_room = room["exits"][direction]
        look()
    else:
        print("You can't go that way!")
        look()

# Function to add to the available item to the player inventory list
def get(item):
    room = rooms[current_room]
    if item in room["items"]:
        inventory.append(item)
        room["items"].remove(item)
        print(f"You picked up {item}.")
    else:
        print(f"There is no {item} here.")
    look()

# Player inventory getter
def show_inventory():
    if inventory:
        print(f"\nYou are carrying: {', '.join(inventory)}")
    else:
        print("\nYou are not carrying anything.")
    look()

# Keeps the game repeating while the player makes an invalid input or has not exited
def play_game():
    print("Welcome to the text adventure!")
    look()

    while True:
        command = input("\nWhat do you want to do? ").lower().split()
        if len(command) < 1:
            continue

        action = command[0]
        if action == "go" and len(command) > 1:
            go(command[1])
        elif action == "look":
            look()
        elif action == "get" and len(command) > 1:
            get(command[1])
        elif action == "inventory":
            show_inventory()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")
            look()

# Main
play_game()