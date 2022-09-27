from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class HousePosition:
    def __init__(self, color: str):
        self.__widget = QPushButton()
        self.__color = color

        self.style = ['''
        *{  
            height: 80%;
            margin: 30%;
          
            border-radius: 42%;
            border: 2px solid 'black';  
    
        }
        *:hover{
            background: 'grey';
        }
        ''']

        self.__start()

    @property
    def color(self) -> str:
        return self.__color

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __start(self) -> None:
        #self.__widget.setFixedWidth(60)
        #self.__widget.setFixedHeight(60)
        self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.__widget.setStyleSheet(self.style[0])
