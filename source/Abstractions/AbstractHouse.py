from abc import abstractmethod


class AbstractHouse:
    @abstractmethod
    def receivePawn(self, pawn) -> None:
        pass
