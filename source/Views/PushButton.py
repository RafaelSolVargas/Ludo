from typing import Callable
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class PushButton:
    def __init__(self, text: str, style: str, callback: Callable = None):
        self.__widget = QPushButton(f'{text}')
        self.__text = text
        self.__style = style
        self.__start()

        if callback is not None:
            self.__widget.clicked.connect(callback)

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    @property
    def text(self) -> str:
        return self.__text

    def __start(self):
        self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.__widget.setStyleSheet(self.__style)
