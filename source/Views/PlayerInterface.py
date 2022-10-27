from PyQt5.QtWidgets import QWidget, QGridLayout, QMainWindow, QLineEdit
from PyQt5.QtCore import QMetaObject, pyqtSlot
from Config.ButtonsStyles import ButtonsStyles
from Config.ImagesPath import ImagesPath
from Game.Player import Player
from Dog.dog_actor import DogActor
from Views.PushButton import PushButton
from Game.Board import Board
from Views.Panel import Panel
from Views.Image import Image
from typing import List, Tuple
from Dog.start_status import StartStatus
from Abstractions.AbstractGame import AbstractGame

# Não é necessário efetivamente herdar a classe Interface, somente basta implementar os métodos lá definidos
# simplesmente colocar DogPlayerInterface como classe base de PlayerInterface irá causar um conflito com a classe base
# QMainWindow.


class PlayerInterface(QMainWindow):
    def __init__(self, game: AbstractGame):
        QMainWindow.__init__(self)
        self.__game: AbstractGame = game

        self.__window = QWidget()
        self.__grid = QGridLayout()

        self.__images: List[Image] = []
        self.__playerButtons: List[PushButton] = []
        self.__pawnsButtons: List[PushButton] = []
        self.__playButton: PushButton = None
        self.__inputText: QLineEdit = None

        self.__quantPlayers: int = None
        self.__quantPawns: int = None

        self.__board: Board = None
        self.__panel: Panel = None
        # ID para identificar qual o player local
        self.__localID: str = None

    @property
    def board(self) -> Board:
        return self.__board

    def run(self):
        self.__configureFirstWindow()

    def receive_move(self, a_move):
        return super().receive_move(a_move)

    def receive_start(self, status: StartStatus):
        # Chama o método para desenhar a tela, caso seja chamado diretamente irá ocorrer um erro de threads
        QMetaObject.invokeMethod(self, '_buildBoard')

        # Cria as instâncias de players
        players = self.__buildPlayers(status.get_players())
        self.__localID = status.get_local_id()

        # Manda para a instância de game iniciar a partida
        self.__game.startMatch(players, self.__board, self.__localID)

    def receive_withdrawal_notification(self):
        return super().receive_withdrawal_notification()

    def __configureFirstWindow(self):
        # Clear widgets
        self.__clear()

        # Configure the window
        self.__window.setWindowTitle('LUDO')
        self.__window.setStyleSheet("background: black;")
        self.__window.move(640, 108)

        # Create the widgets
        self.__images.append(Image(ImagesPath.ludoLogo, 35))
        self.__inputText = QLineEdit(self)
        self.__inputText.setStyleSheet("background: white; width: 20%")
        self.__inputText.setPlaceholderText('Your name: ')

        self.__playerButtons.append(self.__inputText)
        self.__playButton = PushButton(
            'PLAY', ButtonsStyles.PlayButton, self.__configureSecondWindow)

        # Add the widgets to the grid
        self.__grid.addWidget(self.__images[0], 0, 0)
        self.__grid.addWidget(self.__inputText, 1, 0)
        self.__grid.addWidget(self.__playButton, 2, 0)

        # Configure the grid and start the window
        self.__window.setLayout(self.__grid)
        self.__window.show()

    def __configureSecondWindow(self) -> None:
        userName = self.__inputText.text()

        if userName == '':
            print('Escolha um nome')
            return None

        self.__localActor = DogActor()
        connResult = self.__localActor.initialize(userName, self)

        # If could not connect then we do not pass to the next window
        if not self.__successfullyConnected(connResult):
            print(connResult)
            return None

        print('Conectado ao servidor')

        # Clear widgets
        self.__clear()

        # Configure the window
        self.__window.setWindowTitle('LUDO')
        self.__window.setStyleSheet("background: black;")
        self.__window.move(640, 108)

        # Configure the widgets
        self.__images.append(Image(ImagesPath.ludoLogo, 25))
        self.__images.append(Image(ImagesPath.numberPlayers, 50))

        # Cria os botões de escolher players
        for index in range(2, 5):
            button = PushButton(index, ButtonsStyles.Menu, self.__playersButtonCallback, index)
            self.__playerButtons.append(button)

        # Cria o botão de play e conecta com o método Play quando clicado
        self.__playButton = PushButton(
            'PLAY', ButtonsStyles.PlayButton, self.__configureThirdWindow)

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

        # Adiciona o button de Play na grid
        self.__grid.addWidget(self.__playButton, 4, 0)

    def __configureThirdWindow(self):
        if self.__quantPlayers == None or self.__quantPawns == None:
            print('Defina a quantidade de jogadores e de pinos')
            return None

        print(self.__quantPlayers)
        status = self.__localActor.start_match(self.__quantPlayers)

        failed, message = self.__failedToStartMatch(status)
        if failed:
            print(message)
            return None

        # Desenha a tela
        self._buildBoard()

        # Cria as instâncias de players
        players = self.__buildPlayers(status.get_players())
        self.__localID = status.get_local_id()

        # Manda para a instância de game iniciar a partida
        self.__game.startMatch(players, self.__quantPawns, self.__board, self.__localID)

    def __clear(self) -> None:
        # Clear all the buttons
        for button in self.__pawnsButtons:
            button.hide()
        self.__pawnsButtons.clear()

        for button in self.__playerButtons:
            button.hide()
        self.__playerButtons.clear()

        for image in self.__images:
            image.hide()
        self.__images.clear()

        if self.__inputText is not None:
            self.__inputText.hide()
            self.__inputText = None

        if self.__playButton is not None:
            self.__playButton.hide()
            self.__playButton = None

    def __playersButtonCallback(self, *args) -> None:
        # O args é passado duas vezes e está ocorrendo a colocação de uma tupla dentro de outra
        text: str = args[0][0]

        for pButton in self.__playerButtons:
            if pButton.text == text:
                pButton.selected = True
                pButton.style = ButtonsStyles.MenuSelected
                self.__quantPlayers = int(text)
            else:
                pButton.selected = False
                pButton.style = ButtonsStyles.Menu

    def __pawnsButtonCallback(self, *args) -> None:
        # O args é passado duas vezes e está ocorrendo a colocação de uma tupla dentro de outra
        text: str = args[0][0]

        for pButton in self.__pawnsButtons:
            if pButton.text == text:
                pButton.selected = True
                pButton.style = ButtonsStyles.MenuSelected
                self.__quantPawns = int(text)
            else:
                pButton.selected = False
                pButton.style = ButtonsStyles.Menu

    def __successfullyConnected(self, connResult: str) -> bool:
        if 'Conectado' in connResult:
            return True
        return False

    def __failedToStartMatch(self, status: StartStatus) -> Tuple[bool, str]:
        if int(status.get_code()) == 1:
            return (True, status.get_message())
        return (False, '')

    @pyqtSlot()
    def _buildBoard(self) -> None:
        # Clear widgets
        self.__clear()

        # Set the window
        self.__window.setStyleSheet("background: white;")
        self.__window.setWindowTitle('LUDO')
        self.__window.showMaximized()

        # Add the widgets
        self.__board = Board()
        self.__panel = Panel()

        self.__grid.addWidget(self.__board, 0, 0)
        self.__grid.addWidget(self.__panel, 0, 1)

    def __buildPlayers(self, playersInfo: List) -> List[Player]:
        players = []
        for playerInfo in playersInfo:
            name = playerInfo[0]
            playerID = playerInfo[1]
            player = Player(name, playerID)
            players.append(player)

        return players
