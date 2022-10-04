from Dog.dog_actor import DogActor
from Source.Dog.dog_interface import DogPlayerInterface


class Player(DogActor):
    def __init__(self):
        super().__init__()
        self.__started: bool = False
        self.__name: str = None

    def initialize(self, playerName: str, playerActor: DogPlayerInterface):
        self.__started = True
        self.__name = playerName
        return super().initialize(playerName, playerActor)
