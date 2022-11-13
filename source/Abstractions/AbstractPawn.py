from abc import ABC, abstractmethod
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Abstractions.AbstractPlayer import AbstractPlayer


class AbstractPawn(ABC):
    @property
    @abstractmethod
    def path(self):
        pass

    @property
    @abstractmethod
    def status(self) -> PawnStatus:
        pass

    @property
    @abstractmethod
    def color(self) -> PlayerColor:
        pass

    @property
    @abstractmethod
    def player(self) -> AbstractPlayer:
        pass

    @abstractmethod
    def returnToHouse(self) -> None:
        pass

    @property
    @abstractmethod
    def currentPosIndex(self) -> int:
        pass

    @property
    @abstractmethod
    def currentPosition(self):
        pass
