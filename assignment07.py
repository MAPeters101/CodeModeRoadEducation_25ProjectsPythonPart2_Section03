print("Welcome to Birthday Party Planner!\n")

players = ["Adam", "Sam", "Johnny", "Smith", "Jack", "John", "William", "Tanner"]

def add_guest(name):
    players.append(name)

def remove_guest(name):
    if name in players:
        players.remove(name)

def display_guests():
    players.sort()
    for i in range(len(players)-1):
        print(f"{i+1}. {players[i]}")


while True:
    action = input("Do you want to 'add', 'remove', 'display', or 'stop'? ")

    if action.lower() == "add":
        name = input("Please enter the guest's name: ")
        add_guest(name)

    elif action.lower() == "remove":
        name = input("Please enter the guest's name: ")
        remove_guest(name)

    elif action.lower() == "display":
        display_guests()

    elif action.lower() == "stop":
        break

    else:
        print(
            "Invalid choice. Please enter 'add', 'remove', 'display', or 'stop'.")

print("\nHave a great birthday!")
