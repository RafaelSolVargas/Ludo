from Config.PlayerColor import PlayerColor
from Game.House import House
from Views.PlayerInterface import PlayerInterface
from PyQt5.QtWidgets import QApplication
from Dog.dog_actor import DogActor
from Game.Player import Player
from Game.Board import Board
from typing import List
import sys


class Game:
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__interface: PlayerInterface = None

        self.__players: List[Player] = None
        self.__board: Board = None

    @property
    def board(self) -> Board:
        return self.__board

    def startWindow(self) -> None:
        self.__interface = PlayerInterface(self)
        self.__interface.run()
        self.__app.exec()

    def startMatch(self, players: List[Player], pawnsQuant: int, board: Board):
        self.__board = board
        housesColors = [PlayerColor.GREEN, PlayerColor.BLUE, PlayerColor.YELLOW, PlayerColor.RED]
        for index, player in enumerate(players):
            path = self.__board.getPlayerPath(housesColors[index])
            house = House(housesColors[index], pawnsQuant, path)
            player.setHouse(house)
