from typing import List
from Game.Player import Player
from Source.Dog.dog_actor import DogActor
from Game.Board import Board


class Game:
    def __init__(self) -> None:
        self.__players: List[Player] = None
        self.__board: Board = None

    @property
    def board(self) -> Board:
        return self.__board

    def addPlayer(self, player: Player):
        if isinstance(player, DogActor):
            self.__players.append(player)
        else:
            print(f'{player.__class__} não é instancia de DogActor')
