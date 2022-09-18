from typing import Callable
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class PushButton(QPushButton):
    def __init__(self, text: str, style: str, callback: Callable = None):
        super().__init__(f'{text}')
        self.__text = text
        self.__style = style
        self.__config()

        if callback is not None:
            self.clicked.connect(callback)

    @property
    def text(self) -> str:
        return self.__text

    def __config(self):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(self.__style)
