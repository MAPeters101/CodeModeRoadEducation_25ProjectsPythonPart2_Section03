players = ["Adam", "Sam", "Johnny", "Smith", "Jack", "John", "William", "Tanner"]

teamA = players[::2]
teamB = players[1::2]
teamA.sort()
teamB.sort()
print(f"Team A: {teamA}")
print(f"Team B: {teamB}")
