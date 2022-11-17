from Game.PawnStatus import PawnStatus
from Views.PlayerInterface import PlayerInterface
from PyQt5.QtWidgets import QApplication
from Game.Player import Player
from Game.Board import Board
from Game.Pawn import Pawn
from typing import List, Tuple
import sys


class Game:
    def __init__(self) -> None:
        self.__app = QApplication(sys.argv)
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

    def processMove(self, move: dict) -> None:
        """
        Um move é um dicionário com as seguintes chaves:
        pawnPositionList -> Lista de Tuplas de id de peões e id de positions que eles estão agora: List[Tuple[int, int]]
        pawnToHouseList -> Lista de id de peões que foram mortos no ultimo movimento: List[int]
        playerID -> ID do player que acabou de jogar
        willPlayAgain -> Bool se o jogador irá jogar novamente ou não
        """
        pawnPositionList = self.getPawnPositionList(move)
        movePlayer = self.getPlayerFromMove(move)

        for (pawnID, posID) in pawnPositionList:
            pawn = movePlayer.getPawnFromID(pawnID)
            position = self.__board.getPositionFromID(posID)
            position.receivePawn(pawn)

        # Se tiver vencedor o atributo self.__winner será modificado
        self.verifyWinner(movePlayer)

        if self.__winner == None:
            rollAgain = self.checkReroll(move)

            if not rollAgain:
                movePlayer.endTurn()
                self.goToNextPlayer(movePlayer)
        else:
            self.__interface.setMessage(f'{movePlayer.name} WON', movePlayer.color)

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
        endIndex = startIndex + distance + 1

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

        return (killedPawn, overreachedQuant)

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
            # Pega o path da casa
            path = self.__board.getPlayerPath(house.color)
            # Configura a casa e adiciona os Pawns criados para dentro do Player
            pawns = house.configureMatch(path, player)
            player.pawns = pawns
            # Já configura a cor do player pela casa que ele recebe
            player.house = house

        # Configura o primeiro jogador que irá jogar
        self.__turnPlayer = self.__players[0]
        self.__interface.setMessage(
            f'Player Turn: {self.__turnPlayer.name}', self.__turnPlayer.color)
        self.__turnPlayer.startTurn()

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
        return move['willPlayAgain']

    def goToNextPlayer(self, currentPlayer: Player) -> Player:
        # Pega o index do currentPlayer na lista de players
        currentPlayerIndex = 0
        for index, player in enumerate(self.__players):
            if player == currentPlayer:
                currentPlayerIndex = index
                break

        # Passa para o próximo
        currentPlayerIndex += 1
        # Se ultrapassar o final volta para o começo da lista
        if currentPlayerIndex == len(self.__players):
            currentPlayerIndex = 0

        self.__turnPlayer = self.__players[currentPlayerIndex]
        self.__turnPlayer.startTurn()

    def getPawnPositionList(self, move: dict) -> List[Tuple[int, int]]:
        return move['pawnPositionList']
