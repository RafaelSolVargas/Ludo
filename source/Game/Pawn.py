from typing import List
from Views.Position import Position
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Abstractions.AbstractHouse import AbstractHouse
from Abstractions.AbstractPlayer import AbstractPlayer


class Pawn:
    def __init__(self, player: AbstractPlayer, path: List[Position], house: AbstractHouse) -> None:
        self.__path: List[Position] = path
        self.__player: AbstractPlayer = player
        self.__color: PlayerColor = player.color

        self.__status: PawnStatus = PawnStatus.STORED
        # -1 for in house or > -1 for current position in Path
        self.__currentPosIndex = -1
        self.__house = house

    @property
    def player(self) -> AbstractPlayer:
        return self.__player

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
    def currentPosIndex(self) -> int:
        return self.__currentPosIndex

    @currentPosIndex.setter
    def currentPosIndex(self, value) -> int:
        if value > len(self.__path):
            print('Erro tentando settar current position index de peão maior que o path')
        self.__currentPosIndex = value

    @property
    def currentPosition(self) -> Position:
        if self.__currentPosIndex == -1:
            return None

        return self.__path[self.__currentPosIndex]
