import os
from TeamGenerator import TeamsGenerator

os.system("color 70")

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

valid_player_numbers = ["4", "6", "8"]
while True:
    player_number = input("Input number of players (4, 6, 8): ")
    if player_number in valid_player_numbers:
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
        current_game.generateTeams()
        cls()
        for player in current_game.player_objects:
            input(f"Press enter as player {player.name}\n")
            cls()
            print(player.getInformation())
            input("\nPress enter to clear screen.")
            cls()
        input("Press enter again to see end information.")
        cls()
        print(current_game.displayEndInformation())
        input()
    else:
        cls()
        print("Invalid input (4, 6, 8).")
