from Config.PlayerColor import PlayerColor
from Views.House import House
from Abstractions.AbstractPlayer import AbstractPlayer


class Player(AbstractPlayer):
    def __init__(self, name: int, id: str):
        self.__name: str = name
        self.__id = id
        self.__house: House = None
        self.__color: PlayerColor = None

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def house(self) -> House:
        return self.__house

    @house.setter
    def house(self, house: House):
        self.__house = house
        self.__color = self.__house.color

    @property
    def color(self) -> PlayerColor:
        return self.__color
