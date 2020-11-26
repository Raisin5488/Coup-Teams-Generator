import os
from TeamGenerator import TeamsGenerator


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()

valid_player_numbers = ["4", "6", "8"]
while True:
    inputed_string = input("Input number of players (4, 6, 8): ")
    if inputed_string in valid_player_numbers:
        inputed_integer = int(inputed_string)
        current_game = TeamsGenerator(int(inputed_string))
        current_player_number = 0
        for i in range(inputed_integer):
            player_name = input(f"Input player {current_player_number}\'s name: ")
            if not(current_game.addPlayer(player_name)):
                inputed_integer += 1
                print("Name is taken, try another.")
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
        current_game.displayEndInformation()
        input()
    else:
        cls()
        print("Incorrect input, 4, 6, 8.")
