from typing import List
from Views.Position import Position
from Config.PlayerColor import PlayerColor
from Game.PawnStatus import PawnStatus
from Abstractions.AbstractHouse import AbstractHouse
from Abstractions.AbstractPlayer import AbstractPlayer


class Pawn:
    def __init__(self, player: AbstractPlayer, path: List[Position], house: AbstractHouse, id: int) -> None:
        self.__path: List[Position] = path
        self.__player: AbstractPlayer = player
        self.__color: PlayerColor = player.color
        self.__iconPath = self.__getIconPath()
        self.__id = id

        self.__status: PawnStatus = PawnStatus.STORED
        # -1 for in house or > -1 for current position in Path
        self.__currentPosIndex = -1
        self.__house = house

    @property
    def id(self) -> int:
        return self.__id

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

    @property
    def iconPath(self) -> str:
        return self.__iconPath
    
    def __getIconPath(self) -> str:
        return f"Assets/{self.__color.lower()}Pawn.png"
    
    def returnToHouse(self) -> None:
        self.__status = PawnStatus.STORED
        self.__house.receivePawn(self)

    @property
    def currentPosIndex(self) -> int:
        return self.__currentPosIndex

    @currentPosIndex.setter
    def currentPosIndex(self, value) -> int:
        if value > len(self.__path):
            print('Erro tentando settar current position index de peão maior que o path')
            return
        
        self.__currentPosIndex = value

    @status.setter
    def status(self, value: PawnStatus) -> None:
        self.__status = value    

    @property
    def currentPosition(self) -> Position:
        if self.__currentPosIndex == -1:
            return None

        return self.__path[self.__currentPosIndex]
