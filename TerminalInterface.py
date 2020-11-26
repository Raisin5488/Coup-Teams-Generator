import os
from TeamGenerator import TeamsGenerator

os.system("color 70")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()


possible_input = ["4", "6", "8"]

while True:
    player_number = input("Input number of players (4, 6, 8): ")
    if player_number in possible_input:
        cls()
        current_game = TeamsGenerator(int(player_number))
        current_player_number = 0
        while current_player_number < int(player_number):
            player_name = input(f"Input player {current_player_number}\'s name: ")
            if player_name == "":
                print("Player name cannot be empty.")
            elif not(current_game.addPlayer(player_name)):
                print("Player name is taken.")
            else:
                current_player_number += 1
        cls()
        while True:
            current_game.generateTeams()
            for player in current_game.player_objects:
                input(f"ENTER as {player.name}\n")
                cls()
                print(player.getInformation())
                input("\nENTER to clear screen.")
                cls()
            input("ENTER again to see end information.")
            cls()
            print(current_game.displayEndInformation())
            temp = input("\nInput 0 to keep current names: ")
            if temp == "0":
                print("Regenerating game.")
                cls()
            else:
                cls()
                break
    else:
        print("Invalid input (4, 6, 8).")

