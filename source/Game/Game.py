from Views.PlayerInterface import PlayerInterface
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QMetaObject, pyqtSlot
from Game.PawnStatus import PawnStatus
from PyQt5.QtWidgets import QApplication
from Game.Player import Player
from Game.Board import Board
from Game.Pawn import Pawn
from typing import List, Tuple
from Views.Position import Position
import sys


class Game(QMainWindow):
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
        super().__init__()
        self.__interface: PlayerInterface = None

        self.__localPlayer: Player = None
        self.__players: List[Player] = None
        self.__board: Board = None

        self.__winner: Player = None
        self.__endOfGame: bool = False

        self.__turnPlayer: Player = None

    @property
    def board(self) -> Board:
        return self.__board

    def startWindow(self) -> None:
        self.__interface = PlayerInterface(self)
        self.__interface.run()
        self.__app.exec()

    def handleRoll(self) -> None:
        if not self.__localPlayer.hasTurn:
            self.__interface.setNotifyMessage('Not Your Turn')
            print('Not Your Turn')
            return
        if not self.__localPlayer.canRollDice:
            self.__interface.setNotifyMessage('Dice already rolled')
            print('Dice rolled, Choose your piece')
            return

        # Rola o dado
        self.__localPlayer.canRollDice = False
        self.__interface.panel.roll()
        diceValue = self.__interface.panel.diceValue
        self.__interface.setNotifyMessage(f'You rolled {diceValue}')
        self.__interface.setTurnMessage(f'Now choose your pawn to move')

        hasPawnsOut = self.__localPlayer.hasPawnsOutOfHouse()

        # Não tirou 1 nem 6 e não tem peões fora, logo não consegue jogar e a rodada termina aqui
        if diceValue != 6 and diceValue != 1 and not hasPawnsOut:
            self.__interface.sendMove(self.__localPlayer, [], False, False)
            self.goToNextPlayer()
            return

        # Caso o dado seja 6 ou 1 ele irá poder selecionar da casa
        if diceValue == 6 or diceValue == 1:
            self.__localPlayer.canSelectFromHouse = True

        # Caso tenha tirado 6 pode jogar novamente
        if diceValue == 6:
            self.__localPlayer.canRollAgain = True

        self.__localPlayer.canMovePawn = True

    def checkIfValidPosition(self, pos: Position) -> bool:
        """
        Função para verificar se a position selecionada durante o processo de choose piece está correto
        Deve verificar se existe um peão que pertença ao jogador.
        """
        player = self.__turnPlayer
        isValid: bool = True
        messageCode: int = 0

        # Se ainda não rodou dado
        if player.canRollDice:
            self.__interface.setNotifyMessage('You must roll the dice')
            return False

        # Se tiver 1 peão na casa
        if not pos.isFree:
            # E for do mesmo jogador
            if player == pos.pawns[0].player:
                # Olha o status do peão na casa
                status = pos.pawns[0].status
                # Caso seja STORED significa que o jogador clicou em uma posição da casa
                if status == PawnStatus.STORED:
                    # Verifica se ele consegue levar o peão para a primeira casa do caminho do jogador
                    if player.canSelectFromHouse:
                        # Caso não tenha uma barreira no local retorna Falso
                        if not player.path[0].isBlocked:
                            isValid = True
                        else:
                            # Verifica se é do mesmo jogador, se sim pode passar
                            if player.path[0].pawns[0].player == player:
                                isValid = True
                            else:
                                # Se não fica travado dentro da casa
                                isValid = False
                                messageCode = 3
                    # Caso não possa selecionar da casa
                    else:
                        isValid = False
                        messageCode = 2
                # Nesse caso o cara clicou na última posição
                elif status == PawnStatus.FINISHED:
                    isValid = False
                    messageCode = 4
                # Caso seja outros status pode selecionar a posição
                else:
                    isValid = True
            # Caso não seja do mesmo jogador retorna falso pq não é válido
            else:
                isValid = False
                messageCode = 1
        # Nenhum peão na casa
        else:
            isValid = False
            messageCode = 0

        # Caso tenha sido um movimento válido altera a posição selecionada
        if isValid:
            player.canConfirmPiece = True
            player.selectedPawn = pos.pawns[0]
            self.__board.selectedPosition = pos

            message = 'Pawn selected'
        else:
            message = self.getInvalidPositionMessage(messageCode)

        self.__interface.setNotifyMessage(message)

    def handleConfirmPiece(self) -> None:
        # TODO -> Revisar todo o diagrama de sequencia disso
        # Caso o jogador não tenha o turno
        if not self.__localPlayer.hasTurn:
            self.__interface.setNotifyMessage('Not Your Turn')
            return

        # Caso o jogador ainda não tenha rolado o dado
        if self.__localPlayer.canRollDice:
            self.__interface.setNotifyMessage('Roll the dice first')
            return

        # Caso o jogador ainda não tenha selecionado uma position ou não pode fazer isso
        if not self.__localPlayer.canConfirmPiece or self.__board.selectedPosition is None:
            self.__interface.setNotifyMessage('You must select a piece')
            return

        player = self.__turnPlayer
        player.canConfirmPiece = False

        pawn = self.__board.selectedPosition.pawns[0]
        hasWinner = False

        # Se o peão ainda estiver dentro da casa vai retirar um peão aleatório da casa
        if pawn.status == PawnStatus.STORED:
            # Reescreve o objeto Pawn que vai ser removido para ser o que a house decidir remover
            pawn = player.house.removePawn()
            # Pega a primeira posição do caminho
            firstPosition = player.path[0]
            # Coloca o peão que saiu da casa dentro da primeira posição
            firstPosition.receivePawn(pawn)
        else:
            diceValue = self.__interface.diceValue
            amountOverreached = self.movePawn(pawn, diceValue)

            if amountOverreached == 0:
                if pawn.status == PawnStatus.FINISHED:
                    hasWinner = self.verifyWinner(player)
                    # se o jogador do turno é vencedor
                    if hasWinner:
                        self.__interface.setTurnMessage("You won!")

        pawnPositionList = [(pawn.id, pawn.currentPosition.id)]
        self.__interface.sendMove(player, pawnPositionList, player.canRollAgain, hasWinner)

        # Tira a seleção da position que teve o peão removido
        self.__board.selectedPosition.selected = False

        self.__interface.setNotifyMessage('Pawn moved')
        if player.canRollAgain:
            self.__interface.setTurnMessage('You can play again, roll the dice')
            player.reset()
            player.startTurn()
        else:
            self.goToNextPlayer()

    @pyqtSlot()
    def processMove(self, move: dict) -> None:
        """
        Um move é um dicionário com as seguintes chaves:
        pawnPositionList -> Lista de Tuplas de id de peões e id de positions que eles estão agora: List[Tuple[int, int]]
        playerID -> ID do player que acabou de jogar
        willPlayAgain -> Bool se o jogador irá jogar novamente ou não
        """
        print('Processing Move', move)
        pawnPositionList = self.getPawnPositionList(move)
        movePlayer = self.getPlayerFromMove(move)

        for (pawnID, posID) in pawnPositionList:
            pawn = movePlayer.getPawnFromID(pawnID)
            newPosition = self.__board.getPositionFromID(posID)

            # Caso o peão que moveu estava em uma casa anteriormente retira ele da house
            if pawn.status == PawnStatus.STORED:
                pawn = movePlayer.house.removePawn()

                # Coloca o peão que saiu da casa na nova position
                newPosition.receivePawn(pawn)
            # Caso estivesse no caminho irá remover da position anterior
            else:
                # Remove o peão da posição anterior
                pawn.currentPosition.removePawn()
                # Coloca dentro da nova posição
                newPosition.receivePawn(pawn)
                # Método para alterar o index interno de Pawn
                pawn.updatePositionIndex(newPosition)

        # Se tiver vencedor o atributo self.__winner será modificado
        self.verifyWinner(movePlayer)

        if self.__winner == None:
            rollAgain = self.checkReroll(move)
            if not rollAgain:
                self.goToNextPlayer()
            else:
                notifyMessage = f'{str(movePlayer.color)} will play again'
                self.__interface.setNotifyMessage(notifyMessage)
                print(f'Esperando próxima jogada do {movePlayer.color}')
        else:
            self.__interface.setTurnMessage(f'{movePlayer.name} WON', movePlayer.color)

    def goToNextPlayer(self) -> Player:
        # Para o primeiro caso
        if self.__turnPlayer is None:
            self.__turnPlayer = self.__players[0]

        self.__turnPlayer.endTurn()

        # Pega o index do currentPlayer na lista de players
        currentPlayerIndex = 0
        for index, player in enumerate(self.__players):
            if player == self.__turnPlayer:
                currentPlayerIndex = index
                break

        # Passa para o próximo
        currentPlayerIndex += 1
        # Se ultrapassar o final volta para o começo da lista
        if currentPlayerIndex == len(self.__players):
            currentPlayerIndex = 0

        self.__turnPlayer = self.__players[currentPlayerIndex]

        # Atualiza a interface para o próximo jogador
        if self.__localPlayer == self.__turnPlayer:
            turnMessage = f'Your Turn, roll the dice'
            # TODO Adicionar essa msg nos diagramas
            self.__interface.setNotifyMessage('-', self.__turnPlayer.color)
        else:
            turnMessage = f'{str(self.__turnPlayer.color)} Turn'
        self.__interface.setTurnMessage(turnMessage, self.__turnPlayer.color)
        self.__turnPlayer.startTurn()

    def movePawn(self, pawn: Pawn, distance: int) -> Tuple[Pawn, int]:
        """
        Move um peão por uma distance determinada, o retorno é uma tupla com um Pawn e um
        inteiro, caso o Pawn seja diferente de nulo está contendo um peão que foi morto pelo que se movimentou.
        Caso o inteiro seja diferente de 0 é a quantidade overreached que teve
        """
        # Pega a posição atual do peão
        firstPosition = pawn.path[pawn.currentPosIndex]
        # Faz um loop começando na próxima posição até distance ser atingida
        startIndex = pawn.currentPosIndex + 1
        endIndex = startIndex + distance

        # Caso ultrapasse o final do caminho atualiza o destino final
        overreachedQuant = 0
        if endIndex > len(pawn.path):
            overreachedQuant = endIndex - len(pawn.path)
            endIndex -= overreachedQuant

        actualQuantMoved = 0
        finalPosition = None
        for positionIndex in range(startIndex, endIndex):
            # Pega a posição atual para verificar
            position = pawn.path[positionIndex]
            # Verifica se existe uma barreira nela
            if position.isBlocked:
                # Verifica se a barreira é de outro jogador, se for para uma antes
                if not position.pawns[0].player.color == pawn.color:
                    finalPosition = pawn.path[positionIndex - 1]
                    break

                # Caso a posição final do peão seja na casa com barreira
                # e a barreira seja do mesmo player paramos uma antes
                if positionIndex == endIndex - 1:
                    finalPosition = pawn.path[positionIndex - 1]
                    break

            # Vai atualizando a ultima posição
            finalPosition = position
            actualQuantMoved += 1

        # Move o peão da casa inicial para a final
        firstPosition.removePawn()

        killedPawn = None
        # Se existe alguém na posição final
        if not finalPosition.isFree:
            # E caso seja peão de outro jogador
            if finalPosition.pawns[0].player != pawn.player:
                killedPawn = finalPosition.pawns[0]
                killedPawn.returnToHouse()

        finalPosition.receivePawn(pawn)
        # Add a quantidade correta de casas que foram movidas
        pawn.currentPosIndex += actualQuantMoved

        if finalPosition == pawn.path[-1]:
            pawn.status = PawnStatus.FINISHED

        return overreachedQuant

    def startMatch(self, players: List[Player], board: Board, localID: int):
        self.__players = players
        # Order the list in place
        self.__players.sort(key=lambda x: x.name)

        self.__board = board

        for index, player in enumerate(self.__players):
            # Configura o player local pelo ID
            if player.id == localID:
                self.__localPlayer = player

            # Seleciona uma casa para o jogador acessando a lista de casas pelo index
            house = board.houses[index]
            player.house = house
            # Pega o path da casa
            path = self.__board.getPlayerPath(house.color)
            # Configura a casa e adiciona os Pawns criados para dentro do Player
            pawns = house.configureMatch(path, player)
            player.pawns = pawns
            # Já configura a cor do player pela casa que ele recebe
            player.house = house

        titleMessage = f'{self.__localPlayer.name} - {str(self.__localPlayer.color)}'
        self.__interface.setTitleMessage(titleMessage, self.__localPlayer.color)

        # Essa função irá iniciar a rodada com o primeiro jogador
        self.goToNextPlayer()

    def verifyWinner(self, player: Player) -> bool:
        pawns = player.pawns
        allPawnsFinished = True
        for pawn in pawns:
            if pawn.status != PawnStatus.FINISHED:
                allPawnsFinished = False
                break

        if allPawnsFinished:
            self.__winner = player
            self.__endOfGame = True
            return True
        return False

    def getPlayerFromMove(self, move: dict) -> Player:
        playerID = move['playerID']

        for player in self.__players:
            if player.id == playerID:
                return player

        print('getPlayerFromMove não encontrou player')

    def checkReroll(self, move: dict) -> bool:
        if move['willPlayAgain'] == 'False':
            return False
        return True

    def getPawnPositionList(self, move: dict) -> List[Tuple[int, int]]:
        if 'pawnPositionList' in move.keys():
            return move['pawnPositionList']
        return []

    def clearPlayers(self) -> None:
        for player in self.__players:
            player.reset()

        self.__board.reset()

    def getTurnPlayer(self) -> Player:
        for player in self.__players:
            if player.hasTurn:
                return player

        print('No Turn Player')

    def getLocalPlayer(self) -> Player:
        return self.__localPlayer

    @property
    def players(self) -> List[Player]:
        return self.__players

    def reset(self) -> None:
        self.__board.reset()
        players = self.__players

        for player in players:
            player.reset()

    def getInvalidPositionMessage(self, code: int) -> str:
        if code == 0:
            return 'No pawn in this position'
        if code == 1:
            return "Pawn's not yours"
        if code == 2:
            return 'Cannot choose from house'
        if code == 3:
            return 'Barrier is blocking your way out'
        if code == 4:
            return 'Pawn already finished the run'
