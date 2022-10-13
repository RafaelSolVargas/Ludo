from abc import abstractmethod
from Abstractions.AbstractHouse import AbstractHouse


class AbstractPlayer:
    @abstractmethod
    def setHouse(self, house: AbstractHouse) -> None:
        pass
