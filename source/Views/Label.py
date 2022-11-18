from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from Config.PlayerColor import PlayerColor


class Label:
    def __init__(self, message: str, color: PlayerColor, width: int = 800, fontSize: int = 32):
        self.__widget = QLabel(message)
        self.__width = width
        self.__style = self.__getStyle(self.__convertPlayerColorToString(color), fontSize)
        self.__start()

    @property
    def widget(self) -> QLabel:
        return self.__widget

    def __start(self):
        self.__widget.setAlignment(QtCore.Qt.AlignCenter)
        self.__widget.setFixedWidth(self.__width)
        self.__widget.setFixedHeight(100)
        self.__widget.setStyleSheet(self.__style)

    def __convertPlayerColorToString(self, color: PlayerColor) -> str:
        if color == PlayerColor.BLUE:
            return 'blue'
        if color == PlayerColor.GREEN:
            return 'green'
        if color == PlayerColor.RED:
            return 'red'
        if color == PlayerColor.YELLOW:
            return 'yellow'
        return 'black'

    def __getStyle(self, colorStr: str, fontSize: int = 32) -> str:
        return f'''
        *{{
            border-top: 5px solid '{colorStr}';
            border-bottom: 5px solid '{colorStr}';
            font-size: {fontSize}px;
            font-weight: bold;
            color: '{colorStr}';
        }}
        '''
