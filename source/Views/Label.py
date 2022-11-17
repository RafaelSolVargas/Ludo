from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from Config.PlayerColor import PlayerColor


class Label:
    def __init__(self, name, color: PlayerColor):
        self.__widget = QLabel(name)
        self.__style = self.__getStyle(self.__convertPlayerColorToString(color))
        self.__start()

    @property
    def widget(self) -> QLabel:
        return self.__widget

    def __start(self):
        self.__widget.setAlignment(QtCore.Qt.AlignCenter)
        self.__widget.setFixedWidth(800)
        self.__widget.setFixedHeight(100)
        self.__widget.setStyleSheet(self.__style)

    def __convertPlayerColorToString(self, color: PlayerColor) -> str:
        if color == PlayerColor.BLUE:
            return 'blue'
        if color == PlayerColor.GREEN:
            return 'green'
        if color == PlayerColor.RED:
            return 'red'
        return 'yellow'

    def __getStyle(self, colorStr: str) -> str:
        return f'''
        *{{
            border-top: 5px solid '{colorStr}';
            border-bottom: 5px solid '{colorStr}';
            font-size: 32px;
            font-weight: bold;
            color: '{colorStr}';
        }}
        '''
