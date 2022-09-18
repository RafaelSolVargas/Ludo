from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class OptionButton:
    def __init__(self, number: int):
        self.__widget = QPushButton(f'{number}')
        self.__number = number
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    @property
    def number(self) -> int:
        return self.__number

    def __start(self):
        self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.__widget.setStyleSheet(self.__style)

    def __getStyle(self) -> str:
        return '''
        *{
            border: 2px solid 'white';
            font-size: 18px;
            font-weight: bold;
            border-radius: 27px;
            width: 50px;
            
            color: 'white';
            padding: 15px 0;
            

            margin-top:50px; 
            margin-left: 40px;
            margin-right: 40px;
        }
        *:hover{
            background: '#494949';
        }
        '''
