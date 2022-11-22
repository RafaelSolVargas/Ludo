from abc import ABC, abstractmethod


class AbstractBoard(ABC):
    @property
    @abstractmethod
    def selectedPosition(self, position) -> None:
        pass

    @abstractmethod
    def trySelectPosition(self, position) -> None:
        pass
    
    @abstractmethod
    def getPositionFromID(self, posId: int) -> None:
        pass