import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from play.quadrado import Quadrado
from play.casa_inicial import CasaInicial
from play.casa_final import CasaFinal
from play.dice import Dice
from play.roll_button import RollButton
from play.label import Label
class Control:
    def __init__(self, width = 800):
        self.width = width
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.widgets = {
            'dice' : [],
            'roll_button': []
        }

        self.init()

    def window_set(self):
        
        self.widget.setFixedWidth(self.width)
        
        self.widget.setStyleSheet("background: white;")

    def clear_dice(self):
        for i in self.widgets['dice']:
            i.hide()
        
        self.widgets['dice'] = []
        
    def roll(self):
        print('ROLL')
        self.clear_dice()
        self.set_dice()

    def set_dice(self):
        grid_dice = QGridLayout()
        for l in range(3):
            for c in range(3):
                if l == 1 and c == 1:
                    widget = Dice(int(self.width/5)).widget
                    
                    grid_dice.addWidget(widget, l, c)
                else:
                    widget = QWidget()
                    widget.setStyleSheet("background: white;")
                    widget.setFixedHeight(int(self.width/5))
                    widget.setFixedWidth(int(self.width/5))
                    grid_dice.addWidget(widget, l, c)
                
                self.widgets['dice'].append(widget)
        
        self.grid.addLayout(grid_dice, 1, 0)

    def set_control(self):
        
        self.grid.addWidget(Label('YOUR TIME').widget, 0, 0)

        self.set_dice()

        r_b = RollButton('ROLL DICE')

        r_b.widget.clicked.connect(self.roll)

        self.widgets['roll_button'].append(r_b) 

        self.grid.addWidget(r_b.widget, 2, 0)

        
    def init(self):
        
        self.window_set()
        
        self.set_control()
        self.widget.setLayout(self.grid)
    