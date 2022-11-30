from PyQt5.QtWidgets import QWidget, QGridLayout, QMainWindow, QLineEdit, QLabel
from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5 import QtCore
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
from Config.PlayerColor import PlayerColor

# TODO -> Adicionar todas as ocorrências do atributo currentLabel que é o QLabel para textos no inicio


class PlayerInterface(QMainWindow):
    def __init__(self, game: AbstractGame):
        QMainWindow.__init__(self)
        self.__game: AbstractGame = game

        self.__window = QWidget()
        self.__grid = QGridLayout()

        self.__images: List[Image] = []
        self.__playerButtons: List[PushButton] = []
        self.__playButton: PushButton = None
        self.__inputText: QLineEdit = None

        self.__quantPlayers: int = None

        self.__board: Board = None
        self.__panel: Panel = None
        # ID para identificar qual o player local
        self.__localID: str = None
        self.__playerName: str = None
        # Atributo privado para passar instância de move para a thread principal
        self.__currentMove: dict = None

    def sendMove(self, player: Player, pawnPositionList, canRollAgain: bool, gameFinished: bool, resetGame: bool) -> None:
        dictToSend = {}
        dictToSend['playerID'] = str(player.id)
        dictToSend['pawnPositionList'] = pawnPositionList

        if canRollAgain:
            dictToSend["willPlayAgain"] = str(True)
        else:
            dictToSend["willPlayAgain"] = str(False)

        dictToSend["match_status"] = "next"
        dictToSend["reset"] = bool(resetGame)
        dictToSend["finished"] = bool(gameFinished)

        print(f'Mandando move {dictToSend}')
        self.__localActor.send_move(dictToSend)

    @property
    def diceValue(self) -> int:
        return self.__panel.diceValue

    @property
    def playerName(self) -> str:
        return self.__playerName

    @property
    def board(self) -> Board:
        return self.__board

    def run(self):
        self.__configureFirstWindow()

    def receive_move(self, move: dict):
        self.__currentMove = move
        QMetaObject.invokeMethod(self, '_receiveMove')

    @pyqtSlot()
    def _receiveMove(self):
        """
        Método para ser executado na thread principal e chamar o processMove do Game
        """
        self.__game.processMove(self.__currentMove)

    def receive_start(self, status: StartStatus):
        print(f'Receiving Start, localPlayer: {self.__playerName}')
        # Chama o método para desenhar a tela, caso seja chamado diretamente irá ocorrer um erro de threads
        QMetaObject.invokeMethod(self, '_buildBoard')

        # Cria as instâncias de players e coloca como propriedade interna da classe para poder enviar para a main thread
        players = self.__buildPlayers(status.get_players())
        self.__localID = status.get_local_id()
        self.__players = players

        # Chama o método _startMatch para ser executado na thread principal
        QMetaObject.invokeMethod(self, '_startMatch')

    @pyqtSlot()
    def _buildBoard(self) -> None:
        # Clear widgets
        self.__clear()

        # Set the window
        self.__window.setStyleSheet("background: white;")
        self.__window.setWindowTitle('LUDO')
        self.__window.showMaximized()

        # Add the widgets
        self.__board = Board(self.__game)
        self.__panel = Panel(rollCB=self.__handleRollButton,
                             confirmCB=self.__handleConfirmClick, resetCB=self.__handleResetClick)

        self.__grid.addWidget(self.__board, 0, 0)
        self.__grid.addWidget(self.__panel, 0, 1)

    @pyqtSlot()
    def _startMatch(self) -> None:
        self.__game.startMatch(self.__players, self.__board, self.__localID)

    def receive_withdrawal_notification(self):
        print('Withdraw')

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

        self.__currentLabel: QLabel = QLabel('-')

        self.__currentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.__currentLabel.setFixedWidth(500)
        self.__currentLabel.setFixedHeight(50)
        self.__currentLabel.setStyleSheet(self.__getStyle())

        # Add the widgets to the grid
        self.__grid.addWidget(self.__images[0], 0, 0)
        self.__grid.addWidget(self.__inputText, 1, 0)
        self.__grid.addWidget(self.__playButton, 2, 0)
        self.__grid.addWidget(self.__currentLabel, 3, 0)

        # Configure the grid and start the window
        self.__window.setLayout(self.__grid)
        self.__window.show()

    def __configureSecondWindow(self) -> None:
        self.__playerName = self.__inputText.text()

        if self.__playerName == '':
            self.__currentLabel.setText('Escolha um nome')
            return None

        self.__localActor = DogActor()
        connResult = self.__localActor.initialize(self.__playerName, self)

        # If could not connect then we do not pass to the next window
        if not self.__successfullyConnected(connResult):
            self.__currentLabel.setText(connResult)
            return None

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

        self.__currentLabel.setText('Você está conectado')

        # Adiciona o button de Play na grid
        self.__grid.addWidget(self.__playButton, 4, 0)
        self.__grid.addWidget(self.__currentLabel, 5, 0)

    def __configureThirdWindow(self):
        if self.__quantPlayers == None:
            self.__currentLabel.setText('Escolha a quantidade de jogadores')
            return None

        print(
            f'Iniciando partida com {self.__quantPlayers} players, localPlayer: {self.__playerName}')
        status = self.__localActor.start_match(self.__quantPlayers)

        failed, message = self.__failedToStartMatch(status)
        if failed:
            self.__currentLabel.setText(message)
            return None

        self.__currentLabel = None
        # Desenha a tela
        self._buildBoard()

        # Cria as instâncias de players
        players = self.__buildPlayers(status.get_players())
        self.__localID = status.get_local_id()

        # Manda para a instância de game iniciar a partida
        self.__game.startMatch(players, self.__board, self.__localID)

    def __clear(self) -> None:
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

    def __handleRollButton(self) -> None:
        self.__game.handleRoll()

    def __handleConfirmClick(self) -> None:
        self.__game.handleConfirmPiece()

    def __handleResetClick(self) -> None:
        self.__game.handleResetMatch()

    def setTurnMessage(self, message: str, color: PlayerColor = PlayerColor.BLACK) -> None:
        self.__panel.setTurnMessage(message, color)

    def setTitleMessage(self, message: str, color: PlayerColor = PlayerColor.BLACK) -> None:
        self.__panel.setTitleMessage(message, color)

    def setNotifyMessage(self, message: str, color: PlayerColor = PlayerColor.BLACK) -> None:
        self.__panel.setNotifyMessage(message, color)

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

    def __successfullyConnected(self, connResult: str) -> bool:
        if 'Conectado' in connResult:
            return True
        return False

    def __failedToStartMatch(self, status: StartStatus) -> Tuple[bool, str]:
        if int(status.get_code()) == 1:
            return (True, status.get_message())
        return (False, '')

    def __buildPlayers(self, playersInfo: List) -> List[Player]:
        players = []
        for playerInfo in playersInfo:
            name = playerInfo[0]
            playerID = playerInfo[1]
            player = Player(name, playerID)
            players.append(player)

        return players

    @property
    def panel(self) -> Panel:
        return self.__panel

    def __getStyle(self) -> str:
        return '''
        *{
            border-top: 2px solid white;
            border-bottom: 2px solid white;
            font-size: 25px;
            font-weight: bold;
            color: white;
        }
        '''
