from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class PlayButton:
    def __init__(self, name):
        self.__widget = QPushButton(name)
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __start(self):
        self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.__widget.setStyleSheet(self.__style)

    def __getStyle(self) -> str:
        return '''
        *{
            border: 4px solid '#ff6400';
            border-radius: 25px;
            font-size: 30px;
            font-weight: bold;
            color: '#ff5733';
            padding: 15px 0;
            margin-top: 50px;
            margin-bottom: 25px;
            margin-left: 200px;
            margin-right: 200px;
        }
        *:hover{
            background: '#542100';
        }
        '''
