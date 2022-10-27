from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.PlayerColor import PlayerColor
from Game.Pawn import Pawn
from Abstractions.AbstractHouse import AbstractHouse
from Views.Position import Position
from Views.HousePosition import HousePosition
from Abstractions.AbstractPlayer import AbstractPlayer
from Game.PawnStatus import PawnStatus


class House(AbstractHouse):
    def __init__(self, color: PlayerColor):
        self.__pawns: List[Pawn] = []
        self.__player = None
        self.__widget = QWidget()
        self.__color = color
        self.__grid = QGridLayout()
        self.__style = self.__getStyle()
        self.__start()

    def configureMatch(self, path: List[Position], player: AbstractPlayer) -> None:
        # Após já ter o path definido cria os peões
        for x in range(4):
            self.__pawns.append(Pawn(self.__color, path, self))
        self.__player = player

    @property
    def widget(self) -> QWidget:
        return self.__widget

    @property
    def color(self) -> PlayerColor:
        return self.__color

    def getColor(self) -> PlayerColor:
        return self.__color

    @property
    def pawns(self) -> List[Pawn]:
        return self.__pawns

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

    def __setGrid(self) -> None:
        for l in range(2):
            for c in range(2):
                self.__grid.addWidget(HousePosition(self.__color).widget, l,  c)

    def __start(self) -> None:
        self.__widget.setStyleSheet(self.__style)
        self.__setGrid()
        self.__widget.setLayout(self.__grid)

    def __getStyle(self):
        if self.__color == PlayerColor.BLUE:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PlayerColor.YELLOW:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PlayerColor.GREEN:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''
        else:  # Red
            return '''
            *{  
                border-radius: 159%;
                background-color: 'red';
                border: 2px solid 'black';  
            }
            '''
