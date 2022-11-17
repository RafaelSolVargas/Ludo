from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.PositionsColor import PositionsColor
from Config.PlayerColor import PlayerColor
from Views.House import House
from Views.EndHouse import EndHouse
from Views.Position import Position
from Views.EndHouse import EndHouse
from typing import List


class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.__grid = QGridLayout()
        # YELLOW - BLUE - GREEN - RED
        self.__houses: List[House] = []
        # A primeira é a do meio em cima, anda no sentido horário entrando nos caminhos
        self.__positions: List[Position] = [None for _ in range(80)]

        self.__selectedPosition: Position = None

        self.__start()
        self.__bluePath = self.__getBluePath()
        self.__redPath = self.__getRedPath()
        self.__yellowPath = self.__getYellowPath()
        self.__greenPath = self.__getGreenPath()

    def reset(self) -> None:
        # Retorna todos os peões para suas específicas casas
        # Já atualiza as referências de peões e posições
        for position in self.__positions:
            for pawn in position.pawns:
                pawn = position.removePawn()
                pawn.returnToHouse()

    def getPositionFromID(self, posID: int) -> Position:
        # O ID da posição é a entrada dele na lista de posições
        return self.__positions[posID]

    @property
    def selectedPosition(self) -> Position:
        return self.__selectedPosition

    @selectedPosition.setter
    def selectedPosition(self, value: Position) -> Position:
        self.__selectedPosition = value

    @property
    def houses(self) -> List[House]:
        """0 -> BLUE | 1 -> GREEN | 2 -> RED | 3 -> YELLOW"""
        return self.__houses

    def getPlayerPath(self, playerColor: PlayerColor):
        if playerColor == PlayerColor.RED:
            return self.__redPath
        if playerColor == PlayerColor.BLUE:
            return self.__bluePath
        if playerColor == PlayerColor.YELLOW:
            return self.__yellowPath
        if playerColor == PlayerColor.GREEN:
            return self.__greenPath

        raise TypeError(f'{playerColor} passed as instance of PlayerColor')

    def __setWindow(self):
        self.__topLeftGrid = QGridLayout()
        self.__topRightGrid = QGridLayout()
        self.__topMidGrid = QGridLayout()
        self.__midLeftGrid = QGridLayout()
        self.__midRightGrid = QGridLayout()
        self.__midMidGrid = QGridLayout()
        self.__botLeftGrid = QGridLayout()
        self.__botRightGrid = QGridLayout()
        self.__botMidGrid = QGridLayout()
        self.setStyleSheet("background: white;")

    def __start(self):
        self.__setWindow()
        self.__setBoardWidgets()
        self.setLayout(self.__grid)

    def __getYellowPath(self) -> List[Position]:
        yellowPath = []
        positionsIndex = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                          47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 69, 70, 70, 72, 73, 74, 75, 76, 77, 78, 79, 0, 1, 2, 3, 4, 5, 6]

        for pos in positionsIndex:
            yellowPath.append(self.__positions[pos])
        return yellowPath

    def __getRedPath(self) -> List[Position]:
        redPath = []
        positionsIndex = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27,
                          28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]

        for pos in positionsIndex:
            redPath.append(self.__positions[pos])
        return redPath

    def __getBluePath(self) -> List[Position]:
        bluePath = []
        positionsIndex = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                          67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

        for pos in positionsIndex:
            bluePath.append(self.__positions[pos])
        return bluePath

    def __getGreenPath(self) -> List[Position]:
        greenPath = []
        positionsIndex = [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 0, 7,
                          8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]

        for pos in positionsIndex:
            greenPath.append(self.__positions[pos])
        return greenPath

    def __setBoardWidgets(self):
        self.__setHousesGrid()
        self.__setMiddleGrid()
        self.__setTopMidGrid()
        self.__setMiddleLeftGrid()
        self.__setMiddleRightGrid()
        self.__setBottomMidGrid()

    def __setHousesGrid(self) -> None:
        blueHouse = House(PlayerColor.BLUE)
        greenHouse = House(PlayerColor.GREEN)
        redHouse = House(PlayerColor.RED)
        yellowHouse = House(PlayerColor.YELLOW)
        self.__houses.append(blueHouse)
        self.__houses.append(greenHouse)
        self.__houses.append(redHouse)
        self.__houses.append(yellowHouse)

        self.__topRightGrid.addWidget(yellowHouse.widget, 0, 2)
        self.__grid.addLayout(self.__topRightGrid, 0, 2)

        self.__botRightGrid.addWidget(blueHouse.widget, 2, 2)
        self.__grid.addLayout(self.__botRightGrid, 2, 2)

        self.__botLeftGrid.addWidget(greenHouse.widget, 2, 0)
        self.__grid.addLayout(self.__botLeftGrid, 2, 0)

        self.__topLeftGrid.addWidget(redHouse.widget, 0, 0)
        self.__grid.addLayout(self.__topLeftGrid, 0, 0)

    def __setTopMidGrid(self) -> None:
        # --------------- Primeira linha do bloco central top
        # Positions que possuem PositionsColor == None terão id == None pois só servem para montar o tabuleiro no formato correto
        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 0, 0)

        # Para outras positions o id será o index na lista geral de Positions
        position = Position(PositionsColor.WHITE, 79)
        self.__positions[79] = position
        self.__topMidGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.WHITE, 0)
        self.__positions[0] = position
        self.__topMidGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.WHITE, 7)
        self.__positions[7] = position
        self.__topMidGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 1, 0)

        position = Position(PositionsColor.WHITE, 78)
        self.__positions[78] = position
        self.__topMidGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.YELLOW, 1)
        self.__positions[1] = position
        self.__topMidGrid.addWidget(position.widget, 1, 2)

        position = Position(PositionsColor.WHITE, 8)
        self.__positions[8] = position
        self.__topMidGrid.addWidget(position.widget, 1, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 2, 0)

        position = Position(PositionsColor.WHITE,  77)
        self.__positions[77] = position
        self.__topMidGrid.addWidget(position.widget, 2, 1)

        position = Position(PositionsColor.YELLOW,  2)
        self.__positions[2] = position
        self.__topMidGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.WHITE, 9)
        self.__positions[9] = position
        self.__topMidGrid.addWidget(position.widget, 2, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 3, 0)

        position = Position(PositionsColor.WHITE, 76)
        self.__positions[76] = position
        self.__topMidGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.YELLOW, 3)
        self.__positions[3] = position
        self.__topMidGrid.addWidget(position.widget, 3, 2)

        position = Position(PositionsColor.WHITE, 10)
        self.__positions[10] = position
        self.__topMidGrid.addWidget(position.widget, 3, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.WHITE, 75)
        self.__positions[75] = position
        self.__topMidGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.YELLOW, 4)
        self.__positions[4] = position
        self.__topMidGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.WHITE, 11)
        self.__positions[11] = position
        self.__topMidGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__topMidGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__topMidGrid, 0, 1)

    def __setMiddleGrid(self) -> None:
        # --------------- Primeira linha do bloco central
        # --------------- Vai ser position
        position = Position(PositionsColor.WHITE, 73)
        self.__positions[73] = position
        self.__midMidGrid.addWidget(position.widget, 0, 0)

        position = Position(PositionsColor.WHITE, 74)
        self.__positions[74] = position
        self.__midMidGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.YELLOW, 5)
        self.__positions[5] = position
        self.__midMidGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.WHITE, 12)
        self.__positions[12] = position
        self.__midMidGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.WHITE, 13)
        self.__positions[13] = position
        self.__midMidGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central
        # --------------- Somente a primeira e ultima coluna vai ser position
        position = Position(PositionsColor.WHITE, 72)
        self.__positions[72] = position
        self.__midMidGrid.addWidget(position.widget, 1, 0)

        # --------------- Casa final(inicio)
        position = EndHouse(PositionsColor.RED_YELLOW)
        self.__midMidGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.YELLOW, 6)
        self.__positions[6] = position
        self.__midMidGrid.addWidget(position.widget, 1, 2)

        position = EndHouse(PositionsColor.BLUE_YELLOW)
        self.__midMidGrid.addWidget(position.widget, 1, 3)
        # --------------- Casa final(fim)

        position = Position(PositionsColor.WHITE, 14)
        self.__positions[14] = position
        self.__midMidGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central
        position = Position(PositionsColor.RED, 65)
        self.__positions[65] = position
        self.__midMidGrid.addWidget(position.widget, 2, 0)

        # --------------- Casa final(inicio)
        position = Position(PositionsColor.RED, 66)
        self.__positions[66] = position
        self.__midMidGrid.addWidget(position.widget, 2, 1)

        position = EndHouse(PositionsColor.FULL)
        self.__midMidGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.BLUE, 26)
        self.__positions[26] = position
        self.__midMidGrid.addWidget(position.widget, 2, 3)
        # --------------- Casa final(fim)

        position = Position(PositionsColor.BLUE, 25)
        self.__positions[25] = position
        self.__midMidGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central
        position = Position(PositionsColor.WHITE, 54)
        self.__positions[54] = position
        self.__midMidGrid.addWidget(position.widget, 3, 0)

        # --------------- Casa final(inicio)
        position = EndHouse(PositionsColor.RED_GREEN)
        self.__midMidGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.GREEN, 46)
        self.__positions[46] = position
        self.__midMidGrid.addWidget(position.widget, 3, 2)

        position = EndHouse(PositionsColor.BLUE_GREEN)
        self.__midMidGrid.addWidget(position.widget, 3, 3)
        # --------------- Casa final(fim)

        position = Position(PositionsColor.WHITE, 32)
        self.__positions[32] = position
        self.__midMidGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central(Full Position)
        position = Position(PositionsColor.WHITE, 53)
        self.__positions[53] = position
        self.__midMidGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.WHITE, 52)
        self.__positions[52] = position
        self.__midMidGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.GREEN, 45)
        self.__positions[45] = position
        self.__midMidGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.WHITE, 34)
        self.__positions[34] = position
        self.__midMidGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.WHITE, 33)
        self.__positions[33] = position
        self.__midMidGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__midMidGrid, 1, 1)

    def __setMiddleLeftGrid(self) -> None:
        # --------------- Primeira linha do bloco central esquerdo
        # --------------- Vai ser position
        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 0, 0)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central esquerdo
        position = Position(PositionsColor.WHITE, 67)
        self.__positions[67] = position
        self.__midLeftGrid.addWidget(position.widget, 1, 0)

        position = Position(PositionsColor.WHITE, 68)
        self.__positions[68] = position
        self.__midLeftGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.WHITE, 69)
        self.__positions[69] = position
        self.__midLeftGrid.addWidget(position.widget, 1, 2)

        position = Position(PositionsColor.WHITE, 70)
        self.__positions[70] = position
        self.__midLeftGrid.addWidget(position.widget, 1, 3)

        position = Position(PositionsColor.WHITE, 71)
        self.__positions[71] = position
        self.__midLeftGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central
        position = Position(PositionsColor.WHITE, 60)
        self.__positions[60] = position
        self.__midLeftGrid.addWidget(position.widget, 2, 0)

        position = Position(PositionsColor.RED, 61)
        self.__positions[61] = position
        self.__midLeftGrid.addWidget(position.widget, 2, 1)

        position = Position(PositionsColor.RED, 62)
        self.__positions[62] = position
        self.__midLeftGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.RED, 63)
        self.__positions[63] = position
        self.__midLeftGrid.addWidget(position.widget, 2, 3)

        position = Position(PositionsColor.RED, 64)
        self.__positions[64] = position
        self.__midLeftGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central
        position = Position(PositionsColor.WHITE, 59)
        self.__positions[59] = position
        self.__midLeftGrid.addWidget(position.widget, 3, 0)

        position = Position(PositionsColor.WHITE, 58)
        self.__positions[58] = position
        self.__midLeftGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.WHITE, 57)
        self.__positions[57] = position
        self.__midLeftGrid.addWidget(position.widget, 3, 2)

        position = Position(PositionsColor.WHITE, 56)
        self.__positions[56] = position
        self.__midLeftGrid.addWidget(position.widget, 3, 3)

        position = Position(PositionsColor.WHITE, 55)
        self.__positions[55] = position
        self.__midLeftGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central(Full Position)
        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__midLeftGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__midLeftGrid, 1, 0)

    def __setMiddleRightGrid(self) -> None:
        # --------------- Primeira linha do bloco central direito
        # --------------- Vai ser position
        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 0, 0)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central direito
        position = Position(PositionsColor.WHITE, 15)
        self.__positions[15] = position
        self.__midRightGrid.addWidget(position.widget, 1, 0)

        position = Position(PositionsColor.WHITE, 16)
        self.__positions[16] = position
        self.__midRightGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.WHITE, 17)
        self.__positions[17] = position
        self.__midRightGrid.addWidget(position.widget, 1, 2)

        position = Position(PositionsColor.WHITE, 18)
        self.__positions[18] = position
        self.__midRightGrid.addWidget(position.widget, 1, 3)

        position = Position(PositionsColor.WHITE, 19)
        self.__positions[19] = position
        self.__midRightGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central
        position = Position(PositionsColor.BLUE, 24)
        self.__positions[24] = position
        self.__midRightGrid.addWidget(position.widget, 2, 0)

        position = Position(PositionsColor.BLUE, 23)
        self.__positions[23] = position
        self.__midRightGrid.addWidget(position.widget, 2, 1)

        position = Position(PositionsColor.BLUE, 22)
        self.__positions[22] = position
        self.__midRightGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.BLUE, 21)
        self.__positions[21] = position
        self.__midRightGrid.addWidget(position.widget, 2, 3)

        position = Position(PositionsColor.WHITE, 20)
        self.__positions[20] = position
        self.__midRightGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central
        position = Position(PositionsColor.WHITE, 31)
        self.__positions[31] = position
        self.__midRightGrid.addWidget(position.widget, 3, 0)

        position = Position(PositionsColor.WHITE, 30)
        self.__positions[30] = position
        self.__midRightGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.WHITE, 29)
        self.__positions[29] = position
        self.__midRightGrid.addWidget(position.widget, 3, 2)

        position = Position(PositionsColor.WHITE, 28)
        self.__positions[28] = position
        self.__midRightGrid.addWidget(position.widget, 3, 3)

        position = Position(PositionsColor.WHITE, 27)
        self.__positions[27] = position
        self.__midRightGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central(Full Position)
        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__midRightGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__midRightGrid, 1, 2)

    def __setBottomMidGrid(self) -> None:
        # --------------- Primeira linha do bloco central de baixo
        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 0, 0)

        position = Position(PositionsColor.WHITE, 51)
        self.__positions[51] = position
        self.__botMidGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.GREEN, 44)
        self.__positions[44] = position
        self.__botMidGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.WHITE, 35)
        self.__positions[35] = position
        self.__botMidGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 1, 0)

        position = Position(PositionsColor.WHITE, 50)
        self.__positions[50] = position
        self.__botMidGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.GREEN, 43)
        self.__positions[43] = position
        self.__botMidGrid.addWidget(position.widget, 1, 2)

        position = Position(PositionsColor.WHITE, 36)
        self.__positions[36] = position
        self.__botMidGrid.addWidget(position.widget, 1, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 2, 0)

        position = Position(PositionsColor.WHITE, 49)
        self.__positions[49] = position
        self.__botMidGrid.addWidget(position.widget, 2, 1)

        position = Position(PositionsColor.GREEN, 42)
        self.__positions[42] = position
        self.__botMidGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.WHITE, 37)
        self.__positions[37] = position
        self.__botMidGrid.addWidget(position.widget, 2, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 3, 0)

        position = Position(PositionsColor.WHITE, 48)
        self.__positions[48] = position
        self.__botMidGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.GREEN, 41)
        self.__positions[41] = position
        self.__botMidGrid.addWidget(position.widget, 3, 2)

        position = Position(PositionsColor.WHITE, 38)
        self.__positions[38] = position
        self.__botMidGrid.addWidget(position.widget, 3, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central top
        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.WHITE, 47)
        self.__positions[47] = position
        self.__botMidGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.WHITE, 40)
        self.__positions[40] = position
        self.__botMidGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.WHITE, 39)
        self.__positions[39] = position
        self.__botMidGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.NONE, id=None)
        self.__botMidGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__botMidGrid, 2, 1)
