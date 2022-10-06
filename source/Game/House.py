from typing import List
from Game.Pawn import Pawn
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Views.Position import Position
from Views.HouseView import House
from Abstractions.AbstractHouse import AbstractHouse


class House(AbstractHouse):
    def __init__(self, color: PlayerColor, pawnsQuant: int, path: List[Position]) -> None:
        self.__pawns: List[Pawn] = []
        for x in range(pawnsQuant):
            self.__pawns.append(Pawn(color, path, self))
        self.__color: PlayerColor = color
        self.__interface: House = None

    @property
    def color(self) -> PlayerColor:
        return self.__color

    @property
    def pawns(self) -> List[Pawn]:
        return self.__pawns

    def setView(self, houseView: House) -> None:
        self.__interface = houseView

    def removePawn(self) -> Pawn:
        if len(self.__pawns) > 0:
            pawn = self.__pawns.pop()
            pawn.status = PawnStatus.MOVING
            return pawn

        raise IndexError('Tentativa de remover peão de casa já vazia')

    def pawnsQuant(self) -> int:
        return len(self.__pawns)

    def receivePawn(self, pawn: Pawn) -> None:
        if pawn.color != self.__color:
            print(f'House de cor {self.__color} recebendo peão de cor {pawn.color}')
            return

        self.__pawns.append(pawn)
