from PyQt5.QtWidgets import QWidget, QGridLayout
from play.Board import Board
from play.control import Control
from play.roll_button import RollButton


class BoardWindow:
    def __init__(self):
        self.__grid = QGridLayout()
        self.__widget = QWidget()
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    @property
    def grid(self) -> QGridLayout:
        return self.__grid

    def __start(self):
        self.__setGrid()
        self.__setWindow()

    def teste(self):
        print('Aoba Board')

    def __setGrid(self):
        # self.__grid.addWidget(Board().widget, 0, 0)
        # self.__grid.addWidget(Control().widget, 0, 1)
        pass

    def __setWindow(self):
        # self.__widget.setStyleSheet("background: white;")
        # self.__widget.setWindowTitle('LUDO')

        button2 = RollButton('Rola Board')
        gridTeste = QGridLayout()
        gridTeste.addWidget(button2.widget, 3, 0)
        self.__grid.addLayout(gridTeste, 0, 1)
        button2.widget.clicked.connect(self.teste)
        self.__widget.setLayout(self.__grid)
