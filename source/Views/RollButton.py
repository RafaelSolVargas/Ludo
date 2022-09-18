from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class RollButton(QPushButton):
    def __init__(self, name: str):
        super().__init__(name)
        self.__style = self.__getStyle()
        self.__config()

    def __config(self):
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(self.__style)

    def __getStyle(self) -> str:
        return '''
            *{
            border: 4px solid 'green';
            border-radius: 25px;
            font-size: 32px;
            font-weight: bold;
            color: 'green';
            padding: 15px;
            margin-left: 270px;
            margin-right: 270px;
            }

            *:hover{
            background: '#caeabd';
            }
            '''
