import abc
from abc import abstractmethod
import copy
import random


class AbstractTeamGenerator(abc.ABC):
    @abstractmethod
    def addPlayer(player_name: str):
        pass

    @abstractmethod
    def getPlayerInformation(player_name: str) -> list:
        pass

    @abstractmethod
    def displayEndInformation() -> list:
        pass


class TeamsGenerator(AbstractTeamGenerator):
    def __init__(self, number_of_players):
        self.player_number = number_of_players
        self.player_dict = {}
        self.player_list = []
        self.player_objects = []
        self.max_player_name_length = 0
        self.spade_symbol = "♠"
        self.heart_symbol = "♡"

    def generateTeams(self):

        if self.player_number == 4:
            peek_number_list = [0, 1, 1, 1]
        elif self.player_number == 6:
            peek_number_list = [1, 1, 1, 2, 2, 2]
        elif self.player_number == 8:
            peek_number_list = [2, 2, 2, 2, 2, 2, 2, 2]
        random.shuffle(peek_number_list)

        teams = []
        for i in range(0, self.player_number//2):
            teams.append("spade")
            teams.append("heart")
        random.shuffle(teams)

        for i in self.player_list:
            player = Player(i)
            temp = teams.pop()
            player.setTeam(temp)
            if temp == "spade":
                player.setSymbol(self.spade_symbol)
            else:
                player.setSymbol(self.heart_symbol)
            self.player_objects.append(player)

        for i in self.player_objects:
            player_objects_copy = copy.copy(self.player_objects)
            player_objects_copy.remove(i)
            random.shuffle(player_objects_copy)
            number_of_known_people = peek_number_list.pop()
            for j in range(0, number_of_known_people):
                i.addKnownPlayer(player_objects_copy.pop())

    def addPlayer(self, player_name):
        if not(player_name in self.player_list) and player_name != "":
            self.player_list.append(player_name)
            return True
        else:
            return False

    def getPlayerInformation(self, player_name):
        return self.player_dict[player_name]

    def setMaxPlayerNameLength(self):
        self.max_player_name_length = max(
            len(i.name) for i in self.player_objects)

    def displayEndInformation(self):
        self.setMaxPlayerNameLength()

        spade_list = self.makeTeamList("spade")
        heart_list = self.makeTeamList("heart")
        print(f"{self.spade_symbol} {spade_list}")
        print(f"{self.heart_symbol} {heart_list}\n")

        to_print = " " * self.max_player_name_length + "   "
        line = " " * self.max_player_name_length + "   "
        for player in self.player_objects:
            to_print += f" {player.name}{player.symbol}"
            line += "_" * (len(player.name) + 2)
        print(to_print)
        print(line)
        for player in self.player_objects:
            toPrint = ""
            for possible_player_to_see in self.player_objects:
                if possible_player_to_see in player.known_players:
                    toPrint += f"{possible_player_to_see.name}{possible_player_to_see.symbol} "
                else:
                    to_print += "-" *(len(possible_player_to_see.name) + 1) + " "
            padding = " " * (self.max_player_name_length - len(possible_player_to_see.name))
            print(f"{padding}{player.name}{player.symbol} | {toPrint}")

    def __repr__(self):
        pass

    def makeTeamList(self, team):
        team_list = []
        for i in self.player_objects:
            if i.team == team:
                team_list.append(i)
        return team_list


class Player:

    def __init__(self, player_name):
        self.name = player_name
        self.known_players = []
        self.team = ""
        self.symbol = ""

    def setTeam(self, team):
        self.team = team

    def setSymbol(self, symbol):
        self.symbol = symbol

    def addKnownPlayer(self, player):
        self.known_players.append(player)

    def getTeam(self):
        return self.team

    def getInformation(self):
        to_print = f"{self.name} {self.team}\n"
        for i in self.known_players:
            to_print += f"\n{i.name} {i.team}"
        return to_print
