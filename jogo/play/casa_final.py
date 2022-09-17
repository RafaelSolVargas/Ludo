
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


class CasaFinal:

    def __init__(self, cor):
        
        self.widget = QWidget()
        self.cor = cor
        self.style = self.choose_color_and_type()
        
        self.init()

    def choose_color_and_type(self):
        if self.cor == 'full':
            return  [
                                                    '''
                *{  
                    border-top: 30px solid yellow;
                    border-right: 30px solid blue;
                    border-bottom: 30px solid green;
                    border-left: 30px solid red
                }
                ''']

        elif self.cor == 'red':

             return  [
                                                    '''
                *{  
                    background-color : red
                }
                ''']
        
        elif self.cor == 'green':

            return  [
                                                    '''
                *{  
                    background-color : green
                }
                ''']

        elif self.cor == 'blue':
            
            return  [
                                                    '''
                *{  
                    background-color : blue
                }
                ''']
        
        elif self.cor == 'yellow':

            return  [
                                                    '''
                *{  
                    background-color : yellow
                }
                ''']
        
        elif self.cor == 'red-yellow':

             return  [
                                                    '''
                *{  
                    border-top: 100px solid yellow;
                    border-left: 100px solid red
                }
                ''']

        elif self.cor == 'red-green':

             return  [
                                                    '''
                *{  
                    border-bottom: 100px solid green;
                    border-left: 100px solid red
                }
                ''']
        
        elif self.cor == 'green-blue':

             return  [
                                                    '''
                *{  
                    border-right: 100px solid blue;
                    border-bottom: 100px solid green;
                }
                ''']

        elif self.cor == 'blue-yellow':

             return  [
                                                    '''
                *{  
                    border-left: 100px solid yellow;
                    border-bottom: 100px solid blue;
                }
                ''']

    def init(self):
        
        self.widget.setStyleSheet(self.style[0])
        