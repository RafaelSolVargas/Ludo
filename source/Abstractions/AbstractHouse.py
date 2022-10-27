from abc import abstractmethod
from PyQt5.QtWidgets import QWidget


class AbstractHouse:
    @abstractmethod
    def receivePawn(self, pawn) -> None:
        pass

    @abstractmethod
    def configureMatch(self, path, player) -> None:
        pass

    @property
    @abstractmethod
    def widget(self) -> QWidget:
        pass
