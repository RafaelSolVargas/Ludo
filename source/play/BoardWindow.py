from PyQt5.QtWidgets import QWidget, QGridLayout
from play.Board import Board
from play.control import Control


class BoardWindow:
    def __init__(self):
        self.__grid = QGridLayout()
        self.__widget = QWidget()
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __start(self):
        self.__setGrid()
        self.__setWindow()

    def __setGrid(self):
        self.__grid.addWidget(Board().widget, 0, 0)
        self.__grid.addWidget(Control().widget, 0, 1)

    def __setWindow(self):
        self.__widget.setStyleSheet("background: white;")
        self.__widget.setLayout(self.__grid)
        self.__widget.setWindowTitle('LUDO')
