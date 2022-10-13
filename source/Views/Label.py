from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore


class Label:
    def __init__(self, name):
        self.__widget = QLabel(name)
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QLabel:
        return self.__widget

    def __start(self):
        self.__widget.setAlignment(QtCore.Qt.AlignCenter)
        self.__widget.setFixedWidth(800)
        self.__widget.setFixedHeight(100)
        self.__widget.setStyleSheet(self.__style)

    def __getStyle(self) -> str:
        return '''
        *{
            border-top: 5px solid 'blue';
            border-bottom: 5px solid 'blue';
            font-size: 32px;
            font-weight: bold;
            color: 'blue';
        }
        '''
