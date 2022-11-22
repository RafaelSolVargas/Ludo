from abc import abstractmethod
from typing import List
from Game.Player import Player
from Abstractions.AbstractBoard import AbstractBoard


class AbstractGame:
    @abstractmethod
    def startMatch(self, players: List[Player], board: AbstractBoard, localID: int):
        pass

    @abstractmethod
    def goToNextPlayer(self, currentPlayer: Player):
        pass

    @abstractmethod
    def processMove(self, move: dict):
        pass

    @abstractmethod
    def getLocalPlayer(self) -> Player:
        pass

    @abstractmethod
    def handleConfirmPiece(self) -> None:
        pass

    @abstractmethod
    def handleRoll(self) -> None:
        pass

    @abstractmethod
    def clearPlayers(self) -> None:
        pass

    @abstractmethod
    def checkIfValidPosition(self, position) -> bool:
        pass
