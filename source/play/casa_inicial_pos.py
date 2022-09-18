from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class CasaInicialPos:
    def __init__(self, color: str):
        self.__widget = QPushButton()
        self.__color = color

        self.style = '''
        *{
            border: 2px solid 'white';
            
            
            border-radius: 40px;
            color: 'white';
        }
        *:hover{
            background: 'white';
        }
        '''

        self.__start()

    @property
    def color(self) -> str:
        return self.__color

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __start(self) -> None:
        self.__widget.setFixedWidth(80)
        self.__widget.setFixedHeight(80)
        self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.__widget.clicked.connect(self.teste)
        self.__widget.setStyleSheet(self.style[0])

    def teste(self) -> None:
        print('Aoba2')
