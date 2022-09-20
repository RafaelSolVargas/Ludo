from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.HouseColor import HouseColor
from Config.PositionsColor import PositionsColor
from Views.Position import Position
from Views.House import House


class Board(QWidget):
    def __init__(self, width: int = 1000, height: int = 1000):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__grid = QGridLayout()
        # YELLOW - BLUE - GREEN - RED
        self.__houses: List[House] = []
        # A primeira é a do meio em cima, anda no sentido horário entrando nos caminhos
        self.__positions: List[Position] = [None for _ in range(80)]

        self.__start()

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

    def __setBoardWidgets(self):
        n_pins_grid = QGridLayout()
        self.__grid.addLayout(n_pins_grid, 4, 0)

        self.__boardGrid = QGridLayout()
        self.__setHousesGrid()
        self.__setMiddleGrid()

        for linha in range(3):
            for coluna in range(3):
                self.__boardGrid = QGridLayout()

                if linha == 0 and coluna == 1:
                    # Cria os 15 quadrados entre as casas iniciais vermelhas e amarelas
                    for l in range(5):
                        for c in range(5):
                            if c in [1, 2, 3]:
                                if c == 2 and l != 0:
                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.YELLOW).widget, l, c)
                                else:

                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.WHITE).widget, l, c)
                            else:
                                self.__boardGrid.addWidget(
                                    Position(PositionsColor.NONE).widget, l, c)

                elif linha == 1 and coluna == 0:
                    # caminho vermelho
                    for l in range(5):
                        for c in range(5):
                            if l in [1, 2, 3]:
                                if l == 2 and c != 0:
                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.RED).widget, l, c)
                                else:

                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.WHITE).widget, l, c)
                            else:

                                self.__boardGrid.addWidget(
                                    Position(PositionsColor.NONE).widget, l, c)

                elif linha == 1 and coluna == 1:
                    pass

                elif linha == 1 and coluna == 2:
                    # caminho azul
                    for l in range(5):
                        for c in range(5):
                            if l in [1, 2, 3]:
                                if l == 2 and c != 4:
                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.BLUE).widget, l, c)
                                else:

                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.WHITE).widget, l, c)

                            else:

                                self.__boardGrid.addWidget(
                                    Position(PositionsColor.NONE).widget, l, c)

                elif linha == 2 and coluna == 1:
                    # caminho verde
                    for l in range(5):
                        for c in range(5):
                            if c in [1, 2, 3]:
                                if c == 2 and l != 4:
                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.GREEN).widget, l, c)
                                else:
                                    self.__boardGrid.addWidget(
                                        Position(PositionsColor.WHITE).widget, l, c)
                            else:
                                self.__boardGrid.addWidget(
                                    Position(PositionsColor.NONE).widget, l, c)
                else:
                    continue

                if not ((linha == 0 or linha == 2) and (coluna == 0 or coluna == 2) or (linha == 1 and coluna == 1)):
                    self.__grid.addLayout(self.__boardGrid, linha, coluna)

    def __setHousesGrid(self) -> None:
        yellowHouse = House(HouseColor.YELLOW)
        blueHouse = House(HouseColor.BLUE)
        greenHouse = House(HouseColor.GREEN)
        redHouse = House(HouseColor.RED)
        self.__houses.append(yellowHouse.widget)
        self.__houses.append(blueHouse.widget)
        self.__houses.append(greenHouse.widget)
        self.__houses.append(redHouse.widget)

        self.__topRightGrid.addWidget(yellowHouse.widget, 0, 2)
        self.__grid.addLayout(self.__topRightGrid, 0, 2)

        self.__botRightGrid.addWidget(blueHouse.widget, 2, 2)
        self.__grid.addLayout(self.__botRightGrid, 2, 2)

        self.__botLeftGrid.addWidget(greenHouse.widget, 2, 0)
        self.__grid.addLayout(self.__botLeftGrid, 2, 0)

        self.__topLeftGrid.addWidget(redHouse.widget, 0, 0)
        self.__grid.addLayout(self.__topLeftGrid, 0, 0)

    def __setMiddleGrid(self) -> None:
        # --------------- Primeira linha do bloco central
        position = Position(PositionsColor.WHITE)
        self.__positions[73] = position
        self.__midMidGrid.addWidget(position.widget, 0, 0)

        position = Position(PositionsColor.WHITE)
        self.__positions[74] = position
        self.__midMidGrid.addWidget(position.widget, 0, 1)

        position = Position(PositionsColor.YELLOW)
        self.__positions[5] = position
        self.__midMidGrid.addWidget(position.widget, 0, 2)

        position = Position(PositionsColor.WHITE)
        self.__positions[12] = position
        self.__midMidGrid.addWidget(position.widget, 0, 3)

        position = Position(PositionsColor.WHITE)
        self.__positions[13] = position
        self.__midMidGrid.addWidget(position.widget, 0, 4)

        # --------------- Segunda linha do bloco central
        position = Position(PositionsColor.WHITE)
        self.__positions[72] = position
        self.__midMidGrid.addWidget(position.widget, 1, 0)

        position = Position(PositionsColor.RED_YELLOW)
        self.__midMidGrid.addWidget(position.widget, 1, 1)

        position = Position(PositionsColor.YELLOW)
        self.__positions[6] = position
        self.__midMidGrid.addWidget(position.widget, 1, 2)

        position = Position(PositionsColor.BLUE_YELLOW)
        self.__midMidGrid.addWidget(position.widget, 1, 3)

        position = Position(PositionsColor.WHITE)
        self.__positions[14] = position
        self.__midMidGrid.addWidget(position.widget, 1, 4)

        # --------------- Terceira linha do bloco central
        position = Position(PositionsColor.RED)
        self.__positions[65] = position
        self.__midMidGrid.addWidget(position.widget, 2, 0)

        position = Position(PositionsColor.RED)
        self.__positions[66] = position
        self.__midMidGrid.addWidget(position.widget, 2, 1)

        position = Position(PositionsColor.FULL)
        self.__midMidGrid.addWidget(position.widget, 2, 2)

        position = Position(PositionsColor.BLUE)
        self.__positions[26] = position
        self.__midMidGrid.addWidget(position.widget, 2, 3)

        position = Position(PositionsColor.BLUE)
        self.__positions[25] = position
        self.__midMidGrid.addWidget(position.widget, 2, 4)

        # --------------- Quarta linha do bloco central
        position = Position(PositionsColor.WHITE)
        self.__positions[54] = position
        self.__midMidGrid.addWidget(position.widget, 3, 0)

        position = Position(PositionsColor.RED_GREEN)
        self.__midMidGrid.addWidget(position.widget, 3, 1)

        position = Position(PositionsColor.GREEN)
        self.__positions[46] = position
        self.__midMidGrid.addWidget(position.widget, 3, 2)

        position = Position(PositionsColor.BLUE_GREEN)
        self.__midMidGrid.addWidget(position.widget, 3, 3)

        position = Position(PositionsColor.WHITE)
        self.__positions[32] = position
        self.__midMidGrid.addWidget(position.widget, 3, 4)

        # --------------- Quinta linha do bloco central
        position = Position(PositionsColor.WHITE)
        self.__positions[53] = position
        self.__midMidGrid.addWidget(position.widget, 4, 0)

        position = Position(PositionsColor.WHITE)
        self.__positions[52] = position
        self.__midMidGrid.addWidget(position.widget, 4, 1)

        position = Position(PositionsColor.GREEN)
        self.__positions[45] = position
        self.__midMidGrid.addWidget(position.widget, 4, 2)

        position = Position(PositionsColor.WHITE)
        self.__positions[34] = position
        self.__midMidGrid.addWidget(position.widget, 4, 3)

        position = Position(PositionsColor.WHITE)
        self.__positions[33] = position
        self.__midMidGrid.addWidget(position.widget, 4, 4)

        self.__grid.addLayout(self.__midMidGrid, 1, 1)
