from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QCursor
from typing import Callable
from PyQt5 import QtCore


class PushButton(QPushButton):
    """
    Recebe um callback que será chamado quando clicado, junto com o callback recebe args que serão passados
    para o callback quando executado
    """

    def __init__(self, text: str, style: str, callback: Callable = None, *args):
        super().__init__(f'{text}')
        self.__text = text
        self.__style = style
        self.__selected = False
        self.__config()

        if callback is not None:
            if args != ():
                self.clicked.connect(lambda: callback(args))
            else:
                self.clicked.connect(lambda: callback())

    @property
    def text(self) -> str:
        return self.__text

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected) -> bool:
        self.__selected = selected

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, newStyle) -> None:
        self.__style = newStyle
        self.setStyleSheet(self.__style)

    def __config(self):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(self.__style)
