from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Logo:
    def __init__(self, image: str, margin: int):
        self.__widget = QLabel()
        self.__image = image
        self.__margin_top = margin
        self.__start()

    @property
    def widget(self) -> QLabel:
        return self.__widget

    @property
    def image(self) -> str:
        return self.__image

    def __start(self):
        self.__widget.setPixmap(QPixmap(self.__image))
        self.__widget.setAlignment(QtCore.Qt.AlignCenter)
        self.__widget.setStyleSheet(f"margin-top: {self.__margin_top}px;")
