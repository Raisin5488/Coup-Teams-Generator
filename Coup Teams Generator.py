import random
import os
import sys
import copy

"""randomly generates 2 teams
4 players: players sees [0, 1, 1, 1] other player
6 players: players sees [1, 1, 1, 2, 2, 2] other players
8 players: players sees [2, 2, 2, 2, 2, 2, 2, 2] other players"""

os.system("color 70")

spade_symbol = "♠"
heart_symbol = "♡"

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getTeam(number):
    if master_dict[number][0] == "spade":
        return f"Spade {spade_symbol}"
    else:
        return f"Heart {heart_symbol}"

def getSymbol(number):
    if master_dict[number][0] == "spade":
        return f"{spade_symbol}"
    else:
        return f"{heart_symbol}"

def makeTeamList(team):
    list = []
    for i in master_dict:
        if master_dict[i][0] == team:
            list.append(master_dict[i][2])
    return list

while True:
    cls()
    print("Start of Discord Coup.\n")
    correct_number = True
    while correct_number:
        print("Enter number of players (4, 6, 8):")
        player_number = sys.stdin.readline()
        if player_number == "4\n"or player_number == "6\n" or player_number == "8\n":
            correct_number = False
        else:
            print("Invalid number, try again.")

    player_number = int(player_number)
    player_name_list = []
    max_player_name_length = 0
    
    for i in range(0, player_number):
        print(f"Enter name for player {i}:")
        player_name_to_add = sys.stdin.readline()[:-1]
        player_name_list.append(player_name_to_add)
        if len(player_name_to_add) > max_player_name_length:
            max_player_name_length = len(player_name_to_add)
    
    if player_number == 4:
        peek_number_list = [0, 1, 1, 1]
    elif player_number == 6:
        peek_number_list = [1, 1, 1, 2, 2, 2]
    elif player_number == 8:
        peek_number_list = [2, 2, 2, 2, 2, 2, 2, 2]

    team_list = []
    for i in range(int(player_number/2)):
        team_list.append("spade")
        team_list.append("heart")
    random.shuffle(team_list)
    
    master_dict = {}
    pristine_player_list = []
        
    random.shuffle(peek_number_list)
    for i in range(player_number):
        master_dict[i] = (team_list.pop(), peek_number_list.pop(), player_name_list[i])
        pristine_player_list.append(i)
    
    adjacency_list = []
    
    for i in range(0, player_number):
        to_add_to_adjacency_list = []
        list_without_current_player = copy.deepcopy(pristine_player_list)
        list_without_current_player.remove(i)
        random.shuffle(list_without_current_player)
        for j in range(0, master_dict[i][1]):
            temp_player = list_without_current_player.pop()
            to_add_to_adjacency_list.append(temp_player)
        adjacency_list.append((i, to_add_to_adjacency_list))
    
    
    for i in range(0, player_number):
        print(f"Press ENTER as {master_dict[i][2]}.")
        input()
        cls()
        print(f"{master_dict[i][2]}, team: {getTeam(i)}\n")
        
        for j in adjacency_list[i][1]:
            print(f"{master_dict[j][2]} is team: {getTeam(j)}.")
        print("")
        print("Press ENTER to clear screen, then pass to next player.")
        input()
        cls()
    print("All players information given, press ENTER twice to see teams.")
    input()
    print("Press ENTER again.")
    
    input()
    cls()
    spade_list = makeTeamList("spade")
    heart_list = makeTeamList("heart")
    print(f"Spade {spade_symbol}: {spade_list}")
    print(f"Heart {heart_symbol}: {heart_list}\n")
    
    toPrint = " " * max_player_name_length + "   "
    line = " " * max_player_name_length + "   "
    for i in range(0, player_number):
        toPrint += f" {master_dict[i][2]}{getSymbol(i)}"
        line += "_" * (len(master_dict[i][2]) + 2)
    print(toPrint)
    print(line)
    for i in range(player_number):
        toPrint = ""
        for j in range(player_number):
            if j in adjacency_list[i][1]:
                toPrint += f"{master_dict[j][2]}{getSymbol(j)} "
            else:
                toPrint += "-" * (len(master_dict[j][2]) + 1) + " "
        padding = " " * (max_player_name_length - len(master_dict[i][2]))
        print(f"{padding}{master_dict[i][2]}{getSymbol(i)} | {toPrint}")
    print("\n")
    print("End of game, press ENTER twice to exit.")
    input()
    print("Press ENTER again.")
    input()

