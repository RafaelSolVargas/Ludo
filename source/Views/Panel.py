from typing import Callable
from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout
from Views.RollButton import RollButton
from Views.PushButton import PushButton
from Config.ButtonsStyles import ButtonsStyles
from Views.Label import Label
from Views.Dice import Dice
from Config.PlayerColor import PlayerColor


class Panel(QWidget):
    def __init__(self, rollCB: Callable = None, confirmCB: Callable = None):
        super().__init__()
        self.setMaximumWidth(800)
        # Settings
        self.setStyleSheet("background: white;")
        self.grid = QGridLayout()
        self.__width = 800

        # Dice
        self.__dice: Dice = None

        # Rows grids
        self.__secondRow: QHBoxLayout = None
        self.__buttonsRow: QHBoxLayout = None

        # Buttons
        self.__confirmButton: PushButton = None
        self.__rollButton: RollButton = None

        # Default Color
        self.__defaultColor: PlayerColor = PlayerColor.BLACK

        # Messages
        self.__titleMessage: str = "Title"
        self.__notifyMessage: str = "-"
        self.__turnMessage: str = "Turn"

        self.__setTitleRow()
        self.__setDice()
        self.__setSecondMessageRow(self.__defaultColor)
        self.__setButtonsRow(rollCB, confirmCB)

        self.setLayout(self.grid)

    def roll(self):
        self.__clearDice()
        self.__setDice()

    def setTitleMessage(self, message: str, color: PlayerColor = None) -> None:
        if color is None:
            color = self.__defaultColor

        self.__titleMessage = message
        self.__setTitleRow(color)

    def setNotifyMessage(self, message: str, color: PlayerColor = None) -> None:
        if color is None:
            color = self.__defaultColor

        self.__notifyMessage = message
        self.__setSecondMessageRow(color)

    def setTurnMessage(self, message: str, color: PlayerColor = None) -> None:
        if color is None:
            color = self.__defaultColor

        self.__turnMessage = message
        self.__setSecondMessageRow(color)

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

        self.grid.addLayout(grid_dice, 2, 0)

    def __setTitleRow(self, color: PlayerColor = None) -> None:
        if color is None:
            color = self.__defaultColor

        self.grid.addWidget(Label(self.__titleMessage, color).widget, 0, 0)

    def __setSecondMessageRow(self, color: PlayerColor) -> None:
        self.__secondRow = QHBoxLayout()
        self.__secondRow.addWidget(Label(self.__notifyMessage, color, 400, 20).widget, 0)
        self.__secondRow.addWidget(Label(self.__turnMessage, color, 400, 28).widget, 1)
        self.grid.addLayout(self.__secondRow, 1, 0)

    def __setButtonsRow(self, rollCB: Callable, confirmPieceCB: Callable) -> None:
        self.__buttonsRow = QHBoxLayout()

        self.__rollButton = PushButton('ROLL DICE', ButtonsStyles.RollButton, lambda: rollCB())
        self.__confirmButton = PushButton(
            'CONFIRM PIECE', ButtonsStyles.RollButton, lambda: confirmPieceCB())

        self.__buttonsRow.addWidget(self.__rollButton)
        self.__buttonsRow.addWidget(self.__confirmButton)
        self.grid.addLayout(self.__buttonsRow, 3, 0)

    @property
    def diceValue(self) -> int:
        return self.__dice.diceValue

    def __clearDice(self):
        self.__dice.widget.hide()

    @property
    def notifyMessage(self) -> str:
        return self.__notifyMessage

    @property
    def turnMessage(self) -> str:
        return self.__turnMessage

    @property
    def titleMessage(self) -> str:
        return self.__titleMessage
