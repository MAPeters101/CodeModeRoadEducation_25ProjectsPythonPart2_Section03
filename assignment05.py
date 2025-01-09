print("Welcome to the Gaming Lobby!\n")

# Initialize an empty list to store player names
players = []

# Input Loop
while True:
    # Ask the user to input the name of a player in the gaming lobby
    player = input("Please enter the name of a player: ")
    # Add the player's name to the 'players' list
    players.append(player)
    print(players)

    # Check if the user wants to stop entering names. If so, break from the loop
    ans = input("Would you like to stop entering names? ").upper()
    if ans == "YES" or ans == "Y":
        break


# Player Changes Loop
while True:
    # Ask the user if a new player joined
    ans = input("Did a new player join? ").upper()

    # If the user types 'yes', run the following code
    if ans == "YES" or ans == "Y":
        # Ask for the new player's name and add them to the 'players' list
        player = input("Please enter the name of a player: ")
        players.append(player)

    # Ask the user if a player left
    ans = input("Did a player leave? ").upper()

    # If the user types 'yes', run the following code
    if ans == "YES" or ans == "Y":
        # Ask for the leaving player's name and remove them from the 'players' list if they are in the 'players' list
        player = input("Please enter the name of a player: ")
        # If the name of the leaving player is not in the 'players' list, print a message saying that the player is not in the lobby
        if player in players:
            players.remove(player)
        else:
            print(f"{player} is not in the group.")
    print(players)

    # Ask the user if there are more changes
    ans = input("Are there more changes to be made (No to exit)? ").upper()
    # If they type 'no', break out of the loop
    if ans == "NO" or ans =="N":
        break

print("Gaming Lobby Management Program has ended.")
print(players)
