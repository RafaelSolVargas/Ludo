from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Image(QLabel):
    def __init__(self, image: str, margin: int):
        super().__init__()
        self.__imagePath = image
        self.__margin_top = margin
        self.__config()

    @property
    def imagePath(self) -> str:
        return self.__imagePath

    def __config(self):
        self.setPixmap(QPixmap(self.__imagePath))
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet(f"margin-top: {self.__margin_top}px;")
