from typing import List
from Views.Position import Position
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Abstractions.AbstractHouse import AbstractHouse


class Pawn:
    def __init__(self, playerColor: PlayerColor, path: List[Position], house: AbstractHouse) -> None:
        self.__path: List[Position] = []
        self.__color: PlayerColor = None
        self.__status: PawnStatus = PawnStatus.STORED
        # -1 for in house or > -1 for current position in Path
        self.__currentPos = -1
        self.__house = house

    @property
    def path(self) -> List[Position]:
        return self.__path

    @property
    def status(self) -> PawnStatus:
        return self.__status

    @property
    def color(self) -> PlayerColor:
        return self.__color

    def kill(self) -> None:
        self.__house.receivePawn(self)

    @property
    def currentPosition(self) -> Position:
        if self.__currentPos == -1:
            return None

        return self.__path[self.__currentPos]
