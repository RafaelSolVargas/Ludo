from abc import ABC, abstractmethod
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Abstractions.AbstractPlayer import AbstractPlayer


class AbstractPawn(ABC):
    @abstractmethod
    @property
    def path(self):
        pass

    @abstractmethod
    @property
    def status(self) -> PawnStatus:
        pass

    @abstractmethod
    @property
    def color(self) -> PlayerColor:
        pass

    @abstractmethod
    @property
    def player(self) -> AbstractPlayer:
        pass

    @abstractmethod
    def kill(self) -> None:
        pass

    @abstractmethod
    @property
    def currentPosIndex(self) -> int:
        pass

    @abstractmethod
    @property
    def currentPosition(self):
        pass
