print("Welcome to Birthday Party Planner!\n")

# Initialize the Guest List
players = ["Adam", "Sam", "Johnny", "Smith", "Jack", "John", "William", "Tanner"]

# Functions
# Create your add_guest function, that appends the string inside of its parameters to the guest list
def add_guest(name):
    players.append(name)

# Create your remove_guest function, that removes the string inside of its parameters from the guest list
# NOTE: Remember to first check if the guest is in the guest list. If not, you can't remove them
def remove_guest(name):
    if name in players:
        players.remove(name)

# Create your display_guests function, that sorts the guest list, and then prints it out
# SUGGESTION: To make the output look nicer, try to print print an ordered guest list
# ex.
# 1. John
# 2. Sarah
# 3. Bobby
def display_guests():
    players.sort()
    for i in range(len(players)-1):
        print(f"{i+1}. {players[i]}")

# User Interaction
while True:
    action = input("Do you want to 'add', 'remove', 'display', or 'stop'? ")

    if action.lower() == "add":
    # Ask for the guest name, and then call the add_guest function

    elif action.lower() == "remove":
    # Ask for the guest name, and then call the remove_guest function

    elif action.lower() == "display":
    # Call the display_guests function

    elif action.lower() == "stop":
        break

    else:
        print(
            "Invalid choice. Please enter 'add', 'remove', 'display', or 'stop'.")

print("\nHave a great birthday!")
