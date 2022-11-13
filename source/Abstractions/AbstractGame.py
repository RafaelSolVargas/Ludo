from abc import abstractmethod
from typing import List
from Game.Player import Player
from Abstractions.AbstractBoard import AbstractBoard


class AbstractGame:
    @abstractmethod
    def startMatch(self, players: List[Player], board: AbstractBoard, localID: int):
        pass
