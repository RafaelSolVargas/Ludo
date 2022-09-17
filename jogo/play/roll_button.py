
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

class RollButton:

    def __init__(self, name):
        self.widget = QPushButton(name)
        self.style = [
                                            '''
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
        ''']

        self.init()
        
    def init(self):
        self.widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.widget.setStyleSheet(self.style[0])