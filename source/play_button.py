import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

class PlayButton():
    def __init__(self, name):
        self.widget = QPushButton(name)
        self.style = [
                                            '''
        *{
            border: 4px solid '#ff6400';
            border-radius: 25px;
            font-size: 30px;
            font-weight: bold;
            color: '#ff5733';
            padding: 15px 0;
            margin-top: 50px;
            margin-bottom: 25px;
            margin-left: 200px;
            margin-right: 200px;
        }
        *:hover{
            background: '#542100';
        }
        ''']

        self.init()
        
    def init(self):
        
        self.widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.widget.setStyleSheet(self.style[0])
        