print("Welcome to the Gaming Lobby!\n")

players = []

while True:
    player = input("Please enter the name of a player: ")
    players.append(player)

    ans = input("Would you like to stop entering names? ").upper()
    if ans == "YES" or ans == "Y":
        break

while True:
    ans = input("Did a new player join? ").upper()

    if ans == "YES" or ans == "Y":
        player = input("Please enter the name of a player: ")
        players.append(player)

    ans = input("Did a player leave? ").upper()

    if ans == "YES" or ans == "Y":
        player = input("Please enter the name of a player: ")
        if player in players:
            players.remove(player)
        else:
            print(f"{player} is not in the group.")

    ans = input("Are there more changes to be made (No to exit)? ").upper()
    if ans == "NO" or ans =="N":
        break

print("Gaming Lobby Management Program has ended.")
