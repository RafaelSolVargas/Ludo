from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.PlayerColor import PlayerColor
from Game.Pawn import Pawn
from Abstractions.AbstractHouse import AbstractHouse
from Abstractions.AbstractBoard import AbstractBoard
from Views.Position import Position
from Abstractions.AbstractPlayer import AbstractPlayer
from Game.PawnStatus import PawnStatus


class House(AbstractHouse):
    def __init__(self, color: PlayerColor, board: AbstractBoard):
        self.__pawns: List[Pawn] = []
        self.__positions: List[Position] = []
        self.__board = board
        self.__player = None
        self.__widget = QWidget()
        self.__color = color
        self.__grid = QGridLayout()
        self.__style = self.__getStyle()
        self.__start()

    def configureMatch(self, path: List[Position], player: AbstractPlayer) -> List[Pawn]:
        # Após já ter o path definido cria os peões
        pawnID = self.__getFirstPawnID()
        for x in range(4):
            self.__pawns.append(Pawn(player, path, self, pawnID))
            pawnID += 1

        # Coloca um peão dentro de cada position que está na house
        pawnIndex = 0
        for position in self.__positions:
            position.receivePawn(self.__pawns[pawnIndex])
            pawnIndex += 1

        self.__player = player
        return self.__pawns

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
        # Para remover um peão verifica se existe peões suficientes
        if len(self.__pawns) > 0:
            # Remove da lista de peões
            pawn = self.__pawns.pop()
            # Atualiza o status do Pawn
            pawn.status = PawnStatus.MOVING
            # Atualiza o index da posição atual
            pawn.currentPosIndex = 0
            # Procura pela mesma referência do peão só que dentro das positions e remove ele da position
            for position in self.__positions:
                if len(position.pawns) > 0:
                    if position.pawns[0] == pawn:
                        position.removePawn()

            return pawn

        raise IndexError('Tentativa de remover peão de casa já vazia')

    def __getFirstPawnID(self) -> int:
        if self.__color == PlayerColor.BLUE:
            return 0
        if self.__color == PlayerColor.RED:
            return 4
        if self.__color == PlayerColor.GREEN:
            return 8
        return 12

    def pawnsQuant(self) -> int:
        return len(self.__pawns)

    def receivePawn(self, pawn: Pawn) -> None:
        if pawn.color != self.__color:
            print(f'House de cor {self.__color} recebendo peão de cor {pawn.color}')
            return

        pawn.status = PawnStatus.STORED
        self.__pawns.append(pawn)

        # Armazena o peão recebido dentro de uma position que estava vazia dentro de house
        for position in self.__positions:
            if len(position.pawns) == 0:
                position.receivePawn(pawn)
                break

    def __setGrid(self) -> None:
        pawnIndex = -1
        for l in range(2):
            for c in range(2):
                pawnIndex += 1
                # Cria as 4 posições dentro da casa
                position = Position(self.__color, self.__board, None)
                self.__positions.append(position)
                self.__grid.addWidget(position.widget, l, c)

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
