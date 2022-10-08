from PyQt5.QtWidgets import QWidget, QGridLayout
from Views.DiceHerdado import DiceHerdado
from Views.RollButton import RollButton
from Views.PushButton import PushButton
from Config.ButtonsStyles import ButtonsStyles
from Views.Label import Label
from Views.Dice import Dice


class Panel(QWidget):
    def __init__(self, width: int = 800):
        super().__init__()
        self.__width = width
        self.grid = QGridLayout()
        self.__dice: Dice = None
        self.__rollButton: RollButton = None

        self.__setWindow()
        self.__setControl()
        self.setLayout(self.grid)

    def __setWindow(self):
        # self.setFixedWidth(self.__width)
        self.setStyleSheet("background: white;")

    def roll(self):
        self.__clearDice()
        self.__setDice()

    def __clearDice(self):
        self.__dice.widget.hide()

    def __setDice(self):
        # Desenha o dado
        grid_dice = QGridLayout()
        self.__dice = Dice(int(self.__width/5))
        grid_dice.addWidget(self.__dice.widget, 1, 1)

        for l in range(3):
            for c in range(3):
                if l == 1 and c == 1:
                    continue

                widget = QWidget()
                widget.setStyleSheet("background: white;")
                widget.setFixedHeight(int(self.__width/5))
                widget.setFixedWidth(int(self.__width/5))
                grid_dice.addWidget(widget, l, c)

        self.grid.addLayout(grid_dice, 1, 0)

    def __setControl(self):
        self.grid.addWidget(Label('YOUR TIME').widget, 0, 0)
        self.__setDice()

        self.__rollButton = PushButton('ROLL DICE', ButtonsStyles.RollButton, lambda: self.roll())
        self.grid.addWidget(self.__rollButton, 2, 0)
