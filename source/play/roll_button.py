from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


class RollButton:
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
