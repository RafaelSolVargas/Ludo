from typing import List
from PyQt5.QtWidgets import QWidget, QGridLayout, QMainWindow
from Config.ButtonsStyles import ButtonsStyles
from Config.ImagesPath import ImagesPath
from Views.Image import Image
from Views.PushButton import PushButton
from Views.Board import Board
from Views.Panel import Panel


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__window = QWidget()
        self.__grid = QGridLayout()

        self.__images: List[Image] = []
        self.__playerButtons: List[PushButton] = []
        self.__pinsButtons: List[PushButton] = []
        self.__playButton: PushButton = None

        self.__board: Board = None
        self.__panel: Panel = None

    def __setWindow(self) -> None:
        self.__window.setWindowTitle('LUDO')
        self.__window.setStyleSheet("background: black;")
        self.__window.move(640, 108)

    def __addWidgets(self) -> None:
        # Cria as imagens que aparecem no Menu principal
        self.__images.append(Image(ImagesPath.numberPins, 50))
        self.__images.append(Image(ImagesPath.ludoLogo, 25))
        self.__images.append(Image(ImagesPath.numberPlayers, 50))

        # Cria os botões de escolher players e pinos
        for index in range(1, 5):
            self.__pinsButtons.append(PushButton(index, ButtonsStyles.MainMenuOptions))
        for index in range(2, 5):
            self.__playerButtons.append(PushButton(index, ButtonsStyles.MainMenuOptions))

        # Cria o botão de play e conecta com o método Play quando clicado
        self.__playButton = PushButton('PLAY', ButtonsStyles.PlayButton, self.__playButtonClick)

    def __setGrids(self) -> None:
        # Adiciona as imagens na grid
        for image in self.__images:
            if image.imagePath == ImagesPath.numberPlayers:
                row = 1
            elif image.imagePath == ImagesPath.ludoLogo:
                row = 0
            else:
                row = 3
            self.__grid.addWidget(image, row, 0)

        # Adiciona os botões de players na grid
        playersGrid = QGridLayout()
        for button in self.__playerButtons:
            column = int(button.text) - 1
            playersGrid.addWidget(button, 0, column)
        self.__grid.addLayout(playersGrid, 2, 0)

        # Adiciona os botões de pins na grid
        pinsGrid = QGridLayout()
        for button in self.__pinsButtons:
            column = int(button.text) - 1
            pinsGrid.addWidget(button, 0, column)
        self.__grid.addLayout(pinsGrid, 4, 0)

        # Adiciona o button de Play na grid
        self.__grid.addWidget(self.__playButton, 5, 0)

    def __clear(self) -> None:
        # Clear all the buttons
        for button in self.__pinsButtons:
            button.hide()

        for button in self.__playerButtons:
            button.hide()

        for image in self.__images:
            image.hide()

        self.__playButton.hide()

    def __playButtonClick(self):
        self.__clear()
        self.__window.setStyleSheet("background: white;")
        self.__window.setWindowTitle('LUDO')

        self.__board = Board()
        self.__panel = Panel()
        self.__grid.addWidget(self.__board, 0, 0)
        self.__grid.addWidget(self.__panel, 0, 1)

    def run(self):
        self.__setWindow()
        self.__addWidgets()
        self.__setGrids()
        self.__window.setLayout(self.__grid)
        self.__window.show()
