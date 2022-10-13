from Views.PlayerInterface import PlayerInterface
from PyQt5.QtWidgets import QApplication
from Game.Player import Player
from Game.Board import Board
from typing import List
import sys


class Game:
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
        self.__interface: PlayerInterface = None

        self.__localPlayer: Player = None
        self.__players: List[Player] = None
        self.__board: Board = None

    @property
    def board(self) -> Board:
        return self.__board

    def startWindow(self) -> None:
        self.__interface = PlayerInterface(self)
        self.__interface.run()
        self.__app.exec()

    def startMatch(self, players: List[Player], pawnsQuant: int, board: Board, localID: int):
        print(board)
        self.__board = board

        for index, player in enumerate(players):
            # Configura o player local pelo ID
            if player.id == localID:
                self.__localPlayer = player

            # Seleciona uma casa para o jogador acessando a lista de casas pelo index
            house = board.houses[index]
            # Pega o path da casa
            path = self.__board.getPlayerPath(house.color)
            # Configura a casa
            house.configureMatch(path, pawnsQuant, player)
            # Já configura a cor do player pela casa que ele recebe
            player.house = house
