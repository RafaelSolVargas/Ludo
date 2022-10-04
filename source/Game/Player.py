from Dog.dog_actor import DogActor
from Dog.dog_interface import DogPlayerInterface
from Config.PlayerColor import PlayerColor
from Game.House import House


class Player(DogActor):
    def __init__(self):
        super().__init__()
        self.__started: bool = False
        self.__name: str = None
        self.__house: House = None
        self.__color: PlayerColor = None

    def setHouse(self, house: House):
        self.__house = house
        self.__color = self.__house.color

    @property
    def color(self) -> PlayerColor:
        return self.__color

    def initialize(self, playerName: str, playerActor: DogPlayerInterface):
        self.__started = True
        self.__name = playerName
        return super().initialize(playerName, playerActor)
