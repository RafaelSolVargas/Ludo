from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from play.casa_inicial_pos import CasaInicialPos
class CasaInicial:

    def __init__(self, cor):

        self.widget = QWidget()
        self.cor = cor
        self.grid = QGridLayout()
        self.style = self.choose_color()
        
        self.init()

    def choose_color(self):
        if self.cor == 'white':
            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'white';
                border: 2px solid 'black';  
            }
            ''']
        elif self.cor == 'blue':
            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            ''']

        elif self.cor == 'yellow':

            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            ''']

        elif self.cor == 'green':

            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'green';
                border: 2px solid 'black';  
            }
            ''']
        
        elif self.cor == 'red':

            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'red';
                border: 2px solid 'black';  
            }
            ''']
        
        elif self.cor == 'none':

            return  [
                                                '''
            *{  
                border-radius: 161px;
                background-color: 'white';
                border: 2px solid 'white';  
            }
            ''']

    

    def set_grid(self):

        for l in range (2):
            for c in range (2):
                self.grid.addWidget(CasaInicialPos(self.cor).widget, l,  c)

    def init(self):
        
        self.widget.setStyleSheet(self.style[0])
        self.set_grid()
        self.widget.setLayout(self.grid)