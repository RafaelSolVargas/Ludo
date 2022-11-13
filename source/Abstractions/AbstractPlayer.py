from abc import abstractmethod
from Abstractions.AbstractHouse import AbstractHouse
from Config.PlayerColor import PlayerColor


class AbstractPlayer:
    @abstractmethod
    def setHouse(self, house: AbstractHouse) -> None:
        pass

    @property
    @abstractmethod
    def color(self) -> PlayerColor:
        pass
