from typing import List
from Config.PlayerColor import PlayerColor
from Game.Pawn import Pawn
from Views.House import House
from Abstractions.AbstractPlayer import AbstractPlayer
from Views.Position import Position


class Player(AbstractPlayer):
    def __init__(self, name: int, id: str):
        self.__name: str = name
        self.__id = id
        self.__house: House = None
        self.__color: PlayerColor = None
        self.__pawns: List[Pawn] = []
        self.__selectedPawn: Pawn = None
        self.__hasTurn: bool = False
        self.__isWinner: bool = False
        self.__canRollDice: bool = False
        self.__canRollAgain: bool = False
        self.__canSelectFromHouse: bool = False
        self.__canConfirmPiece: bool = False
        self.__path: List[Position] = []
        self.__pawnIcon: str = ""

    @property
    def house(self) -> House:
        return self.__house

    @house.setter
    def house(self, house: House):
        self.__house = house
        self.__color = self.__house.color

    @property
    def pawns(self) -> List[Pawn]:
        return self.__pawns

    @pawns.setter
    def pawns(self, pawns: List[Pawn]):
        self.__pawns = pawns
        self.__path = pawns[0].path

    def reset(self) -> None:
        self.__hasTurn: bool = False
        self.__isWinner: bool = False
        self.__canRollDice: bool = False
        self.__canRollAgain: bool = False
        self.__canSelectFromHouse: bool = False
        self.__canConfirmPiece: bool = False
        self.__selectedPawn: Pawn = None

    def startTurn(self):
        # TODO implement
        pass

    def endTurn(self):
        # TODO implement
        pass

    @property
    def selectedPawn(self) -> Pawn:
        return self.__selectedPawn

    @selectedPawn.setter
    def selectedPawn(self, pawn: Pawn) -> None:
        self.__selectedPawn = pawn

    @property
    def hasTurn(self) -> bool:
        return self.__hasTurn

    @hasTurn.setter
    def hasTurn(self, value: bool) -> None:
        self.__hasTurn = value

    @property
    def isWinner(self) -> bool:
        return self.__isWinner

    @isWinner.setter
    def isWinner(self, value: bool) -> None:
        self.__isWinner = value

    @property
    def canRollDice(self) -> bool:
        return self.__canRollDice

    @canRollDice.setter
    def canRollDice(self, value: bool) -> None:
        self.__canRollDice = value

    @property
    def canRollAgain(self) -> bool:
        return self.__canRollAgain

    @canRollAgain.setter
    def canRollAgain(self, value: bool) -> None:
        self.__canRollAgain = value

    @property
    def canSelectFromHouse(self) -> bool:
        return self.__canSelectFromHouse

    @canSelectFromHouse.setter
    def canSelectFromHouse(self, value: bool) -> None:
        self.__canSelectFromHouse = value

    @property
    def canConfirmPiece(self) -> bool:
        return self.__canConfirmPiece

    @canConfirmPiece.setter
    def canConfirmPiece(self, value: bool) -> None:
        self.__canConfirmPiece = value

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def color(self) -> PlayerColor:
        return self.__color

    @property
    def path(self) -> List[Position]:
        return self.__path
