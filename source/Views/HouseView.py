from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.PlayerColor import PlayerColor
from Views.HousePosition import HousePosition


class House:
    def __init__(self, color: PlayerColor):
        self.__widget = QWidget()
        self.__color = color
        self.__grid = QGridLayout()
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __setGrid(self) -> None:
        for l in range(2):
            for c in range(2):
                self.__grid.addWidget(HousePosition(self.__color).widget, l,  c)

    def __start(self) -> None:
        self.__widget.setStyleSheet(self.__style)
        self.__setGrid()
        self.__widget.setLayout(self.__grid)

    def __getStyle(self):
        if self.__color == PlayerColor.BLUE:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PlayerColor.YELLOW:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PlayerColor.GREEN:
            return '''
            *{  
                border-radius: 159%;
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''
        else:  # Red
            return '''
            *{  
                border-radius: 159%;
                background-color: 'red';
                border: 2px solid 'black';  
            }
            '''
