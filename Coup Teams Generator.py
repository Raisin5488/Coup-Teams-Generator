import random
import os
import sys
import copy

"""randomly generates 2 teams
4 players: players sees 1 other player
6 players: players sees 1.5 other players
8 players: players sees 2 other players"""

os.system("color 70")

spade_symbol = "♠"
heart_symbol = "♡"
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getTeam(list, number):
    for i in list:
        if i == number:
            return f"Spade {spade_symbol}"
    return f"Heart {heart_symbol}"

def getSymbol(list, number):
    for i in list:
        if i == number:
            return f"{spade_symbol}"
    return f"{heart_symbol}"
while True:
    cls()
    print("Start of Random Modified Coup.\n")
    correct_number = True
    while correct_number:
        print("Enter number of players (4, 6, 8):\n")
        temp = sys.stdin.readline()
        if temp == "4\n"or temp == "6\n" or temp == "8\n":
            correct_number = False
        else:
            print("Invalid number, try again.")

    if temp == "4\n":
        player_number = 4
        toSeeOne = [0, 1, 2, 3]
        spade = [0, 1, 2, 3]
        heart = []
        temp_list_copy = [0, 1, 2, 3]
    elif temp == "6\n":
        player_number = 6
        toSeeOne = [0, 1, 2, 3, 4, 5]
        spade = [0, 1, 2, 3, 4, 5]
        heart = []
        temp_list_copy = [0, 1, 2, 3, 4, 5]
        for i in range(3):
            toSeeOne.remove(random.choice(toSeeOne))
    elif temp == "8\n":
        player_number = 8
        spade = [0, 1, 2, 3, 4, 5, 6, 7]
        heart = []
        temp_list_copy = [0, 1, 2, 3, 4, 5, 6, 7]
        toSeeOne = []
    
    for i in range(int(player_number/2)):
        temp = random.choice(spade)
        heart.append(temp)
        spade.remove(temp)

    spade.sort()
    heart.sort()
    adjacencyList = []

    for i in range(player_number):
        peekNumber = 2
        for j in toSeeOne:
            if i == j:
                peekNumber = 1
        toSee = []
        templist = copy.deepcopy(temp_list_copy)
        templist.remove(i)
        if peekNumber == 1:
            temp = random.choice(templist)
            toSee.append(temp)
        else:
            temp = random.choice(templist)
            toSee.append(temp)
            templist.remove(temp)
            toSee.append(random.choice(templist))
        toSee.sort()
        adjacencyList.append(toSee)
    
    for i in range(0, player_number):
        print("Press ENTER as player {}.".format(i))
        input()
        cls()
        print("You are player {}, team: {}\n".format(i, getTeam(spade, i)))
        for j in adjacencyList[i]:
            print("Player {} is team: {}.".format(j, getTeam(spade, j)))
        print("\n" * 3)
        print("Press ENTER to clear screen, then pass to next player.")
        input()
        cls()
    print("All players information given, press ENTER twice to see teams.")
    input()
    print("Press ENTER again.")
    input()
    cls()
    print(f"Team spade {spade_symbol}: {spade}")
    print(f"Team heart {heart_symbol}: {heart}\n")
    
    toPrint = "    "
    line = "    "
    for i in range(player_number):
        toPrint += f" {i}{getSymbol(spade, i)}"
        line += "___"
    print(toPrint)
    print(line)
    for i in range(player_number):
        toPrint = ""
        for j in range(player_number):
            if j in adjacencyList[i]:
                toPrint += str(j) + getSymbol(spade, j) + " "
            else:
                toPrint += "-- "
        print("{}{} | {}".format(i, getSymbol(spade, i), toPrint))
    print("\n" * 5)
    print("End of game, press ENTER twice to exit.")
    input()
    print("Press ENTER again.")
    input()

