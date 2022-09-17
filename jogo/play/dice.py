import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from play.dice_ball import DiceBall
from play.quadrado import Quadrado
from play.casa_inicial import CasaInicial
from play.casa_final import CasaFinal
from random import randint


class Dice:

    def __init__(self, width):
        self.widget = QWidget()
        self.width = width
        self.grid = QGridLayout()
        self.number = randint(1, 6)
        self.style = [
                            '''
        *{
            border: 4px solid 'black';
            border-radius : 20px;
            background-color: white;

        }
        '''
        ]
        
        self.init()


    def set_dice(self):
        print(self.number)
        for linha in range(3):
            for coluna in range(3):
                if self.number == 1:
                    if linha == 1 and coluna == 1:
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)
                
                elif self.number == 2:
                    if (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0):
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)

                elif self.number == 3:
                    if (linha == 0 and coluna == 2) or (linha == 1 and coluna == 1) or (linha == 2 and coluna == 0):
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)

                elif self.number == 4:

                    if (linha == 0 and coluna == 0) or (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0) or (linha == 2 and coluna == 2):
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)

                elif self.number == 5:

                    if (linha == 0 and coluna == 0) or (linha == 0 and coluna == 2) or (linha == 2 and coluna == 0) or (linha == 2 and coluna == 2) or (linha == 1 and coluna == 1):
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)

                elif self.number == 6:

                    if coluna == 0 or coluna == 2:
                        self.grid.addWidget(DiceBall('black', int(self.width/9)).widget, linha, coluna)
                    else:
                        self.grid.addWidget(DiceBall('white', int(self.width/9)).widget, linha, coluna)
                    



    def widget_set(self):

        self.widget.setLayout(self.grid)
        self.widget.setStyleSheet(self.style[0])

    def init(self):
        
        self.widget_set()
        self.set_dice()
    