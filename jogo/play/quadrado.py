import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

class Quadrado():
    def __init__(self, cor):
        self.widget = QWidget()
        self.cor = cor
        self.style = self.choose_color()
       

        self.init()

    def choose_color(self):
        if self.cor == 'white':
            return  [
                                                '''
            *{  
        
                background-color: 'white';
                border: 2px solid 'black';  
            }
            ''']
        elif self.cor == 'blue':
            return  [
                                                '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            ''']

        elif self.cor == 'yellow':

            return  [
                                                '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            ''']

        elif self.cor == 'green':

            return  [
                                                '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';  
            }
            ''']
        
        elif self.cor == 'red':

            return  [
                                                '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';  
            }
            ''']
        
        elif self.cor == 'none':

            return  [
                                                '''
            *{  
                background-color: 'white';
                border: 2px solid 'white';  
            }
            ''']

    def init(self):
        
        self.widget.setStyleSheet(self.style[0])