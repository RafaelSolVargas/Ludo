from PyQt5.QtWidgets import QWidget, QGridLayout
from Views.DicePoint import DicePoint
from random import randint


class DiceHerdado(QWidget):
    def __init__(self, width: int):
        super().__init__()
        self.__width = width
        self.__grid = QGridLayout()
        self.__number = randint(1, 6)
        self.__style = '''
                    Dice {
                        border: 4px solid 'black';
                        border-radius : 20px;
                        background-color: white;
                    }
                    '''

        self.__start()

    def __setWidget(self) -> None:
        self.setLayout(self.__grid)
        self.setStyleSheet(self.__style)

    def __start(self) -> None:
        self.__setWidget()
        self.__setDice()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __setDice(self):
        print(self.__number)
        for linha in range(3):
            for coluna in range(3):
                if self.__number == 1:
                    if linha == 1 and coluna == 1:
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)

                elif self.__number == 2:
                    if (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0):
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)

                elif self.__number == 3:
                    if (linha == 0 and coluna == 2) or (linha == 1 and coluna == 1) or (linha == 2 and coluna == 0):
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)

                elif self.__number == 4:

                    if (linha == 0 and coluna == 0) or (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0) or (linha == 2 and coluna == 2):
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)

                elif self.__number == 5:

                    if (linha == 0 and coluna == 0) or (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0) or (linha == 2 and coluna == 2) or (linha == 1 and coluna == 1):
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)

                elif self.__number == 6:

                    if coluna == 0 or coluna == 2:
                        self.__grid.addWidget(DicePoint('black', int(
                            self.__width/9)).widget, linha, coluna)
                    else:
                        self.__grid.addWidget(DicePoint('white', int(
                            self.__width/9)).widget, linha, coluna)
