import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from option_button import OptionButton

class Logo:
    
    def __init__(self, image, margin):

        self.widget = QLabel()
        self.image = image
        self.margin_top = margin
        self.init()

    def init(self):
        
        self.widget.setPixmap(QPixmap(self.image))
        self.widget.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setStyleSheet(f"margin-top: {self.margin_top}px;")