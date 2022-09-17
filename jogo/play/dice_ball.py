import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from play.quadrado import Quadrado
from play.casa_inicial import CasaInicial
from play.casa_final import CasaFinal
from random import randint

class DiceBall:

    def __init__(self, type, width) -> None:
        self.widget = QWidget()
        self.width = width
        self.type = type
        self.init()

    def type_style(self):

        if self.type == 'white':
            return [
                            '''
        *{  
            border-color: white;
            border-radius: 8px;
            background-color: white;

        }
        '''
        ]
        elif self.type == 'black':
            return [
                            '''
        *{  
            border-color: black;
            border-radius : 8px;
            background-color: black;
      
       
        }
        '''
        ]

    def widget_set(self):

        self.widget.setFixedHeight(self.width)
        self.widget.setFixedWidth(self.width)
        self.widget.setStyleSheet(self.type_style()[0])

    
    def init(self):
        self.widget_set()