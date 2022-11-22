from typing import List
from Config.PositionsColor import PositionsColor
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QCursor
from Abstractions.AbstractPawn import AbstractPawn
from PyQt5 import QtCore
from Abstractions.AbstractBoard import AbstractBoard


class Position:
    def __init__(self, color: PositionsColor, board: AbstractBoard, id: int):
        self.__widget = QPushButton()
        self.__selected: bool = False

        self.__board: AbstractBoard = board

        self.__id: int = id

        self.__pawns: List[AbstractPawn] = []
        self.__color = color
        self.__configureClick()

        self.__defaultStyle = self.__getStyle()
        self.__selectedStyle = '''
            *{
                background-color: 'grey';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;
            }
        '''
        self.__widget.setStyleSheet(self.__defaultStyle)

    def __configureClick(self) -> None:
        if (self.__color in [PositionsColor.BLUE, PositionsColor.YELLOW,
                             PositionsColor.RED, PositionsColor.GREEN, PositionsColor.WHITE]):
            # Configura o callback e passa a instância de position como parâmetro do callback
            self.__widget.clicked.connect(lambda: self.__selectPosition())
            self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.__widget.setDisabled(True)

    def __selectPosition(self):
        self.__board.trySelectPosition(self)

    @property
    def id(self) -> int:
        if self.__id == None:
            print('Erro tentando acessar id de Position não válida')
        return self.__id

    def removePawn(self) -> AbstractPawn:
        if len(self.__pawns) == 0:
            print('Erro tentando remover peão de casa vazia')

        return self.__pawns.pop(0)

    def receivePawn(self, pawn: AbstractPawn) -> None:
        if len(self.__pawns) == 2:
            print('Erro tentando adicionar um terceiro peão a uma casa')

        if len(self.__pawns) == 0:
            self.__pawns.append(pawn)
            return None

        # Caso seja peão de outro jogador
        killedPawn = None
        if self.__pawns[0].player != pawn.player:
            killedPawn = self.__pawns.pop(0)
            killedPawn.returnToHouse()

        self.__pawns.append(pawn)
        # Modificar a imagem da posição atual
        return killedPawn

    @property
    def pawns(self) -> List[AbstractPawn]:
        return self.__pawns

    @property
    def isBlocked(self) -> bool:
        return len(self.__pawns) == 2

    @property
    def isFree(self) -> bool:
        return len(self.__pawns) == 0

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool) -> bool:
        self.__selected = selected
        if not self.__selected:
            self.__widget.setStyleSheet(self.__defaultStyle)
        else:
            self.__widget.setStyleSheet(self.__selectedStyle)

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __getStyle(self):

        if self.__color == PositionsColor.WHITE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;  
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.BLUE:
            return '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;    
            }
            *:hover{
                background-color: 'grey';
            }
            '''

        elif self.__color == PositionsColor.YELLOW:
            return '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;   
            }
            *:hover{
                background-color: 'grey';
            }
            '''

        elif self.__color == PositionsColor.GREEN:
            return '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;   
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.RED:
            return '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;    
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.NONE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'white';
                width: 55%;
                height: 55%;     
            }
            '''
