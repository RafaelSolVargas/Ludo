from PyQt5.QtWidgets import QWidget, QGridLayout
from play.dice import Dice
from play.roll_button import RollButton
from play.label import Label


class Control:
    def __init__(self, width: int = 800):
        self.width = width
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.widgets = {
            'dice': [],
            'roll_button': []
        }

        self.__start()

    def __setWindow(self):
        self.widget.setFixedWidth(self.width)
        self.widget.setStyleSheet("background: white;")

    def __clearDice(self):
        for i in self.widgets['dice']:
            i.hide()

        self.widgets['dice'] = []

    def roll(self):
        print('ROLL')
        self.__clearDice()
        self.__setDice()

    def __setDice(self):
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

    def __setControl(self):
        self.grid.addWidget(Label('YOUR TIME').widget, 0, 0)
        self.__setDice()

        r_b = RollButton('ROLL DICE')
        r_b.widget.clicked.connect(lambda: self.roll())

        self.widgets['roll_button'].append(r_b)
        self.grid.addWidget(r_b.widget, 2, 0)

    def __start(self):
        self.__setWindow()
        self.__setControl()
        self.widget.setLayout(self.grid)
