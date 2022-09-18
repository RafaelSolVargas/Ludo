import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from Config.ImagesPath import ImagesPath
from option_button import OptionButton
from play_button import PlayButton
from logo import Logo
from play.game import Game


class MainMenu:
    def __init__(self, width: int = 640):
        self.__width = width
        self.__app = QApplication(sys.argv)
        self.__window = QWidget()
        self.__grid = QGridLayout()

        self.__widgets = {
            "n_players_buttons": [],
            "n_pins_buttons": [],
            "logos": [],
            "play_button": []
        }

    def __setWindow(self) -> None:
        self.__window.setWindowTitle(' ')
        self.__window.setStyleSheet("background: black;")
        self.__window.move(640, 108)

    def __addWidgets(self) -> None:
        self.__widgets['logos'].append(Logo(ImagesPath.numberPins, 50))
        self.__widgets['logos'].append(Logo(ImagesPath.ludoLogo, 25))
        self.__widgets['logos'].append(Logo(ImagesPath.numberPlayers, 50))

        for i in range(4):
            b = OptionButton(i+1)
            self.__widgets['n_players_buttons'].append(b)

        for i in range(4):
            b = OptionButton(i+1)
            self.__widgets['n_pins_buttons'].append(b)

        p_b = PlayButton('PLAY')
        p_b.widget.clicked.connect(self.play)
        self.__widgets['play_button'].append(p_b)

    def __setGrids(self) -> None:
        n_pins_grid = QGridLayout()
        n_players_grid = QGridLayout()

        for k in self.__widgets:
            linha = None
            if k == 'logos':
                for i in self.__widgets[k]:

                    if i.image == ImagesPath.numberPlayers:
                        linha = 1
                    elif i.image == ImagesPath.ludoLogo:
                        linha = 0
                    elif i.image == ImagesPath.numberPins:
                        linha = 3

                    self.__grid.addWidget(i.widget, linha, 0)

            elif k == "n_pins_buttons":
                for i in self.__widgets[k]:
                    coluna = i.number - 1
                    n_pins_grid.addWidget(i.widget, 0, coluna)

                self.__grid.addLayout(n_pins_grid, 4, 0)

            elif k == "n_players_buttons":
                for i in self.__widgets[k]:
                    coluna = i.number - 1
                    n_players_grid.addWidget(i.widget, 0, coluna)

                self.__grid.addLayout(n_players_grid, 2, 0)

            elif k == "play_button":
                self.__grid.addWidget(self.__widgets[k][0].widget, 5, 0)

    def __clear(self) -> None:
        for v in self.__widgets.values():
            if v != []:
                for i in v:
                    i.widget.hide()
                for i in range(len(v)):
                    v.pop()

    def play(self):
        self.__clear()
        self.__window.setStyleSheet("background: white;")
        self.__window.setWindowTitle('LUDO')

        self.__grid.addWidget(Game().widget, 0, 0)

    def run(self):
        self.__setWindow()
        self.__addWidgets()
        self.__setGrids()
        self.__window.setLayout(self.__grid)
        self.__window.show()

        sys.exit(self.__app.exec())


interface = MainMenu()
interface.run()
