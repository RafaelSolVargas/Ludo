from PyQt5.QtWidgets import QWidget, QGridLayout
from play.quadrado import Quadrado
from play.casa_inicial import CasaInicial
from play.casa_final import CasaFinal


class Board:
    def __init__(self, width: int = 1000, height: int = 1000):
        self.__width = width
        self.__height = height
        self.__widget = QWidget()
        self.__grid = QGridLayout()

        self.__start()

    def __setWindow(self):
        self.__widget.setFixedWidth(self.__width)
        self.__widget.setFixedHeight(self.__height)
        self.__widget.setStyleSheet("background: white;")

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __setBoardWidgets(self):
        n_pins_grid = QGridLayout()
        self.__grid.addLayout(n_pins_grid, 4, 0)

        for linha in range(3):
            for coluna in range(3):
                apoio_grid = QGridLayout()
                if linha == 0 and coluna == 0:
                    # casa vermelha
                    apoio_grid.addWidget(CasaInicial('red').widget, linha, coluna)
                elif linha == 0 and coluna == 1:
                    # caminho amarelo
                    for l in range(5):
                        for c in range(5):
                            if c in [1, 2, 3]:
                                if c == 2 and l != 0:
                                    apoio_grid.addWidget(Quadrado('yellow').widget, l, c)
                                else:

                                    apoio_grid.addWidget(Quadrado('white').widget, l, c)
                            else:

                                apoio_grid.addWidget(Quadrado('none').widget, l, c)

                elif linha == 0 and coluna == 2:
                    # casa amarela
                    apoio_grid.addWidget(CasaInicial('yellow').widget, linha, coluna)

                elif linha == 1 and coluna == 0:
                    # caminho vermelho
                    for l in range(5):
                        for c in range(5):
                            if l in [1, 2, 3]:
                                if l == 2 and c != 0:
                                    apoio_grid.addWidget(Quadrado('red').widget, l, c)
                                else:

                                    apoio_grid.addWidget(Quadrado('white').widget, l, c)
                            else:

                                apoio_grid.addWidget(Quadrado('none').widget, l, c)

                elif linha == 1 and coluna == 1:
                    # centro do tabuleiro
                    for l in range(5):
                        for c in range(5):
                            if l in [0, 4] or c in [0, 4]:
                                if l == 0 and c == 2:
                                    apoio_grid.addWidget(Quadrado('yellow').widget, l, c)

                                elif l == 4 and c == 2:
                                    apoio_grid.addWidget(Quadrado('green').widget, l, c)

                                elif l == 2 and c == 0:
                                    apoio_grid.addWidget(Quadrado('red').widget, l, c)

                                elif l == 2 and c == 4:
                                    apoio_grid.addWidget(Quadrado('blue').widget, l, c)

                                else:
                                    apoio_grid.addWidget(Quadrado('white').widget, l, c)
                            else:
                                if l == 1:
                                    if c == 1:
                                        apoio_grid.addWidget(CasaFinal('red-yellow').widget, l, c)
                                    elif c == 2:
                                        apoio_grid.addWidget(CasaFinal('yellow').widget, l, c)
                                    elif c == 3:
                                        apoio_grid.addWidget(
                                            CasaFinal('blue-yellow').widget, l, c)

                                elif l == 2:

                                    if c == 1:
                                        apoio_grid.addWidget(CasaFinal('red').widget, l, c)
                                    elif c == 2:
                                        apoio_grid.addWidget(CasaFinal('full').widget, l, c)
                                    elif c == 3:
                                        apoio_grid.addWidget(CasaFinal('blue').widget, l, c)

                                elif l == 3:

                                    if c == 1:
                                        apoio_grid.addWidget(CasaFinal('red-green').widget, l, c)
                                    elif c == 2:
                                        apoio_grid.addWidget(CasaFinal('green').widget, l, c)
                                    elif c == 3:
                                        apoio_grid.addWidget(CasaFinal('green-blue').widget, l, c)

                elif linha == 1 and coluna == 2:
                    # caminho azul
                    for l in range(5):
                        for c in range(5):
                            if l in [1, 2, 3]:
                                if l == 2 and c != 4:
                                    apoio_grid.addWidget(Quadrado('blue').widget, l, c)
                                else:

                                    apoio_grid.addWidget(Quadrado('white').widget, l, c)

                            else:

                                apoio_grid.addWidget(Quadrado('none').widget, l, c)
                elif linha == 2 and coluna == 0:
                    # casa verde
                    apoio_grid.addWidget(CasaInicial('green').widget, linha, coluna)

                elif linha == 2 and coluna == 1:
                    # caminho verde
                    for l in range(5):
                        for c in range(5):
                            if c in [1, 2, 3]:
                                if c == 2 and l != 4:
                                    apoio_grid.addWidget(Quadrado('green').widget, l, c)
                                else:

                                    apoio_grid.addWidget(Quadrado('white').widget, l, c)

                            else:

                                apoio_grid.addWidget(Quadrado('none').widget, l, c)
                elif linha == 2 and coluna == 2:
                    # casa azul
                    apoio_grid.addWidget(CasaInicial('blue').widget, linha, coluna)

                self.__grid.addLayout(apoio_grid, linha, coluna)

    def __start(self):

        self.__setWindow()

        self.__setBoardWidgets()
        self.__widget.setLayout(self.__grid)
