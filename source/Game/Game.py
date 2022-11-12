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

    @property
    def board(self) -> Board:
        return self.__board

    def startWindow(self) -> None:
        self.__interface = PlayerInterface(self)
        self.__interface.run()
        self.__app.exec()

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
        print(board)
        self.__board = board

        for index, player in enumerate(players):
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
