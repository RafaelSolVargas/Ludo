
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from play.tabuleiro import Tabuleiro
from play.control import Control
class Game:
    def __init__(self):
        
        self.grid = QGridLayout()
        self.widget = QWidget()

        self.init()

    def set_grid(self):
        self.grid.addWidget(Tabuleiro().widget,0,0)
        self.grid.addWidget(Control().widget,0,1)

    def set_window(self):
        self.widget.setStyleSheet("background: white;")
        self.widget.setLayout(self.grid)
        self.widget.setWindowTitle('LUDO')

    def init(self):

        self.set_grid()
        self.set_window()


