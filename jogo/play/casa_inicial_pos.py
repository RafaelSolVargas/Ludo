import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

class CasaInicialPos:

    def __init__(self, color):
        self.widget = QPushButton()
        self.color = color
        
        self.style = [
                            '''
        *{
            border: 2px solid 'white';
            
            
            border-radius: 40px;
            color: 'white';
        }
        *:hover{
            background: 'white';
        }
        ''']

        self.init()
        

    def init(self):
        self.widget.setFixedWidth(80)
        self.widget.setFixedHeight(80)
        self.widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.widget.setStyleSheet(self.style[0])