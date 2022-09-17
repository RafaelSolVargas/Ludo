import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


class OptionButton():
    def __init__(self, number):
        self.widget = QPushButton(f'{number}')
        self.number = number
        self.style = [
            '''
        *{
            border: 2px solid 'white';
            font-size: 18px;
            font-weight: bold;
            border-radius: 26px;
            color: 'white';
            padding: 15px 0;
            

            margin-top:50px; 
            margin-left: 40px;
            margin-right: 40px;
        }
        *:hover{
            background: '#494949';
        }
        ''']

        self.init()

    def init(self):

        self.widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.widget.setStyleSheet(self.style[0])
