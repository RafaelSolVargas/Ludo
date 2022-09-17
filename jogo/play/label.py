import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore



class Label:

    def __init__(self, name):

        self.widget = QLabel(name)
        self.style = [
                 '''
        *{
            border-top: 5px solid 'blue';
            border-bottom: 5px solid 'blue';
            font-size: 32px;
            font-weight: bold;
            color: 'blue';
    
        }
        ''']
        self.init()

    def init(self):
        self.widget.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setFixedWidth(800)
        self.widget.setFixedHeight(100)
        self.widget.setStyleSheet(self.style[0])
        
        